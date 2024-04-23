def Display(No = 5):

    for i in range(1,No+1):
        for j in range(No,0,-1):
            if(i <= j):
                print("*",end="\t")
        print(end = "\n")
    

def main():

    Value = 0

    print("Enter the frequency :",end = " ")
    Value = int(input())
    Display(Value)


if __name__ == "__main__":
    main()