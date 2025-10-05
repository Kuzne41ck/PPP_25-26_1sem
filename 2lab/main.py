#Задание №1
import string
stroka = "aCaaCAcAbcbBCBB"
print(stroka)
l = len(stroka)
try:
    for i in range(l): 
        a = stroka[i]
        c = stroka.count(a)
        if 97<=ord(a)<=122:
            if c>stroka.count(chr(ord(a)-32)):
                stroka = stroka.replace(a, '')
                stroka = stroka.replace(chr(ord(a)-32), '')
except IndexError:
    print(stroka)
