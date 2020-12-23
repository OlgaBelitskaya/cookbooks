import warnings; warnings.filterwarnings('ignore')
import imageio,numpy as np,pandas as pd
import os,h5py,seaborn as sn,pylab as pl
from skimage.transform import resize
from skimage import io
from IPython.display import display,HTML

def randcoord(img_size_out,img_size=1024):
    a=(.5+.1**6*np.random.randint(1,999999))*\
      np.random.choice([-1,1],1)[0]
    b=np.random.randint(3,10)
    c=.1**3*np.random.randint(1,99)*\
      np.random.choice([-1,1],1)[0]
    t=np.arange(0,12*np.pi,1/7200)
    fx=np.sin(t/6)+a*np.sin(b*t)*np.cos(t)-\
       c*np.sin(16*b*t)
    fy=np.cos(t/6)+a*np.sin(b*t)*np.sin(t)-\
       c*np.cos(16*b*t)
    fx=.951*(fx-1.051*fx.min())/(fx.max()-fx.min())
    fy=.951*(fy-1.051*fy.min())/(fy.max()-fy.min())
    f=np.array([[fx[i],fy[i]] for i in range(len(t))])
    return f,np.around(a,6),b,np.around(c,3)

def interpolate_hypersphere(v1,v2,steps):
    v1norm=np.linalg.norm(v1)
    v2norm=np.linalg.norm(v2)
    v2normalized=v2*(v1norm/v2norm)
    vectors=[]
    for step in range(steps):
        interpolated=v1+(v2normalized-v1)*step/(steps-int(1))
        interpolated_norm=np.linalg.norm(interpolated)
        interpolated_normalized=\
        interpolated*(v1norm/interpolated_norm)
        vectors.append(interpolated_normalized)
    return np.array(vectors)

def create_images(coords_int,img_size_out,img_size=1024):
    imgs=[]
    for i in range(coords_int.shape[0]):
        fx=coords_int[i,:,0]; fy=coords_int[i,:,1]
        fx=np.array(np.clip(fx*img_size,0,img_size-1),dtype='int32')
        fy=np.array(np.clip(fy*img_size,0,img_size-1),dtype='int32')
        f=np.array([[fx[i],fy[i]] for i in range(len(fx))])
        img=np.ones((img_size,img_size))
        for [x,y] in f: img[y,x]=0
        img=resize(img,(img_size_out,img_size_out))
        imgs.append(img)
    return np.array(imgs)

def preprocess_img(
    file1,file2,
    file_path='../input/image-examples-for-mixed-styles/'):
    img1=io.imread(file_path+file1)
    img2=io.imread(file_path+file2)
    imgbw1=np.ones(img1.shape[:2])
    imgbw1[img1[:,:,1]<int(200)]=0
    imgbw2=np.ones(img2.shape[:2])
    imgbw2[img2[:,:,1]<int(200)]=0
    coords1=np.array(np.where(imgbw1<1)).T
    coords2=np.array(np.where(imgbw2<1)).T
    while not coords2.shape==coords1.shape:
        randi=np.random.randint(
            0,coords2.shape[0]-1,
            coords2.shape[0]-coords1.shape[0])
        coords2=np.delete(coords2,list(randi),axis=0)
    return coords1,coords2

def create_display_gif(img_size_out=256,steps=60):
    sh=randcoord(img_size_out)[0].shape
    coords=np.zeros((2,sh[0],sh[1]),dtype=np.float32)
    labels=np.zeros((2,),dtype=np.int32)
    targets=np.zeros((2,2),dtype=np.float32)
    for i in range(2):
        coord,a,b,c=randcoord(img_size_out)
        coords[i,:,:]=coord
        labels[i],targets[i,0],targets[i,1]=b-3,a,c
    coords_int=np.vstack(
        [interpolate_hypersphere(coords[1],coords[0],steps),
         interpolate_hypersphere(coords[0],coords[1],steps)])
    imgs=create_images(coords_int,img_size_out)
    file_name='pic.gif'
    imageio.mimsave(file_name,imgs)
    s1='<div id="imgs_gif"><img src="'
    s2='" height="400" width="400"></img></div>'
    display(HTML(s1+file_name+s2))
