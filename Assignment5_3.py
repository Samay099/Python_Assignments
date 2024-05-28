

def Display(No):

    if(0 < No):
        print(No,end="\t")
        No = No-1
        Display(No)


def main():

    print("Enter frequency : ",end ="")
    Value =int(input())

    Display(Value)
    print(end="\n")



if __name__ == "__main__" :
    main()