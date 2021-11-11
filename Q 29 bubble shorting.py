a = [1,2,5,6,3,2,9,8,7]
for j in range(0,10):
    for i in range(0,8):
        if a[i]>a[i+1]:
            d=a[i]
            a[i]=a[i+1]
            a[i+1] = d
print("sorted list is:",a)
print()

#  c = int (input("enter the number:"))


# size = int(input("enter the size of list:"))
# value = int(input("enter the number:"))
# a = []



# a=[1,2,5,4,3,2,4,8]
# for j in range(0,9):
#     for i in range(0,7):
#         if a[i]>a[i+1]:
#             b=a[i]
#             a[i]=a[i+1]
#             a[i+1]=b
# print(a)
