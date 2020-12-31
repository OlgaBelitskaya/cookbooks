import warnings; warnings.filterwarnings('ignore')
import tensorflow as tf,numpy as np,pandas as pd
import tensorflow_datasets as tfds
from IPython.display import display,HTML
pd.set_option('precision',3)
tf.keras.backend.set_floatx('float64')
tfds.disable_progress_bar()
img_size=32
buffer_size,batch_size=10000,64

c1,c2,f1,f2,fs1,fs2=\
'#11ff66','#6611ff','Wallpoet','Orbitron',20,10

def dhtml(string,fontcolor=c1,font=f1,fontsize=fs1):
    display(HTML("""<style>
    @import 'https://fonts.googleapis.com/css?family="""\
    +font+"""&effect=3d-float';</style>
    <h1 class='font-effect-3d-float' 
    style='font-family:"""+font+\
    """; color:"""+fontcolor+\
    """; font-size:"""+str(fontsize)+"""px;'>
    %s</h1>"""%string))

def load_cifar():
    cifar=tfds.builder('cifar10')
    cifar.download_and_prepare()
    ds=cifar.as_dataset(shuffle_files=False,
                        split=['train','test'])
    cifar_train,cifar_test=ds[0],ds[1]
    dhtml(cifar.info.features['image'],c2,f2,fs2)
    dhtml(cifar.info.features['label'],c2,f2,fs2)
    cifar_train=cifar_train.map(
        lambda item:(tf.cast(item['image'],tf.float32)/255., 
                     tf.cast(item['label'],tf.int32)))
    cifar_test=cifar_test.map(
        lambda item:(tf.cast(item['image'],tf.float32)/255., 
                      tf.cast(item['label'],tf.int32)))
    tf.random.set_seed(123)
    cifar_train=cifar_train.shuffle(
        buffer_size=buffer_size,
        reshuffle_each_iteration=False)
    cifar_valid=cifar_train.take(buffer_size).batch(batch_size)
    cifar_train=cifar_train.skip(buffer_size).batch(batch_size)
    return cifar_train,cifar_valid,cifar_test   
