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

class Edge:
    def __init__(self, capacity, isResidual):
        if isResidual:
            self.capacity = 0
            self.flow = 0
            self.residual = 0
            self.isResidual = isResidual
        else:
            self.capacity = capacity
            self.flow = 0
            self.residual = capacity
            self.isResidual = isResidual
    
    def __repr__(self):
        return str(self.capacity) + " " + str(self.flow) + " " + \
        str(self.residual) + " " + str(self.isResidual) 

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

# Tworzy graf w postaci listy sąsiedctwa
def makeGraph(graph):
    graphList = AdjList()
    for i in graph:
        graphList.insert_edge(Vertex(i[0]), Vertex(i[1]), Edge(i[2], False))
        graphList.insert_edge(Vertex(i[1]), Vertex(i[0]), Edge(0, True))
    
    return graphList

def bfs(graphList, s):
    visited = set() # odwiedzone wierzchołki
    parent = {} # kolejni rodzice
    queue = [] # kolejka, potrzebna do bfs
    
    visited.add(s)
    queue.append(s)
    
    while queue:
        vertex = queue.pop()
        for neighbour, edge in graphList.neighbours(vertex):
            if neighbour not in visited and edge.residual > 0:
                visited.add(neighbour)
                parent[neighbour] = vertex
                queue.append(neighbour)
    
    return parent

def bottle_neck(graphList, parent, s, t):
    if t not in parent.keys():
        return 0
    
    current_vertex = t
    min_flow = np. float('inf') # Bottle-neck
    while current_vertex != s:
        current_edge = graphList.adj_list[parent[current_vertex]][current_vertex]
        if current_edge.residual < min_flow:
            min_flow = current_edge.residual
        current_vertex = parent[current_vertex]
    
    return min_flow

def augment(graphList, parent, s, t, min_flow):
    if t in parent.keys():
        current_vertex = t
        while current_vertex != s:
            if graphList.adj_list[parent[current_vertex]][current_vertex].isResidual:
                graphList.adj_list[parent[current_vertex]][current_vertex].residual -= min_flow
                graphList.adj_list[current_vertex][parent[current_vertex]].flow -= min_flow
                graphList.adj_list[current_vertex][parent[current_vertex]].residual += min_flow
            else:
                graphList.adj_list[parent[current_vertex]][current_vertex].flow += min_flow
                graphList.adj_list[parent[current_vertex]][current_vertex].residual -= min_flow
                graphList.adj_list[current_vertex][parent[current_vertex]].residual += min_flow
            current_vertex = parent[current_vertex]

def algorithm(graph_list, s, t):
    parent = bfs(graph_list, s)
    min_flow = bottle_neck(graph_list, parent, s, t)
    
    if min_flow == 0:
        print("Brak ścieżki pomiędzy {0} a {1}".format(s, t))
        return 0
    
    while min_flow > 0:
        augment(graph_list, parent, s, t, min_flow)
        parent = bfs(graph_list, s)
        min_flow = bottle_neck(graph_list, parent, s, t)
    
    flow = 0
    for neighbour, _ in graph_list.neighbours(t):
        edge = graph_list.adj_list[neighbour][t]
        flow += edge.flow
    return flow


def main():
    graf_0 = [('s','u',2), ('u','t',1), ('u','v',3), ('s','v',1), ('v','t',2)]
    graph_list_0 = makeGraph(graf_0)
    print(algorithm(graph_list_0, Vertex('s'), Vertex('t')))
    printGraph(graph_list_0)
    
    graf_1 = [('s', 'a', 16), ('s', 'c', 13), ('c', 'a', 4), ('a', 'b', 12),\
    ('b', 'c', 9), ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4)]
    graph_list_1 = makeGraph(graf_1)
    print(algorithm(graph_list_1, Vertex('s'), Vertex('t')))
    printGraph(graph_list_1)
    
    graf_2 = [('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), \
    ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6), ('c', 'd', 2), \
    ('d', 't', 1), ('e', 't', 9)]
    graph_list_2 = makeGraph(graf_2)
    print(algorithm(graph_list_2, Vertex('s'), Vertex('t')))
    printGraph(graph_list_2)
    
main()
