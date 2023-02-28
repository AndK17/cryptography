import numpy as np
import math

alphabet = 'abcdefghijklmnopqrstuvwxyz'


def str_to_int(s):
    s.lower()
    res = [alphabet.find(i) for i in s]
    return res


def int_to_str(s):
    res = [alphabet[i] for i in s]
    return ''.join(res)


def invert_alpha(a):
    print(a)
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
        print(det)
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
    
import itertools
pairs = [([7, 4, 11], [15, 15, 3]), ([8, 0, 12], [20, 4, 6]), ([2, 0, 13], [3, 2, 2]), ([24, 4, 18], [4, 8, 8]), ([13, 8, 2], [0, 1, 17]),
         ([12, 24, 13], [1, 4, 24]), ([18, 4, 17], [3, 24, 0]), ([1, 0, 18], [20, 21, 11]), ([1, 3, 5], [13, 20, 11])]
for i in itertools.combinations(pairs, len(pairs[0][0])):
    o_text = []
    c_text = []
    for j in i:
        o_text.append(j[0])
        c_text.append(j[1])
    
    print(np.array(o_text).T)
    print(invert_matrix(np.array(o_text).T))
    print()
if __name__ == '__main__':
    pass
    # print(get_m(pairs))
    
    # key = get_key(r'ot.txt')
    # print(key)
    # key = invert_matrix(key)
    # print(key)
    
    # t = get_key(r't.txt')
    
    
    # print(t.dot(key)%26)