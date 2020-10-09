import h5py,os,pandas as pd,numpy as np
import seaborn as sn,pylab as pl
from IPython.display import display,HTML
# Crayola Colors
c1,c2,c3,c4,c5,c6,c7,c8,c9,c10=\
'#FF355E','#FF6037','#FF9966','#FFCC33','#FFFF66',\
'#CCFF00','#66FF66','#50BFE6','#FF6EFF','#FF00CC'
fs1,fs2,fs3,fs4,fs5,fs6,fs7,fs8=10,12,14,16,18,20,25,30
f1,f2,f3,f4,f5,f6,f7=\
'Smokum','Akronim','Wallpoet','Orbitron',\
'Ewert','Lobster','Roboto'

def dhtml(string,fontcolor=c1,font=f1,fontsize=fs7):
    display(HTML("""<style>
    @import 'https://fonts.googleapis.com/css?family="""\
    +font+"""&effect=3d-float';</style>
    <h1 class='font-effect-3d-float' 
    style='font-family:"""+font+\
    """; color:"""+fontcolor+\
    """; font-size:"""+str(fontsize)+"""px;'>
    %s</h1>"""%string))

def h5file2data(h5file,cmap):
    with h5py.File(h5file,'r') as f:
        keys=list(f.keys())
        dhtml('file keys: '+', '.join(keys))
        images=np.array(f[keys[0]])
        labels=np.array(f[keys[1]])
        names=[el.decode('utf-8') 
               for el in f[keys[2]]]
        f.close()
    del h5file
    N=labels.shape[0]; n=int(.1*N)
    shuffle_ids=np.arange(N)
    np.random.RandomState(12).shuffle(shuffle_ids)
    images=images[shuffle_ids]
    labels=labels[shuffle_ids]
    x_test,x_valid,x_train=\
    images[:n],images[n:2*n],images[2*n:]
    y_test,y_valid,y_train=\
    labels[:n],labels[n:2*n],labels[2*n:]
    dhtml('function outputs: ')
    df=pd.DataFrame([[x_train.shape,x_valid.shape,x_test.shape],
                     [x_train.dtype,x_valid.dtype,x_test.dtype],
                     [y_train.shape,y_valid.shape,y_test.shape],
                     [y_train.dtype,y_valid.dtype,y_test.dtype]],
                    columns=['train','valid','test'],
                    index=['image shape','image type',
                           'label shape','label type'])
    display(df)
    dhtml('distribution of labels: ')
    df=pd.DataFrame(labels,columns=['label'])
    df['name']=[names[l] for l in labels]
    pl.figure(figsize=(7,5))
    sn.countplot(y='name',data=df,
                 palette=cmap,alpha=.5)
    pl.show()
    return names,x_train,x_valid,x_test,\
           y_train,y_valid,y_test
           
def display_images(images,labels,names,n):
    fig=pl.figure(figsize=(10,n//2))
    randch=np.random.choice(
        len(labels),size=n,replace=False)
    for i,idx in enumerate(randch):
        ax=fig.add_subplot(
            n//4,4,i+1,xticks=[],yticks=[])
        ax.imshow(images[idx])
        label=names[labels[idx]]
        ax.set_title("{} * {}"\
                     .format(labels[idx],label),
                     fontsize=10)
    pl.show()