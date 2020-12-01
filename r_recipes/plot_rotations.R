#unlock for running in SageMathCell 
#%%r
#svg(filename='Rplots.svg',onefile=T,width=10,height=10,
#    pointsize=12,family='times',bg='black',
#    antialias=c('default','none','gray','subpixel'))
options(repr.plot.width=10,repr.plot.height=10,
        repr.plot.bg='black')
rotate_xy<-function (k,x,y){
    i<-1; xyi<-array(c(0,0),c(2*k,2))
    while (i<=2*k) {xyi[i,1]<-cos(i*pi/k)*x-sin(i*pi/k)*y 
                    xyi[i,2]<-sin(i*pi/k)*x+cos(i*pi/k)*y
                    i<-i+1}
    return(xyi)}
k<-sample(100:900,1)/1000; n<-sample(5:15,1)
m<-sample(5:9,1); r<-sample(5:35,m)
lm<-3.5+m*k+max(scale(r,4)[3:m,1])
cat(c('r:',r,'; k =',k,'n =',n,'m =',m,'
'))
for (i in 1:m) {
    ci<-rotate_xy(n,.5+k*i,.5+k*i)
    col1=rgb(runif(1),runif(1),1)
    col2=rgb(runif(1),runif(1),1,alpha=.07) 
    plot(ci[,1],ci[,2],type='p',cex=r[i],
         col=col1,xlab='',ylab='',
         xaxt='n',yaxt='n',frame=FALSE,
         xlim=c(-lm,lm),ylim=c(-lm,lm))
    par(new=T)
    plot(ci[,1],ci[,2],type='p',pch=16,cex=r[i],
         col=col2,xlab='',ylab='',
         xaxt='n',yaxt='n',frame=FALSE,
         xlim=c(-lm,lm),ylim=c(-lm,lm))
    par(new=T)}
#dev.off()
