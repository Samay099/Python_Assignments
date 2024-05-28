

Sum = 0

def SumDigits(No):
    
    Digit = 0
    global Sum

    if(No != 0):
        Digit = int(No%10)
        Sum = Sum + Digit
        SumDigits(int(No/10))

    return Sum

def main():

    print("Enter a number : ",end ="")
    Value =int(input())

    Ret = SumDigits(Value)
    print("Sum of digits is",Ret)



if __name__ == "__main__" :
    main()