import hashlib
import string
import random
m=0
while True:
    str=""
    for i in range(10):
        str += random.choice(string.ascii_lowercase)
        """10자리 랜덤 문자열을 만들어서 해쉬함수에 넣어줌 """
    hashs = hashlib.sha256(str.encode())
    """bytes객체로 바꾼 문자열을 해쉬함수로 암호화 """
    hashs256 = hashs.hexdigest()
    """암호화된 문자열을 바이너리 16진수로 표현 """
    if hashs256[0]=="0" and hashs256[1]=="0" and hashs256[2]=="0" and hashs256[3]=="0":
        m+=1
        print(str," " ,hashs256)
    if m==2:
        break
"""16진수 0~3번 비트가 다 0이면 2진수에서 0~15번 비트까지 다 0 """