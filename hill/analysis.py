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



if __name__ == '__main__':
    key = get_key(r'ot.txt')
    print(key)
    key = invert_matrix(key)
    print(key)
    
    t = get_key(r't.txt')
    
    
    print(t.dot(key)%26)