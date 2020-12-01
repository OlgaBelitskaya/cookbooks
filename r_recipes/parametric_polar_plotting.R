#unlock for running in SageMathCell 
#%%r
#svg(filename='Rplots.svg',onefile=T,width=10,height=10,
#    pointsize=12,family='times',bg='black',
#    antialias=c('default','none','gray','subpixel'))
options(repr.plot.width=10,repr.plot.height=10,
        repr.plot.bg='black')
t<-seq(0,2*pi,len=360); c0<-'slategray'
f<-exp(cos(t)^2+sin(t))-3*cos(4*t)+sin(t/12)
x<-f*cos(t); y<-f*sin(t) 
for(i in 1:25) {
    plot(.04*i*x,.04*i*y,type='l',
         cex=.7,col=rgb(.04*i,0,1-.04*i),
         xlim=c(-6,6),ylim=c(-4,6),xlab='x',ylab='y',
         fg=c0,col.axis=c0,col.lab=c0)
    par(new=T)}
grid(col=c0)
#dev.off()
