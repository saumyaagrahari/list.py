# These are the marks of any student for the last three years. 
# You have to calculate total marks for all the three years.



marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65, 76],
    [95, 45, 78, 52, 49]
]
index = 0
sum = 0
while index<len(marks):
    j = 0 
    while j<len(marks[index]):
        sum=sum+marks[index][j]
        j=j+1
    index=index+1
print(sum)



# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65],
#     [95, 45, 78]
# ]
# index = 0
# sum = 0
# while index<len(marks):
#     j = 0 
#     while j<len(marks[index]):
#         sum=sum+marks[index][j]
#         j=j+1
#     index=index+1
# print(sum)


marks = [
    [78, 76, 94, 86, 88],
    [91, 71, 98, 65],
    [95, 45, 78],
    [87, 67, 49, 68, 88]
]
index = 0
sum = 0
while index<len(marks):
    j = 0 
    while j<len(marks[index]):
        sum=sum+marks[index][j]
        j=j+1
    index=index+1
print(sum)



