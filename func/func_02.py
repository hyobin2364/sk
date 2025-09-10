# 매개변수 O, 반환값 O
# 매개변수 O, 반환값 X
# 매개변수 X, 반환값 O
# 매개변수 X, 반환값 X

# 1.
def temp(C):
    F = C * 9/5 + 32 
    return F
print(temp(10))

#2. 
def myself(name):
    print(f'제 이름은 {name}입니다.' )
myself('김효빈')

#3.
import datetime
def gettime():
    self = f'현재시각은 {datetime.datetime.now()}입니다.'
    return self
print(gettime())

#4. 
def weather():
    print('날씨가 좋습니다.')
weather()