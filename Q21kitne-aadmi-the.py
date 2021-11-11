# Write a code that works for any list, and that tells how many odd numbers and how many even numbers are there in a given list.


elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]

Index = 0
k = 0
num = 0
while Index < len (elements):
    if elements[Index] % 2==0:
        k=k+1
    if elements[Index] % 2!=0:
        num=num+1
    Index=Index+1
print("even number in elemnts are:",k)
print("odd number in elements are:",num)