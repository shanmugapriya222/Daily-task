n = 5
arr = [1,2,3,4,5]
num = 3

index = -1
for i in range(n):
    if arr[i] == num:
        index = i
        break

print(index)
