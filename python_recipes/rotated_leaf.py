import numpy as np,pylab as pl
def randi(nmin,nmax): 
    return np.random.randint(nmin,nmax)
def rotated_leaf(n,ms,fig_size):
    t=np.arange(0,2*np.pi,.1**(ms+1)*2*np.pi/n)
    a,b,c=randi(5,11),randi(12,24),randi(25,81)
    d,m=randi(216,256),randi(100,300)
    pl.figure(figsize=(fig_size,fig_size))
    ax=pl.gca(); ax.set_facecolor('black')
    for i in range(n):
        f1=a+.9*np.cos(b*t+2*np.pi*i/n)
        f2=1+.1*np.cos(c*t+2*np.pi*i/n)
        f3=1+.01*np.cos(d*t+2*np.pi*i/n)
        f4=1+np.sin(t+2*np.pi*i/n)
        x=f1*f2*f3*f4*np.cos(t)
        y=f1*f2*f3*f4*np.sin(t)
        pl.scatter(x,y,s=.1**ms,
                   c=[np.random.random(3)])
    pl.title('$\mathscr{a=%d; \; b=%d; c=%d; \;}$'%(a,b,c)+\
             '$\mathscr{d=%d; \; m=%d}$'%(d,m),
             fontsize=20)
    pl.show()