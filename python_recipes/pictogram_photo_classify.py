import pandas as pd,numpy as np,tensorflow as tf
import os,seaborn as sn,pylab as pl
from IPython.display import display
from tensorflow.keras.preprocessing \
import image as tkimg
from tensorflow.keras.datasets import cifar10
from IPython.core.magic import register_line_magic
import tensorflow_hub as th
from tensorflow.keras.models import Sequential
from tensorflow.keras import layers as tkl
from tensorflow.keras import callbacks as tkc

img_size1,img_size2=32,96
cmap1,cmap2='spring','autumn'
fw='weights.best.hdf5'
names1=[['pictogram','contour','sketch'],
        ['flower','bird','butterfly','tree',
         'plane','crane','dog','horse','deer',
         'truck','car','cat','frog',
         'ship','fish','house']]
names2=[['plane','car','bird','cat','deer',
         'dog','frog','horse','ship','truck']]
model,history=[],[]

def images2array(files_path,img_size,
                 preprocess=False,grayscale=False):
    files_list=sorted(os.listdir(files_path))
    n,img_array=len(files_list),[]
    for i in range(n):
        if i%round(.1*n)==0:
            print('=>',end='',flush=True)
        img_path=files_path+files_list[i]
        if preprocess:
            img=tkimg.load_img(
                img_path,grayscale=grayscale)
            img=tkimg.img_to_array(img)
            img=tkimg.smart_resize(
                img,(img_size,img_size))
        else:
            img=tkimg.load_img(
                img_path,target_size=(img_size,img_size))
            img=tkimg.img_to_array(img)
        img=np.expand_dims(img,axis=0)/255
        img_array.append(img)
    return np.array(np.vstack(img_array),
                    dtype='float32')

def labels2array(files_path):
    files_list=sorted(os.listdir(files_path))
    files_split=np.array([el.split('_') 
                          for el in files_list])
    num_labels=files_split.shape[1]-1
    labels=[files_split[:,i] 
            for i in range(num_labels)]
    labels=np.array(labels).astype('int32')
    for i in range(num_labels):
        label_set=list(set(labels[i]))
        replace_dict=\
        dict(zip(label_set,
                 list(range(len(label_set)))))
        labels[i]=[replace_dict.get(x,x) 
                   for x in labels[i]]
    return labels

def get_data(files_path,img_size,names1,names2,
             preprocess=False,grayscale=False):
    images=images2array(files_path,img_size,
                        preprocess,grayscale)
    labels=labels2array(files_path)
    n=len(labels[0][labels[0]==0])
    images=images[:n]; labels=labels[1][:n]
    rd=dict(zip([names1[1].index(names2[0][i])
                 for i in range(10)],range(10)))
    labels=np.array([rd.get(el,el) for el in labels],
                     dtype='int32')
    cond=np.where([l<10 for l in labels])[0]
    return images[cond],labels[cond]

def get_cifar():
    (images,labels),(_,_)=cifar10.load_data()
    images=np.array(images,dtype='float32')/255
    labels=np.array(labels,dtype='int32').reshape(-1)
    return images,labels

def data2nnarrays(images,labels,num,cmap,names=names2):
    N=num; n=int(.1*N)
    shuffle_ids=np.arange(images.shape[0])
    np.random.RandomState(12).shuffle(shuffle_ids)
    shuffle_ids=shuffle_ids[:N]
    images=images[shuffle_ids]
    labels=labels[shuffle_ids]
    x_test,x_valid,x_train=\
    images[:n],images[n:2*n],images[2*n:]
    y_test,y_valid,y_train=\
    labels[:n],labels[n:2*n],labels[2*n:]
    print('data outputs: ')
    df=pd.DataFrame([[x_train.shape,x_valid.shape,x_test.shape],
                     [x_train.dtype,x_valid.dtype,x_test.dtype],
                     [y_train.shape,y_valid.shape,y_test.shape],
                     [y_train.dtype,y_valid.dtype,y_test.dtype]],
                    columns=['train','valid','test'],
                    index=['image shape','image type',
                           'label shape','label type'])
    display(df)
    print('distribution of labels: ')
    df=pd.DataFrame(labels,columns=['label'])
    df['name']=[names[0][l] for l in labels]
    fig=pl.figure(figsize=(10,5))    
    ax=fig.add_subplot(1,1,1)
    sn.countplot(x='name',data=df,
                 palette=cmap,alpha=.5,ax=ax)
    pl.show()       
    return x_train,x_valid,x_test,\
           y_train,y_valid,y_test

def display_images(images,labels,n,names=names2):
    fig=pl.figure(figsize=(10,n//2))
    randch=np.random.choice(
        images.shape[0],size=n,replace=False)
    for i,idx in enumerate(randch):
        ax=fig.add_subplot(
            n//4,4,i+1,xticks=[],yticks=[])
        ax.imshow(images[idx])
        label=labels[idx]
        name=names[0][label]
        ax.set_title('{} \n {}'\
                     .format(str(label),str(name)),
                     fontsize=10)
    pl.show()
    
def img_resize(x,img_size=img_size2):       
    x=tf.image.resize(x,[img_size,img_size])
    return x.numpy()