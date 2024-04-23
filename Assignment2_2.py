def Display(No = 5):

    for i in range(0,No):
        for j in range(0,No):
            print("*",end = "\t")
        print(end = "\n")
    

def main():

    Value = 0

    print("Enter the frequency :",end = " ")
    Value = int(input())
    Display(Value)


if __name__ == "__main__":
    main()