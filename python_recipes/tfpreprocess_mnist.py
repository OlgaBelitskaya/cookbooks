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

def load_mnist():
    mnist=tfds.builder('mnist')
    mnist.download_and_prepare()
    ds=mnist.as_dataset(shuffle_files=False,
                        split=['train','test'])
    mnist_train,mnist_test=ds[0],ds[1]
    dhtml(mnist.info.features['image'],c2,f2,fs2)
    dhtml(mnist.info.features['label'],c2,f2,fs2)
    mnist_train=mnist_train.map(
        lambda item:(tf.image.resize(
            tf.cast(item['image'],tf.float32),
            [img_size,img_size])/255., 
                     tf.cast(item['label'],tf.int32)))
    mnist_test=mnist_test.map(
        lambda item:(tf.image.resize(
            tf.cast(item['image'],tf.float32),
            [img_size,img_size])/255., 
                     tf.cast(item['label'],tf.int32)))
    tf.random.set_seed(123)
    mnist_train=mnist_train.shuffle(
        buffer_size=buffer_size,
        reshuffle_each_iteration=False)
    mnist_valid=mnist_train.take(buffer_size).batch(batch_size)
    mnist_train=mnist_train.skip(buffer_size).batch(batch_size)
    return mnist_train,mnist_valid,mnist_test
