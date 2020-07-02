x = int(input("Enter a integer between 0 and 1024: "))
a=0
b=1024
test = True
if x == 0:
    print("Your Nunber is 0, Thanks for playing.")
    test = False
else:
    if x == 1024:
        print("Your Number is 1024, Thanks for playing.")
        test = False

        while test == True:
            m= int((a+b)/2)
            if m == x:
                print("Your Number is", m, "Thanks for playing.")
                break
            else:
                if m < x:
                    a=m
                else:
                    b=m
