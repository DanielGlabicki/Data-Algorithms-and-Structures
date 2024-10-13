#Poprawione - teraz zwalnianie pamięci powinno działać

# def destroy(self):
# if self.head != None:
# self.head = None
# self.tail = None -- to nie spowoduje zwolnienia pamięci

class Obj:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LL:
    def __init__(self): #create
        self.head = None
        self.tail = None
        
    def destroy(self):
        if self.head != None:
            ptr = self.head
            while ptr.next != None:
                ptr = ptr.next
                ptr.prev = None
            self.head = None
            self.tail = None
        
    def add(self, obj):
        obj.next = self.head
        if self.head != None:
            self.head.prev = obj
        else:
            self.tail = obj
        self.head = obj
        
    def append(self, obj):
        obj.prev = self.tail
        if self.tail != None:
            self.tail.next = obj
        else:
            self.head = obj
        self.tail = obj
        
    def remove(self):
        if self.head != None:
            self.head = self.head.next
            if self.head != None:
                self.head.prev = None
            else:
                self.tail = None
        else:
            print("Lista pusta\n")
            
    def remove_end(self):
        if self.tail != None:
            self.tail = self.tail.prev
            if self.tail != None:
                self.tail.next = None
            else:
                self.head = None
        else:
            print("Lista pusta\n")
    
    def is_empty(self):
        return self.head == None
        
    def length(self):
        if self.head != None:
            i = 0
            ptr = self.head
            while ptr != None:
                ptr = ptr.next
                i += 1
            return i
        else:
            return 0
    
    def get(self):
        if self.head == None:
            return None
        else:
            return self.head.data
            
    def disp(self):
        if self.head == None:
            print(self.head)
        else:
            lst = ""
            ptr = self.head
            while ptr != None:
                lst += "-> {}\n".format(ptr.data)
                ptr = ptr.next
            print(lst) # w skrypcie jest mowa o wypisaniu, a nie o zwróceniu
                       # dlatego użyłem printa
        

def main():
    uczelnie = [('AGH', 'Kraków', 1919),
    ('UJ', 'Kraków', 1364),
    ('PW', 'Warszawa', 1915),
    ('UW', 'Warszawa', 1915),
    ('UP', 'Poznań', 1919),
    ('PG', 'Gdańsk', 1945)]
    
    ucz_list = LL()
    
    for i in range(3):
        ucz_list.append(Obj(uczelnie[i]))
    
    for i in range(3, 6):
        ucz_list.add(Obj(uczelnie[i]))
    
    ucz_list.disp()
    
    print(ucz_list.length(), "\n")
    
    ucz_list.remove()
    
    print(ucz_list.get(), "\n")
    
    ucz_list.remove_end()
    
    ucz_list.disp()
    
    ucz_list.destroy()
    
    print(ucz_list.is_empty(), "\n")
    
    ucz_list.remove()
    
    ucz_list.append(Obj(uczelnie[0]))
    
    ucz_list.remove_end()
    
    print(ucz_list.is_empty())
    
main()
        