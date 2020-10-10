import numpy as np,pylab as pl,random as rd
def looped_curve(fig_size):
    r=[-1,0,1]; th=.1+rd.random()
    a,b,c=rd.randint(1,3),rd.randint(4,6),rd.randint(2,4)
    d,e,f=rd.randint(9,11),rd.randint(14,16),rd.randint(1,3)
    t=np.arange(0,2*np.pi+.5,1/10**rd.randint(1,3)) 
    fx=-d*np.cos(t)-f*np.cos(b*t)+e*np.sin(a*t)
    fy=-e*np.cos(a*t)+d*np.sin(t)-f*np.sin(b*t) 
    fz=d*np.cos(c*t)
    fig=pl.figure(figsize=(fig_size,fig_size))
    ax=fig.gca(projection='3d')
    for i in r:
        for j in r:
            for k in r:
                col=[rd.random() for l in range(3)]
                ax.plot(i*fx,j*fy,k*fz,c=col,linewidth=th)
    pl.title('$\mathbb{a=%d; b=%d; c=%d; d=%d; e=%d; f=%d}$'\
             %(a,b,c,d,e,f))
    pl.axis('off'); pl.show()