import numpy as np,pylab as pl

def randi(nmin,nmax): 
    return np.random.randint(nmin,nmax)

def t(i,k,p): 
    return np.arange(
        (i-1)*np.pi/(2*k+2),i*np.pi/(2*k+2),1/10**p)
    
def x(a,b,i,k,p): 
    return np.cos(t(i,k,p)+k*np.pi/6)+\
           np.cos(a*t(i,k,p))/2+\
           np.sin((a+b)*t(i,k,p))/3

def y(a,b,i,k,p): 
    return np.sin(t(i,k,p)+k*np.pi/6)+\
           np.sin(a*t(i,k,p))/2+\
           np.cos((a+b)*t(i,k,p))/3

def mcolors(rgb,m):
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

def random_pattern_plot(rgb,fig_size):      
    a,b,p=randi(3,18),randi(10,30),5
    cols=mcolors(rgb,24)
  
    pl.figure(figsize=(fig_size,fig_size))
    ax=pl.gca()
    for i in range(48):
        for k in range(12): 
            pl.scatter(x(a,b,i,k,p),
                       y(a,b,i,k,p),
                       s=.1**(p-1),c=[cols[k]])
    pl.title('$\mathscr{a=%d; \; b=%d;}$'%(a,b),
             fontsize=20)
    pl.axis('off'); pl.show()