a = [[3,6],[5,7,8],[9,5,7]]
index = 0
sum=0
while index<len(a):
    j=0
    while j <len(a[index]):
        sum = sum + a[index][j]
        j+=1
    index = index +1
print(sum)

    

# index = 0
# while index <len(a[index]):
#     j = 0
#     num = 0
#     while j<len(a[index]):
#         num = num + a[index][j]
#         b = num//len(a[index])
#         j = j + 1
#     index = index + 1
# print(b)
