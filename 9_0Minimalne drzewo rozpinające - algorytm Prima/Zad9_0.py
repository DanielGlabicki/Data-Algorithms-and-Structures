# Skończone
import numpy as np


class Vertex:
    def __init__(self, key):
        self.key = key
        self.colour = None
    
    def __eq__(self, other):
        try:
            return self.key == other.key
        except AttributeError as e:
            print(e)
            return False
    
    def __hash__(self):
        return hash(self.key)
    
    def __str__(self):
        return self.key
    
    def get_colour(self):
        return(self.colour)
    
    def set_colour(self, colour):
        self.colour = colour

class AdjList:
    def __init__(self):
        self.adj_list = {}
    
    def is_empty(self):
        return True if self.adj_list == {} else False
    
    def insert_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = {}
    
    # jeśli wierzchołki nie istnieją, również je tworzy
    def insert_edge(self, vertex1, vertex2, edge=None):
        self.insert_vertex(vertex1)
        self.insert_vertex(vertex2)
        self.adj_list[vertex1][vertex2] = edge
    
    def delete_vertex(self, vertex):
        if vertex in self.adj_list:
            del self.adj_list[vertex]
            for i in self.adj_list.values():
                if vertex in i:
                    del i[vertex]
    
    def delete_edge(self, vertex1, vertex2):
        del self.adj_list[vertex1][vertex2]
    
    def vertices(self):
        return self.adj_list.keys()
    
    def neighbours(self, vertex_id):
        return self.adj_list[vertex_id].items()
    
    def get_vertex(self, vertex_id):
        return vertex_id

def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")

def MST_prim(graphList, vertex0):
    vertices = graphList.vertices()
    intree = {v:0 for v in vertices}
    distance = {v:np.float('inf') for v in vertices}
    parent = {v:None for v in vertices}
    
    graphMST = AdjList()
    height = 0
    
    v = vertex0
    while intree[v] == 0:
        intree[v] = 1
        for neighbour, edge in graphList.neighbours(v):
            if edge < distance[neighbour] and intree[neighbour] == 0:
                distance[neighbour] = edge
                parent[neighbour] = v
        
        min_edge = np.float('inf')
        min_v = None
        for next_v in vertices:
            if intree[next_v] == 0 and distance[next_v] < min_edge:
                min_edge = distance[next_v]
                min_v = next_v
        
        if min_v is not None:
            graphMST.insert_edge(parent[min_v], min_v, min_edge)
            graphMST.insert_edge(min_v, parent[min_v], min_edge)
            v = min_v
            height += 1
    
    return graphMST, height
