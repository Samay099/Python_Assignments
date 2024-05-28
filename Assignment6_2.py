import threading


def EvenFactor(No):
    
    Sum = 0
    for no in range(1,int((No/2)+1)):
        if(no % 2 == 0):
            if((No % no) == 0):
                Sum = Sum + no

    print("Sum of Even Factors is :",Sum)

def OddFactor(No):

    Sum = 0
    for no in range(1,int((No/2)+1)):
        if(no % 2 != 0):
            if((No % no) == 0):
                Sum = Sum + no

    print("Sum of Odd Factors is :",Sum)

def main():

    print("Enter a number : ",end="")
    Value = int(input())

    t1 = threading.Thread(target= EvenFactor,args=(Value,))
    t2 = threading.Thread(target= OddFactor,args=(Value,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("End of main")

if __name__ == "__main__" :
    main()