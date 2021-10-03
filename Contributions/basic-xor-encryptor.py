text = "flag{be551b494eac9a69a4584b8e2db0bb20}"

def encrypt(text,key):
    encrypted_txt = ''
    hex_enc_txt = ''
    for i in range(0,len(text)):
        xored = ord(text[i]) ^ ord(key)
        encrypted_txt +=  chr(xored)
        hex_enc_txt += hex(xored) + '-'
    li = list(hex_enc_txt)
    li.pop()
    hex_enc_txt = ''.join(li)
    return encrypted_txt,hex_enc_txt

def decrypt(ciphered_txt,key):
    decrypted_txt = ''
    for i in range(0,len(ciphered_txt)):
        xored = ord(ciphered_txt[i]) ^ ord(key)
        decrypted_txt += chr(xored)
    return decrypted_txt

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in alpha:
    ciphered_txt,cip_hex = encrypt(text, 'Q')

    # print(ciphered_txt)
    print(cip_hex)

    deciphered_txt = decrypt(ciphered_txt, i)
    print(deciphered_txt)
