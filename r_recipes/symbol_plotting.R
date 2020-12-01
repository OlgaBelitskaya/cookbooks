#unlock for running in SageMathCell 
#%%r
#svg(filename='Rplots.svg',onefile=T,width=10,height=10,
#    pointsize=12,family='times',bg='black',
#    antialias=c('default','none','gray','subpixel'))
options(repr.plot.width=10,repr.plot.height=10,
        repr.plot.bg='black')
x<-seq(-2.1,2.1,len=90); y1<-exp(-x^2)
y2<--exp(-x^2); y3<-exp(-x^2)*sin(pi*x^3)
colors<-c('slategray','#3636ff','#ff3636','#ff36ff')
plot(x,y1,type='o',cex=.7,col=colors[2],
     xlim=c(-2.2,2.2),ylim=c(-1,1),xlab='x',ylab='y',
     fg=colors[1],col.axis=colors[1],col.lab=colors[1]) 
lines(x,y2,type='o',cex=.7,col=colors[3])
df<-data.frame(x=x,y=y3)
df$utf_sym<-sapply((32:121),intToUtf8)
points(df$x,df$y,pch=df$utf_sym,
       cex=.9,col=colors[4])
grid(col=colors[1])
#dev.off()
