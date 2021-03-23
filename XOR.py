import sys

class Crypt:
    def __init__(self,key):
        self.key = key

    def encrypt(self,msg):
        keylist = list(self.key)
        msglist = list(msg)
        keylen = len(keylist)
        msglen = len(msglist)
        cipherText = [''] * msglen

        for i in range(msglen):
            cipherText[i] = chr(ord(msglist[i])^ord(keylist[i % keylen]))  
            return ''.join(cipherText)

    def decrypt(self,msg):
        keylist = list(self.key)
        msglist = list(msg)
        keylen = len(keylist)
        msglen = len(msglist)
        cipherText = [''] * msglen

        for i in range(msglen):
            cipherText[i] = chr(ord(msglist[i])^ord(keylist[i % keylen]))  
            return ''.join(cipherText)

    if __name__ == "__main__":
        if len(sys.argv) > 2:
            if sys.argv[1] == '-e': 
                c = Crypt(sys.argv[2])
                print(c.encrypt(sys.argv[3])) 
            elif sys.argv[1] == '-d':
                c = Crypt(sys.argv[2])
                print(c.decrypt(sys.argv[3]))