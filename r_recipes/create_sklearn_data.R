# with the libraries rpy_sklearn.R
ip<-function(x) {as.integer(x)}
N<-ip(5000)

# 5000x5 matrix with 5 features (4 responsible for targets), 
# 1 target, 0.97 - the bias factor
artreg<-slds$make_regression(N,ip(5),ip(4),ip(1),.97)
nX3<-np$array(artreg[1]); ny3<-np$array(artreg[2])
X3<-array_reshape(nX3,c(N,5)); y3<-array_reshape(ny3,N)
options(repr.plot.width=10,repr.plot.height=5)
matplot(y3[1:500],X3[1:500,1:5],type='p')
print('Make Regression =>>>')
print(paste0(c('dim: features -',list(dim(X3)),
               ', target -',dim(y3)),
             collapse=' '))

ce<-array_reshape(c(1,1,-1,-1,1,-1,-1,1),c(4,2))
artclu<-slds$make_blobs(n_samples=N,cluster_std=.5,centers=ce)
nX4<-np$array(artclu[1]); ny4<-np$array(artclu[2])
X4<-array_reshape(nX4,c(N,2)); y4<-array_reshape(ny4,N)
pl$figure(figsize=c(10,5))
pl$scatter(X4[,1],X4[,2],c=y4,s=3,
           cmap=pl$cm$tab10)
pl$scatter(c(1,-1,1,-1),c(1,-1,-1,1),
           c='black',marker='*',s=150)
pl$savefig('rpy_p1.png'); im<-load.image('rpy_p1.png')
options(repr.plot.width=10,repr.plot.height=5)
par(mar=c(0,0,0,0)); plot(im,axes=FALSE)
print('Make Blobs =>>>')
print(paste0(c('dim: features -',list(dim(X4)),
               ', target -',dim(y4)),
             collapse=' '))

artmlc<-slds$make_multilabel_classification(n_classes=ip(3),
                                            n_samples=N,
                                            n_features=ip(2))
nX5<-np$array(artmlc[[1]]); ny5<-np$array(artmlc[[2]])
X5<-array_reshape(nX5,c(N,2)); y5<-array_reshape(ny5,c(N,3))
m=c('o','v','*'); a=c(.2,.5,1); s=c(500,300,100)
pl$figure(figsize=c(10,5))
for (i in 1:3) {
    pl$scatter(X5[1:50,1],X5[1:50,2],c=y5[1:50,i],s=s[i],
               marker=m[i],alpha=a[i],cmap=pl$cm$bwr)}
pl$savefig('rpy_p1.png'); im<-load.image('rpy_p1.png')
options(repr.plot.width=10,repr.plot.height=5)
par(mar=c(0,0,0,0)); plot(im,axes=FALSE)
print('Make Multilabel Classification =>>>')
print(paste0(c('dim: features -',list(dim(X5)),
               ', target -',list(dim(y5))),
             collapse=' '))