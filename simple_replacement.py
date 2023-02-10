zm = 'abcdefghijklmnopqrstuvwxyz'


def encrypt(open_text, key='zyxwvutsrqponmlkjihgfedcba'):
    res = []
    for i in open_text:
        res.append(key[zm.find(i)])
        
    return ''.join(res)


def decrypt(close_text, key='zyxwvutsrqponmlkjihgfedcba'):
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
    action = input('Input action(e-encrypt, d-decrypt): ')
    if action == 'e':
        print(encrypt(text, key))
    elif action == 'd':
        print(decrypt(text, key))
    
    # text = 'abde'
    # key = 'zyxwvutsrqponmlkjihgfedcba'
    # text = encrypt(text, key)
    # print(text)
    # print(decrypt(text, key))