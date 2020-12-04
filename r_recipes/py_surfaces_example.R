
options(repr.plot.width=10,repr.plot.height=10,
        repr.plot.bg='white')
X3<-Z3<-X4<-Z4<-Y5<-Z5<-seq(from=-5,to=5,by=.1)
surface1<-function(p,q,X,Z){
    for (x in X){for (z in Z){
        y<-q*(1-x^2/p^2)^.5; v<-c(x,y,z,x,-y,z)
        if (sum(is.na(v))==0){
            write.table(matrix(v,nrow=2,ncol=3,byrow=TRUE),
                        file='surface1.csv',
                        append=TRUE,quote=FALSE,
                        col.names=FALSE,row.names=FALSE)}}}}
surface2<-function(p,q,X,Z){
    for (x in X){for (z in Z){
        y<-q*(x^2/p^2-1)^.5; v<-c(x,y,z,x,-y,z)
        if (sum(is.na(v))==0){
            write.table(matrix(v,nrow=2,ncol=3,byrow=TRUE),
                        file='surface2.csv',
                        append=TRUE,quote=FALSE,
                        col.names=FALSE,row.names=FALSE)}}}}
surface3<-function(p,Y,Z){
    for (y in Y){for (z in Z){
        x<-y^2/2/p; v<-c(x,y,z)
        write.table(matrix(v,nrow=1,ncol=3,byrow=TRUE),
                    file='surface3.csv',
                    append=TRUE,quote=FALSE,
                    col.names=FALSE,row.names=FALSE)}}}
surface1(3,4,X3,Z3); surface2(2,3,X4,Z4); surface3(2,Y5,Z5)

files<-c('surface1.csv','surface2.csv','surface3.csv')
colors<-c('#36ff36','#36ffff','#ff36ff')
labels<-c('$x^2/3^2+y^2/4^2=1$','$x^2/2^2-y^2/3^2=1$',
          '$y^2=2*2*x$')
XYZ<-function(i){
    np$array(np$loadtxt(files[i],delimiter=' ',unpack=TRUE))}
fig<-pl$figure(figsize=c(10,10))
ax<-fig$add_subplot('111',projection='3d')
for (i in 1:3){
    ax$scatter(XYZ(i)[1,],XYZ(i)[2,],XYZ(i)[3,],
               s=1,c=colors[i],marker='1')}
fl2D<-function(i){
    ml$Line2D(c(0,1),c(0,1),linestyle='none',
              c=colors[i],marker='1')}
ax$legend(c(fl2D(1),fl2D(2),fl2D(3)),labels,loc=9)
file_name_out<-paste0(
    'rpy_plot',sample(1:9999999,1),'.png')
pl$savefig(file_name_out)
im<-load.image(file_name_out)
par(mar=c(0,0,0,0)); plot(im,axes=FALSE)

