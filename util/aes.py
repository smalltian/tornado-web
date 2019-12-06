#!-*- coding:utf-8 -*-

from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import base64
from hashlib import md5
import config


# 部位
def add_to_16(text):
    if len(text.encode('utf-8')) % 16:
        add = 16 - (len(text.encode('utf-8')) % 16)
    else:
        add = 0
    text = text + ('\0' * add)
    return text.encode('utf-8')


class AESCrypto:

    def __init__(self, aes_key):
        self.key = aes_key
        self.iv = self.key[:16]
        self.mode = AES.MODE_CBC

    # 加密
    def encrypt(self, text):
        try:
            text = add_to_16(text)
            cryptos = AES.new(self.key, self.mode, self.iv)
            cipher_text = cryptos.encrypt(text)
            b2a_hex_text = b2a_hex(cipher_text)
            return base64.b64encode(b2a_hex_text)
        except Exception:
            return None

    # 解密
    def decrypt(self, text):
        try:
            cryptos = AES.new(self.key, self.mode, self.iv)
            base64_text = base64.b64decode(text)
            plain_text = cryptos.decrypt(a2b_hex(base64_text))
            return bytes.decode(plain_text).rstrip('\0')
        except Exception:
            return None


# if __name__ == "__main__":
#     aes = AESCrypto(config.AES_KEY)
#     e = aes.encrypt('5de9bd7a421aa90b9009cf6e')
#     d = aes.decrypt(e)
#     print('encrypt:', e)
#     print('decrypt', d)

def md5_data(data):
    m = md5()
    m.update(data)
    return m.hexdigest()
