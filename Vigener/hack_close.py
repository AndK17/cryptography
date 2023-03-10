alphabet = 'abcdefghijklmnopqrstuvwxyz'


def str_to_int(s):
    s.lower()
    res = [alphabet.find(i) for i in s]
    return res


def int_to_str(s):
    res = [alphabet[i] for i in s]
    return ''.join(res)


def decrypt(close_text, key='a'):
    res = []
    close_text_int = str_to_int(close_text)
    key_int = str_to_int(key)[0]
    for i in close_text_int:
        ot = (i-key_int)%26
        res.append(ot)
        key_int = i
    return ''.join(int_to_str(res))


if __name__ == "__main__":
    text = input('Input text: ')
    
    for i in alphabet:
        print(i, decrypt(text, i))