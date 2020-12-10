
print('Data Preprocessing =>>>')
ip<-function(x) {as.integer(x)}
m<-sample(1:1700,1); N<-ip(5000)
ohe<-function(x) {
    x<-array_reshape(x,c(-1,1))
    tohe<-slpp$OneHotEncoder(categories='auto')
    as.matrix(tohe$fit(x)$transform(x)) }
tts<-function(X,y) {
    slms$train_test_split(
        X,y,test_size=.2,random_state=ip(1))}
cy2<-ohe(y2); cy7<-ohe(y7)
print(paste0(c(cy2[m,],'=>',y2[m]),collapse=''))
cy_train6<-ohe(y_train6)
print(paste0(c(cy_train6[m,],'=>',y_train6[m]),collapse=''))
cy_test6<-ohe(y_test6); 
print(paste0(c(cy_test6[m,],'=>',y_test6[m]),collapse=''))
print(paste0(c(cy7[m,],'=>',y7[m]),collapse=''))
X_train1<-tts(X1,y1)[[1]]; X_test1<-tts(X1,y1)[[2]]
y_train1<-tts(X1,y1)[[3]]; y_test1<-tts(X1,y1)[[4]]
print(c('train:',dim(X_train1),dim(y_train1),
        'test:',dim(X_test1),dim(y_test1)))
X_train2<-tts(X2,y2)[[1]]; X_test2<-tts(X2,y2)[[2]]
y_train2<-tts(X2,y2)[[3]]; y_test2<-tts(X2,y2)[[4]]
print(c('train:',dim(X_train2),dim(y_train2),
        'test:',dim(X_test2),dim(y_test2)))
X_train7<-tts(X7,y7)[[1]]; X_test7<-tts(X7,y7)[[2]]
y_train7<-tts(X7,y7)[[3]]; y_test7<-tts(X7,y7)[[4]]
print(c('train:',dim(X_train7),dim(y_train7),
        'test:',dim(X_test7),dim(y_test7)))

