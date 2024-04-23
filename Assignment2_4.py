def AddFactors(No):

    Sum = 0

    for cnt in range(1,int(No/2+1)):
        if(No % cnt == 0):
            Sum = Sum + cnt
    
    return Sum


def main():
    
    Value = 0

    Ret = 0
    print("Enter a number :", end= " ")
    Value = int(input())

    Ret = AddFactors(Value)

    print("Sum of Factors is :",Ret)

if __name__ == "__main__":
    main()