# Skończone
from copy import deepcopy


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
    
    def __eq__(self, other):
        try:
            return self.matrix == other.matrix
        except AttributeError as e:
            print (e)
            return False
    
    def __copy__(self):
        return deepcopy(self.matrix)
    
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


def transpose(matrix):
    result = Matrix((matrix.size()[1], matrix.size()[0]))
    for i in range(matrix.size()[0]):
            for j in range(matrix.size()[1]):
                result[j][i] = matrix[i][j]
    return result


def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")


def ullmann(used_cols, curr_row, M, graph_G, graph_P, isomorphisms, iterations):
    iterations += 1
    if curr_row == M.size()[0]:
        if graph_P == M * transpose(M * graph_G):
            isomorphisms.append(deepcopy(M))
        return iterations
    
    for idx, col in enumerate(used_cols):
        if not col:
            used_cols[idx] = True
            # col = True - TO TAK NIE DZIAŁA!!!
            M.matrix[curr_row] = [0 for _ in range(M.size()[1])]
            M.matrix[curr_row][idx] = 1
            iterations = ullmann(used_cols, curr_row + 1, M, graph_G, graph_P, isomorphisms, iterations)
            used_cols[idx] = False
            # col = False - TO TAK NIE DZIAŁA!!!
    return iterations
    
    
def ullmann_2(used_cols, curr_row, M0, graph_G, graph_P, isomorphisms, iterations):
    iterations += 1
    if curr_row == M0.size()[0]:
        if graph_P == M0 * transpose(M0 * graph_G):
            isomorphisms.append(deepcopy(M0))
        return iterations
    
    M = deepcopy(M0)
    
    for idx, col in enumerate(used_cols):
        if not col and M0[curr_row][idx] != 0:
            used_cols[idx] = True
            M.matrix[curr_row] = [0 for _ in range(M.size()[1])]
            M.matrix[curr_row][idx] = 1
            iterations = ullmann_2(used_cols, curr_row + 1, M, graph_G, graph_P, isomorphisms, iterations)
            used_cols[idx] = False
    return iterations


def prune(M, graph_G, graph_P):
    changes = True
    while changes:
        changes = False
        for i in range(M.size()[0]):
            for j in range(M.size()[1]):
                if M[i][j] == 1:
                    neighbour = False
                    for x in range(graph_P.size()[0]):
                        if sum(M[x]) == 0:
                            M.matrix[i][j] = 0
                            changes = True
                            break


def ullmann_3(used_cols, curr_row, M0, graph_G, graph_P, isomorphisms, iterations):
    iterations += 1
    if curr_row == M0.size()[0]:
        if graph_P == M0 * transpose(M0 * graph_G):
            isomorphisms.append(deepcopy(M0))
        return iterations
    
    M = deepcopy(M0)
    prune(M, graph_G, graph_P)
    
    for idx, col in enumerate(used_cols):
        if not col and M0[curr_row][idx] != 0:
            used_cols[idx] = True
            M.matrix[curr_row] = [0 for _ in range(M.size()[1])]
            M.matrix[curr_row][idx] = 1
            iterations = ullmann_3(used_cols, curr_row + 1, M, graph_G, graph_P, isomorphisms, iterations)
            used_cols[idx] = False
    return iterations


def main():
    graph_G = [('A','B',1), ('B','F',1), ('B','C',1), ('C','D',1), ('C','E',1), ('D','E',1)]
    graph_G_mat = AdjMatrix()
    for i in graph_G:
        graph_G_mat.insert_edge(Vertex(i[0]), Vertex(i[1]), i[2])
        graph_G_mat.insert_edge(Vertex(i[1]), Vertex(i[0]), i[2]) # GRAF MUSI BYĆ DWUKIERUNKOWY
    
    graph_P = [('A','B',1), ('B','C',1), ('A','C',1)]
    graph_P_mat = AdjMatrix()
    for i in graph_P:
        graph_P_mat.insert_edge(Vertex(i[0]), Vertex(i[1]), i[2])
        graph_P_mat.insert_edge(Vertex(i[1]), Vertex(i[0]), i[2]) # GRAF MUSI BYĆ DWUKIERUNKOWY
    
    
    M = Matrix((graph_P_mat.adj_mat.size()[0], graph_G_mat.adj_mat.size()[1]))
    used_cols = [False for _ in range(M.size()[1])]
    
    isomorphisms = []
    iterations = ullmann(used_cols, 0, M, graph_G_mat.adj_mat, graph_P_mat.adj_mat, isomorphisms, 0)
    print(len(isomorphisms), iterations)
    
    
    M0 = Matrix((graph_P_mat.adj_mat.size()[0], graph_G_mat.adj_mat.size()[1]))
    for i in range(M0.size()[0]):
        for j in range(M0.size()[1]):
            if sum(graph_P_mat.adj_mat[i]) <= sum(graph_G_mat.adj_mat[j]):
                M0[i][j] = 1
    
    isomorphisms_2 = []
    iterations_2 = ullmann_2(used_cols, 0, M0, graph_G_mat.adj_mat, graph_P_mat.adj_mat, isomorphisms_2, 0)
    print(len(isomorphisms_2), iterations_2)
    
    
    isomorphisms_3 = []
    iterations_3 = ullmann_3(used_cols, 0, M0, graph_G_mat.adj_mat, graph_P_mat.adj_mat, isomorphisms_3, 0)
    print(len(isomorphisms_3), iterations_3)
    # W przypadku tych grafów, funkcja prune nie pomaga zoptymalizować algorytmu

main()