import numpy as np,pylab as pl
from IPython.core.display import display
from lightning import Lightning
lgn=Lightning(ipython=True,local=True)

def light_line(file_path,file_name,lw,cmap,w,h):
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