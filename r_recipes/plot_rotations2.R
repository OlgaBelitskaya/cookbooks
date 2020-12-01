#unlock for running in SageMathCell 
#%%r
#svg(filename='Rplots.svg',onefile=T,width=10,height=10,
#    pointsize=12,family='times',bg='black',
#    antialias=c('default','none','gray','subpixel'))
options(repr.plot.width=10,repr.plot.height=10,
        repr.plot.bg='black')
a<-sample(5:9,1); b<-sample(10:14,1)
c<-sample(15:19,1); q<-2*sample(3:10,1) 
n<-sample(4:16,1); l<-5; t<-seq(1,2*n+1,1)
cat(c('a =',a,'b =',b,'c =',c,'q =',q,'n =',n,'
'))
par(mar=c(0,0,0,0))
plot(0,0,type='n',xlim=c(-l,l),ylim=c(-l,l),
     xlab='',ylab='',xaxt='n',yaxt='n',frame=FALSE)
for (k in 1:q) {
    col1=rgb(runif(1)/2,runif(1)/2,1)
    col2=rgb(runif(1),runif(1),1,alpha=.1)
    par(mar=c(0,0,0,0))
    fy<-cos(pi*t/n+2*k*pi/q)+cos(a*pi*t/n+2*k*pi/q)+
        cos(b*pi*t/n+2*k*pi/q)+cos(c*pi*t/n+2*k*pi/q)
    fx<-sin(pi*t/n+2*k*pi/q)-sin(a*pi*t/n+2*k*pi/q)+
        sin(b*pi*t/n+2*k*pi/q)-sin(c*pi*t/n+2*k*pi/q)
    polygon(1.5*fx,1.2*fy,col=col2,border=FALSE,
            xlab='',ylab='',xlim=c(-l,l),ylim=c(-l,l),
            xaxt='n',yaxt='n'); par(new=T)
    polygon(fx,fy,lwd=1,border=col1,xlab='',ylab='',
            xlim=c(-l,l),ylim=c(-l,l),
            xaxt='n',yaxt='n'); par(new=T)}
#dev.off()
