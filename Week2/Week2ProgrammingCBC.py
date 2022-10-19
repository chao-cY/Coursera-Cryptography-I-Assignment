#本文件为完成Cryptography I 编程作业中CBC部分

import binascii
import re
from Crypto.Cipher import AES
import codecs
 
class AESCBC:
    def __init__(self):
        self.key = '140b41b22a29beb4061bda66b6747e14'  #定义key值    
        
        self.mode = AES.MODE_CBC
        self.bs = 16  # block size
        self.PADDING = lambda s: s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)
 
    def encrypt(self, text,iv):
        generator = AES.new(bytes.fromhex(self.key), self.mode,bytes.fromhex(iv))    #这里的key 和IV 一样 ，可以按照自己的值定义
        crypt = generator.encrypt(self.PADDING(text).encode("utf8"))
        # crypted_str = base64.b64encode(crypt)   #输出Base64
        crypted_str =binascii.b2a_hex(crypt)      #输出Hex
        result = crypted_str.decode()
        return result
 
    def decrypt(self, ctWithIv):
        generator = AES.new(bytes.fromhex(self.key), self.mode,bytes.fromhex(ctWithIv[0:32]))
        ct = ctWithIv[32:]
        ct += (len(ct) % 4) * '='
        # decrpyt_bytes = base64.b64decode(text)           #输出Base64
        decrpyt_bytes = binascii.a2b_hex(ct)           ##先把text转换成二进制数据然后在用十六进制表示,输出Hex
        print(len(decrpyt_bytes)%32)
        meg = generator.decrypt(decrpyt_bytes)
        # 去除解码后的非法字符
        try:
            result = re.compile('[\\x00-\\x08\\x0b-\\x0c\\x0e-\\x1f\n\r\t]').sub('', meg.decode())
        except Exception:
            result = '解码失败，请重试!'
        return result
 
 
if __name__ == '__main__':
    aes = AESCBC()

    #在本程序中需要去掉，密文中的IV前缀
    #hex格式的16byte为32个字符，所以直接去掉密文中的前32个字符
    CypherText_Hex = "4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81"   
    print("解密前:{0}\n解密后：{1}".format(CypherText_Hex,aes.decrypt(CypherText_Hex)))

    CypherText_Hex2 = "5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253"    
    print("解密前:{0}\n解密后：{1}".format(CypherText_Hex2,aes.decrypt(CypherText_Hex2)))

    

