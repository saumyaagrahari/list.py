print("creat your new facebook account")
first_name=(input("enter the first name:"))
if first_name>= "A" and first_name<="Z" or first_name>="a" and first_name<="z":
    print("it is a first name")
    last_name=(input("enter the last name:"))
    if last_name>="A" and last_name<="Z" or last_name>="a" and last_name<="z":
        print("it is a last name")
        date=int(input("enter the date:"))
        if date>=1 or date<=31:
            month=int(input("enter the month:"))
            if month>=1 or month<=12:
                year=int(input("enter the year:"))
                if year>=1800 and year<=2021:
                    print(date,month,year)
                    gender=(input("enter the gender:"))
                    if gender=="female":
                        print("female")
                        gamil = (input("create a gmail address:"))
                        if gamil=="saumyaagrahari011@.com":
                            print("gmail")
                            mobile_no=int(input("enter the mobile number:"))
                            if mobile_no>=0 or mobile_no<=9:
                                print("mobile number")
                                otp=int(input("enter the otp:"))
                                if otp>=0 or otp<=9:
                                    print("suggest strong password")
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
                                else:
                                    print("wrong otp")
                            else:
                                ("incorrect number")
                        else:
                            print("incorrect gmail")
                    else:
                        print("incorrect gender")
                else:
                    print("incorrect year")
            else:
                print("incorrect month")
        else:
            print("incorrect date")
    else:
        print("incorrect last name")
else:
    print("incorrect first name")
