# ---------------------- MathCase (switchCase) -------------------------------------------

a=int(input("Enter a number : "))

match a:
    case 1:
        print ("case is 1")
    case 2 :
        print ("case is 2")
    case 20:
        print ("case is 20")
    case 50 :
        print ("case is 50")
    
    # Default Case
    case(_):   
        print("Default case ")