import numpy as np,os,h5py
import tensorflow_datasets as tfds
from tensorflow.keras.preprocessing \
import image as tkimg

def tfdata2h5(data_name,names,num_points,img_size):
    ds=tfds.load(data_name,split='train',
                 shuffle_files=True,
                 as_supervised=True)
    h5file=data_name+str(img_size)+'.h5'
    images=np.zeros((num_points,img_size,img_size,3),
                     dtype='float32')
    labels=np.zeros((num_points,),dtype='int32')
    i=0
    for img,lbl in ds.take(num_points):
        img=tkimg.smart_resize(
                img,(img_size,img_size))
        images[i,:]=img.numpy()/255
        labels[i]=lbl; i+=1
    maxlen=max([len(n) for n in names])
    names=np.array([np.string_(name) 
                    for name in names])
    with h5py.File(h5file,'w') as f:
        f.create_dataset('images',data=images,
                         compression='gzip')
        f.create_dataset('labels',data=labels,
                         compression='gzip')
        f.create_dataset('names',data=names,
                         dtype='S%d'%maxlen,
                         compression='gzip')
        f.close()
    print('\nfile size: %s'%list(os.stat(h5file))[6])
    return h5file