#현재 파이썬의 working diretory 확인
import os
print(os.getcwd())

#CWD가 다르므로 절대경로로 path 지정
path = '/Users/choyoung/data.txt'
fp = open(path)
str = fp.read()
print(str, end='')
fp.close()