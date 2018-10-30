
基于 AES  CBC 模式的加密解密工具脚本

兼容 py2.7 py3.6

require pycrypto


```bash
pip install pycrypto

```

使用方法
```python
    import json
    from aes_cbc import AESCipher

    sig_message_decrypted = json.dumps({"name":"王炸","age":25,"addr":"珠海西山居","tel":"13888888888"})
    print("加密前明文: {}".format(sig_message_decrypted))
    aeskey = Random.new().read(32)
    aescipher = AESCipher(aeskey)
    message_aes_encrypted = aescipher.encrypt(sig_message_decrypted)
    print("密文: {}".format(message_aes_encrypted))
    message_aes_decrypted = aescipher.decrypt(message_aes_encrypted)
    print("解密后明文: {}".format(message_aes_decrypted))
```
