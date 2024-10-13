#Skończone

size = 6
half = size // 2

class Table:
    def __init__(self):
        self.tab = [None for i in range(size)]
        self.count = 0
        self.next = None
    
    def insert(self, idx, elem):
        self.count += 1
        for i in reversed(range(idx, self.count)):
            try:
                self.tab[i + 1] = self.tab[i]
            except IndexError:
                pass
        self.tab[idx] = elem
    
    def delete(self, idx):
        elem = self.tab[idx]
        for i in range(idx, self.count):
            try:
                self.tab[i] = self.tab[i + 1]
            except IndexError:
                self.tab[i] = None
        self.count -= 1
        return elem
    
class List:
    def __init__(self):
        self.head = None
        
    def __str__(self):
        string = '['
        tab = self.head
        while tab != None:
            for i in tab.tab:
                if i != None:
                    string += str(i) + ', '
            string += '|'
            tab = tab.next
        if self.head != None:
            string = string[:-3]
        string += ']'
        return string
        
    def get(self, idx):
        try:
            if idx < 0:
                raise IndexError
            total_count = 0
            nxt = self.head
            while nxt != None:
                if total_count + nxt.count >= idx:
                    return nxt.tab[idx - total_count]
                total_count += nxt.count
                nxt = nxt.next
            if total_count + nxt.count >= idx:
                return nxt.tab[idx - total_count]
            raise IndexError
        except IndexError:
            print('Out of range!')
            return None
        except TypeError:
            print('Empty list or invalid argument')
            return None
        
    def insert(self, idx, elem):
        try:
            if idx < 0:
                raise IndexError
            if self.head == None:
                self.head = Table()
                self.head.insert(0, elem)
                return
            total_count = 0
            nxt = self.head
            while nxt != None:
                if total_count + nxt.count >= idx:
                    insertion_tab = nxt
                    tab_idx = idx - total_count
                    break
                total_count += nxt.count
                if nxt.next == None:
                    prev = nxt
                nxt = nxt.next
            if "insertion_tab" not in locals():
                insertion_tab = prev
                tab_idx = prev.count
        except IndexError:
            print('Out of range!')
            return None
        
        if insertion_tab.count < size:
            insertion_tab.insert(tab_idx, elem)
        else:
            aux_tab = Table()
            aux_tab.next = insertion_tab.next
            insertion_tab.next = aux_tab
            for _ in range(half, size):
                aux_tab.insert(aux_tab.count, insertion_tab.delete(half))
            if tab_idx <= half:
                insertion_tab.insert(insertion_tab.count, elem)
            else:
                aux_tab.insert(tab_idx - aux_tab.count, elem)
        
    def delete(self, idx):
        try:
            if idx < 0:
                raise IndexError
            if self.head == None:
                raise TypeError
            total_count = 0
            nxt = self.head
            while nxt != None:
                if total_count + nxt.count > idx:
                    deletion_tab = nxt
                    tab_idx = idx - total_count
                    break
                total_count += nxt.count
                if nxt.next == None:
                    prev = nxt
                nxt = nxt.next
            if total_count + nxt.count > idx:
                deletion_tab = nxt
                tab_idx = idx - total_count
            else:
                raise IndexError
            if "deletion_tab" not in locals():
                insertion_tab = prev
                tab_idx = prev.count
        except IndexError:
            print('Out of range!')
            return None
        except TypeError:
            print('Empty list or invalid argument')
            return None
            
        deletion_tab.delete(tab_idx)
        if deletion_tab.count <= half and deletion_tab.next != None:
            deletion_tab.insert(deletion_tab.count, deletion_tab.next.delete(0))
            if deletion_tab.next.count < half:
                for _ in range(deletion_tab.next.count):
                    deletion_tab.insert(deletion_tab.count, deletion_tab.next.delete(0))
                deletion_tab.next = deletion_tab.next.next

def main():
    lst = List()
    for i in range(1, 10):
        lst.insert(i, i)
    print(lst.get(4))
    lst.insert(1, 10)
    lst.insert(8, 11)
    print(lst)
    lst.delete(1)
    lst.delete(2)
    print(lst)
    
main()
