import numpy as np
import math

alphabet = 'abcdefghijklmnopqrstuvwxyz'


def invert_alpha(a):
    n = 0
    res = 0
    while True:
        s = 26*n+1
        if s%a == 0:
            res = s//a
            return res
        n += 1


def str_to_int(s):
    s.lower()
    res = [alphabet.find(i) for i in s]
    return res


def int_to_str(s):
    res = [alphabet[i] for i in s]
    return ''.join(res)


def get_key(file='key.txt'):
    with open(file, 'r') as f:
        q = []
        for line in f.readlines():
            q.append([int(i) for i in line.split()])
        
        return np.array(q) 


def encrypt(open_text, key, block_size):
    res = []
    open_text_int = str_to_int(open_text)
    for i in range(0, len(open_text), block_size):
        block = np.array(open_text_int[i:i+block_size])
        res += [i%26 for i in list(key.dot(block))]
    
    return res


def decrypt(close_text, key):
    
    return 0


if __name__ == '__main__':
    key = get_key()
    block_size = len(key)
    text = input('Input text: ')
    text = text + 'z'*(block_size * math.ceil(len(text)/block_size) - len(text))
    print(encrypt(text, key, block_size))
    # action = input('Input action(e-encrypt, d-decrypt): ')
    # if action == 'e':
    #     print(encrypt(text, key1, key2))
    # elif action == 'd':
    #     print(decrypt(text, key1, key2))