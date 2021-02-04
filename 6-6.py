# 11분

n=int(input())
array=[]
for i in range(n):
    array.append(int(input()))

array=sorted(array, reverse=1)

for i in array:
    print(i, end=' ')