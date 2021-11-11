# Magic Square is that kind of square in which sum of each row, sum of each column and sum of both the diagonals is equal.

# You have to write this program that takes a nested list as input and checks whether it is a magic square or not?

# This is a magic square because,

magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
i=0
row_sum=0
while i<len(magic_square):
    j=0
    while j<len(magic_square):
        row_sum=row_sum+magic_square[j][i]
        j=j+1
    i=i+1
    print(row_sum)
    print()
i=0
colomn_sum=0
while i<len(magic_square):
    j=0
    while j<len(magic_square):
        colomn_sum=colomn_sum+magic_square[j][i]
        j=j+1
    i=i+1
    print(colomn_sum)
    print()
i=0
left_diagonal=0
while i<len(magic_square):
    j=0
    while j<len(magic_square):
        left_diagonal=left_diagonal+magic_square[j][i]
        j=j+1
    i=i+1
    print(left_diagonal)
    print()
i=0
right_diagonal=0
while i<len(magic_square):
    j=0
    while j<len(magic_square):
        right_diagonal=right_diagonal+magic_square[j][i]
        j=j+1
    i=i+1
    print(right_diagonal)
    print()
if row_sum==colomn_sum==left_diagonal==right_diagonal:
    print("it is a magic square",row_sum,colomn_sum,left_diagonal,right_diagonal)
else:
    print("it is not magic square",row_sum,colomn_sum,left_diagonal,right_diagonal)


