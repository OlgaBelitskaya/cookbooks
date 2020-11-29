#unlock for running in SageMathCell 
#%%r
#svg(filename='Rplots.svg',onefile=T,width=10,height=10,
#    pointsize=12,family='times',bg='whitesmoke',
#    antialias=c('default','none','gray','subpixel'))
options(repr.plot.width=10,repr.plot.height=10,
        repr.plot.bg='whitesmoke')
a<-.01*sample(30:99,1); b<-.01*sample(30:99,1)
c<-.01*sample(30:99,1); d<-max(a,2*b,3*c)
cat(c('a =',a,'b =',b,'c =',c,'
'))
n=sample(5:10,1); w=144; c0<-'slategray'
coli<-function(){rgb(runif(1),runif(1),runif(1))}
t1<-seq(0,8.95*pi,len=w*n)
x1<-sin(1.9*t1)*cos(t1); y1<-sin(1.9*t1)*sin(t1)
t2<-seq(0,12.18*pi,len=w*n)
x2<-2*sin(2.3*t2)*cos(t2); y2<-2*sin(2.3*t2)*sin(t2)
t3<-seq(0,11.77*pi,len=w*n)
x3<-3*sin(1.7*t3)*cos(t3); y3<-3*sin(1.7*t3)*sin(t3)
plot(a*x1,a*y1,type='o',pch=sample(0:18,1),cex=.1,
     col=coli(),lwd=1,xlab='',ylab='',
     xlim=c(-d,d),ylim=c(-d,d)); par(new=TRUE)
plot(b*x2,b*y2,type='o',pch=sample(0:18,1),cex=.2,
     col=coli(),lwd=1,xlab='',ylab='',
     xlim=c(-d,d),ylim=c(-d,d)); par(new=TRUE)
plot(c*x3,c*y3,type='o',pch=sample(0:18,1),cex=.3,
     col=coli(),lwd=1,xlim=c(-d,d),ylim=c(-d,d),
     xlab='x',ylab='y',fg=c0,col.axis=c0,col.lab=c0)
grid(col=c0)
#dev.off()
