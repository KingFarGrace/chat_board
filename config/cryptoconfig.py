# from Crypto.PublicKey import RSA
# key = RSA.generate(1024)
# # 生成密钥对
# # 提取私钥并存入文件 private_key.pem
# private_key = key.export_key(passphrase='123456', pkcs=8, protection="scryptAndAES128-CBC")
# file_out = open("private_key.pem", "wb")
# file_out.write(private_key)
#
# # 提取公钥存入文件 public_key.pem
# public_key = key.publickey().export_key()
# file_out = open("public_key.pem", "wb")
# file_out.write(public_key)
