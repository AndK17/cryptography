from affin_requr import *


def encript(open_text, key1=(1, 0), key2=(1, 0)):
    y = []
    open_text_int = str_to_int(open_text)
    alpha, beta = key1
    y.append((open_text_int[0]*alpha + beta)%26)
    alpha, beta = key2
    y.append((open_text_int[1]*alpha + beta)%26)
    
    for i in open_text_int[2:]:
        new_key = get_new_key(key1, key2)
        key1, key2 = key2, new_key
        alpha, beta = new_key
        y.append((i*alpha + beta)%26)
        
    
    return int_to_str(y)

s = 'cryptography'
for i in range(1, 30):
    s = encript(s, (3, 1), (5, 1))
    print(i, s)