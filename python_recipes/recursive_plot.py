import numpy as np,pylab as pl

def gen(f,a,b,n):
    i=1; xyi=[0.,0.]
    while i<=n:
        yield xyi; i+=1; xi,yi=xyi[0],xyi[1]
        xyi=[f(xi,yi,a,b),xi]

def recursive_plot(f,a,b,n,fig_size=10,
                   face_color='ghostwhite'):
    xy=gen(f,a,b,n)
    xyn=np.array([el for el in xy])
    pl.figure(figsize=(fig_size,fig_size))
    ax=pl.gca(); ax.set_facecolor(face_color)
    if n>25000: ms=n*.1**6 
    else: ms=.1
    pl.scatter(xyn[:,0],xyn[:,1],
               s=ms,c=[np.random.random(3)])
    pl.tight_layout(); pl.axis('off'); pl.show()

def recursive_f1(x,y,a,b):
    return (1+.1**2*a)*abs(x)-(1+.1**5*b)*y+1