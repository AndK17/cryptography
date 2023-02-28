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


def encrypt(open_text, key1, key2, block_size):
    res = []
    open_text_int = str_to_int(open_text)
    for i in range(0, len(open_text), block_size):
        block = np.array(open_text_int[i:i+block_size])
        res += [i%26 for i in list(key1.dot(block))]
        
        new_key = key1.dot(key2)
        key1, key2 = key2, new_key
    print(res)   
    
    return res


def decrypt(close_text, key1, key2, block_size):
    res = []
    close_text_int = str_to_int(close_text)
    for i in range(0, len(close_text_int), block_size):
        inv_key = invert_matrix(key1)
        block = np.array(close_text_int[i:i+block_size])
        res += [i%26 for i in list(inv_key.dot(block))]
        
        new_key = key1.dot(key2)
        key1, key2 = key2, new_key
    print(res)   
    return res


if __name__ == '__main__':
    key1 = get_key(r'D:\programming\hse\crypt\hill\key1.txt')
    key2 = get_key(r'D:\programming\hse\crypt\hill\key2.txt')
    block_size = len(key1)
    text = input('Input text: ')
    

    action = input('Input action(e-encrypt, d-decrypt): ')
    if action == 'e':
        text = text + 'z'*(block_size * math.ceil(len(text)/block_size) - len(text))
        res = encrypt(text, key1, key2, block_size)
        print(int_to_str(res))
    elif action == 'd':
        res = decrypt(text, key1, key2, block_size)
        print(int_to_str(res))