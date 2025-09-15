def change(obj):
    obj[0] = 100

data = [1,2,3]
a = 5
b = 4
change(data)
print(data)
print(f'a = {a} b = {b}')
print('-' * 30)

list_a = [1,2,3]
list_b = list_a.copy()
list_b[0] = 100
print(f'list_a = {list_a} list_b = {list_b}')