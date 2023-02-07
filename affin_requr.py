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


def get_new_key(key1, key2):
    return(key1[0]*key2[0]%26, (key1[1]+key2[1])%26)
    
    
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


def decript(close_text, key1=(1, 0), key2=(1, 0)):
    y = []
    close_text_int = str_to_int(close_text)
    ialpha = invert_alpha(key1[0])
    beta = key1[1]
    y.append(((close_text_int[0] - beta)*ialpha)%26)
    ialpha = invert_alpha(key2[0])
    beta = key2[1]
    y.append(((close_text_int[1] - beta)*ialpha)%26)
    
    for i in close_text_int[2:]:
        new_key = get_new_key(key1, key2)
        key1, key2 = key2, new_key
        alpha, beta = new_key
        ialpha = invert_alpha(alpha)
        y.append(((i - beta)*ialpha)%26)
    
    return int_to_str(y)


if __name__ == '__main__':
    text = input('Input text: ')
    key1 = (int(input('Input alpha1: ')), int(input('Input beta1: ')))
    key2 = (int(input('Input alpha2: ')), int(input('Input beta2: ')))
    action = input('Input action(e-encript, d-decript): ')
    if action == 'e':
        print(encript(text, key1, key2))
    elif action == 'd':
        print(decript(text, key1, key2))