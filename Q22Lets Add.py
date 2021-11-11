# Write a code that works for any list, it should give two sums as outputs, one is the sum of odd numbers present in the list and the other is the sum of even numbers present in the list.



elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
index = 0
k = 0
j = 0
s = 0
n = 0
while index<len(elements):
    if elements[index]%2==0:
        s=s+elements[index]
        k=k+1
    if elements[index]%2!=0:
        j=j+elements[index]
        n=n+1
    index=index+1
print("even number in elements are:",s)
print("odd number in elements are:",j)