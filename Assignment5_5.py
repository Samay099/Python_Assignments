
Fact = 1

def Factorial(No):
    
    global Fact

    if(No != 0):
        Fact = Fact * No
        Factorial(No-1)

    return Fact

def main():

    print("Enter a number : ",end ="")
    Value =int(input())
    Ret = 0 

    if(Value == 0):
        Ret = 0
    else :
        Ret = Factorial(Value)
        
    print("Factorial of",Value," is :",Ret)

if __name__ == "__main__" :
    main()