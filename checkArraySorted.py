n = 5
arr = [5,6,4,3,8]

is_sorted = True
for i in range(n - 1):
    if arr[i] > arr[i + 1]:
        is_sorted = False
        break

print(is_sorted)
