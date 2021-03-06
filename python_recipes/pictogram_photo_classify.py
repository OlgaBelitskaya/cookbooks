%%writefile pictogram_photo_classify.py
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
         'plane','crane','dog','horse',
         'deer','truck','car','cat',
         'frog','ship','fish','house']]
names2=[['plane','car','bird','cat','deer',
         'dog','frog','horse','ship','truck']]

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
    cond1=np.where([l in names2[0] for l in names1[1]])[0]
    cond2=np.where([l in cond1 for l in labels])[0]
    images=images[cond2]; labels=labels[cond2]
    rd=dict(zip([names1[1].index(names2[0][i])
                 for i in range(10)],range(10)))
    labels=[rd.get(el,el) for el in labels]
    labels=np.array(labels,dtype='int32')
    return images,labels

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
            n//5,5,i+1,xticks=[],yticks=[])
        ax.imshow(images[idx])
        label=labels[idx]
        name=names[0][label]
        ax.set_title('{} => {}'\
                     .format(str(label),str(name)),
                     fontsize=10)
    pl.show()
    
def img_resize(x,img_size=img_size2):       
    x=tf.image.resize(x,[img_size,img_size])
    return x.numpy()

def get_resized_data(data):
    [rx_train,rx_valid,rx_test]=\
    [img_resize(el) for el in data[:3]]
    [y_train,y_valid,y_test]=data[3:]
    print([rx_train.shape,rx_train.dtype])
    print('Label: ',names2[0][y_valid[100]])
    pl.figure(figsize=(1,1))
    pl.xticks([]); pl.yticks([])
    pl.imshow(rx_valid[100]); pl.show()
    return rx_train,rx_valid,rx_test,\
           y_train,y_valid,y_test

def get_mixed_data(data1,data2):
    data=[np.vstack([data1[i],data2[i]])
          for i in range(3)]+\
         [np.hstack([data1[i+3],data2[i+3]])
          for i in range(3)]
    [x_train,x_valid,x_test,
     y_train,y_valid,y_test]=data
    for [x,y] in [[x_train,y_train],
                  [x_valid,y_valid],
                  [x_test,y_test]]:
        N=len(y); shuffle_ids=np.arange(N)
        np.random.RandomState(23).shuffle(shuffle_ids)
        x,y=x[shuffle_ids],y[shuffle_ids]
    return x_train,x_valid,x_test,\
           y_train,y_valid,y_test

def cnn_model(data):
    [x_train,x_valid,x_test,
     y_train,y_valid,y_test]=data
        
    model=Sequential()
    model.add(tkl.Conv2D(32,(5,5),padding='same',
                         input_shape=x_train.shape[1:]))
    model.add(tkl.Activation('relu'))
    model.add(tkl.MaxPooling2D(pool_size=(2,2)))
    model.add(tkl.Dropout(.25))
    model.add(tkl.Conv2D(196,(5,5)))
    model.add(tkl.Activation('relu'))    
    model.add(tkl.MaxPooling2D(pool_size=(2,2)))
    model.add(tkl.Dropout(.25))
    model.add(tkl.GlobalAveragePooling2D())    
    model.add(tkl.Dense(1024,activation='relu'))
    model.add(tkl.Dropout(.5))         
    model.add(tkl.Dense(10))
    model.add(tkl.Activation('softmax'))
    model.compile(loss='sparse_categorical_crossentropy',
                  optimizer='adam',metrics=['accuracy'])
    early_stopping=tkc.EarlyStopping(monitor='val_loss',
                                     patience=20,verbose=2)
    checkpointer=tkc.ModelCheckpoint(filepath=fw,verbose=2,
                                     save_best_only=True)
    lr_reduction=tkc.ReduceLROnPlateau(monitor='val_loss',verbose=2,
                                       patience=5,factor=.8)
    history=model.fit(x_train,y_train,epochs=100,
                      batch_size=64,verbose=2,
                      validation_data=(x_valid,y_valid),
                      callbacks=[checkpointer,
                                 early_stopping,
                                 lr_reduction])
    return model,history

def hub_model(data):
    [rx_train,rx_valid,rx_test,
     ry_train,ry_valid,ry_test]=data
    handle_base="mobilenet_v2_050_96"
    mhandle="https://tfhub.dev/google/imagenet/{}/feature_vector/4"\
    .format(handle_base)
    
    model=tf.keras.Sequential([
        tf.keras.layers.Input((img_size2,img_size2,3),
                              name='input'),
        th.KerasLayer(mhandle,trainable=True),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(2048,activation='relu'),
        tf.keras.layers.Dropout(rate=.5),
        tf.keras.layers.Dense(10,activation='softmax')])
    model.compile(optimizer='adam',metrics=['accuracy'],
                  loss='sparse_categorical_crossentropy') 
    early_stopping=tkc.EarlyStopping(monitor='val_loss',
                                     patience=20,verbose=2)
    checkpointer=tkc.ModelCheckpoint(filepath=fw,verbose=2,
                                     save_best_only=True)
    lr_reduction=tkc.ReduceLROnPlateau(monitor='val_loss',verbose=2,
                                       patience=5,factor=.8)
    history=model.fit(rx_train,ry_train,epochs=50,
                      batch_size=64,verbose=2,
                      validation_data=(rx_valid,ry_valid),
                      callbacks=[checkpointer,
                                 early_stopping,
                                 lr_reduction])
    return model,history

def history_plot(fit_history,fig_size,color):
    pl.style.use('seaborn-whitegrid')
    keys=list(fit_history.history.keys())
    list_history=[fit_history.history[keys[i]] 
                  for i in range(len(keys))]
    dfkeys=pd.DataFrame(list_history).T
    dfkeys.columns=keys
    fig=pl.figure(figsize=(fig_size,fig_size))
    ax1=fig.add_subplot(311)
    dfkeys.iloc[:,[0,2]].plot(
        ax=ax1,color=['slategray',color])
    ax2=fig.add_subplot(312)
    dfkeys.iloc[:,4].plot(ax=ax2,color=color)
    pl.legend()
    ax3=fig.add_subplot(313)
    dfkeys.iloc[:,[1,3]].plot(
        ax=ax3,color=['slategray',color])
    pl.show();