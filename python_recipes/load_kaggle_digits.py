import numpy as np,pandas as pd,pylab as pl
from IPython.display import display
def load_kaggle_digits(k):
    df_train=pd.read_csv(
        '../input/digit-recognizer/train.csv')
    df_test=pd.read_csv(
        '../input/digit-recognizer/test.csv')
    pixel_idx=['%s%s'%('pixel',idx) 
               for idx in range(0,784)]
    train_images=np.array(
        df_train[pixel_idx].values,
                 dtype='float32').reshape(-1,28,28,1)
    train_images=(train_images/255)**k
    test_images=np.array(
        df_test[pixel_idx].values,
                dtype='float32').reshape(-1,28,28,1)
    test_images=(test_images/255)**k
    train_labels=np.array(
        df_train['label'].values,dtype='int32')
    num_classes=len(set(train_labels))
    N=train_labels.shape[0]; n=int(.1*N)
    shuffle_ids=np.arange(N)
    np.random.RandomState(12).shuffle(shuffle_ids)
    train_images=train_images[shuffle_ids]
    train_labels=train_labels[shuffle_ids]
    fig=pl.figure(figsize=(10,6))
    randch=np.random.choice(N,size=12,replace=False)
    for i,idx in enumerate(randch):
        ax=fig.add_subplot(3,4,i+1,xticks=[],yticks=[])
        ax.imshow(train_images[idx].reshape(28,28),
                  cmap=pl.cm.bone)
        ax.set_title('%d'%train_labels[idx],
                     fontsize=10)
    pl.show()
    x_test,x_valid,x_train=\
    train_images[:n],train_images[n:2*n],train_images[2*n:]
    y_test,y_valid,y_train=\
    train_labels[:n],train_labels[n:2*n],train_labels[2*n:]
    print('function outputs: \n')
    df=pd.DataFrame(
        [[x_train.shape,x_valid.shape,
          x_test.shape,test_images.shape],
         [x_train.dtype,x_valid.dtype,
          x_test.dtype,test_images.dtype],
         [y_train.shape,y_valid.shape,y_test.shape,np.nan],
         [y_train.dtype,y_valid.dtype,y_test.dtype,np.nan]],
        columns=['train','valid','test','global test'],
        index=['image shape','image type',
               'label shape','label type'])
    display(df)
    return x_train,y_train,x_valid,y_valid,\
           x_test,y_test,test_images,num_classes