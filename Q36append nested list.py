a=[[10,20],[30,40],[50,60],[30,20,80]]
b=[[61],[12,14,15],[12,13,19,20],[12]]
c=[]
i=0
while i < len(a):
     c.append(a[i]+b[i])
     i=i+1
print(c)




a=[[10,20],[30,40],[50,60],[30,20,80],[11,22]]
b=[[61],[12,14,15],[12,13,19,20],[12]]
c=[]
i=0
if len(a)<len(b):
    j=0
    while j<len(a):
        c.append(b[j]+a[j])
        j+=1
    c=c+b[len(a):len(b)]
if len(b)<len(a):
    j=0
    while j<len(b):
        c.append(b[j]+a[j])
        j+=1
    c=c+a[len(b):len(a)]
print(c)