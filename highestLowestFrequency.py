arr = [10,5,10,20,5,10]
freq = {}
for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
max_f = max(freq.values())
min_f = min(freq.values())
high = None
low = None

for a, b in freq.items():
    if b == max_f:
        high = a
    if b == min_f:
        low = a
print(high, low)