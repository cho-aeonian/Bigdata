import os
os.system('clear')

# 16진수, 8진수, 2진수 변수 초기화
a = 0xff
b = 0o67
c = 0b1010

# 10진수로 출력
print(a,b,c)

# 각 진수별로 표현
# %는 문자열 포매팅을 위한 기호
print("%x, %o, %s" %(a,b,bin(c)))

# 12를 각 진수별로 출력
print("%d, %x, %o" %(12,12,12))
print("%s, %s, %s" % (bin(12), hex(12), oct(12)))