# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 19:32:34 2019

@author: 90415
"""
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


# 如果text不足16位的倍数就用空格补足为16位
def add_to_16(text):
    if len(text.encode('utf-8')) % 16:
        add = 16 - (len(text.encode('utf-8')) % 16)
    else:
        add = 0
    text = text + ('\0' * add)
    return text.encode('utf-8')


# 加密函数
def encrypt(text,key):
    key = key.encode('utf-8')
    mode = AES.MODE_CBC
    iv = b'qqqqqqqqqqqqqqqq'
    text = add_to_16(text)
    cryptos = AES.new(key, mode, iv)
    cipher_text = cryptos.encrypt(text)
    #因为AES加密后的字符串不一定是ascii字符集的，输出保存可能存在问题，所以这里转为16进制字符串
    return b2a_hex(cipher_text)


# 解密后，去掉补足的空格用strip() 去掉
def decrypt(text,key):
    key = key.encode('utf-8')
    iv = b'qqqqqqqqqqqqqqqq'
    mode = AES.MODE_CBC
    cryptos = AES.new(key, mode, iv)
    plain_text = cryptos.decrypt(a2b_hex(text))
    return bytes.decode(plain_text).rstrip('\0')


if __name__ == '__main__':
    str1 = "I am so handsome..."
    e = encrypt(str1,'0123456789101112')  # 加密
    d = decrypt(e,'0123456789101112')  # 解密
    print("原文:",str1)
    print("加密:", e)
    print("解密:", d)


