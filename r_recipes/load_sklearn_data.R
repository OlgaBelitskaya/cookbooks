# with libraries rpy_sklearn.R
print('Boston Data =>>>')
boston<-slds$load_boston()
X1<-boston$data; y1<-boston$target
print(paste0(c('dim: features -',list(dim(X1)),
               ', target -', dim(y1)),
             collapse=' '))
dfboston<-data.frame(boston$data)
colnames(dfboston)<-boston$feature_names
dfboston['MEDV']<-boston$target

print('Digit Data =>>>')
digits<-slds$load_digits()
X2<-digits$data; y2<-digits$target
print(paste0(c('dim: features -',list(dim(X2)),
               ', target -', dim(y2)),
             collapse=' '))