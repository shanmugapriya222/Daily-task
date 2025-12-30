n = 5
arr = [2,5,1,3,0]

largest = arr[0]
for i in range(1, n):
    if arr[i] > largest:
        largest = arr[i]

print(largest)
