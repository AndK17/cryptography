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
    key_int = str_to_int(key*(len(close_text)//len(key)+1))
    for i in range(len(close_text_int)):
        res.append((close_text_int[i]-key_int[i])%26)
        
    return ''.join(int_to_str(res))


if __name__ == "__main__":
    text = input('Input text: ')
    
    for i in range(len(text)-3):
        print(text[i:i+3])