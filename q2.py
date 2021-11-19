import networkx as nx
import matplotlib.pyplot as plt
%matplotlib inline
from networkx.algorithms.community import greedy_modularity_communities
G = nx.karate_club_graph()
 
# viewing the graph
nx.draw(G,with_labels = True)
 
# finding communities in G using greedy modularity maximization
comm = list(greedy_modularity_communities(G))
sorted(comm[0])
sorted(comm[1])
 
# plotting the communities
color_map = []
for node in G:
    if node in comm[0]:
        color_map.append('blue')
    else: 
        color_map.append('green')
nx.draw(G,node_color=color_map, with_labels=True)
plt.show()

