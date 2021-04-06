import hashlib
import sys
import hmac
import  binascii

passwordlist = []
with open('passwordList.txt' , 'r') as filehandle:
    for  line in filehandle:
        currentPlace = line[:-1]
        passwordlist.append(currentPlace)


if len(sys.argv) == 2:
    msg = sys.argv[1].encode()
    hashValue256 = hashlib.sha256(msg)
    hashValue512 = hashlib.sha512(msg)
    hashValue1 = hashlib.sha1(msg)
    hashValueMD5 = hashlib.md5(msg)
    print('msg:',msg)
    print('sha256:',hashValue256.hexdigest().upper())
    print('sha512:',hashValue512.hexdigest().upper())
    print('sha1:',hashValue1.hexdigest().upper())
    print('md5:',hashValueMD5.hexdigest().upper())
    