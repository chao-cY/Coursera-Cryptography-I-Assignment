#参考网址：https://cryptobook.nakov.com/symmetric-key-ciphers/aes-encrypt-decrypt-examples
#可运行的不可更改的，AES-CTR-256bits key 

import pyaes, pbkdf2, binascii, os, secrets

# Derive a 256-bit AES encryption key from the password    生成加密秘钥，但是作业中秘钥是直接给出的 
password = "s3cr3t*c0d3"
passwordSalt = os.urandom(16)  #生成16个字节=128bit的随机盐
key = pbkdf2.PBKDF2(password, passwordSalt).read(32)  #32个字节=256位key   十六进制 \x格式
print("AES encryption key in hex initial:", key)  
b_hex =  binascii.hexlify(key)
print('binascii.hexlify(key), AES encryption key in hex without \\x:',b_hex) #先把key转换成二进制数据然后在用十六进制表示，十六进制字符串编码
print('binascii.b2a_hex(key), AES encryption key in hex without \\x:',binascii.b2a_hex(key)) 
print("String.encode(): ",'你好'.encode())
hex_string = binascii.a2b_hex(b_hex)
print('binascii.a2b_hex(b_hex), we derive hex with \'\\x\': ',hex_string)


#加密算法，参数（256位key,随机生成的iv,明文）
# Encrypt the plaintext with the given key:
#   ciphertext = AES-256-CTR-Encrypt(plaintext, key, iv) 
iv = secrets.randbits(256)   #随机生成 32字节 = 256bits IV 
plaintext = "Text for encryption"
aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
ciphertext = aes.encrypt(plaintext)
print("Ciphertext in hex: ", ciphertext)
print('Ciphertext in bytes: ', binascii.hexlify(ciphertext))

#解密算法，参数（256key,iv，密文）
# Decrypt the ciphertext with the given key:
#   plaintext = AES-256-CTR-Decrypt(ciphertext, key, iv)
aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
decrypted = aes.decrypt(ciphertext)   #给hex格式，得到String格式明文
print('Decrypted:', decrypted)

