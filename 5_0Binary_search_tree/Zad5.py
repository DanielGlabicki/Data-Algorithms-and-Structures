# Skończone

class Node: # klasa reprezentująca węzeł drzewa
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        
class Tree: # klasa reprezentująca drzewo, posiada korzeń
    def __init__(self):
        self.root = None
    
    def search(self, key):
        if self.root == None:
            print("Drzewo puste")
            return None
        else:
            return self.__search(key, self.root)
    
    def __search(self, key, node):
        try:
            if key < node.key:
                return self.__search(key, node.left)
            elif key > node.key:
                return self.__search(key, node.right)
            elif key == node.key:
                return node.value
        except AttributeError:
            print("Nie znalezniono")
            return None
    
    def insert(self, key, value):
        if self.root == None:
            self.root = Node(key, value)
            return None #nie ma poprzednika - zwraca None
        else:
            return self.__insert(key, value, self.root)
    
    def __insert(self, key, value, node):
        if key < node.key:
            if node.left != None:
                return self.__insert(key, value, node.left)
            else:
                node.left = Node(key, value)
                return node
        elif key > node.key:
            if node.right != None:
                return self.__insert(key, value, node.right)
            else:
                node.right = Node(key, value)
                return node
        elif key == node.key:
            node.value = value
            return node # Nie zwracam poprzednika, tylko obecny węzeł
            # tego fragmentu nie ma w wykładzie...
    
    def delete(self, key):
        if self.root == None:
            print("Drzewo puste")
            return None
        else:
            self.__delete(key, self.root, None)
        
    def __delete(self, key, node, node_prev):
        try:
            if key < node.key:                  # znajdowanie węzła do usunięcia
                self.__delete(key, node.left, node)
            elif key > node.key:
                self.__delete(key, node.right, node)
            elif key == node.key:
                if node.left == None and node.right == None: # węzeł bez dzieci
                    try:
                        if node_prev.right == node:
                            node_prev.right = None
                        else:
                            node_prev.left = None
                    except AttributeError:
                        self.root = None
                elif node.left == None and node.right != None: # węzły z 1 dzieckiem
                    try:
                        if node_prev.right == node:
                            node_prev.right = node.right
                        else:
                            node_prev.left = node.right
                    except AttributeError:
                        self.root = node.right
                elif node.left != None and node.right == None:
                    try:
                        if node_prev.right == node:
                            node_prev.right = node.left
                        else:
                            node_prev.left = node.left
                    except AttributeError:
                        self.root = node.left
                else:                                         # węzeł z 2 dzieci
                    node_new = node.right
                    node_new_prev = node.right
                    while node_new.left != None:
                        node_new_prev = node_new
                        node_new = node_new.left
                    try:
                        if node_prev.right == node:
                            node_prev.right = node_new
                        else:
                            node_prev.left = node_new
                    except AttributeError:
                        self.root = node_new
                        node_new_prev.left = node_new.right
                        self.root.right = node.right
                        self.root.left = node.left
                        return
                    node_new_prev.left = node_new.right
                    if node_new.key != node_new_prev.key:
                        node_new.right = node.right
                    node_new.left = node.left
        except AttributeError:
            print("Nie znalezniono", key)
            return None
    
    def __str__(self):
        return self.__visit(self.root)
    
    def __visit(self, node):
        res = ""
        if node.left != None:
            res += self.__visit(node.left)
        res += "{0} {1}, ".format(node.key, node.value)
        if node.right != None:
            res += self.__visit(node.right)
        return res
    
    def height(self):
        return self.__height(self.root)
    
    def __height(self, node):
        if node == None:
            return -1   # zakładam, że chodzi o ilosć połączeń, a nie węzłów
        left = self.__height(node.left)
        right = self.__height(node.right)
        if left > right:
            return left + 1
        else:
            return right + 1
        
    
    def print_tree(self):
        print("==============")
        self.__print_tree(self.root, 0)
        print("==============")

    def __print_tree(self, node, lvl):
        if node!=None:
            self.__print_tree(node.right, lvl+5)

            print()
            print(lvl*" ", node.key, node.value)
     
            self.__print_tree(node.left, lvl+5)
    
    
def main():
    tree = Tree()
    
    tree.insert(50, 'A')
    tree.insert(15, 'B')
    tree.insert(62, 'C')
    tree.insert(5, 'D')
    tree.insert(20, 'E')
    tree.insert(58, 'F')
    tree.insert(91, 'G')
    tree.insert(3, 'H')
    tree.insert(8, 'I')
    tree.insert(37, 'J')
    tree.insert(60, 'K')
    tree.insert(24, 'L')
    
    tree.print_tree()
    print(tree)
    
    print(tree.search(24))
    tree.insert(20, 'AA')
    tree.insert(6, 'M')
    tree.delete(62)
    tree.insert(59, 'N')
    tree.insert(100, 'P')
    tree.delete(8)
    tree.delete(15)
    tree.insert(55, 'R')
    tree.delete(50)
    tree.delete(5)
    tree.delete(24)
    print(tree.height())
    print(tree)
    tree.print_tree()
    
main()
