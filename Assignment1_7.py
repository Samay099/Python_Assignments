def ChkDivisible(No):
    
    flag = False

    if(No % 5 == 0):
        flag = True
    
    return flag


def main():
    
    Value = 0

    Ret = False
    print("Enter a number :", end= " ")
    Value = int(input())

    Ret = ChkDivisible(Value)

    if(Ret == True):
        print("Divisible by 5")
    else:
        print("Not Divisible by 5")


if __name__ == "__main__":
    main()