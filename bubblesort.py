n = 5
arr = [10,5,20,15,25]

for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

for x in arr:
    print(x, end=" ")