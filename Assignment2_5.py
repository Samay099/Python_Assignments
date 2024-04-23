def ChkPrime(No):
    
    flag = True

    for cnt in range(2,int(No/2+1)):
        if(No % cnt == 0):
            flag = False
            break
    
    return flag


def main():
    
    Value = 0

    Ret = False
    print("Enter a number :", end= " ")
    Value = int(input())

    Ret = ChkPrime(Value)

    if(Ret == True):
        print("It is a Prime Number")
    else:
        print("It is not a Prime Number")


if __name__ == "__main__":
    main()