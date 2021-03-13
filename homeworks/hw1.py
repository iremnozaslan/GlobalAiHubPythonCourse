even = [0,2,4,6,8,]
odd = [1,3,5,7,9]
merged  = even + odd
merged.sort()
for i in range(0, len(merged)):
    merged[i] = merged[i] * 2
    print(type(merged[i]))