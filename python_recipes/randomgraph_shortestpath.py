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