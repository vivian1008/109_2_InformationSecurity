import random as rand
class RSA:
    def __init__(self):
        print('Hello')
    def encrypt(self,msg):
        print('encrypt')
    def decrypt(self,msg):
        print('decrypt')
def genRandomList(self):
    data = []
    while len(data) < 6 :
        y = rand.randint(1024,65536)
        if(isPrime(y)):
            data.append(y)
    return data
def isPrime(self,x):
    flag = True
    i = 2
    while i < x/2:
        if x % i == 0:
            flag = False
            break
        i = i + 1
        return flag
def fun(self,N1,e):
    maxVal = max(N1,e)
    minVal = min(N1,e)
    if maxVal % minVal == 0:
        return minVal
    else:
        return fun(minVal,maxVal % minVal)
if __name__ == '__main__':
    rsa = RSA()
    rsa.encrypt('abcdefghijk')                             
    