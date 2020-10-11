import pylab as pl,numpy as np
from mpl_toolkits.mplot3d import Axes3D
def quivers(num,fig_size): 
    t=((3*num/10)**2+2)**.5
    cq=np.arange(0,1,.13)
    cq=np.concatenate((cq,np.repeat(cq,2)))
    xq=np.array([1,-1,1,-1,1,-1,1,-1])
    yq=np.array([1,1,-1,-1,1,1,-1,-1])
    zq=np.array([1,1,1,1,-1,-1,-1,-1])
    f=pl.figure(figsize=(fig_size,fig_size))
    ax=f.add_subplot(111,projection='3d')
    for k in range(num):
        q=ax.quiver(8*[0],8*[0],8*[0],
                    xq,yq,3*(k+1)*zq/10,
                    lw=5,alpha=.5,
                    colors=pl.cm.hsv(cq))
    ax.set_xlabel('$\mathscr{X}$',fontsize=15)
    ax.set_ylabel('$\mathscr{Y}$',fontsize=15) 
    ax.set_zlabel('$\mathscr{Z}$',fontsize=15)
    ax.set_xlim(-t,t)
    ax.set_ylim(-t,t)
    ax.set_zlim(-t,t)
    pl.show()