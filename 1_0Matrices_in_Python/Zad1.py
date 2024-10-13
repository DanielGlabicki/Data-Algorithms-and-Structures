#Skończone

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

def transpose(matrix):
    result = Matrix((matrix.size()[1], matrix.size()[0]))
    for i in range(matrix.size()[0]):
            for j in range(matrix.size()[1]):
                result[j][i] = matrix[i][j]
    return result
    
def main():
    m1 = Matrix(
    [ [1, 0, 2],
      [-1, 3, 1] ]
    )
    
    m2 = Matrix(
    [ [3, 1],
      [2, 1],
      [1, 0]]
    )
    
    m3 = Matrix((m1.size()), 1)
    
    print(transpose(m1))
    print(m1+m3)
    print(m1*m2)
    
main()