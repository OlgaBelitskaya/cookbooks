import numpy as np,networkx as nx,pylab as pl

def random_graph(num_min=7,num_max=15):
    num_nodes=np.random.randint(num_min,num_max+1)
    letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    nodes=list(letters)[:num_nodes]
    edges=[]
    for i in range(num_nodes):
        num_edges=np.random.randint(1,num_nodes-1)
        curr_edges=sorted(np.random.choice(
            nodes[:i]+nodes[i+1:],
            num_edges,replace=False))
        curr_edges=[(ce,np.random.randint(1,15))
                    for ce in curr_edges]
        edges+=[curr_edges]
    return dict(zip(nodes,edges))

def random_shortestpath(graph):
    n=len(graph.keys()); rg=nx.Graph()
    for key in graph.keys():
        for value in graph[key]:
           rg.add_edge(key,value[0],
                       length=value[1])
    [start,end]=np.random.choice(
        n,2,replace=False)
    start=list(graph.keys())[start]
    end=list(graph.keys())[end]
    shortest_path=nx.shortest_path(
        rg,start,end,
        weight='length')
    shortest_path_list=[]
    for i in range(len(shortest_path)-1):   
        shortest_path_list.append(
            (shortest_path[i],shortest_path[i+1]))
    print('start: '+start+'; end: '+end)
    print('the shortest path: ',shortest_path_list)
    return rg,shortest_path,shortest_path_list

def randomgraph_shortestpath(graph,fig_size=7):
    rg,shortest_path,shortest_path_list=\
    random_shortestpath(graph)
    lengths=nx.get_edge_attributes(rg,'length')   
    pos=nx.spring_layout(rg)
    pl.figure(figsize=(fig_size,fig_size))
    nx.draw(rg,pos,with_labels=True,
            node_shape='8',node_size=1000, 
            node_color='steelblue',
            edge_color='silver',
            width=5,alpha=.75)
    nx.draw_networkx_edge_labels(
        rg,pos,edge_labels=lengths)
    nx.draw_networkx_edges(
        rg,pos=pos,edgelist=shortest_path_list,
        edge_color='#ff9966',width=10,alpha=.5)
    pl.show();