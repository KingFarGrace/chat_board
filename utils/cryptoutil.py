import base64

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

from exts import app


def decrypt(encrypted_data):
    """
    1.接收前端通过公钥加密后的数据，使用 base64 编码为字节流
    2.使用私钥初始化一个密码工具，对加密串进行解密，返回字节流
    注：公钥和私钥的生成见 config.cryptoconfig 只在生成时运行
    :param encrypted_data: 待解密字符串
    :return: 解密后字符串的字节流
    """
    missing_padding = 4 - len(encrypted_data) % 4
    if missing_padding != 4:
        encrypted_data += '=' * missing_padding
    app.logger.info('base64 decoding...')
    decode_data = base64.b64decode(encrypted_data)
    private_key = RSA.import_key(open("config/private_key.pem").read(), passphrase='123456')
    cipher = PKCS1_v1_5.new(private_key)
    data = ''
    try:
        sentinel = None
        data = cipher.decrypt(decode_data, sentinel)
        app.logger.info('finish decrypting')
    except Exception as e:
        app.logger.error('failed to decrypt.')
    return data
