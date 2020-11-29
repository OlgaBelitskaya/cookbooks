#unlock for running in SageMathCell 
#%%r
#svg(filename='Rplots.svg',onefile=T,width=8,height=8,
#    pointsize=12,family='times',bg='black',
#    antialias=c('default','none','gray','subpixel'))
options(repr.plot.width=8,
        repr.plot.height=8,repr.plot.bg='black')
t<-seq(0,2*pi,len=360); n=12; d=.4
x1<-cos(n*t)*cos(t); y1<-cos(n*t)*sin(t) 
x2<-(cos(n*t)+d)*cos(t); y2<-(cos(n*t)+d)*sin(t)
plot(x2,y2,type='o',cex=1,col='#3636ff',lwd=2,
     xlab='',ylab=''); par(new=TRUE); 
plot(x1,y1,type='o',cex=1,col='#ff3636',lwd=2,
     xlim=c(-1-d,1+d),ylim=c(-1-d,1+d),xlab='x',ylab='y',
     fg='white',col.axis='white',col.lab='white'); 
grid(col='white');
#dev.off()
