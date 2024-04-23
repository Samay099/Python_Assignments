def Display():

    Cnt = 0
    i = 1

    print("First 10 even numbers are : ")

    while(Cnt < 10):
        if(i % 2 == 0):
            print(i,end="\t")
            Cnt = Cnt+1
        i = i+1
    print(end="\n")


def main():

    Display()


if __name__ == "__main__":
    main()