import hashlib

def gen_md5_digest(content):
    return hashlib.md5(content.encode()).hexdigest()

# if __name__=="__main__":
#     print("admin123456-->{}".format(gen_md5_digest("admin123456")))
#     # admin123456-->a66abb5684c45962d887564f08346e8d


import random

ALL_CHARS = '23456789abcdefghjklmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'


def gen_random_code(length=4):
    return ''.join(random.choices(ALL_CHARS, k=length))
