import hashlib
import sys

if len(sys.argv) > 1:
    msg = sys.argv[1].encode()
    hashvalue256 = hashlib.sha256(msg)
    hashvalue512 = hashlib.sha512(msg)
    hashvalue1 = hashlib.sha1(msg)
    hashvalueMD5 = hashlib.md5(msg)
    print(hashvalue256)
    print(hashvalue512)
    print(hashvalue1)
    print(hashvalueMD5)
    print(hashvalue256.hexdigest().upper())
    print(hashvalue512.hexdigest().upper())
    print(hashvalue1.hexdigest().upper())
    print(hashvalueMD5.hexdigest().upper())