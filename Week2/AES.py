import Crypto.Cipher 
from os import urandom
from Crypto.Cipher import AES


#1.Generating a secret key
secret_key = urandom(16)

#2.Generating an initialization vector
iv  = urandom(16)

#3.Create an AES cipher
obj = AES.new(secret_key,AES.MODE_CBC,iv)

#4.Encrpt the message with AES
message = 'Lorem Ipsum text'.encode('utf8')
print('Original message is: ', message)
encrypted_text = obj.encrypt(message)
print('The encrypted text', encrypted_text)


obj = AES.new(secret_key,AES.MODE_CBC,iv)
decrypt_text = obj.decrypt(encrypted_text)
print('The decrypted text', decrypt_text)
