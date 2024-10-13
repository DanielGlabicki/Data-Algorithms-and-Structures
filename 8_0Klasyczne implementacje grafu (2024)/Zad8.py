# Skończone
# Czy graf miał być skierowany czy nieskierowany?
import polska

class Matrix: # Baza pod macierz sąsiedctwa AdjMatrix
    def __init__(self, parameters, const=0):
        if isinstance(parameters, tuple):
            self.matrix = [[const for i in range(parameters[1])] for i in range(parameters[0])]
        else:
            self.matrix = parameters 
        # Pole z macierzą uczyniłem publiczne, aby można ją było powiększać i pomniejszać

    def __add__(self, other):
        if other.size() == self.size():
            result = Matrix(self.size())
            for i in range(self.size()[0]):
                for j in range(self.size()[1]):
                    result[i][j] = self.matrix[i][j] + other[i][j]
            return result
        else:
            print("Wrong dimensions")
            return 0
    
    def __mul__(self, other):
        if other.size()[0] == self.size()[1]:
            result = Matrix((self.size()[0], other.size()[1]))
            for i in range(self.size()[0]):
                for j in range(other.size()[1]):
                    for k in range(self.size()[1]):
                        result[i][j] += self.matrix[i][k] * other[k][j]
            return result
        else:
            print("Wrong dimensions")
            return 0
    
    def __getitem__(self, ind):
        return self.matrix[ind]
    
    def __str__(self):
        string = ""
        for row in self.matrix:
            string += '|'
            for elem in row:
                string += '{0: }'.format(elem) + ' '
            string += '|\n'
        return string
        
    def size(self):
        try:
            return len(self.matrix), len(self.matrix[0])
        except IndexError:
            return 0, 0


class Vertex:
    def __init__(self, key):
        self.key = key
    
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
    

class AdjMatrix:
    def __init__(self):
        self.adj_mat = Matrix([])
        self.node_list = []
    
    def is_empty(self):
        return True if self.adj_mat.size() == (0, 0) else False
    
    def insert_vertex(self, vertex):
        if vertex not in self.node_list:
            self.node_list.append(vertex)
            self.adj_mat.matrix.append([0] * (self.adj_mat.size()[1]))
            for i in self.adj_mat.matrix:
                i.append(0)
    
    # jeśli wierzchołki nie istnieją, również je tworzy
    def insert_edge(self, vertex1, vertex2, edge=1):
        self.insert_vertex(vertex1)
        self.insert_vertex(vertex2)
        self.adj_mat.matrix[self.get_vertex_id(vertex1)][self.get_vertex_id(vertex2)] = edge
    
    def delete_vertex(self, vertex):
        if vertex in self.node_list:
            idx = self.get_vertex_id(vertex)
            self.adj_mat.matrix.pop(idx)
            for i in self.adj_mat.matrix:
                i.pop(idx)
            self.node_list.pop(idx)
    
    def delete_edge(self, vertex1, vertex2):
        self.adj_mat.matrix[self.get_vertex_id(vertex1)][self.get_vertex_id(vertex2)] = 0
    # czy jeśli usuniemy ostatnią krawędź pomiędzy jakimś węzłem a resztą grafu,
    # to powinno się usunąć również taki węzeł?
    
    def vertices(self):
        for v_id in range(len(self.node_list)):
            yield v_id
    
    def neighbours(self, vertex_id):
        for v_id, edge in enumerate(self.adj_mat.matrix[vertex_id]):
            if edge > 0:
                yield  v_id, edge
    
    def get_vertex(self, vertex_id):
        return self.node_list[vertex_id]
    
    def get_vertex_id(self, vertex):
        for v_id, v in enumerate(self.node_list):
            if v == vertex:
                return v_id
        return None

def main():
    graphList = AdjList()
    graphMat = AdjMatrix()
    for i in polska.graf:
        # w zasadzie korzystam z insert_vertex - wywoływana w insert_edge
        graphList.insert_edge(Vertex(i[0]), Vertex(i[1]))
        graphMat.insert_edge(Vertex(i[0]), Vertex(i[1]))
        
    graphList.delete_vertex(Vertex("K"))
    # potrzeba usunąć krawędź w obie strony
    graphList.delete_edge(Vertex("W"), Vertex("E"))
    graphList.delete_edge(Vertex("E"), Vertex("W"))
    polska.draw_map(graphList)
    
    # niestety równocześnie nie da się narysować 2 grafów - widoczny będzie
    # jedynie ten pierwszy, czyli graphList
    graphMat.delete_vertex(Vertex("K"))
    # potrzeba usunąć krawędź w obie strony
    graphMat.delete_edge(Vertex("W"), Vertex("L"))
    graphMat.delete_edge(Vertex("L"), Vertex("W"))
    polska.draw_map(graphMat)

main()
