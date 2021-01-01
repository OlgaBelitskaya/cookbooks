import warnings; warnings.filterwarnings('ignore')
import tensorflow as tf
import tensorflow.keras.layers as tkl
import tensorflow.keras.utils as tku
from IPython.core.magic import register_line_magic
from IPython.display import display

@register_line_magic
def get_model_plot1d(pars):
    pars=pars.split()
    num_timesteps=int(pars[0])
    num_features=int(pars[1])
    num_filters=int(pars[2])
    ks=int(pars[3])
    ps=int(pars[4])
    model=tf.keras.Sequential()
    model.add(tkl.InputLayer((num_timesteps,
                              num_features),
                             name='input'))
    model.add(tkl.Conv1D(
        filters=num_filters,
        kernel_size=ks,
        padding='same',name='conv1d',
        activation='relu'))
    model.add(tkl.MaxPool1D(
        pool_size=ps,name='pool1d'))
    display(tku.plot_model(model,show_shapes=True))

@register_line_magic
def get_model_plot2d(pars):
    pars=pars.split()
    img_size=int(pars[0])
    num_channels=int(pars[1])
    num_filters=int(pars[2])
    ks=int(pars[3])
    ps=int(pars[4])
    model=tf.keras.Sequential()
    model.add(tkl.InputLayer((img_size,img_size,
                              num_channels),
                             name='input'))
    model.add(tkl.Conv2D(
        filters=num_filters,
        kernel_size=(ks,ks),strides=(1,1),
        padding='same',name='conv2d',
        activation='relu'))
    model.add(tkl.MaxPool2D(
        pool_size=(ps,ps),name='pool2d'))
    display(tku.plot_model(model,show_shapes=True))
