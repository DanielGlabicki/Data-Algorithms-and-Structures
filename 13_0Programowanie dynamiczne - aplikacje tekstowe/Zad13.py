# Skończone
import numpy as np
import re

def string_compare(P, T, i, j):
    if i == 0:
        return j
    if j == 0:
        return i
    
    if P[i] != T[j]:
        switches = string_compare(P,T,i-1,j-1) + 1
    else:
        switches = string_compare(P,T,i-1,j-1)
    inserts = string_compare(P,T,i,j-1) + 1
    deletions = string_compare(P,T,i-1,j) + 1
    
    return min(switches, inserts, deletions)
    

def PD_compare(P, T, i, j):
    D = np.zeros((i, j))
    D[:, 0] = np.arange(0, i)
    D[0, :] = np.arange(0, j)
    
    C = np.chararray((i, j)) # Rodzice
    C[:] = 'X'
    C[:, 0] = 'D'
    C[0, :] = 'I'
    C[0, 0] = 'X'
    
    for ii in range(1, i):
        for jj in range(1, j):
            if P[ii] != T[jj]:
                switches = D[ii-1,jj-1] + 1
            else:
                switches = D[ii-1,jj-1]
            inserts = D[ii,jj-1] + 1
            deletions = D[ii-1,jj] + 1
            
            operations = [switches, inserts, deletions]
            idx = operations.index(min(operations))
            D[ii][jj] = operations[idx]
            if idx == 0:
                if P[ii] != T[jj]:
                    C[ii][jj] ='S'
                else:
                    C[ii][jj] ='M'
            elif idx == 1:
                C[ii][jj] ='I'
            elif idx == 3:
                C[ii][jj] ='D'
    
    path = []
    ii = i - 1
    jj = j - 1
    char = str(C[-1][-1])[2]
    while char != 'X':
        char = str(C[ii][jj])[2]
        if char == 'M' or char == 'S':
            ii -= 1
            jj -= 1
        elif char == 'I':
            jj -= 1
        else:
            ii -= 1
        path.append(char)
    
    path.reverse()
    path =re.sub("[],'[ ]","",str(path))
    return int(D[-1][-1]), path[1:]


def PD_compare_d(P, T, i, j):
    D = np.zeros((i, j))
    D[:, 0] = np.arange(0, i)
    
    C = np.chararray((i, j)) # Rodzice
    C[:] = 'X'
    C[1:, 0] = 'D'
    
    for ii in range(1, i):
        for jj in range(1, j):
            if P[ii] != T[jj]:
                switches = D[ii-1,jj-1] + 1
            else:
                switches = D[ii-1,jj-1]
            inserts = D[ii,jj-1] + 1
            deletions = D[ii-1,jj] + 1
            
            operations = [switches, inserts, deletions]
            idx = operations.index(min(operations))
            D[ii][jj] = operations[idx]
    
    last_row = list(D[-1])
    return last_row.index(min(last_row)) - i + 2


def PD_compare_e(P, T, i, j):
    D = np.zeros((i, j))
    D[:, 0] = np.arange(0, i)
    D[0, :] = np.arange(0, j)
    
    C = np.chararray((i, j)) # Rodzice
    C[:] = 'X'
    C[:, 0] = 'D'
    C[0, :] = 'I'
    C[0, 0] = 'X'
    
    for ii in range(1, i):
        for jj in range(1, j):
            if P[ii] != T[jj]:
                switches = np.inf
            else:
                switches = D[ii-1,jj-1]
            inserts = D[ii,jj-1] + 1
            deletions = D[ii-1,jj] + 1
            
            operations = [switches, inserts, deletions]
            idx = operations.index(min(operations))
            D[ii][jj] = operations[idx]
            if idx == 0:
                if P[ii] != T[jj]:
                    C[ii][jj] ='S'
                else:
                    C[ii][jj] ='M'
            elif idx == 1:
                C[ii][jj] ='I'
            elif idx == 3:
                C[ii][jj] ='D'
    
    seq = []
    ii = i - 1
    jj = j - 1
    char = str(C[-1][-1])[2]
    while ii > 0 and jj > 0:
        char = str(C[ii][jj])[2]
        if char == 'M' or char == 'S':
            seq.append(P[ii])
            ii -= 1
            jj -= 1
        elif char == 'I':
            jj -= 1
        else:
            ii -= 1
    
    seq.reverse()
    seq = re.sub("[],'[ ]","",str(seq))
    return seq


def PD_compare_f(T, j):
    P = ''.join(sorted(T))
    i = j
    
    D = np.zeros((i, j))
    D[:, 0] = np.arange(0, i)
    D[0, :] = np.arange(0, j)
    
    C = np.chararray((i, j)) # Rodzice
    C[:] = 'X'
    C[:, 0] = 'D'
    C[0, :] = 'I'
    C[0, 0] = 'X'
    
    for ii in range(1, i):
        for jj in range(1, j):
            if P[ii] != T[jj]:
                switches = np.inf
            else:
                switches = D[ii-1,jj-1]
            inserts = D[ii,jj-1] + 1
            deletions = D[ii-1,jj] + 1
            
            operations = [switches, inserts, deletions]
            idx = operations.index(min(operations))
            D[ii][jj] = operations[idx]
            if idx == 0:
                if P[ii] != T[jj]:
                    C[ii][jj] ='S'
                else:
                    C[ii][jj] ='M'
            elif idx == 1:
                C[ii][jj] ='I'
            elif idx == 3:
                C[ii][jj] ='D'
    
    seq = []
    ii = i - 1
    jj = j - 1
    char = str(C[-1][-1])[2]
    while ii > 0 and jj > 0:
        char = str(C[ii][jj])[2]
        if char == 'M' or char == 'S':
            seq.append(P[ii])
            ii -= 1
            jj -= 1
        elif char == 'I':
            jj -= 1
        else:
            ii -= 1
    
    seq.reverse()
    seq = re.sub("[],'[ ]","",str(seq))
    return seq

def main():
    P = ' kot'
    T = ' pies'
    print(string_compare(P, T, len(P) - 1, len(T) - 1))
    
    P = ' biały autobus'
    T = ' czarny autokar'
    print(PD_compare(P, T, len(P), len(T))[0])
    
    P = ' thou shalt not'
    T = ' you should not'
    print(PD_compare(P, T, len(P), len(T))[1])
    
    P = ' ban'
    T = ' mokeyssbanana'
    print(PD_compare_d(P, T, len(P), len(T)))
    
    P = ' democrat'
    T = ' republican'
    print(PD_compare_e(P, T, len(P), len(T)))
    
    T = ' 243517698'
    print(PD_compare_f(T, len(T)))


main()