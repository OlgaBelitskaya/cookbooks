
library(magrittr); library(keras)
mlp_model<-keras_model_sequential()
mlp_model %>%  
layer_dense(128,input_shape=c(128*128*3)) %>%  
layer_activation_leaky_relu(.2) %>%  
layer_batch_normalization() %>%  
layer_dense(256) %>%  
layer_activation_leaky_relu(.2) %>%  
layer_batch_normalization() %>%
layer_dense(512) %>%  
layer_activation_leaky_relu(.2) %>%  
layer_batch_normalization() %>%
layer_dense(1024) %>%  
layer_activation('relu') %>%  
layer_dropout(.2) %>% 
layer_dense(10) %>%    
layer_activation('softmax')
mlp_model %>%
    compile(loss='sparse_categorical_crossentropy',
            optimizer='adam',metrics='accuracy')
mlp_fit<-mlp_model %>%
    fit(x=array_reshape(x_train,dd),y=y_train,shuffle=TRUE,
        batch_size=24,epochs=120,callbacks=cb(model_weights),
        validation_data=list(array_reshape(x_valid,dd),y_valid))

