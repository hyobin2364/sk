# 가위 바위 보 게임 (컴퓨터 vs 휴먼)
# 가위:1 바위:2 보:3
# 규칙 : 컴퓨터가 임의로 숫자를 선택    :Random
# 인간이 숫자를 입력                   :input
# 승패를 기록
# 3번마다 계속 할지 물어보기            :for

import random
random.randint(1,3)
가위 = 1
바위 = 2
보 = 3

win = 0
lose = 0

def game():
    global win, lose
    computer = random.randint(1,3)
    user_input =  int(input('가위바위보!'))

    print(f'사용자= {user_input}, 컴퓨터 = {computer}')
    

    if computer == user_input:
        print("비겼습니다")

    elif user_input == 1 and computer == 2 or \
        user_input == 3 and computer == 1 or \
        user_input == 2 and computer == 3:
        win += 1
        print("이겼습니다.")
    else :
        lose +=1
        print("졌습니다.")

def is_user_continue():
    global win, lose
    if (win+lose) % 3 == 0:
        user_want =  input('게임을 이어서 하실건가요?(Y/N)').upper()
        if user_want == "Y":
            return True
        else:
            return False
    return True
        
is_continue = True         
while is_continue:
    game()
    is_continue = is_user_continue()

print(f'최종결과 : 승 = {win}, 패 = {lose}')
    