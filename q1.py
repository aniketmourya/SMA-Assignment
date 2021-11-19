# networkX is a Python library for studying graphs and networks
import networkx as nx
# a library for visualizing a graphs
import matplotlib.pyplot as plt
%matplotlib inline
# loading pre-installed graph in networkX library
K = nx.karate_club_graph()
# visualizing the graph
nx.draw(K,with_labels = True)
 
# function to eliminate edges one-by-one based on the edge betweenness centrality (EBC) score. 
def edgeremove(graph):
# assigning EBC values to all the edges in the graph 
  G_dict = nx.edge_betweenness_centrality(graph)
  edge = ()
  # lambda function to take off the edge with highest EBC value
  for key, value in sorted(G_dict.items(), key=lambda item: item[1], reverse = True):
      edge = key
      break
  return edge
# function for partitioning graph into different communities
def girvan_newman(graph):
    # finding no. of connected components
    cc = nx.connected_components(graph)
    cc_count = nx.number_connected_components(graph)
    while(cc_count == 1):
        graph.remove_edge(edgeremove(graph)[0], edgeremove(graph)[1])
        cc = nx.connected_components(graph)
        cc_count = nx.number_connected_components(graph)
    return cc
 
# passing karate club graph to girvan newman algorithm 
x = girvan_newman(K.copy())
# list of nodes forming the communities
groups = []
for i in x:
  groups.append(list(i))
print(groups)
 
# plot the communities
color_map = []
for node in K:
    if node in groups[0]:
        color_map.append('blue')
    else: 
        color_map.append('green')  
 
nx.draw(K,node_color=color_map, with_labels=True)
plt.show()

