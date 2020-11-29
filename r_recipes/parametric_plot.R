#unlock for running in SageMathCell 
#%%r
#svg(filename='Rplots.svg',onefile=T,width=8,height=8,
#    pointsize=12,family='times',bg='slategray',
#    antialias=c('default','none','gray','subpixel'))
options(repr.plot.width=8,repr.plot.height=8,
        repr.plot.bg='slategray')
T<-seq(from=0,to=2*pi,by=.01*pi)
col<-function(i) {rgb(.005*i,0,1-.005*i)}
curve<-function(t) {list(sin(2*t),sin(5*t))}
X<-sapply(T,curve)[1,]; Y<-sapply(T,curve)[2,] 
for(i in 1:200){
    plot(X[i],Y[i],pch=13,cex=1.5,
         xlim=c(-1.2,1.2),ylim=c(-1.2,1.2),
         col=col(i),xlab='x',ylab='y')
    par(new=TRUE)}
grid(col='black');
#dev.off()
