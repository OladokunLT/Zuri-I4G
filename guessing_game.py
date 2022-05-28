user_no = input("Enter number: ")

try: 
    user_no = float(user_no)
    print("Hooray, you entered a number: ")

    if user_no == 10:
        print("true, you guess right")
    elif user_no > 10:
        print("number is bigger, try again")
    else :
        print("number is lesser than value, try again")
        

except:
    print("this is not a number, pls enter valid number")
