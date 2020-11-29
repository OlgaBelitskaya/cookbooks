
networkx_graphplot<-
function(edge_list,sfig,sarrow,snode,sfont)
    {g<-nx$MultiDiGraph()
     pl$figure(figsize=c(sfig,sfig))
     g$add_edges_from(edge_list)
     pos<-nx$shell_layout(g)
     nx$draw_networkx_edges(
         g,pos,width=3,edge_color='silver',
         alpha=.5,arrowsize=sarrow,arrowstyle='-|>')
     nx$draw_networkx_nodes(
         g,pos,node_size=snode,alpha=.7,
         node_color='steelblue',node_shape='h')
     nx$draw_networkx_labels(
         g,pos,font_size=sfont,font_weight='bold')
     pl$axis('off')
     pl$title('MultiDiGraph & Pyplot in R')
     file_name<-paste0('rpy_multidigraph_plot',
                       sample(1:9999999,1),'.png')
     pl$savefig(file_name)
     im<-load.image(file_name)
     options(repr.plot.width=sfig,repr.plot.height=sfig,
             repr.plot.bg='whitesmoke')
     par(mar=c(0,0,0,0)); plot(im,axes=FALSE)}

