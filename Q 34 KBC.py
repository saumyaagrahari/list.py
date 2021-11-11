print("<<<<<<<< Welcome To KBC Game >>>>>>>>>")
question_list = [
    "How many continents are there?",                # first question
    "What is the capital of india?",                 # second question
    "NG mai kaun sa course padhaya jaata hai?"       # third question
]



options_list = [

    # first question ke liye options
    ["Four","Nine","Seven","Eight"],
    # second question ke liye options
    ["Chandigarh","Bhopal","Chennai","Delhi"],
    # third question ke liye options
    ["Software Enginearing","Counseling","Tourism","Agriculture"]
]
# har ek question ke liye, uski solution key (yeh index nahi hai)

# solution_list = [3,4,1]
# 50_50 = [["(1).Four","(2).Seven"],
#         ["(1).Bhopal","(2).Delhi"]
#         ["(1).Tourism","(2).Software Enginearing"]
# ]

solution_list = [3,4,1]
anslist= [["1 Four","3 Seven"],["2  Bhopal","4 Delhi"],["1 Software Enginearing","2Counseling"]]
i = 0
count = 0
price=0
while i<len(question_list):
    print(question_list[i])
    j = i
    serialno=0
    while serialno<len(options_list[i]):
        k=options_list[j][serialno]
        print(serialno+1,k)
        serialno+=1
    life_line=input("do you want to use life line 50-50 yes/no:")
    if life_line=="yes":
        print("you use 50-50 life line")
        if count<1:
            serial=0
            a=i
            while serial<len(anslist[i]):
                s=anslist[a][serial]
                serial+=1
                print(s)
            n=int(input("enter your ans:"))
            if n==solution_list[i]:
                price+=10000
                print("right ans and your wining price is:",price)
            else:
                print("wrong ans")
                break
            count+=1
        else:
            print("you have already used life line:")
            n1 = int(input("enter the number:"))
            if n1==solution_list[i]:
                price+=10000
                print("your ans is correct and your wining price is:",price)
            else:
                print("your ans is wrong game is over")
                break
    else:
        n2=int(input("enter your ans:"))
        if n2==solution_list[i]:
            price+=10000
            print("right ans and your wining price is:",price)
        else:
            print("wrong ans")
            break
    i+=1