#Skończone


def realloc(tab, size):
    oldSize = len(tab)
    return [tab[i] if i<oldSize else None  for i in range(size)]
    
class Queue:
    def __init__(self):
        self.tab = [None for i in range(5)]
        self.read = 0
        self.write = 0
    
    def is_empty(self):
        if self.read == self.write:
            return True
        else:
            return False
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.tab[self.read]
    
    def dequeue(self):
        if self.is_empty():
            return None
        else:
            data = self.tab[self.read]
            self.tab[self.read] = None
            self.read += 1
            if self.read == len(self.tab):
                self.read = 0
            return data
    
    def enqueue(self, el):
        if self.tab[self.write - 1] == None:
            self.tab[self.write] = el
            self.write += 1
        elif self.write != self.read:
            self.tab[self.write] = el
            self.write += 1
        else:
            self.tab = realloc(self.tab, 2 * len(self.tab))
            l = int(len(self.tab) / 2)
            for i in range(self.read, l):
                self.tab[i + l] = self.tab[i]
                self.tab[i] = None
            self.read += l
            self.tab[self.write] = el
            self.write += 1
        if self.write == len(self.tab):
                self.write = 0
    
    def __str__(self):
        out = "["
        i = self.read
        while i != self.write:
            out += "{}, ".format(self.tab[i])
            i += 1
            if i == len(self.tab):
                i = 0
        if self.peek() != None:
            out = out[:-2]
        out += "]"
        return out
    
    def test(self):
        return self.tab

def main():
    
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.dequeue())
    print(q.peek())
    print(q)
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    q.enqueue(8)
    print(q.test())
    while q.peek() != None:
        print(q.dequeue())
    print(q)
    

main()