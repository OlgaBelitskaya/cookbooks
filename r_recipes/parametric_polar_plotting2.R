#unlock for running in SageMathCell 
#%%r
#svg(filename='Rplots.svg',onefile=T,width=10,height=10,
#    pointsize=12,family='times',bg='black',
#    antialias=c('default','none','gray','subpixel'))
options(repr.plot.width=10,repr.plot.height=10,
        repr.plot.bg='black')
t<-seq(0,2*pi,len=720); c0<-'slategray'
f1<-(7+.9*cos(12*t))*(1+.05*cos(48*t))
f2<-(1+.05*cos(216*t))*(1+sin(t))
x<-f1*f2*cos(t); y<-f1*f2*sin(t)
for(i in 1:25) {
    plot(i*x,i*y,type='l',cex=.7,col=rgb(0,.04*i,0),
         xlim=c(-270,270),ylim=c(-80,460),xlab='x',ylab='y',
         fg=c0,col.axis=c0,col.lab=c0)
    par(new=T)}
grid(col=c0)
#dev.off()
