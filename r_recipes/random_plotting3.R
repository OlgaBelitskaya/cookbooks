#unlock for running in SageMathCell 
#%%r
#svg(filename='Rplots.svg',onefile=T,width=10,height=10,
#    pointsize=12,family='times',bg='black',
#    antialias=c('default','none','gray','subpixel'))
options(repr.plot.width=10,repr.plot.height=10,
        repr.plot.bg='black')
a<-sample(5:11,1); b<-sample(13:19,1)
c<-2*sample(3:10,1); n<-sample(18:144,1)
cat(c('a =',a,'b =',b,'c =',c,'n =',n,'
'))
t<-seq(1,2*n+1,1); c1=rgb(runif(1),runif(1),1,alpha=.4)
plot(0,0,type='n',xlab='',ylab='',
     xlim=c(-3,3),ylim=c(-3,3))
for (k in 1:c){
    fx<-sin(pi*t/n+k*2*pi/c)-sin(a*pi*t/n+k*2*pi/c)+
        sin(b*pi*t/n+k*2*pi/c)
    fy<-cos(pi*t/n+k*2*pi/c)+cos(a*pi*t/n+k*2*pi/c)+
        cos(b*pi*t/n+k*2*pi/c)
    polygon(fx,fy,lwd=1,border=c1,xlab='',ylab='',
            xlim=c(-3,3),ylim=c(-3,3)); par(new=T)}
#dev.off()
