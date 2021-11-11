list_1 = ["fatima",23,4.6,"hello",58.8,"oye"]
i=0
s=0
while i<len(list_1):
    if list_1[i]==str(list_1[i]):
        print("index",i,list_1[i],"legth os tring=",len(list_1[i]))
    i+=1


    # if type(list_1[i])==str:
    #     print(list_1[i])
    # i+=1