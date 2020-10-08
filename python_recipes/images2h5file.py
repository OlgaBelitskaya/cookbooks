import h5py,os,numpy as np
from tensorflow.keras.preprocessing \
import image as tkimg

def images2array(files_path,img_size,preprocess):
    files_list=sorted(os.listdir(files_path))
    n,img_array=len(files_list),[]
    for i in range(n):
        if i%round(.1*n)==0:
            print('=>',end='',flush=True)
        img_path=files_path+files_list[i]
        if preprocess=='True':
            img=tkimg.load_img(img_path)
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
    labels=[int(el[:2]) for el in files_list]
    label_set=list(set(labels))
    rd=dict(zip(label_set,
                list(range(len(label_set)))))
    labels=np.array([rd.get(x,x) for x in labels],
                    dtype=np.int32)
    return labels
def images2h5file(h5file,files_path,
                  img_size,names,preprocess='False'):
    images=images2array(files_path,img_size,preprocess)
    labels=labels2array(files_path)
    maxlen=max([len(n) for n in names])
    names=np.array([np.string_(name) 
                    for name in names])
    with h5py.File(h5file,'w') as f:
        f.create_dataset('images',data=images,compression="gzip")
        f.create_dataset('labels',data=labels,compression="gzip")
        f.create_dataset('names',data=names,
                         dtype='S%d'%maxlen,
                         compression="gzip")
        f.close()
    print('\nfile size: %s'%list(os.stat(h5file))[6])