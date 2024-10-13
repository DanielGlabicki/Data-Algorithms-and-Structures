# Skończone
import time

def naive_finder(S, W):
    t_start = time.perf_counter()
    
    m = 0
    m_end = len(S) - len(W)
    found = 0
    count = 0
    
    while m <= m_end:
        is_found = True
        for i in range(len(W)):
            count += 1
            if S[m + i] != W[i]:
                is_found = False
                break
        if is_found:
            found += 1
        m += 1
    
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start)) 
    
    return found, count


def my_hash(word, d, q):
    hw = 0
    for i in range(len(word) - 1):
        hw = (hw*d + ord(word[i])) % q
    return hw


def RK_finder(S, W):
    t_start = time.perf_counter()
    
    found = 0
    count = 0
    M = len(S)
    N = len(W)
    
    hW = my_hash(W, 256, 101)
    for m in range(M - N + 1):
        hS = my_hash(S[m:m+N], 256, 101)
        count += 1
        if hS == hW:
            if S[m:m+N] == W:
                found += 1
    
    t_stop = time.perf_counter()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    
    return found, count


def RH_finder(S, W, d, q):
#     t_start = time.perf_counter()
    
    found = 0
    count = 0
    collisions = 0
    M = len(S)
    N = len(W)
    
    h = 1
    for i in range(N - 1):
        h = (h*d) % q 
    
    hS = my_hash(S[0:N], d, q)
    hW = my_hash(W, d, q)
    count += 1
    
    
    for m in range(0, M - N + 1):
        if hS == hW:
            if S[0:N] == W:
                found += 1
            else:
                collisions += 1
        count += 1
        if hS == hW:
            if S[m:m+N] == W:
                found += 1
        try:
            hS = ((d * hS - ord(S[m]) * h) + ord(S[m+N-1])) % q
        except IndexError:
            pass
        if hS < 0:
            hS += q
    
    # t_stop = time.perf_counter()
    # print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start))
    
    return found, count, collisions


def main():
    with open("lotr.txt", encoding='utf-8') as f:
        text = f.readlines()
    
    S = ''.join(text).lower() # tekst
    W = "time." # wzorzec
    
    # res1 = naive_finder(S, W)
    # print(res1[0], "; ", res1[1])
    
    # res2 = RK_finder(S, W)
    # print(res2[0], "; ", res2[1])
    
    res3 = RH_finder(S, W, 256, 101)
    print(res3[0], "; ", res3[1], "; ", res3[2])

main()
