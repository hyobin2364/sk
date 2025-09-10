# 다양한 매개변수
# 기본매개변수 default parameter

def myAdd(num1, num2=0, num3=0):
    return num1 + num2 + num3

result = myAdd(10)
print(f'result = {result}')

result = myAdd(10)
print(f'result = {result}')

result1 = myAdd()
result2 = myAdd(1)
result3 = myAdd(1,2)
result4 = myAdd(1,2,3)  #ctrl키 누르고 함수 누르면 보여줌
print(result1,result2,result3,result4)
