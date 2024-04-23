def Display(No = 5):

    for no in range(0,No):
        print("Marvellous")
    

def main():

    Value = 0

    print("Enter the frequency :",end = " ")
    Value = int(input())
    Display(Value)


if __name__ == "__main__":
    main()