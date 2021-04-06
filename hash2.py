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
    hashValue = hashlib.sha256(msg)
    print(hashValue.hexdigest().upper())