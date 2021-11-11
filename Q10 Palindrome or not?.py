# A palindrome is a word, sentence, verse, or even a number that reads the same backward or forward. 
# Like NITIN. Read Nitin either from left or right, it will be same. Similarly MOM is also a palindrome.

#Write a code that checks whether a list is a palindrome or not. And print “Haan! palindrome hai”
#  if its a pallindrome and “nahi! palindrome nahi hai” if its not a palindromCoursesLogin/Signupe.


# name=[ 'n', 'i', 't', 'i', 'n' ]
# i=0
# a=[]
# sum=0
# sum1=0
# while sum1<len(name):
#     length=a-len[i]
#     if a==name:
#         print("polindrome",name)
#     else:
#         print("not polindrome",name)
#     sum=sum+1
#     sum1=sum1+1
#     # print(a)



name = input(("enter the a text:"))
a = name[::-1]
if a == name:
    print("palindrome",name)
else:
    print("not palindrome",name)


# number = input(("enter the a number"))
# a = number[::-1]
# if a == number:
#     print("palindrome number")
# else:
#     print("not palindrome number")


