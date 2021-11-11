# Write a code that works for any list, and that tells how many odd numbers
#  and how many even numbers are there in a given list.

elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=2
for i in(elements):
    if i%2==0:
        print("even:",i)
    else:
        print("odd:",i)