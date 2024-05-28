import threading

def EvenList(Arr):
    
    Sum = 0

    for no in range(len(Arr)):
        if(Arr[no] % 2 == 0):
            Sum = Sum + Arr[no]
    
    print("Sum of all even elements of list is :",Sum)

def OddList(Arr):

    Sum = 0

    for no in range(len(Arr)):
        if(Arr[no] % 2 != 0):
            Sum = Sum + Arr[no]
    
    print("Sum of all odd elements of list is :",Sum)

def Accept(Arr,length):

    for no in range(length):
        Value = int(input())
        Arr.append(Value)

    return Arr

def main():

    print("Enter the size of list : ",end="")
    Size = int(input())

    Arr = list()

    print("Enter the elements of the list :")

    Arr = Accept(Arr,Size)
    
    t1 = threading.Thread(target= EvenList,args=(Arr,))
    t2 = threading.Thread(target= OddList,args=(Arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__" :
    main()