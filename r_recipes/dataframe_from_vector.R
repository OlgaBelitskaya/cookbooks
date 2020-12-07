# with the libraries rpy_sklearn.R
arr1<-c('Hanoi','Frankfurt','Houston',
        'Riyadh','Barcelona','Ankara')
arr2<-c(33,16,28,38,17,27)
tmp<-pd$DataFrame(
    np$nan,index=1:6,columns=c('city','temperature'))
tmp$city<-arr1; tmp$temperature<-as.integer(arr2)
tmp2<-data.frame(cbind(arr1,arr2))
colnames(tmp2)<-c('city','temperature')
tmp2<-transform(
    tmp2,city=as.character(city),
    temperature=as.integer(as.character(temperature)))
options(repr.plot.width=10,repr.plot.height=5)
p<-ggplot(tmp,aes(x=city,y=temperature,
                  color=as.character(temperature)))+
    scale_color_brewer(palette='Reds',name='°C')+
    geom_point(size=5)+theme_bw()
cat(str(tmp)); cat(str(tmp2)); print(p)