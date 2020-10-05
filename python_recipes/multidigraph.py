import networkx as nx,pylab as pl

def multidigraph(edge_list,fig_size,node_color):
    pl.figure(figsize=(int(fig_size*1.5),fig_size))
    g=nx.MultiDiGraph();
    g.add_edges_from(edge_list)
    pos=nx.shell_layout(g)
    nx.draw_networkx_edges(
        g,pos,width=3,alpha=.6,
        edge_color='silver',
        arrowsize=50,arrowstyle='-|>')
    nx.draw_networkx_nodes(
        g,pos,node_size=2000,alpha=.7,
        node_color=node_color,node_shape='h')
    nx.draw_networkx_labels(
        g,pos,font_size=25,font_weight='bold')
    pl.axis('off'); pl.show();

def multidigraph_example():
    edge_list=[('♔','♕'),('♔','♖'),('♔','♗'),
               ('♔','♘'),('♕','♘'),('♖','♘'),
               ('♖','♚'),('♖','♛'),('♗','♖'),
               ('♗','♚'),('♘','♛'),('♚','♛'),
               ('♛','♜'),('♛','♝'),('♜','♝'),
               ('♜','♞'),('♜','♘')]
    fig_size=5; node_color='crimson'
    multidigraph(edge_list,fig_size,node_color)