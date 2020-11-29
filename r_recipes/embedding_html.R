
embedding_html_string<-
function(html_str,width,height)
    {html_str<-paste(
         as.character(html_str),collapse='
')
     randi<-sample(1:9999999,1)
     file_name<-paste0('chart',randi,'.html')
     write.table(html_str,file=file_name,quote=FALSE,
                 col.names=FALSE,row.names=FALSE)
     str<-paste0('<div id="',randi,
            '"><iframe src="chart',randi,
            '.html" height=',height,
            ' width=',width,'>','</iframe></div>')
     display_html(str)}
embedding_html_page<-
function(file_path,width,height)
    {html_str<-paste(
         readLines(file_path,warn=FALSE),collapse='
')
     randi<-sample(1:9999999,1)
     file_name<-paste0('chart',randi,'.html')
     write.table(html_str,file=file_name,quote=FALSE,
                 col.names=FALSE,row.names=FALSE)
     str<-paste0('<div id="',randi,
                 '"><iframe src="chart',randi,
                 '.html" height=',height,
                 ' width=',width,'>','</iframe></div>')
     display_html(str)}

