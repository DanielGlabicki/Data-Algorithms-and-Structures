# Skończone
class Elem:
    def __init__(self, priority, data):
        self.__dane = data
        self.__priorytet = priority
    
    def __lt__(self, other):
        if other == None:
            return False
        return self.__priorytet < other.__priorytet
    
    def __gt__(self, other):
        if other == None:
            return True
        return self.__priorytet > other.__priorytet
    
    def __repr__(self):
        return str(self.__priorytet) + " : " + str(self.__dane)


class Heap:
    def __init__(self, queue_to_sort=None):
        if queue_to_sort != None:
            self.queue = queue_to_sort
            self.size = len(self.queue)
            self.__sort() # Tworzenie kopca z listy
        else:
            self.queue = []
            self.size = 0
    
    def is_empty(self):
        return False if self.size else True
    
    def peek(self):
        return self.queue[0]

    def dequeue(self):
        try:
            if self.size == 0:
                raise AttributeError
            returned = self.queue[0]
        except AttributeError:
            return None
            
        self.size -= 1
        self.queue[0] = self.queue[self.size]
        self.queue[self.size] = returned
        
        self.__reheap(0)  # Przywracanie kopca
        
        return returned

    def __reheap(self, idx):  # Przywracanie kopca
        while (self.left(idx) < self.size and \
        self.queue[idx] < self.queue[self.left(idx)]) or\
        (self.right(idx) < self.size and \
        self.queue[idx] < self.queue[self.right(idx)]):
            aux = self.queue[idx]
            if aux < self.queue[self.left(idx)] and \
            (self.left(idx) == self.size - 1 or \
            self.queue[self.left(idx)] > self.queue[self.right(idx)]):
                self.queue[idx] = self.queue[self.left(idx)]
                self.queue[self.left(idx)] = aux
                idx = self.left(idx)
            else:
                self.queue[idx] = self.queue[self.right(idx)]
                self.queue[self.right(idx)] = aux
                idx = self.right(idx)
    
    def __sort(self):
        idx = self.parent(self.size - 1)
        while idx >= 0:
            self.__reheap(idx)
            idx -= 1
    
    def enqueue(self, elem):
        if self.size == len(self.queue):
            self.queue.append(elem)
        else:
            self.queue[self.size] = elem
        self.size += 1
        
        # Przywracanie kopca
        idx = self.size - 1
        while idx > 0 and elem > self.queue[self.parent(idx)]:
            self.queue[idx] = self.queue[self.parent(idx)]
            self.queue[self.parent(idx)] = elem
            idx = self.parent(idx)
    
    
    def left(self, idx):
        return 2 * idx + 1
    
    def right(self, idx):
        return 2 * idx + 2
    
    def parent(self, idx):
        if idx == 0:
            print("Root")
            return 0
        return (idx - 1)//2
    
    def print_tree(self, idx, lvl):
        if idx<len(self.queue):           
            self.print_tree(self.right(idx), lvl+1)
            print(2*lvl*'  ', self.queue[idx] if self.queue[idx] else None)           
            self.print_tree(self.left(idx), lvl+1)
    
    def print_tab(self):
        print ('{', end=' ')
        print(*self.queue[:self.size], sep=', ', end = ' ')
        print( '}')

def swap(queue):
    for i in range(len(queue) - 1):
        m = i
        for j in range(i, len(queue)):
            if queue[m] > queue[j]:
                m = j
        queue[i], queue[m] = queue[m], queue[i]

def shift(queue):
    for i in range(len(queue) - 1):
        m = i
        for j in range(i, len(queue)):
            if queue[m] > queue[j]:
                m = j
        queue.insert(i, queue.pop(m))
