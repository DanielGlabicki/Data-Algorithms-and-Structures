# Skończone
# Czy 'metody' przez wybieranie mają być 'metodami' klasy Heap, czy oddzielnymi 'funkcjami'?
# Jeśli to pierwsze, to różnice wydajnościowe w implementacjach byłyby znikome - O(nlog(n))
# Dlatego postanowiłem zrobić je jako oddzielne funkcje - O(n^2), żeby zauważyć różnicę

from Zad7_1 import Elem, Heap, swap, shift
import random, time

def main():
    tab = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), \
    (5,'H'), (1,'I'), (2,'J')]
    
    # Kopcowanie
    print("KOPCOWANIE")
    tab_of_elems =  [Elem(key, value) for key,value in  tab]
    heap = Heap(tab_of_elems)
    heap.print_tab()
    heap.print_tree(0, 0)
    while not heap.is_empty():
        heap.dequeue()
    print(tab_of_elems)
    print("Kopcowanie - Niestabilne sortowanie")
    
    rands = [int(random.random() * 100) for _ in range(10000)]
    t_start = time.perf_counter()
    rand_heap1 = Heap(rands)
    while not rand_heap1.is_empty():
        rand_heap1.dequeue()
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    print("==============================")
    
    
    # Swapowanie
    print("WYBIERANIE - Swap")
    tab_of_elems1 =  [Elem(key, value) for key,value in  tab]
    swap(tab_of_elems1)
    print(tab_of_elems1)
    print("Swapowanie - Niestabilne sortowanie")
    
    rands1 = [int(random.random() * 100) for _ in range(10000)]
    t_start = time.perf_counter()
    swap(rands1)
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    print("==============================")
    
    
    # Shiftowanie
    print("WYBIERANIE - Shift")
    tab_of_elems2 =  [Elem(key, value) for key,value in  tab]
    shift(tab_of_elems2)
    print(tab_of_elems2)
    print("Shiftowanie - Stabilne sortowanie")
    
    rands2 = [int(random.random() * 100) for _ in range(10000)]
    t_start = time.perf_counter()
    swap(rands2)
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    
main()
