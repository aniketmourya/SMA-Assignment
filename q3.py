import networkx as nx
import numpy as np
from numpy import linalg as la
import datetime
import sys
 
# function to find second smallest eigen value and corresponding eigen vector
def second_smallest_eigen(vector):
    second_index = 0
    min_value = vector.min()
    second_value = vector.max()
    for index in range(len(vector)):
        if vector[index] > min_value and vector[index] < second_value:
            second_index = index
            second_value = vector[index]
    return second_index
 
# function to compare two integer values
def mycmp(x, y):
    if int(x) > int(y):
        return 1
    return -1
 
 
starttime = datetime.datetime.now()
#input file as argument
inputfile = sys.argv[1]
k_clustering = int(sys.argv[2])
# output file
output_file = sys.argv[3]#"wiki-output" #
clustering_count = 1
clusters = []
G = nx.Graph()
# reading input file
with open(inputfile, "r") as file:
    lines = file.readlines()
    for line in lines:
        values = line.strip().split()
        G.add_edges_from([(values[0], values[1])])
    clusters.append(list(G.nodes))
 
for iter in range(k_clustering - 1):
    large_size = 0
    large_index = 0
    for i in range(len(clusters)):
        length = len(clusters[i])
        if length > large_size:
            large_index = i
            large_size = length
    cluster_nodes = clusters[large_index]
    sub_G = G.subgraph(cluster_nodes)
 
# constructing laplacian matrix L for the graph
    A = nx.to_numpy_matrix(sub_G)
    D = np.diag([d for n, d in sub_G.degree()])
    L = D - A
# calculating eigen value and eigen vector for matrix L
    w, v = la.eig(L)
    second_index = 0
# second smallest eigen value and corresponding eigen vector
    second_small_index = second_smallest_eigen(w)
 
    index = 0
    sum = 0
    degrees = [n for n, d in sub_G.degree()]
    part1 = []
    part2 = []
    for i in v[:,second_small_index]:
        sum += i[0]
        if i > 0:
            part1.append(degrees[index])
        else:
            part2.append(degrees[index])
        index += 1
    clusters.remove(cluster_nodes)
    clusters.append(part1)
    clusters.append(part2)
with open(output_file, "w") as file:
    for cluster in clusters:
        s = sorted(cluster, cmp=mycmp)
        file.write(",".join(x for x in s) + "\n")

