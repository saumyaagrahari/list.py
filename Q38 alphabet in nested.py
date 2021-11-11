a=['Red,Maron,Yellow,Olive']
b=[]
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        b.append(a[i][j])
        j+=1
    i+=1
print(b)