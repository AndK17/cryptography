zm = 'abcdefghijklmnopqrstuvwxyz'


def encript(open_text, key='zyxwvutsrqponmlkjihgfedcba'):
    res = []
    for i in open_text:
        res.append(key[zm.find(i)])
        
    return ''.join(res)


def decript(close_text, key='zyxwvutsrqponmlkjihgfedcba'):
    res = []
    for i in close_text:
        res.append(zm[key.find(i)])
        
    return ''.join(res)


if __name__ == "__main__":
    text = input('Input text: ')
    while True:
        key = input('Input key: ')
        if len(zm) == len(key):
            break
        else:
            print(f'Key eln must be {len(zm)}')
    action = input('Input action(e-encript, d-decript): ')
    if action == 'e':
        print(encript(text, key))
    elif action == 'd':
        print(decript(text, key))
    
    # text = 'abde'
    # key = 'zyxwvutsrqponmlkjihgfedcba'
    # text = encript(text, key)
    # print(text)
    # print(decript(text, key))