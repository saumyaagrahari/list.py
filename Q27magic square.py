# row = int(input("enter the number:"))
# col = int(input("enter the number:"))
# print("enter elements for matrix1:")
# matrix1 =[[int(input()) for i in range (col)] for j in range (row)]
# print("matrix1:")
# for i in range (row):
#     for j in range(col):
#         print((matrix1[i][j],"<3"),end="")
#     print()
# print("enter elements for matrix2:")
# matrix2 =[[int(input()) for i in range (col)] for j in range (row)]
# print("matrix2:")
# for i in range (row):
#     for j in range(col):
#         print((matrix2[i][j],"<3"),end="")
#     print()




magic_square = [[8,3,4],[1,5,9],[6,7,2]]
a = []
for i in range (3):
    b= []
    for j in range (3):
        j = int(input("enter the number:"))
        b.append(j)
    a.append(b)
print("numbers is .....")
for i in range (3):
    for j in range(3):
        print(a[i][j],end="")
    print()
sumd1 = 0
sumd2 = 0
for i in range (3):
    for i in range (3):
        if i == j:
            sumd1 = sumd1 + a[i][j]
            if i + j == 3-1:
                sumd2 = sumd2 + a[i][j]
if sumd1 != sumd2:
    f=1
else:
    for i in range(3):
        sumr=0
        sumc=0
        for j in range (3):
            sumr=sumr+a[i][j]
            sumc=sumc+a[i][j]
        if sumr!= sumd1:
            f=1
        elif sumc!=sumd1:
            f=1
        else:
            f=0
if f==0:
    print("numbers is magic square")
else:
    print("numbers is not magic square")


