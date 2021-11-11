
# question = "How many continents are there?"
# User_input = int(input("enter your answer"))
# if User_input == 7:
#     print("Congrats! Aapka answer sahi hai")
# else:
#     print("Sadly aapka javab ga1lat hai.")

question = input("please enter the question:")
solution = int(input("enter the solution:"))
i = 0
while i<len(question):
    if question== "How many countries in world":
        print("correct")
        if solution == 195:
            print("Congrats! Aapka answer sahi hai")
        else:
            print("Sadly aapka javab ga1lat hai.")
    else:
        print("wrong")
    break