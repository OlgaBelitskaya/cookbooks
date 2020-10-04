import numpy as np, pylab as pl
import matplotlib.patches as pt
cos=np.cos; sin=np.sin; pi=np.pi

def rotate_xy(k,x,y):
    return np.array([[cos(i*pi/k)*x-sin(i*pi/k)*y,
                      sin(i*pi/k)*x+cos(i*pi/k)*y] 
                     for i in range(2*k)])
    
def circle_center(k,m,n):
    return np.array([rotate_xy(n,.5+k*i,.5+k*i) 
                     for i in range(m)])
    
def circle_radius(m):
    return [np.random.randint(300,1200)/1000 
            for i in range(m)]

def cicle_color(rgb,m):
    if rgb=='r':
        return [[1]+[np.random.randint(100,900)/1000 
                     for j in range(2)] 
                for i in range(m)]
    if rgb=='g':
        return [[np.random.randint(100,900)/1000]+\
                 [1]+[np.random.randint(100,900)/1000] 
                for i in range(m)]
    if rgb=='b':
        return [[np.random.randint(100,900)/1000 
                 for j in range(2)]+[1] 
                for i in range(m)]

def cicle_coef():
    k=np.random.randint(100,900)/1000
    m=np.random.randint(3,9) 
    n=np.random.randint(5,15)
    return k,m,n

def circle_mandala(rgb,fig_size):
    k,m,n=cicle_coef()
    c=circle_center(k,m,n)
    r=circle_radius(m)
    l=.1+r[m-1]+c.max()
    col=cicle_color(rgb,m)
    fig,ax=pl.subplots(
        figsize=(fig_size,fig_size))
    for i in range(m):
        for j in range(2*n):
            ax.add_patch(
                pt.Circle(c[i][j],r[i],
                          alpha=.1,color=col[i]))
            ax.add_patch(
                pt.Circle(c[i][j],r[i],fill=False,
                          edgecolor=col[m-i-1]))
    pl.title('$\mathscr{k=%.3f; \ m=%d; \ n=%d}$'\
             %(k,m,n),fontsize=18)
    pl.axis('off'); pl.xlim(-l,l); pl.ylim(-l,l)
    pl.show();