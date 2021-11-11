# Write a code that works for any list, it shows the two averages as the output.
#  One is the average of even numbers and the other is the average of odd numbers from the given list.



elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
index = 0
k = 0
j = 0
s = 0
n = 0
while index<len(elements):
    if elements[index] % 2==0:
        s = s + elements[index]
        k = k + 1
        a = s//k
    if elements[index] % 2!=0:
        j = j + elements[index]
        n = n + 1
        b = j//n
    index = index + 1
print("even number in elements are",a)
print("odd numbers in elements are",b)