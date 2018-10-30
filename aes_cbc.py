#!/usr/bin/env python
#coding: utf8
# 
# author zhushaohua
# mail zshmmm@163.com
#
# 采用AES的CBC模式，这样AES加密支持VI，加密效果比ECB好
#

import sys

from Crypto import Random
from Crypto.Cipher import AES
import base64

PY2 = sys.version_info[0] == 2

if PY2:
    def s(x):
        return x.encode('utf-8') if isinstance(x, unicode) else x
    
    b = s

else:
    def s(x):
        return x.decode('utf-8') if isinstance(x, bytes) else x

    def b(x):
        return x.encode('utf-8') if not isinstance(x, bytes) else x

class AESCipher(object):

    def __init__(self, key):
        self.key = key
        self.__BS = 16

    @property
    def BS(self):
        return self.__BS

    def encrypt(self, msg):
        msg = b(msg)
        pad = lambda s: s + b((self.BS - len(s) % self.BS) * chr(self.BS - len(s) % self.BS))
        msg = pad(msg)
        iv = Random.new().read(self.BS)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(msg))

    def decrypt(self, enc):
        unpad = lambda s : s[:-ord(s[-1])]
        enc = base64.b64decode(enc)
        iv = enc[:self.BS]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return unpad(s(cipher.decrypt(enc[self.BS:])))

if __name__ == '__main__':
    import json

    sig_message_decrypted = json.dumps({"name":"王炸","age":25,"addr":"珠海西山居","tel":"13888888888"})
    print("加密前明文: {}".format(sig_message_decrypted))
    aeskey = Random.new().read(32)
    aescipher = AESCipher(aeskey)
    message_aes_encrypted = aescipher.encrypt(sig_message_decrypted)
    print("密文: {}".format(message_aes_encrypted))
    message_aes_decrypted = aescipher.decrypt(message_aes_encrypted)
    print("解密后明文: {}".format(message_aes_decrypted))
