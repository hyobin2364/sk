#remove
list_a = [1,2,1,2]
#list_a.remove(1)
#print(list_a)
#1. solution
index = -1
for i in list_a:
    index += 1
    if i == 1:
        del list_a[index]
print(list_a)


list_b = [1,1,1,2]
#list_a.remove(1)
#print(list_a)
#1.solution
for i in range(3,-1,-1):
    if list_b[i]==1:
        del list_b[i]

print(list_b)

list_c = [1,1,1,2]

for i in range(len(list_c),3,1):
    if list_c[i]==1:
        del list_c[i]

print(list_c)

#remove
list_a = [1,1,1,2]
for i in range(len(list_a)):
    if 1 in list_a:
        list_a.remove(1)

