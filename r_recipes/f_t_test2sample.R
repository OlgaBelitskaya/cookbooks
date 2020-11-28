
# samples are random, independent, 
# from normally distributed statistical population
#unlock the magic command in SageMathCell
#%%r
a<-rnorm(16); b<-rnorm(16)
print(a); print(b)
print(var.test(a,b))
print(qf(0.95,15,15))
print(t.test(a,b,var.equal=TRUE,paired=FALSE))
print(qt(.975,30))
