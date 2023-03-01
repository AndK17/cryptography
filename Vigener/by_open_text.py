alphabet = 'abcdefghijklmnopqrstuvwxyz'


def str_to_int(s):
    s.lower()
    res = [alphabet.find(i) for i in s]
    return res


def int_to_str(s):
    res = [alphabet[i] for i in s]
    return ''.join(res)


def encrypt(open_text, key='a'):
    res = []
    open_text_int = str_to_int(open_text)
    key_int = str_to_int(key+open_text[:-1])
    for i in range(len(open_text_int)):
        res.append((open_text_int[i]+key_int[i])%26)
        
    return ''.join(int_to_str(res))


def decrypt(close_text, key='a'):
    res = []
    close_text_int = str_to_int(close_text)
    key_int = str_to_int(key)[0]
    for i in range(len(close_text_int)):
        ot = (close_text_int[i]-key_int)%26
        res.append(ot)
        key_int = ot
    return ''.join(int_to_str(res))


if __name__ == "__main__":
    text = input('Input text: ')
    key = input('Input key: ')
    
    action = input('Input action(e-encrypt, d-decrypt): ')
    if action == 'e':
        print(encrypt(text, key))
    elif action == 'd':
        print(decrypt(text, key))