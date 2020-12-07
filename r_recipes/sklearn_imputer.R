# with the libraries rpy_sklearn.R
X<-np$random$randn(ip(100))
ch<-np$random$choice(ip(100),ip(20))
X[ch]<-np$nan
X<-np$reshape(X,c(ip(100),ip(1)))
mean_imp<-slim$SimpleImputer(strategy='mean')
median_imp<-slim$SimpleImputer(strategy='median')
dfX<-pd$DataFrame(
    cbind(X,mean_imp$fit(X)$transform(X),
          median_imp$fit(X)$transform(X)))
options(repr.plot.width=10,repr.plot.height=7)
matplot(dfX,type='p',main='Sklearn Simple Imputer')
grid() 
legend(80,2,c('1->X','2->X mean','3->X median'),bty='n')