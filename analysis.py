import matplotlib.pyplot as plt
# from simple_replacement import encrypt
from affin import encrypt

a = 'abcdefghijklmnopqrstuvwxyz'

symbols = {}
for i in a:
    symbols[i] = 0
    

with open('text.txt', 'r') as f:
    # text = f.read()
    # text = encrypt(f.read().lower())
    text = encrypt(f.read().lower(), (9, 3))
    symbols_amount = len(text)
print(text[:500], symbols_amount)
# t = ''
for i in text:
    if i in a:
        # t += i
        symbols[i] += 1
symbols = dict(sorted(symbols.items(), key=lambda item: item[1]))
s = list(symbols.keys())
v = [i/symbols_amount*100 for i in symbols.values()]
print(s, v)
plt.bar(s,v)
plt.ylabel('%, процент от общего количества символов')
plt.xlabel('symbol')
plt.show()

# with open('ttext.txt', 'w') as f:
#     f.write(t)
print(symbols.items())

# abcdefghijklmnopqrstuvwxyz
# dmvenwfoxgpyhqzirajsbktclu