import Arithmatic

def main():

    Value1 = 0
    Value2 = 0
    Ret = 0

    print("Enter First number :", end= " ")
    Value1 = int(input())

    print("Enter Second number :", end= " ")
    Value2 = int(input())

    Ret = Arithmatic.Addition(Value1,Value2)
    print("Additon is : ", Ret)

    Ret = Arithmatic.Substraction(Value1,Value2)
    print("Substraction is : ", Ret)

    Ret = Arithmatic.Multiplication(Value1,Value2)
    print("Multiplication is : ", Ret)

    Ret = Arithmatic.Division(Value1,Value2)
    print("Division is : ", Ret)


if __name__ == "__main__":
    main()