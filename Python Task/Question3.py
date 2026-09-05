a=int(input("Enter a number you want to check for hill Number: "))
b=str(a)
up=False
down=False
if len(b)<3:
    print("Number Should be atleast 3 digit")
else:
    for i in range (len(b)-1):
        if int(b[i]) < int(b[1+i]):
            if down:
                print("Not Hill number")
                break
            up=True
            
        elif int(b[i]) > int(b[1+i]):
            if not up:
                print("Not Hill number")
                break
            down=True 
        else :
            print("Not Hill number")
            break
    
    if up and down:
        print("Hill Number")
    else:
        print("Not hill")


