# a=[[3,4,5,6],[7,8,35,23],[5,2,9,6]]
# b=a[0]
# i=0
# while i<len(a):
#     print(str(a))
#     j=0
#     while j<len(a):
#         if (a[j]>b):
#             b=a[j]
#         j=j+1
#     else:
#         (a[i]>b)
#         b=a[i]
#     print(b)
#     i+=1
# print(b)
# print(type(a))




a=[[3,4,5,6],[7,8,35,23],[5,2,9,6]]
max=a[0]
i=0
while i<len(a):
    if (a[i]>max):
        max=a[i]
    i+=1
print(max)