
options(repr.plot.width=10,repr.plot.height=5,
        repr.plot.bg='whitesmoke')
pd_csv_matplot<-function(url,startcol,endcol)
    {df<-pd$read_csv(url); df<-df[,startcol:endcol]
     matplot(1:440,df,type='l')}
pd_csv_ggplot<-function(url,startcol,endcol,palette)
    {df<-pd$read_csv(url); df<-df[,startcol:endcol]
     df$N<-1:dim(df)[1]; df<-melt(df,id.vars='N')
     ggplot(df,aes(N,value,fill=variable))+geom_area()+
     scale_fill_brewer(palette=palette)+theme_bw()}

