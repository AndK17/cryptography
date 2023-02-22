zm = 'abcdefghijklmnopqrstuvwxyz'

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
    res = [zm.find(i) for i in s]
    return res


def int_to_str(s):
    res = [zm[i] for i in s]
    return ''.join(res)


def encrypt(open_text, key=(1, 0)):
    open_text_int = str_to_int(open_text)
    alpha, beta = key
    y = []
    
    for i in open_text_int:
        y.append((i*alpha + beta)%26)
    
    return int_to_str(y)


def decrypt(close_text, key=(1, 0)):
    close_text_int = str_to_int(close_text)
    ialpha = invert_alpha(key[0])
    beta = key[1]
    y = []
    
    for i in close_text_int:
        y.append(((i - beta)*ialpha)%26)
    
    return int_to_str(y)


if __name__ == "__main__":
    text = input('Input text: ')
    key = (int(input('Input alpha: ')), int(input('Input beta: ')))
    action = input('Input action(e-encrypt, d-decrypt): ')
    if action == 'e':
        print(encrypt(text, key))
    elif action == 'd':
        print(decrypt(text, key))