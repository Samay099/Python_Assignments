def ChkNum(No):
    
    flag = 0

    if(No == 0):
        flag = 0

    elif(No > 0):
        flag = 1

    elif(No < 0):
        flag = -1

    return flag


def main():
    
    Value = 0

    Ret = False
    print("Enter a number :", end= " ")
    Value = int(input())

    Ret = ChkNum(Value)

    if(Ret == 0):
        print("Zero")
    elif(Ret == 1):
        print("Positive Number")
    elif(Ret == -1):
        print("Negative Number")


if __name__ == "__main__":
    main()