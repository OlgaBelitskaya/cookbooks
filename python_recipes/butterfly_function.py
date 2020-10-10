import numpy as np,pylab as pl
t=np.arange(0,2*np.pi,.1**4)
def col(): 
    return [np.append([1],np.random.random(2))]
def f(t): 
    return np.exp(np.cos(t)**2+np.sin(t))-3*np.cos(4*t)
def fx(k,t): return .1*(k+1)*f(t)*np.cos(t)
def fy(k,t): return .1*(k+1)*f(t)*np.sin(t)
def butterfly_function(fig_size,num_lines):
    pl.figure(figsize=(fig_size,fig_size))
    ax=pl.gca(); ax.set_facecolor('ivory')
    [pl.scatter(fx(i,t),fy(i,t),s=.1**3,c=col()) 
     for i in range(num_lines)]
    pl.grid(c='silver',alpha=.4); pl.show()