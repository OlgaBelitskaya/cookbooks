import numpy as np,pandas as pd,pylab as pl
from IPython.core.display import display
from sklearn.preprocessing import \
MinMaxScaler as mms
from lightning import Lightning

def lightning_connect(connect):
    host='https://public.lightning-viz.org'
    if connect:
        lgn=Lightning(ipython=True,host=host)
    else:
        lgn=Lightning(ipython=True,local=True)
    return lgn

def light_line(lgn,file_path,file_name,
               lw=1,cmap='hsv',w=680,h=300):
    series=np.loadtxt(
        file_path+file_name,delimiter=',',skiprows=1)
    if series.shape[0]>series.shape[1]:
        series=series.T
    c=np.array([pl.cm.get_cmap(cmap)(i/3)[:3]
                for i in range(3)])
    c=np.array(255*c,dtype='int32')
    viz=lgn.line(series,color=c,thickness=lw,
                 width=w,height=h)
    display(viz)
    
def light_scatter(lgn,file_path,file_name,
                  x,y,value,size,label,cmap,
                  w=680,h=300,sep='\t'):
    data=pd.read_csv(file_path+file_name,sep=sep)
    size_array=data[size].values.reshape(-1,1)
    scaler=mms(feature_range=(3,15)).fit(size_array)
    size_array=scaler.transform(size_array)
    viz=lgn.scatter(data[x].values,data[y].values,
                    values=data[value].values,
                    labels=data[label].values,
                    size=size_array.reshape(-1),
                    colormap=cmap,width=w,height=h)
    display(viz)
