
library(magrittr); library(keras)
rnn_model<-keras_model_sequential()
rnn_model %>% 
layer_batch_normalization(input_shape=c(1,128*128*3)) %>% 
layer_lstm(196,return_sequences=TRUE) %>%  
layer_lstm(196,return_sequences=TRUE) %>%
layer_lstm(196) %>%
layer_batch_normalization() %>% 
layer_dense(1024) %>%
layer_activation('relu') %>%
layer_dropout(.5) %>% 
layer_dense(10) %>%    
layer_activation('softmax')
rnn_model %>%
    compile(loss='sparse_categorical_crossentropy',
            optimizer='adam',metrics='accuracy')
dd2<-c(-1,1,128*128*3)
rnn_fit<-rnn_model %>%
    fit(x=array_reshape(x_train,dd2),y=y_train,shuffle=TRUE,
        batch_size=64,epochs=200,callbacks=cb(model_weights),
        validation_data=list(array_reshape(x_valid,dd2),y_valid))

