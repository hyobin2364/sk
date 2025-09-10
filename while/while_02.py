import time

count = 0
while True:
    count +=1 
    print(f'{count}초')
    time.sleep(5)  #5초간 지연

    #5초 단위로 사용자한테 계속 할건지 물어본다.. "To be continue(Y/N)"
    if count % 5 ==0:
        is_continue = input('To be continue(Y/N)')
        is_continue = is_continue.upper()
        if not is_continue == 'Y':
        # if is_continue == 'Y' or is_continue == 'y'
            break
