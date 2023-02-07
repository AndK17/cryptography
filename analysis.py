import matplotlib.pyplot as plt
# from simple_replacement import encript
from affin import encript

a = 'abcdefghijklmnopqrstuvwxyz'

simbols = {}
for i in a:
    simbols[i] = 0
    

with open('text.txt', 'r') as f:
    # text = f.read()
    text = encript(f.read().lower(), (9, 3))
print(text[:500])
# t = ''
for i in text:
    if i in a:
        # t += i
        simbols[i] += 1
simbols = dict(sorted(simbols.items(), key=lambda item: item[1]))
s = list(simbols.keys())
v = list(simbols.values())
print(s, v)
plt.bar(s,v)
plt.show()

# with open('ttext.txt', 'w') as f:
#     f.write(t)
print(simbols.items())

# abcdefghijklmnopqrstuvwxyz
# dmvenwfoxgpyhqzirajsbktclu