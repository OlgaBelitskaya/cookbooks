#unlock for running in SageMathCell 
#%%r
#svg(filename='Rplots.svg',onefile=T,width=10,height=10,
#    pointsize=12,family='times',bg='black',
#    antialias=c('default','none','gray','subpixel'))
options(repr.plot.width=10,repr.plot.height=10,
        repr.plot.bg='black')
a<-(.5+runif(1))*sample(c(-1,1),1); b<-sample(6:18,1) 
c<-.001*sample(1:99,1)*sample(c(-1,1),1)
t<-seq(0,36*pi,len=12*3600); c0<-'lightgray'
col<-rgb(runif(1),runif(1),runif(1))
x<-sin(t/6)-a*sin(b*t)*cos(t)-c*sin(16*b*t) 
y<-cos(t/6)-a*sin(b*t)*sin(t)-c*cos(16*b*t)
cat(c('a =',a,'b =',b,'c =',c,'color:',col,'
'))
plot(x,y,type='p',cex=.01,col=col,xlab='x',ylab='y',
     fg=c0,col.axis=c0,col.lab=c0)
grid(col=c0)
#dev.off()
