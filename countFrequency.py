def countFrequency(arr):
    freq = {}
    for i in arr:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    for a, b in freq.items():
        print(a, b)
arr = [10,5,10,20,5,10]
countFrequency(arr)