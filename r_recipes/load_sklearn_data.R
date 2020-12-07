# with the libraries rpy_sklearn.R
boston<-slds$load_boston()
X1<-boston$data; y1<-boston$target
dfboston<-data.frame(boston$data)
colnames(dfboston)<-boston$feature_names
dfboston['MEDV']<-boston$target
ip<-function(x) {as.integer(x)}
fig<-pl$figure(figsize=c(10,5))
ax<-fig$add_subplot('111')
sn$histplot(dfboston['MEDV'],stat='density',ax=ax,
            kde='True',bins=ip(30),
            edgecolor='#ff3696',alpha=.1)
pd$plotting$table(ax,head(dfboston,3),loc='top')
pl$tight_layout()
pl$savefig('rpy_p1.png'); im<-load.image('rpy_p1.png')
options(repr.plot.width=10,repr.plot.height=5)
par(mar=c(0,0,0,0)); plot(im,axes=FALSE)
print('Boston Data =>>>')
print(paste0(c('dim: features -',list(dim(X1)),
               ', target -',list(dim(y1))),
             collapse=' '))