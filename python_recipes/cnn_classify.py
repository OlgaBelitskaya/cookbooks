import warnings; warnings.filterwarnings('ignore')
from IPython.display import display
import tensorflow as tf,numpy as np
import tensorflow.keras.layers as tkl
import tensorflow.keras.utils as tku
import tensorflow.keras.callbacks as tkc
tf.keras.backend.set_floatx('float64')

def cb(mw):
    early_stopping=tkc.EarlyStopping(
        monitor='val_loss',patience=20,verbose=2)
    checkpointer=tkc.ModelCheckpoint(
        filepath=mw,save_best_only=True,verbose=2,
        save_weights_only=True,monitor='val_accuracy',mode='max')
    lr_reduction=tkc.ReduceLROnPlateau(
        monitor='val_loss',verbose=2,patience=10,factor=.8)
    return [checkpointer,early_stopping,lr_reduction]

def main_block_cnn(channels,img_size=32,filters=32):
    model=tf.keras.Sequential()
    model.add(tkl.Input(
        (img_size,img_size,channels),name='input'))
    model.add(tkl.Conv2D(
        filters=filters,kernel_size=(7,7),
        strides=(1,1),padding='same',name='conv_1'))
    model.add(tkl.LeakyReLU(alpha=.02,name='lrelu_1'))
    model.add(tf.keras.layers.MaxPool2D(
        pool_size=(2,2),name='pool_1'))
    model.add(tkl.Dropout(.25,name='drop_1'))
    model.add(tkl.Conv2D(
        filters=3*channels*filters,kernel_size=(7,7),
        strides=(1,1),padding='same',name='conv_2'))
    model.add(tkl.LeakyReLU(alpha=.02,name='lrelu_2'))
    model.add(tf.keras.layers.MaxPool2D(
        pool_size=(2,2),name='pool_2'))
    model.add(tkl.Dropout(.25,name='drop_2'))
    model.add(tkl.Conv2D(
        filters=filters,kernel_size=(7,7),
        strides=(1,1),padding='same',name='conv_3'))
    model.add(tkl.LeakyReLU(alpha=.02,name='lrelu_3'))
    model.add(tf.keras.layers.MaxPool2D(
        pool_size=(2,2),name='pool_3'))
    model.add(tkl.Dropout(.25,name='drop_3'))
    return model

def out_block_cnn(model,dense,num_classes,plot=True):
    model.add(tkl.GlobalMaxPooling2D(name='gmpool'))   
    model.add(tkl.Dense(dense,name='dense_1'))
    model.add(tkl.LeakyReLU(alpha=.02,name='lrelu_4'))
    model.add(tkl.Dropout(.5,name='drop_4'))
    model.add(tkl.Dense(num_classes,name='out',
                        activation='softmax'))
    if plot:
        display(tku.plot_model(model,show_shapes=True))
    return model

def compile_model(model):
    return model.compile(
        optimizer=tf.keras.optimizers.Adam(),
        loss=tf.keras.losses\
        .SparseCategoricalCrossentropy(),
        metrics=['accuracy'])
