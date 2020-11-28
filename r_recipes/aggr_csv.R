#unlock for running in SageMathCell 
#%%r
mean_aggr_csv<-function(url,sep,column,group_by) {
    df<-read.csv(url,header=TRUE,sep='	')
    len<-dim(df)[1]
    group_list<-list(df[1:len,group_by])
    result<-aggregate(df[column],group_list,mean)
    colnames(result)<-c(group_by,paste0('mean ',column))
    return(result)}
median_aggr_csv<-function(url,sep,column,group_by) {
    df<-read.csv(url,header=TRUE,sep='	')
    len<-dim(df)[1]
    group_list<-list(df[1:len,group_by])
    result<-aggregate(df[column],group_list,median)
    colnames(result)<-c(group_by,paste0('median ',column))
    return(result)}
sum_aggr_csv<-function(url,sep,column,group_by) {
    df<-read.csv(url,header=TRUE,sep='	')
    len<-dim(df)[1]
    group_list<-list(df[1:len,group_by])
    result<-aggregate(df[column],group_list,sum) 
    colnames(result)<-c(group_by,paste0('sum ',column))
    return(result)}
