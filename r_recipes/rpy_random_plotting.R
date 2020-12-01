
pi<-np$pi; n<-24
t<-np$arange(0,2*pi,.1^3*2*pi/n)
randi<-function(nmin,nmax){np$random$randint(nmin,nmax)}
a<-randi(5,11); b<-randi(12,24); c<-randi(25,81)
d<-randi(216,256); m<-randi(100,300)
fig<-pl$figure(figsize=c(10,10)); ax<-fig$gca()
ax$set_facecolor('black')
for (i in 1:n) {
    f1<-(a+.9*np$cos(b*t+2*pi*i/n))*(1+.1*np$cos(c*t+2*pi*i/n))
    f2<-(1+.01*np$cos(d*t+2*pi*i/n))*(1+np$sin(t+2*pi*i/n)) 
    x<-f1*f2*np$cos(t); y<-f1*f2*np$sin(t)
    pl$scatter(x,y,s=.1^2) }
pl$grid()
file_name<-paste0('rpy_random_plot',
                  sample(1:9999999,1),'.png')
pl$savefig(file_name)
im<-load.image(file_name)
options(repr.plot.width=10,repr.plot.height=10)
par(mar=c(0,0,0,0)); plot(im,axes=FALSE)

