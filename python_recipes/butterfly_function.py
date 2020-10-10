import numpy,pylab; pi=numpy.pi; t=numpy.arange(0,2*pi,.1**4)
def col(): return [numpy.append([1],numpy.random.random(2))]
def f(t): return numpy.exp(numpy.cos(t)**2+numpy.sin(t))-3*numpy.cos(4*t)
def fx(k,t): return .1*(k+1)*f(t)*numpy.cos(t)
def fy(k,t): return .1*(k+1)*f(t)*numpy.sin(t)
pylab.figure(figsize=(10,10)); ax=pylab.gca(); ax.set_facecolor('ivory')
[pylab.scatter(fx(i,t),fy(i,t),s=.1**3,c=col()) for i in range(12)]
pylab.grid(c='silver',alpha=.4); pylab.show()