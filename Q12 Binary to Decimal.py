# In this program, if we are given any number in binary form, then we will learn to convert
#  that number in decimal form.


# binary_number = [1, 0, 0, 1, 1, 0, 1, 1]
# i=0
# d=0
# length=len(binary_number)-1
# while i<len(binary_number):
#     d+=binary_number[i]*2**length
#     i+=1
#     length=length-1
# print(d)


# binary_number = [1, 0, 0, 2, 1]


# binary_number = [1, 0, 0, "1", 1]





decimal_number = int(input("enter the number"))
print("decimal to binary:",bin(decimal_number))

def dtob(num):
    if num>1:
        dtob(num//2)
    print(num%2,end='')
decimal_number = int(input("enter the number"))
dtob(decimal_number)



# binary_number = list(input("enter the number:"))
# decimal = 0
# for i in range(len(binary_number)):
#     digit = binary_number.pop()
#     if digit == '1':
#         decimal=decimal+2**1
# print("decimal number:",decimal)









