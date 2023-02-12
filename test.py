crypt =    'jcaqpekytubdxnfowimhrslzgv'
original = 'qxzjkvpbgfywcmuldrnsihoate'
#jcaqpekytubdxnfowimhrslzgv
#zqjxkvbpgfycwmuldrsnhioate


# abcdefghijklmnopqrstuvwxyz
# zyxwvutsrqponmlkjihgfedcba

def decrypt(close_text, a='abcdefghijklmnopqrstuvwxyz', key='zyxwvutsrqponmlkjihgfedcba'):
    res = []
    for i in close_text:
        if i == ' ':
            res.append(' ')
        else:
            if i in a:
                res.append(a[key.find(i)])
        
    return ''.join(res)


with open('encryptedq.txt', 'r', encoding='UTF-8') as f:
    text = f.read().lower()
print(decrypt(text, original, crypt)[:500])