import numpy as np
import math
import itertools


alphabet = 'abcdefghijklmnopqrstuvwxyz'


def str_to_int(s):
    s.lower()
    res = [alphabet.find(i) for i in s]
    return res


def int_to_str(s):
    res = [alphabet[i] for i in s]
    return ''.join(res)


def invert_alpha(a):
    if a == 0:
        return 0
    n = 0
    res = 0
    while True:
        s = 26*n+1
        if s%a == 0:
            res = s//a
            return res
        n += 1
        

def invert_matrix(matrix):
    m_size = len(matrix)
    det = round(np.linalg.det(matrix))%26
    if math.gcd(det, 26) != 1:
        return 'Bad matrix'
    
    inv_det = invert_alpha(det)
    inv_matrix = matrix.copy()
    
    for i in range(m_size):
        for j in range(m_size):
            q = np.delete(matrix, (i), axis=0)
            q = np.delete(q, (j), axis=1)
            inv_matrix[j][i] = round(((-1)**(i+j))*np.linalg.det(q))*inv_det%26
    return inv_matrix
    
    
def get_key(file='key.txt'):
    with open(file, 'r') as f:
        q = []
        for line in f.readlines():
            q.append([int(i) for i in line.split()])
        
        return np.array(q) 

def get_m(pairs):
    print(pairs)
    if pairs == []:
        return [], []
    
    matr = []
    for i in pairs:
        print(i, pairs.copy().remove(i))
        open_t, close_t = get_m(pairs.copy().remove(i))
        open_t.append(i[0])
        close_t.append(i[1])
        matr.append((open_t, close_t))
        print(matr)
    return matr
    

pairs1 = [([7, 4, 11], [15, 15, 3]), ([12, 24, 13], [1, 4, 12]), ([2, 0, 13], [3, 2, 2]), ([1, 3, 5], [13, 20, 11])]
pairs2 = [([11, 14, 25], [21, 19, 12]), ([1, 12, 4], [4, 9, 15]), ([24, 14, 20], [4, 24, 16]), ([17, 25, 25], [18, 12, 1])]

if __name__ == '__main__':
    pairs = pairs2
    for i in itertools.combinations(pairs, len(pairs[0][0])):
        o_text = []
        c_text = []
        for j in i:
            o_text.append(j[0])
            c_text.append(j[1])
        
        
        m = invert_matrix(np.array(o_text).T)
        if m != 'Bad matrix':
            print(np.array(o_text).T)
            print(np.array(c_text).T)
            print('NICE')
            print(m)
            print(np.array(c_text).T.dot(m)%26)
        print()