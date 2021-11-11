# Write a code, that counts the numbers between 20 and 40 and then print its count.

numbers=[50, 40, 23, 70, 56, 22, 25, 10, 7]
l=len(numbers)
i=0
k=0
while i<l:
    c=numbers[i]
    if c<40 and c>20:
        k+=1
    i+=1
print(k)

