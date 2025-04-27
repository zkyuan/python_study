"""
 * @author: zkyuan
 * @date: 2025/4/17 10:08
 * @description:
 finalshell:
 account:zkyuan
 password:123456
 机器码：zkyuan@0f73727dde74e13d
 生成激活码
"""
# from hashlib import md5, sha3_384
# from Crypto.Hash import keccak
#
# def md5_hash(msg):
#     return md5(msg.encode()).hexdigest()
#
# def keccak384_hash(msg):
#     keccak_hash = keccak.new(digest_bits=384)
#     keccak_hash.update(msg.encode())
#     return keccak_hash.hexdigest()
#
# def main():
#     code = input("输入机器码: ")
#     print("版本号 < 3.9.6 (旧版)")
#     try:
#         print("高级版: " + md5_hash("61305" + code + "8552")[8:24])
#         print("专业版: " + md5_hash("2356" + code + "13593")[8:24])
#     except Exception as e:
#         print(str(e))
#         print("3.9.6 <= 版本号 < 4.3.10")
#     try:
#         print("高级版: " + keccak384_hash(code + "hSf(78cvVlS5E")[12:28])
#         print("专业版: " + keccak384_hash(code + "FF3Go(*Xvbb5s2")[12:28])
#     except Exception as e:
#         print(str(e))


from Crypto.Hash import MD5
from Crypto.Hash import keccak


def md5(msg):
    hash_obj = MD5.new(msg)
    return hash_obj.hexdigest()


def keccak384(msg):
    hash_obj = keccak.new(data=msg, digest_bits=384)
    return hash_obj.hexdigest()


def main():
    code = input('输入机器码: ')
    print('版本号 < 3.9.6 (旧版)')
    print('高级版:', md5(f'61305{code}8552'.encode())[8:24])
    print('专业版:', md5(f'2356{code}13593'.encode())[8:24])
    print('版本号 >= 3.9.6 (新版)')
    print('高级版:', keccak384(f'{code}hSf(78cvVlS5E'.encode())[12:28])
    print('专业版:', keccak384(f'{code}FF3Go(*Xvbb5s2'.encode())[12:28])


if __name__ == "__main__":
    main()
