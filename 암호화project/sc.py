import binascii
import sys
from Crypto.Cipher import AES


class AESCipherCBC:
  
    def __init__(self, key):
        self.key = key
        self.iv = chr(0) *16
        self.blocksize = 16
        """iv는 16비트로 만들어줬고 blocksize는 16으로 지정"""
        self.padding = lambda s: s + (self.blocksize - len(s) % self.blocksize) * chr(self.blocksize - len(s) % self.blocksize)
        """pkcs5이용 data가 16나눠 지지않으면 data뒤에 16-나머지를 chr로 16-나머지만큼 붙힌다 """
        self.unpadding = lambda s: s[0:-ord(s[-1])]

    def encrypt(self, data):

        raw = self.padding(data)

        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        """aes128,cbc로 암호화 """
        encrypt = cipher.encrypt(raw)
        """padding된 raw를 암호화 """


        result = binascii.hexlify(encrypt)
        """결과를 이진 data 16진수로 바꿔서 저장 """
        return result

    def decrypt(self, data):
        enc = binascii.unhexlify(data)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        decrypt = cipher.decrypt(enc)
        """복호화한다"""
        decrypted_text = decrypt.decode('utf8')
        """bytes객체를 str로 바꾼"""
        result = self.unpadding(decrypted_text)

        return result

if __name__ == '__main__':
    ab= sys.argv[1:]
    key =str(sys.argv[2:])
    """ab는 1입력시 암호화 2입력시 복호화한"""
    a=""
    for i in range(2,len(key)-2):
        a+=key[i]



    if ab[0]=='1':
        ac=AESCipherCBC(a)
        for line in sys.stdin:
            """암호화할 파일을 읽어서 암호화하고 encrypt.txt에 str로 바꿔서 저장 """
            x=ac.encrypt(line)
            fw= open('encrypt.txt','w')
            fw.write(x.decode('utf8'))
            fw.close()

    if ab[0]== '2':
        ad= AESCipherCBC(a)
        for line in sys.stdin:
            xx = ad.decrypt(line)
            fw = open('decrypt.txt', 'w')
            fw.write(xx)
            fw.close()
            """encrypt.txt를 읽어서 복호화하고 decryot.txt에 저장"""