import matplotlib.pyplot as plt
# from simple_replacement import encrypt
# from affin import encrypt

a = 'abcdefghijklmnopqrstuvwxyz'

symbols = {}
for i in a:
    symbols[i] = 0
    

def encrypt(open_text, a='abcdefghijklmnopqrstuvwxyz', key='zyxwvutsrqponmlkjihgfedcba'):
    res = []
    for i in open_text:
        if i == ' ':
            res.append(' ')
        else:
            if i in a:
                res.append(key[a.find(i)])
        
    return ''.join(res)


def decrypt(close_text, a='abcdefghijklmnopqrstuvwxyz', key='zyxwvutsrqponmlkjihgfedcba'):
    res = []
    for i in close_text:
        if i == ' ':
            res.append(' ')
        else:
            if i in a:
                res.append(a[key.find(i)])
        
    return ''.join(res)


with open('q.txt', 'r', encoding='UTF-8') as f:
    # text = f.read().lower()
    text = encrypt(f.read().lower())
    # text = encrypt(f.read().lower(), (9, 3))
# print(text[:500])
symbols_amount = 0
for i in text:
    if i in a:
        # t += i
        symbols[i] += 1
        symbols_amount += 1
symbols = dict(sorted(symbols.items(), key=lambda item: item[1]))
print(text, symbols_amount)
s = list(symbols.keys())
v = [i/symbols_amount*100 for i in symbols.values()]
print(''.join(s), v)


print(decrypt(s))
plt.bar(s,v)
plt.ylabel('%, процент от общего количества символов')
plt.xlabel('symbol')
plt.show()


print(symbols.items())

# abcdefghijklmnopqrstuvwxyz
# zyxwvutsrqponmlkjihgfedcba


#zqjxkvbpgfycwmuldrsnhioate
#jcaqpekytubdxnfowimhrslzgv