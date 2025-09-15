list_a = [273,32,103,"문자열", True , False]
print(list_a[3][2])
print(list_a[:])
print(list_a[:3])
print(list_a[3:])
print(list_a[-2:])

#start index : end index -1 : 1
print(list_a[::2])
print(list_a[::-1])

#리스트를 선언합니다
list_a = [1,2,3]
list_b = [4,5,6]

print(list_a + list_b )
print(list_a*3)
print(f'list_a + list_b = {list_a + list_b}')