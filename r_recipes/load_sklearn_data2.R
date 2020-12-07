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