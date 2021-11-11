
# Write a program that tells how many elements are there in a given list. 
# It is similar to len() function, so in order to implement this program we will not
#  use len() function but we will try to understand that how did any programmer implemented
#  this len() function.

numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
count = 0
for i in (numbers):
    count+=1
print((count))