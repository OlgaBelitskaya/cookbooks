
library(magrittr); library(keras)
cnn_model<-keras_model_sequential()
cnn_model %>%  
layer_conv_2d(
    filter=32,kernel_size=c(7,7),padding='same',
    input_shape=c(128,128,3)) %>%  
layer_activation_leaky_relu(.2) %>%  
layer_max_pooling_2d(pool_size=c(2,2)) %>%  
layer_dropout(.25) %>%
layer_conv_2d(
    filter=96,kernel_size=c(7,7),padding='same') %>% 
layer_activation_leaky_relu(.2) %>%
layer_max_pooling_2d(pool_size=c(2,2)) %>%  
layer_dropout(.25) %>%
layer_global_average_pooling_2d() %>%  
layer_dense(1024) %>%  
layer_activation('tanh') %>%  
layer_dropout(.25) %>%  
layer_dense(64) %>%  
layer_activation('tanh') %>%  
layer_dropout(.25) %>%
layer_dense(10) %>%    
layer_activation('softmax')
cnn_model %>%
    compile(loss='sparse_categorical_crossentropy',
            optimizer='nadam',metrics='accuracy')
cnn_fit<-cnn_model %>%
    fit(x=x_train,y=y_train,shuffle=TRUE,
        batch_size=16,epochs=150,callbacks=cb(model_weights),
        validation_data=list(x_valid,y_valid))

