# Skończone, 
# o ile poniższe nie jest konieczne :) :
# Czy priorytety węzłów równoległych (np. na wykładzie dla A, B, C, D) też nie
# powinny spełniać warunku kopca? Jeśli tak, to sprawdzanie jedynie rodzica 
# danego węzła i zamiana do skutku nie wystarczą - należałoby sprawdzić również
# "rodzica równoległego".

class Elem:
    def __init__(self, data, priority):
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
    def __init__(self):
        self.queue = []
        self.size = 0
    
    def is_empty(self):
        return False if len(self.queue) else True
    
    def peek(self):
        return self.queue[0]

    def dequeue(self):
        return self.__dequeue(0)

    def __dequeue(self, idx):
        try:
            if self.size == 0:
                raise AttributeError
            returned = self.queue[idx]
        except AttributeError:
            return None
            
        self.size -= 1
        self.queue[idx] = self.queue[self.size]
        self.queue[self.size] = returned
        
        # Przywracanie kopca
        while (self.left(idx) < self.size and \
        self.queue[idx] < self.queue[self.left(idx)]) or\
        (self.right(idx) < self.size and \
        self.queue[idx] < self.queue[self.right(idx)]):
            aux = self.queue[idx]
            if aux < self.queue[self.left(idx)] and \
            self.queue[self.left(idx)] > self.queue[self.right(idx)]:
                self.queue[idx] = self.queue[self.left(idx)]
                self.queue[self.left(idx)] = aux
                idx = self.left(idx)
            else:
                self.queue[idx] = self.queue[self.right(idx)]
                self.queue[self.right(idx)] = aux
                idx = self.right(idx)
        
        return returned
    
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

def main():
    heap = Heap()
    priorities = [7, 5, 1, 2, 5, 3, 4, 8, 9]
    data = "GRYMOTYLA"
    
    for p, d in zip(priorities, data):
        heap.enqueue(Elem(d, p))
    heap.print_tree(0, 0)
    heap.print_tab()
    dequeued = heap.dequeue()
    print(heap.peek())
    heap.print_tab()
    print(dequeued)
    while dequeued != None:
        dequeued = heap.dequeue()
        print(dequeued)
    heap.print_tab()
    
main()
