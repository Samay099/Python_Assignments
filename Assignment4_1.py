
Square = lambda A : A*A

def main():

    print("Enter a number : ",end = "")
    No = int(input())

    Ret = Square(No)

    print("Square of",No,"is :",Ret)

    

if __name__ == "__main__" :
    main()