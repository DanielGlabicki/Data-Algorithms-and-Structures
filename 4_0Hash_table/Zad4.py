# Poprawione
# Wyszukiwanie (nieistniejącego w tablicy) jest bliskie O(N) przez to, że nie 
# przerywa Pan po znalezieniu pierwszego None-a 
class Obj:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.delete = False
    
    def __str__(self):
        return str(self.key) + ":" + str(self.value)


class Table:
    def __init__(self, size=5, c1=1, c2=0):
        self.tab = [None for i in range(size)]
        self.size = size
        self.c1 = c1
        self.c2 = c2
    
    def mod(self, obj):
        if type(obj.key) is int:
            modulo = obj.key % self.size
        elif type(obj.key) is str:
            obj_sum = 0
            for i in obj.key:
                obj_sum += ord(i)
            modulo = obj_sum % self.size
        else:
            print("Zły typ danych")
            return None
        return modulo
    
    def probe(self, obj):
        inserted = False
        if self.tab[self.mod(obj)] == None \
        or self.tab[self.mod(obj)].delete \
        or self.tab[self.mod(obj)].key == obj.key:
            self.tab[self.mod(obj)] = obj
            inserted = True
        else:
            i = 1
            idx = self.c1 * i + self.c2 * i ** 2
            while i <= self.size:
                if self.tab[(self.mod(obj) + idx) % self.size] == None \
                or self.tab[(self.mod(obj) + idx) % self.size].delete \
                or self.tab[(self.mod(obj) + idx) % self.size].key == obj.key:
                    self.tab[(self.mod(obj) + idx) % self.size] = obj
                    inserted = True
                    break
                else:
                    i += 1
                    idx = self.c1 * i + self.c2 * i ** 2
        return inserted
            
    def search(self, idx):
        i = 0 # <-- alternatywna wersja, która generowała problemy z search(31)
        # edit: z tego co rozumiem z odpowiedzi zwrotnej, to co uważałem za problemy,
        # czyli nie znaleznienie 31:G jest prawidłowe
        while i < self.size:
            c_idx = self.c1 * i + self.c2 * i ** 2
            if self.tab[(idx + c_idx) % self.size] == None:
                print("Nie znaleziono")
                return None
            elif idx == self.tab[(idx + c_idx) % self.size].key:
                return self.tab[(idx + c_idx) % self.size].value
            i += 1
        print("Nie znaleziono")
        return None
        # i = 0
        # while i < self.size:
        #     if self.tab[i] is not None and not self.tab[i].delete:
        #         if idx == self.tab[i].key:
        #             return self.tab[i].value
        #     elif elf.tab[i] is None:
        #         print("Nie znaleziono")
        #         return None
        #     i += 1
        # print("Nie znaleziono")
        # return None
        
    def insert(self, obj):
        if not self.probe(obj):
            print ("Brak miejsca")
            return None
    
    def remove(self, idx):
        if self.tab[idx] == None:
            print ("Brak danej")
            return None
        else:
            self.tab[idx].delete = True
    
    def __str__(self):
        string = "{"
        for i in self.tab:
            if i != None:
                if not i.delete:
                    string += str(i.key) + ":" + str(i.value) + ", "
                else:
                    string += "None, "
            else:
                string += "None, "
        string = string[:-2]
        string += "}"
        return string
    
def test1(size, c1, c2):
    t1 = Table(size, c1, c2)
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', \
    'L', 'M', 'N', 'O']
    for i in range(1, 6):
        t1.insert(Obj(i, letters[i - 1]))
    t1.insert(Obj(18, letters[5]))
    t1.insert(Obj(31, letters[6]))
    for i in range(8, 16):
        t1.insert(Obj(i, letters[i - 1]))
    print(t1)
    print(t1.search(5))
    print(t1.search(14))
    t1.insert(Obj(5, 'Z'))
    print(t1.search(5))
    t1.remove(5)
    print(t1)
    print(t1.search(31))
    t1.insert(Obj('test', 'W'))
    print(t1)

def test2(size, c1, c2):
    t1 = Table(size, c1, c2)
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', \
    'L', 'M', 'N', 'O']
    for i in range(1, 6):
        t1.insert(Obj(13 * i, letters[i - 1]))
    t1.insert(Obj(18, letters[5]))
    t1.insert(Obj(31, letters[6]))
    for i in range(8, 16):
        t1.insert(Obj(13 * i, letters[i - 1]))
    print(t1)
    

def main():
    test1(13, 1, 0)
    print("---------------------------------------------")
    test2(13, 1, 0)
    print("---------------------------------------------")
    test2(13, 0, 1)
    print("---------------------------------------------")
    test1(13, 0, 1)

main()
