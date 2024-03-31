# *arguments는 가변인자 : 별 한 개면 리스트
# **keywords는 키워드인자 : 별 두개면 딕셔너리

def caffe(beverage, *arguments, **keywords):
    print("Do U have any", beverage, "?")
    for arg in arguments:
        print(arg)
    print("*****")