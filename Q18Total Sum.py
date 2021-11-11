# Q: How to find all pairs in an array of integers whose sum is equal to the given number?
number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19]
index = 0
m=[]
while index<len(n):
    j=4
    while j<len(n):
        if n[index]+n[j]==number:
            m.append([n[index],n[j]])
        j+=1
    index+=1
print(m)



# Output:-

# [[11,19], [12,18],[13,17]]
