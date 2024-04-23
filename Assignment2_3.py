def Factorial(No):

    Fact = 1

    for no in range(No,0,-1):
        Fact = Fact * no
    
    return Fact


def main():
    
    Value = 0

    Ret = 0
    print("Enter a number :", end= " ")
    Value = int(input())

    Ret = Factorial(Value)

    print("Factorial is :",Ret)

if __name__ == "__main__":
    main()