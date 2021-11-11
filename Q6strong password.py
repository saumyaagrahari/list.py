upper_case=(input("enter the upper case:"))
if upper_case>="A" and upper_case<="Z":
    print("it is a upper case")
    lower_case=(input("enter the lower case:"))
    if lower_case>="a" and lower_case<="z":
        print("it is a lower case")
        special_char=(input("enter the special character:"))
        if special_char=="@" or special_char=="$" or special_char=="#":
            print("it is a special character")
            numeric=(input("enter the numeric:"))
            if numeric>="0" and numeric<="9":
                print("it is a number")
                a=(upper_case+lower_case+str(numeric)+special_char)
                if len(a)==8:
                    print("it is strong password")
                else:
                    print("it is not strong password")
            else:
                print("it is not a number")
        else:
            print("it is not strong password")
    else:
        print("it is not lower case")
else:
    print("it is not upper case")
                                