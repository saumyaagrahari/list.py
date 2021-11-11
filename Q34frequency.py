a = []
for i in range(5):
    x = input("Enter the value")
    a.append(x)
x = input("enter the value to count frequency:")
f = a.count(x)
print("frequency of",x,"=",f)