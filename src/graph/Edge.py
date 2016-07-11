##
# This implements the Edge class
##

import Vertex


class Edge:

    # Constructor
    # Takes 2 vertex objects as its input
    def __init__(self, vertex_one=Vertex(), vertex_two=Vertex(), weight=1):
        self.vertex_one = vertex_one
        self.vertex_two = vertex_two
        self.weight = weight

    # Returns the first vertex in the edge
    def get_vertex_one(self):
        return self.vertex_one

    # Returns the second vertex in the edge
    def get_vertex_two(self):
        return self.vertex_two

    # Returns both vertices in the edge
    def get_vertices(self):
        return [self.vertex_one, self.vertex_two]

    # Returns the weight of the edge
    def get_weight(self):
        return self.weight

    # Over-rides and sets the weight of the edge
    def set_weight(self, weight):
        self.weight = weight
