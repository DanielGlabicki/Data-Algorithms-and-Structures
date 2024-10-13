# Skończone

import cv2
from matplotlib import pyplot as plt
import numpy as np


class Vertex:
    def __init__(self, key):
        self.key = key
        self.colour = 0
    
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
        return self.colour
    
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

def MST_prim(graphList, vertex0):
    vertices = graphList.vertices()
    intree = {v:0 for v in vertices}
    distance = {v:float('inf') for v in vertices}
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
        
        min_edge = float('inf')
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

def bfs(graphList, s, colour):
    visited = [] # odwiedzone wierzchołki
    queue = [] # kolejka, potrzebna do bfs
    
    visited.append(s)
    queue.append(s)
    
    while queue:
        vertex = queue.pop()
        vertex.set_colour(colour)
        for neighbour, edge in graphList.neighbours(vertex):
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

    return visited


def main():
    I = cv2.imread('sample.png', cv2.IMREAD_GRAYSCALE)
    graph = AdjList()

    for i in range(1, I.shape[0] - 1):
        for j in range(1, I.shape[1] - 1):
            graph.insert_edge(Vertex(str(i + j * I.shape[1])), Vertex(str((i-1) + (j-1) * I.shape[1])), np.abs(I[i][j].astype(int) - I[i-1][j-1].astype(int)))
            graph.insert_edge(Vertex(str(i + j * I.shape[1])), Vertex(str((i-1) + j * I.shape[1])), np.abs(I[i][j].astype(int) - I[i-1][j].astype(int)))
            graph.insert_edge(Vertex(str(i + j * I.shape[1])), Vertex(str((i-1) + (j+1) * I.shape[1])), np.abs(I[i][j].astype(int) - I[i-1][j+1].astype(int)))
            graph.insert_edge(Vertex(str(i + j * I.shape[1])), Vertex(str(i + (j-1) * I.shape[1])), np.abs(I[i][j].astype(int) - I[i][j-1].astype(int)))
            graph.insert_edge(Vertex(str(i + j * I.shape[1])), Vertex(str(i + (j+1) * I.shape[1])), np.abs(I[i][j].astype(int) - I[i][j+1].astype(int)))
            graph.insert_edge(Vertex(str(i + j * I.shape[1])), Vertex(str((i+1) + (j-1) * I.shape[1])), np.abs(I[i][j].astype(int) - I[i+1][j-1].astype(int)))
            graph.insert_edge(Vertex(str(i + j * I.shape[1])), Vertex(str((i+1) + j * I.shape[1])), np.abs(I[i][j].astype(int) - I[i+1][j].astype(int)))
            graph.insert_edge(Vertex(str(i + j * I.shape[1])), Vertex(str((i+1) + (j+1) * I.shape[1])), np.abs(I[i][j].astype(int) - I[i+1][j+1].astype(int)))
    
    graph_MST, height = MST_prim(graph, Vertex(str(1 + 1 * I.shape[1])))
    max_edge, v1, v2 = max([(edge, v1.key, v2.key) for v1, temp_neighbours in graph_MST.adj_list.items() for v2, edge in temp_neighbours.items()])
    graph_MST.delete_edge(Vertex(v1), Vertex(v2))

    IS = np.zeros((I.shape[0], I.shape[1]), dtype='uint8')
    vertices_1 = bfs(graph_MST, Vertex(v1), 100)
    vertices_2 = bfs(graph_MST, Vertex(v2), 200)

    for i in range(I.shape[0]):
        for j in range(I.shape[1]):
            if Vertex(str(str(i + j * I.shape[1]))) in vertices_1:
                IS[i][j] = 100
            elif Vertex(str(str(i + j * I.shape[1]))) in vertices_2:
                IS[i][j] = 200
    
    fig, axs = plt.subplots(1, 2, figsize=(14,7))
    axs[0].imshow(I, cmap ="gray", vmin=0, vmax=255)
    axs[0].axis('off')
    axs[0].set_title("Oryginal")

    axs[1].imshow(IS, cmap ="gray", vmin=0, vmax=255)
    axs[1].axis('off')
    axs[1].set_title("Obraz wynikowy")
    plt.show()

main()
