

cnt = 0

def Display(No):
    global cnt 

    if(cnt < No):
        cnt = cnt+1
        print("*",end="\t")
        Display(No)


def main():

    print("Enter frequency : ",end ="")
    Value =int(input())

    Display(Value)
    print(end="\n")



if __name__ == "__main__" :
    main()