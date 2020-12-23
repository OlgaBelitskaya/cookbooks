import warnings; warnings.filterwarnings('ignore')
import mplcyberpunk,tensorflow as tf,pylab as pl
import pandas as pd,numpy as np
import tensorflow_datasets as tfds
from IPython.display import display
pd.set_option('precision',3)
tf.keras.backend.set_floatx('float64')
tfds.disable_progress_bar()
pl.style.use('cyberpunk')

def get2img(file_name1,file_name2,
            file_path='../input/image-examples-for-mixed-styles/'):
    imgtf1=tf.image.decode_image(
        tf.io.read_file(file_path+file_name1))
    imgtf2=tf.image.decode_image(
        tf.io.read_file(file_path+file_name2))
    display(pd.DataFrame(
    [[str(imgtf1.numpy().shape),str(imgtf2.numpy().shape)],
     [imgtf1.numpy().dtype,imgtf2.numpy().dtype],
     [tf.rank(imgtf1).numpy(),tf.rank(imgtf2).numpy()]],
     index=['shape','dtype','rank'],columns=['flower','cat']))
    return imgtf1,imgtf2
def show2img(imgtf1,imgtf2,fig_size):
    pl.figure(figsize=(2*fig_size,fig_size))
    pl.subplot(1,2,1); pl.imshow(imgtf1)
    pl.subplot(1,2,2); pl.imshow(imgtf2)
    pl.tight_layout(); pl.show()
def bcrop(img,box):
    return tf.image.crop_to_bounding_box(
        img,box[0],box[1],box[2],box[3])
def ccrop(img,c):
    return tf.image.central_crop(img,c)
def hflip(img):
    return tf.image.flip_left_right(img)
def vflip(img):
    return tf.image.flip_up_down(img)
def bright(img,d):
    return tf.image.adjust_brightness(img,delta=d)
@tf.function
def preprocess(item,img_size,crop=.95,contrast=1.1):
    img,lbl=item['image'],item['label']
    img_cropped=tf.image.central_crop(img,crop)
    img_contrast=tf.image.adjust_contrast(
        img_cropped,contrast)
    img_resized=tf.image.resize(
        img_contrast,size=(img_size,img_size))
    img_flip=tf.image\
    .random_flip_left_right(img_resized)
    return (img_flip/255.,tf.cast(lbl,tf.int32))
