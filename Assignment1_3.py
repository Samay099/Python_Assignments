def Add(No1,No2):
    
    Ans = 0

    Ans = No1 + No2
    
    return Ans


def main():
    
    Value1 = 0
    Value2 = 0
    Ret = 0

    print("Enter First number :", end= " ")
    Value1 = int(input())

    print("Enter Second number :", end= " ")
    Value2 = int(input())

    Ret = Add(Value1,Value2)

    print("Addition is : ",Ret)


if __name__ == "__main__":
    main()