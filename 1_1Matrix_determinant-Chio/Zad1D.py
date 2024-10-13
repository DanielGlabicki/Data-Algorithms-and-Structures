#Poprawione - wyliczenie wyznacznikia macierzy z przesuniętymi kolumnami uwzględnia zmianę znaku

class Matrix:
    def __init__(self, parameters, const=0):
        if isinstance(parameters, tuple):
            self.__matrix = [[const for i in range(parameters[1])] for i in range(parameters[0])]
        else:
            self.__matrix = parameters 
            
    def __add__(self, other):
        if other.size() == self.size():
            result = Matrix(self.size())
            for i in range(self.size()[0]):
                for j in range(self.size()[1]):
                    result[i][j] = self.__matrix[i][j] + other[i][j]
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
                        result[i][j] += self.__matrix[i][k] * other[k][j]
            return result
        else:
            print("Wrong dimensions")
            return 0
    
    def __getitem__(self, ind):
        return self.__matrix[ind]
    
    def __str__(self):
        string = ""
        for row in self.__matrix:
            string += '|'
            for elem in row:
                string += '{0: }'.format(elem) + ' '
            string += '|\n'
        return string
        
    def size(self):
        return len(self.__matrix), len(self.__matrix[0])
    
    

def chio(matrix, coef=1, switched = False):
    if matrix.size()[0] == matrix.size()[1] and matrix.size()[0] > 2:
        if matrix[0][0] == 0:
            for ind, i in enumerate(matrix):
                if i[0] != 0:
                    aux_matrix = []
                    for j in matrix:
                        aux_matrix.append(j)
                    
                    aux_matrix[ind] = matrix[0]
                    aux_matrix[0] = i
                    matrix = Matrix(aux_matrix)
                    switched = True
                    break
                if ind == matrix.size()[0]:
                    print("Wrong matrix")
                    return 1
        
        result = Matrix((matrix.size()[0] - 1, matrix.size()[0] - 1))
        coef *= 1/(matrix[0][0] ** (matrix.size()[0] - 2))
        
        for i in range(matrix.size()[0] - 1):
            for j in range(matrix.size()[0] - 1):
                result[i][j] = matrix[0][0] * matrix[i+1][j+1] - \
                matrix[i+1][0] * matrix[0][j+1]
        
        if result.size()[0] > 2:
            return chio(result, coef, switched)
        elif result.size()[0] == 2:
            if switched:
                return -coef*(result[0][0] * result[1][1] - result[1][0] * result[0][1])
            return coef*(result[0][0] * result[1][1] - result[1][0] * result[0][1])

    else:
        print("Wrong dimensions")
        return 0
  
def main():
    m1 = Matrix([
    [5 , 1 , 1 , 2 , 3],
    [4 , 2 , 1 , 7 , 3],
    [2 , 1 , 2 , 4 , 7],
    [9 , 1 , 0 , 7 , 0],
    [1 , 4 , 7 , 2 , 2]
    ])
    
    print(chio(m1))
    
    m2 = Matrix([
    [0 , 1 , 1 , 2 , 3],
    [4 , 2 , 1 , 7 , 3],
    [2 , 1 , 2 , 4 , 7],
    [9 , 1 , 0 , 7 , 0],
    [1 , 4 , 7 , 2 , 2]
    ])
    
    print(chio(m2))

main()
