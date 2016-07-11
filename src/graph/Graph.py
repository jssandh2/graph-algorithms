##
# This implements the (Undirected) Graph Class for use in all Algorithms under ../algorithms/*
# The Graph Class makes use of the Vertex & Edge Classes
# A Graph is written as a 2-tuple, G = (V, E) , where V = set of vertices , E = set of edges
# The Graph Class has provides both, Adjacency List & Adjacency Matrix data-structures for a graph
# The appropriate data-structure is then used to run on the appropriate Algorithm.
# The construction of the Graph has : Time-Complexity : O(n+m), Space-Complexity:O(n+m)
# As m < n^{2} , this holds for the construction of the Adjacency Matrix as well
##

import Vertex
import Edge


class Graph:

    # Constructor -- Constructs a Graph, given (optional) a list of vertices an edges
    # Example: graph = new Graph(["a", "b", "c"], [["a", "b", 1], ["a", "c", 3]])
    # If the Graph has unweighted edges, the weight argument can be avoided altogether
    def __init__(self, vertices=[], edges=[]):
        # Initialize variables
        self.adjacency_matrix = []
        self.adjacency_list = {}
        self.num_vertices = len(vertices)
        self.num_edges = len(edges)
        self.vertex_name_to_int_hash = {}
        # Construct the vertex_to_int_hash dictionary
        count = 0
        for vertex in vertices:
            self.vertex_name_to_int_hash[vertex] = count
            count += 1
        # Initialize the Adjacency Matrix to be all zeroes, initially
        for i in range(self.num_vertices):
            self.adjacency_matrix.append([])
            for j in range(self.num_vertices):
                self.adjacency_matrix[i].append(0)
        # Construct the Adjacency Matrix, with appropriate values corresponding to edge weights
        for edge in edges:
            # Update the Adjacency Matrix to be the final values
            vertex_one = edge[0]
            vertex_two = edge[1]
            weight = 1
            if len(edge) == 2:
                self.adjacency_matrix[self.vertex_name_to_int_hash[vertex_one]][
                    self.vertex_name_to_int_hash[vertex_two]] = 1
            else:
                self.adjacency_matrix[self.vertex_name_to_int_hash[vertex_one]][
                    self.vertex_name_to_int_hash[vertex_two]] = edge[2]
                weight = edge[2]
            # Construct the Adjacency List
            edge_new_one = Edge(Vertex(vertex_one), Vertex(vertex_two), weight)
            edge_new_two = Edge(Vertex(vertex_two), Vertex(vertex_one), weight)
            if vertex_one in self.adjacency_list:
                (self.adjacency_list[vertex_one]).append(edge_new_one)
            else:
                self.adjacency_list[vertex_one] = [edge_new_one]
            if vertex_two in self.adjacency_list:
                (self.adjacency_list[vertex_two]).append(edge_new_two)
            else:
                self.adjacency_list[vertex_two] = [edge_new_two]
        # Make sure that vertices with no edges point to an Empty List in the Adjacency List
        for vertex in vertices:
            if vertex not in self.adjacency_list:
                self.adjacency_list[vertex] = []

    # Adds a vertex to the existing Graph
    def add_vertex(self, vertex_name):
        if vertex_name in self.adjacency_list:
            print("The vertex " + vertex_name + " is already part of the Graph!")
        else:
            # Modify the Data Structures accordingly, and increase the number of vertices
            self.adjacency_list[vertex_name] = []
            self.num_vertices += 1
            self.vertex_name_to_int_hash[vertex_name] = self.num_vertices - 1
            # Initiate a new row in the Adjacency Matrix with 0's
            self.adjacency_matrix[self.vertex_name_to_int_hash[vertex_name]] = []
            for i in range(self.num_vertices):
                (self.adjacency_matrix[self.vertex_name_to_int_hash[vertex_name]]).append(0)

    # Adds a new edge to the existing Graph
    # Edge = ["a", "b", 3] OR ["a", "b"]
    def add_edge(self, edge):
        if len(edge) > 3 or len(edge) < 1:
            print("Illegal Edge: " + str(",".join(edge)) + " provided! ")
        else:
            old_count = self.num_vertices
            self.num_edges += 1
            weight = 1
            if len(edge) == 3:
                weight = edge[2]
            vertex_one = edge[0]
            vertex_two = edge[1]
            # Create the new Edge objects
            edge_new_one = Edge(Vertex(vertex_one), Vertex(vertex_two), weight)
            edge_new_two = Edge(Vertex(vertex_two), Vertex(vertex_one), weight)
            # Update the Adjacency List, and update self.num_vertices accordingly
            if vertex_one in self.adjacency_list:
                (self.adjacency_list[vertex_one]).append(edge_new_one)
            else:
                self.adjacency_list[vertex_one] = [edge_new_one]
                self.vertex_name_to_int_hash[vertex_one] = self.num_vertices
                self.num_vertices += 1
            if vertex_two in self.adjacency_list:
                (self.adjacency_list[vertex_two]).append(edge_new_two)
            else:
                self.adjacency_list[vertex_two] = [edge_new_two]
                self.vertex_name_to_int_hash[vertex_two] = self.num_vertices
                self.num_vertices += 1
            # Declare the new rows for the adjacency matrix
            self.adjacency_matrix[self.vertex_name_to_int_hash[vertex_one]] = []
            self.adjacency_matrix[self.vertex_name_to_int_hash[vertex_two]] = []
            for i in range(self.num_vertices):
                self.adjacency_matrix[self.vertex_name_to_int_hash[vertex_one]].append(0)
                self.adjacency_matrix[self.vertex_name_to_int_hash[vertex_two]].append(0)
            # Update the Adjacency Matrix to have the new edge, as well as add the new edge weight (0) to each row
            self.adjacency_matrix[self.vertex_name_to_int_hash[vertex_one]][
                self.vertex_name_to_int_hash[vertex_two]] = weight
            for i in range(self.num_vertices):
                if i != self.vertex_name_to_int_hash[vertex_one] and i != self.vertex_name_to_int_hash[vertex_two]:
                    (self.adjacency_matrix[i]).append(0)

            




