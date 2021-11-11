
# This is the list of marks of a student for the last three years. You have to calculate the average
# marks for each year. Like, for the above list, the output should be as follows:- Average of 1 
# year - 84 Average of 2 year - 80 Average of 3 year - 63


# Check your program for following nested lists as well ( the code should run without changing the code, 
# if it does not runs properly thatt means you have not written the code properly :

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

