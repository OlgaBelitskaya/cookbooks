#unlock for running in SageMathCell 
#%%r
#svg(filename='Rplots.svg',onefile=T,width=10,height=10,
#    pointsize=12,family='times',bg='black',
#    antialias=c('default','none','gray','subpixel'))
options(repr.plot.width=10,repr.plot.height=10,
        repr.plot.bg='black')
a<-(.5+runif(1))*sample(c(-1,1),1); b<-sample(6:12,1)
c<-.001*sample(1:99,1)*sample(c(-1,1),1); d<-sample(4:8,1)
t<-seq(0,24*pi,len=24*18)
c0<-'whitesmoke'; c1<-rgb(runif(1),runif(1),runif(1))
x<-sin(t/6)+a*sin(b*t)*cos(t)+c*sin(b*t)
y<-cos(t/6)+a*sin(b*t)*sin(t)+c*cos(d*b*t)
cat(paste0('a=',a,'; b=',b,'; c=',c,'; d=',d,'; color:',c1,'
'))
plot(x,y,type='o',cex=.4,col=c0,lwd=3); par(new=T)
plot(x,y,type='o',cex=.3,col=c1,xlab='x',ylab='y',
     fg=c0,col.axis=c0,col.lab=c0)
grid(col=c0)
#dev.off()
