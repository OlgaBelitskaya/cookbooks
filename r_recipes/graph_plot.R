
options(repr.plot.width=10,repr.plot.height=10,
        repr.plot.bg='slategray')
c0<-'white'; c1<-'#3333ff'; c2<-'#ff3333'
edges<-c('A','B', 'A','C', 'A','F', 'B','C', 'B','D',
         'C','D', 'C','E', 'D','E', 'D','F', 'E','F')
weights<-c(3,8,16,4,7,2,6,5,4,2)
g<-graph(edges,directed=FALSE)%>%
    set_edge_attr('weight',value=weights)
shortest_path<-get.shortest.paths(g,'A','F')
E(g)$color<-c1
E(g,path=unlist(shortest_path$vpath))$color<-c2
plot(g,layout=layout_nicely(g),vertex.label.cex=2.5,
     vertex.color=c1,vertex.size=25,
     vertex.label.color=c0,vertex.frame.color=c0,
     edge.label.color=c0,edge.label=E(g)$weight,
     edge.label.cex=2.5,edge.width=E(g)$weight)

