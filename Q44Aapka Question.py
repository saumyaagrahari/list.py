"Aapka Sawaal hai:"
"What is the capital of India?"

"Aapke options hai:"
"1. Chandigarh"
"2. Bhopal"
"3. Chennai"
"4. Delhi"

question = [
    ["what is the capilat of India?"]
]
options = [
    # question ke liye options
    ["Chandigarh",
    "Bhopal",
    "Chennai",
    "Delhi"]
]
solution = [4]
anslist= ["2 Bhopal","4 Delhi"]
i = 0
count = 0
price=0
while i<len(question):
    print(question[i])
    j = i
    serialno=0
    while serialno<len(options[i]):
        k=options[j][serialno]
        print(serialno+1,k)
        serialno+=1
    life_line=input("do you want to use life line 50-50 yes/no:")
    if life_line=="yes":
        print("you use 50-50 life line")
        if count<1:
            serial=0
            a=i
            while serial<len(anslist[1]):
                s=anslist[a][serial]
                serial+=1
                print(s)
            n=int(input("enter your ans:"))
            if n==solution[i]:
                price+=10000
                print("right ans and your wining price is:",price)
            else:
                print("wrong ans")
                break
            count+=1
        else:
            print("you have already used life line:")
    else:
        print("you have already used life line:")
        n1 = int(input("enter the number:"))
        if n1==solution[i]:
            price+=10000
            print("your ans is correct and your wining price is:",price)
        else:
            print("your ans is wrong game is over")
            break