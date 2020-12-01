#unlock for running in SageMathCell 
#%%r
#svg(filename='Rplots.svg',onefile=T,width=10,height=10,
#    pointsize=12,family='times',bg='black',
#    antialias=c('default','none','gray','subpixel'))
options(repr.plot.width=10,repr.plot.height=10,
        repr.plot.bg='black')
gen<-function (a,b,n) {i<-1; xyi<-array(c(0,0),c(n,2))
    while (i<=n-1) {xi<-1-(.2+.01*a)*xyi[i,1]**2+xyi[i,2]
                    yi<-(.9991+.0001*b)*xyi[i,1]; 
                    i<-i+1; xyi[i,1]<-xi; xyi[i,2]<-yi}
    return(xyi)}
xyn<-gen(0,0,7000); c0<-'slategray'
c1<-rgb(runif(1),runif(1),runif(1))
plot(xyn[,1],xyn[,2],type='p',
     cex=.1,col=c1,xlab='x',ylab='y',
     fg=c0,col.axis=c0,col.lab=c0)
grid(col=c0)
#dev.off()
