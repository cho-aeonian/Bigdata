# 파일열기 -> 데이터 읽기/쓰기 -> 파일 닫기
# 파일열기 -> 타 프로그램에서 작업 못하게 막은 뒤 파일 포인터를 가져옴
# 데이터 읽기/쓰기 : 신규 데이터 저장
# 파일 닫기 : 완료되면 파일 닫음 (타 프로그램에서 이제 사용 가능)

# 현재 파이썬의 working directory 확인
import os
print(os.getcwd())

# CWD가 다르므로 절대경로로 path 지정
path = '/Users/choyound/(중략)/data.txt'
fp = open(path)
str = fp.read()
print(str, emd='')
fp.close()