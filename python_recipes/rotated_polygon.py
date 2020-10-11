import pylab as pl
import matplotlib.patches as pt
import numpy as np,random as rd
def fy(t,k,a,b,c,q,n): 
    return np.cos(np.pi*t/n+2*k*np.pi/q)+\
           np.cos(a*np.pi*t/n+2*k*np.pi/q)+\
           np.cos(b*np.pi*t/n+2*k*np.pi/q)+\
           np.cos(c*np.pi*t/n+2*k*np.pi/q)
def fx(t,k,a,b,c,q,n): 
    return np.sin(np.pi*t/n+2*k*np.pi/q)-\
           np.sin(a*np.pi*t/n+2*k*np.pi/q)+\
           np.sin(b*np.pi*t/n+2*k*np.pi/q)-\
           np.sin(c*np.pi*t/n+2*k*np.pi/q)
def rotated_polygon(fig_size):
    a,b,c,q=rd.randint(5,9),rd.randint(10,14),\
            rd.randint(15,19),2*rd.randint(3,6) 
    n=rd.randint(5,17); yl=5.5
    st='$\mathbb{a=%d; \; b=%d; \; c=%d;'+\
       ' \; q=%d; \; n=%d}$'
    L=np.array([[[fx(t,k,a,b,c,q,n),fy(t,k,a,b,c,q,n)] 
                 for t in range(2*n)] 
                for k in range(2*q)])
    LT=[[[1.5*fx(t,k,a,b,c,q,n),1.2*fy(t,k,a,b,c,q,n)] 
         for t in range(2*n)] for k in range(2*q)]
    pl.figure(figsize=(fig_size,fig_size))
    ax=pl.gca(); pl.axis('off')
    for k in range(2*q):
        col=np.array([rd.randint(100,900)/1000 
                      for l in range(2)]+[1])
        ax.add_patch(pt.Polygon(
            LT[k],alpha=.1,color=col))
        ax.add_patch(pt.Polygon(
            L[k],fill=False,color=col/2,lw=.3))
    pl.title(st%(a,b,c,q,n))
    pl.xlim(-yl,yl); pl.ylim(-yl,yl); pl.show()