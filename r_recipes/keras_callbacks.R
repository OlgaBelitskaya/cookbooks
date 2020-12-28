
library(keras)
model_weights<-'/checkpoints'
cb<-function(model_weights){
    checkpoint<-callback_model_checkpoint(
        model_weights,monitor='val_loss',mode='min',
        save_best_only=TRUE,save_weights_only=TRUE)
    reduce_lr<-callback_reduce_lr_on_plateau(
        monitor='val_loss',factor=.75)
    early_stopping<-callback_early_stopping(
        monitor='val_acc',patience=120)
    return(list(checkpoint,reduce_lr,early_stopping))}

