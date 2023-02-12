import matplotlib.pyplot as plt
# from simple_replacement import encrypt
from affin import *

a = 'abcdefghijklmnopqrstuvwxyz'

symbols = {}
for i in a:
    symbols[i] = 0
    
    
def str_to_int(s):
    s.lower()
    res = []
    for i in s:
        if i == ' ':
            res.append(' ')
        else:
            if i in a:
                res.append(a.find(i))
            
    
    return res


def int_to_str(s):
    return a[s]

    
def encrypt(open_text, key=(9, 3)):
    open_text_int = str_to_int(open_text)
    alpha, beta = key
    y = []
    
    for i in open_text_int:
        if i == ' ':
            y.append(' ')
        else:
            y.append(int_to_str((i*alpha + beta)%26))
    
    return ''.join(y)


def decrypt(close_text, key=(9, 3)):
    close_text_int = str_to_int(close_text)
    ialpha = invert_alpha(key[0])
    beta = key[1]
    y = []
    
    for i in close_text_int:
        y.append(((i - beta)*ialpha)%26)
    
    return int_to_str(y)


with open('q.txt', 'r', encoding='UTF-8') as f:
    # text = f.read().lower()
    text = encrypt(f.read().lower(), (9, 3))
print(text[:500])
print()
print(text)


symbols_amount = 0
for i in text:
    if i in a:
        # t += i
        symbols[i] += 1
        symbols_amount += 1
symbols = dict(sorted(symbols.items(), key=lambda item: item[1]))
# print(text, symbols_amount)
s = list(symbols.keys())
v = [i/symbols_amount*100 for i in symbols.values()]
print(''.join(s), v)


# print(decrypt(''.join(s)))
plt.bar(s,v)
plt.ylabel('%, процент от общего количества символов')
plt.xlabel('symbol')
plt.show()


print(symbols.items())


# abcdefghijklmnopqrstuvwxyz
# dmvenwfoxgpyhqzirajsbktclu

# zqjxkvbpgfycwmuldrsnhioate
# urgcpkmlibtfvwhyejzaxoqdsn


#urgcpkmlibtfvwhyejzaxoqdsn