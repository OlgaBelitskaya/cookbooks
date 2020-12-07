# with the libraries rpy_sklearn.R
boston<-slds$load_boston()
X1<-boston$data; y1<-boston$target
dfboston<-data.frame(boston$data)
colnames(dfboston)<-boston$feature_names
dfboston['MEDV']<-boston$target
print('Boston Data =>>>')
print(paste0(c('dim: features -',list(dim(X1)),
               ', target -',list(dim(y1))),
             collapse=' '))

digits<-slds$load_digits()
X2<-digits$data; y2<-digits$target
print('Digit Data =>>>')
print(paste0(c('dim: features -',list(dim(X2)),
               ', target -',list(dim(y2))),
             collapse=' '))
par(mar=c(0,0,0,0)); n<-sample(dim(X2)[1],1)
im<-array_reshape(X2[n,]/max(X2),c(8,8))
options(repr.plot.width=3,repr.plot.height=3)
plot(as.raster(im))