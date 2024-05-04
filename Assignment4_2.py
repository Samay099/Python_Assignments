
Multiplication = lambda No1,No2 : No1*No2

def main():

    print("Enter first number : ",end = "")
    Value1 = int(input())
    print("Enter second number : ",end = "")
    Value2 = int(input())

    Ret = Multiplication(Value1,Value2)

    print(Value1,"*",Value2,"is :",Ret)

    

if __name__ == "__main__" :
    main()