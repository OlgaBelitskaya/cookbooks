#unlock for running in SageMathCell 
#%%r
#svg(filename='Rplots.svg',onefile=T,width=8,height=3,
#    pointsize=12,family='times',bg='white',
#    antialias=c('default','none','gray','subpixel'))
options(repr.plot.width=8,repr.plot.height=3)
col.list<-c('skyblue','red2','coral','orchid3',
            'bisque','tan','green3','blue4')
plot(1:8,rep(1.5,8),axes=FALSE,pch=15,cex=7,
     col=col.list,xlab=NA,ylab=NA,
     xlim=c(1,8),ylim=c(1,2))
axis(1,at=1:8,labels=sprintf('%s',col.list),
     col='white',cex.axis=1.2,padj=-2)
#dev.off()
