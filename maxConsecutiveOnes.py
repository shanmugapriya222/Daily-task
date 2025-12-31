n = 6
arr = [1,0,0,1,0,0]

max_count = 0
current_count = 0

for i in range(n):
    if arr[i] == 1:
        current_count += 1
        if current_count > max_count:
            max_count = current_count
    else:
        current_count = 0

print(max_count)
