from tensorflow.keras.models import Sequential
from tensorflow.keras import layers as tkl

def base_cnn_model(base_conv2d,last_pool,num_classes,img_size):
    model=Sequential()
    model.add(tkl.Conv2D(base_conv2d,(5,5),padding='same',
                         input_shape=(img_size,img_size,3)))
    model.add(tkl.Activation('relu'))
    model.add(tkl.MaxPooling2D(pool_size=(2,2)))
    model.add(tkl.Dropout(.25))
    model.add(tkl.Conv2D(3*base_conv2d,(5,5)))
    model.add(tkl.Activation('relu'))    
    model.add(tkl.MaxPooling2D(pool_size=(2,2)))
    model.add(tkl.Dropout(.25))
    if last_pool=='max':
        model.add(tkl.GlobalMaxPooling2D())
    if last_pool=='avg':
        model.add(tkl.GlobalAveragePooling2D())
    model.add(tkl.Dense(base_conv2d**2))
    model.add(tkl.Activation('relu'))
    model.add(tkl.Dropout(.5))         
    model.add(tkl.Dense(num_classes))
    model.add(tkl.Activation('softmax'))
    model.compile(loss='sparse_categorical_crossentropy',
                  optimizer='adam',metrics=['accuracy'])
    return model