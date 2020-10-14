def cnn_model(num_classes):
    model=Sequential()
    model.add(tkl.Input(shape=(28,28,1)))
    model.add(tkl.BatchNormalization())    
    model.add(tkl.Conv2D(32,(5,5),padding='same'))
    model.add(tkl.LeakyReLU(alpha=.02))
    model.add(tkl.MaxPooling2D(strides=(2,2)))
    model.add(tkl.Dropout(.25))    
    model.add(tkl.Conv2D(96,(5,5)))
    model.add(tkl.LeakyReLU(alpha=.02))
    model.add(tkl.MaxPooling2D(strides=(2,2)))
    model.add(tkl.Dropout(.25)) 
    model.add(tkl.GlobalMaxPooling2D())    
    model.add(tkl.Dense(512))
    model.add(tkl.LeakyReLU(alpha=.02))
    model.add(tkl.Dropout(.5))    
    model.add(tkl.Dense(num_classes,activation='softmax'))    
    model.compile(loss='sparse_categorical_crossentropy',
                  optimizer='nadam', 
                  metrics=[sparse_categorical_accuracy,
                           sparse_top_3_categorical_accuracy])    
    return model

def model_callbacks(weights):
    checkpoint=tkc.ModelCheckpoint(
        filepath=weights,verbose=2,save_best_only=True)
    lr_reduce=tkc.ReduceLROnPlateau(
        monitor='val_loss',patience=5,verbose=2,
        factor=.75,min_lr=.1**6)
    estop=tkc.EarlyStopping(
        monitor='val_loss',patience=20,verbose=2)
    return [checkpoint,lr_reduce,estop]


def model_history(cnn_model,weights,epochs,
                  x_train,y_train,x_valid,y_valid):
    model_history=cnn_model.fit(
        x_train,y_train,validation_data=(x_valid,y_valid), 
        epochs=epochs,batch_size=128,verbose=2, 
        callbacks=model_callbacks(weights))    
    return model_history

def plot_history(model_history,start,color):
    keys=list(model_history.history.keys())
    list_history=[model_history.history[keys[i]] 
                  for i in range(len(keys))]
    dfkeys=pd.DataFrame(list_history).T
    dfkeys.columns=keys
    fig=pl.figure(figsize=(10,12))
    ax1=fig.add_subplot(411)
    dfkeys.iloc[start:,[0,3]].plot(
        ax=ax1,color=['slategray',color])
    ax2=fig.add_subplot(412)
    dfkeys.iloc[start:,6].plot(ax=ax2,color=color)
    pl.legend()
    ax3=fig.add_subplot(413)
    dfkeys.iloc[start:,[1,4]].plot(
        ax=ax3,color=['slategray',color])
    ax3=fig.add_subplot(414)
    dfkeys.iloc[start:,[2,5]].plot(
        ax=ax3,color=['slategray',color])
    pl.show();
    display(dfkeys.tail().T)