# Graph_Algorithms

# Language:
-- Python 3.0

# File_Structure:
 i)  ```graph/*``` -- Implementation of the Vertex, Edge & Graph classes with appropriate Data-Structures
 
 ii) ```algorithms/*``` -- Implementation of the Algorithms that utilize the Graph objects from ```graph/Graph.py```

# Purpose:
-- This is a repository that shall contain the following :

i) Implementation of the Graph, Vertex and Edge Classes

ii) Implementation of Shortest-Path (Djikstra & Bellman-Ford), All pairs Shortest-Path (Floyd-Warshall) Algorithms

iii) Implementation of 2 Minimum Spanning Tree Algorithms (Kruskal & Prim)

iv) Implementation of a 2-partite-ness predictor (Predicts whether a Graph is Bi-Partite)

v) Implementation of Matching Algorithms


# RUNNING INSTRUCTIONS:
i) First, clone the repo: ``` git clone git@github.com:jssandh2/graph_algorithms.git ```

ii) You can instantiate new Graph Classes by adding a ```main``` method in ```Graph.py```. Example:
```Python
if __name__ == "__main__":
    graph_a = Graph(["a", "b", "c", "d"], [["a","b",3], ["b", "d"], ["d", "a", 2], ["a", "c", 5]])
    graph_a.add_vertex("e")
    graph_a.add_edge(["b", "e", 6])
```
iii) You can also remove edges & vertices, along with use the Graph object to implement Algorithms (Coming Soon!)
