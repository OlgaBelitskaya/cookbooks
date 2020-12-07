# with the libraries rpy_sklearn.R
mnist<-ks$datasets$mnist$load_data()
train6<-mnist[[1]]; test6<-mnist[[2]]
X_train6<-array_reshape(np$array(train6[[1]]),c(60000,784))
X_train6<-X_train6/max(X_train6)
y_train6<-np$array(train6[[2]])
X_test6<-array_reshape(np$array(test6[[1]]),c(10000,784))
X_test6<-X_test6/max(X_test6)
y_test6<-np$array(test6[[2]])
im<-array_reshape(X_train6[n,],c(28,28))
options(repr.plot.width=3,repr.plot.height=3)
par(mar=c(0,0,0,0)); plot(as.raster(im))
print('MNIST Keras =>>>')
print(paste0(c(
    'train features -',list(dim(X_train6)),
    ', train target -',list(dim(y_train6))),
    collapse=' '))
print(paste0(c('test features -',list(dim(X_test6)),
    ', test target -',list(dim(y_test6))),
    collapse=' '))

fpath<-'../input/classification-of-handwritten-letters/'
fname<-'LetterColorImages_123.h5'
f<-h5$File(paste0(fpath,fname),'r')
keys<-list(f$keys())
letters<-'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
X7<-array_reshape(np$array(f['images'])/255,c(-1,32*32*3))
y7<-np$array(f['labels'])
im<-array_reshape(X7[n,],c(32,32,3))
options(repr.plot.width=3,repr.plot.height=3)
par(mar=c(0,0,0,0)); plot(as.raster(im))
print('Letters Kaggle =>>>')
print(paste0(c('keys: ',keys)))
print(paste0(
    c('dim: features -',list(dim(X7)),
      ', target -',list(dim(y7))),
    collapse=' '))
print(substring(letters,y7[n],y7[n]))