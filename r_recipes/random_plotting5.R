#unlock for running in SageMathCell 
#%%r
#svg(filename='Rplots.svg',onefile=T,width=10,height=10,
#    pointsize=12,family='times',bg='black',
#    antialias=c('default','none','gray','subpixel'))
options(repr.plot.width=10,repr.plot.height=10,
        repr.plot.bg='black')
tmin<--pi; tmax<-pi; n<-36; t<-seq(0,2*pi,len=360)
c0<-'slategray'
for (i in 1:n) {
    f<-(sample(8:11,1)+.9*cos(sample(12:24,1)*t+
        2*pi*i/n))*(1+.1*cos(sample(25:81,1)*t+
        2*pi*i/n))*(1+.05*cos(sample(216:256,1)*t+
        2*pi*i/n))*(1+sin(t+2*pi*i/n))
    x<-f*cos(t); y<-f*sin(t)
    plot(x,y,type='o',xlim=c(-27,27),ylim=c(-27,27),
         col=rgb(runif(1),runif(1),runif(1)),
         cex=.3,lwd=.7,xlab='x',ylab='y',
         fg=c0,col.axis=c0,col.lab=c0); par(new=T)}
grid(col=c0)
#dev.off()
