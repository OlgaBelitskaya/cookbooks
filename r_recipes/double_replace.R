#unlock for running in SageMathCell 
#%%r
double_replace1<-
function(string,befor1,after1,befor2,after2) 
    {while (grepl(before1,string) | grepl(before2,string)) 
        {print(string)
         if (grepl(before1,string)) 
             {string<-sub(before1,after1,string) } 
         if (grepl(before2,string))
             {string<-sub(before2,after2,string)}}   
    print(string); return(string)}
double_replace2<-
function(string,befor1,after1,befor2,after2) 
    {while (grepl(before1,string) | grepl(before2,string)) 
        {print(string)
         if (grepl(before1,string)) 
             {string<-sub(before1,after1,string) } 
         else {string<-sub(before2,after2,string)}}   
    print(string); return(string)}
