#本章为完成Cryptography I 编程作业中CTR MODE部分

import pyaes, pbkdf2, binascii, os, secrets

CryptographySet = ['69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329',
    '770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451']

key= "36f18357be4dbd77f050515c73fcf9f2"
key = binascii.a2b_hex(key)

for ciphertext in CryptographySet:
    IV = ciphertext[0:32]   #读取IV
    IV_int = int(IV, 16)   #IV 从十六进制转十进制
    ciphertext = ciphertext[32:]
    print("ciphertext before binascii.a2b_hex: ",ciphertext)
    ciphertext = binascii.a2b_hex(ciphertext) #返回由十六进制字符串 hexstr 表示的二进制数据。(str类型转数据类型)
    print("ciphertext after binascii.a2b_hex: ",ciphertext)
    aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(IV_int))
    decrypted = aes.decrypt(ciphertext)   #给hex格式，得到String格式明文
    print('Decrypted:',decrypted)


#Decrypted: b'CTR mode lets you build a stream cipher from a block cipher.'
#Decrypted: b'Always avoid the two time pad!'

