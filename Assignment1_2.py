def ChkEven(No):
    
    flag = False

    if(No % 2 == 0):
        flag = True
    
    return flag


def main():
    
    Value = 0

    Ret = False
    print("Enter a number :", end= " ")
    Value = int(input())

    Ret = ChkEven(Value)

    if(Ret == True):
        print("Even Number")
    else:
        print("Odd Number")


if __name__ == "__main__":
    main()