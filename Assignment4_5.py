
import functools

def Accept(Arr1, size):

    Value = 0
    for no in range(size):
        Value = int(input())
        Arr1.append(Value)
    
    return Arr1

def ChkPrime(No):

    Flag = True

    for cnt in range(2,int(No/2)):
        if(No % cnt == 0):
            Flag = False
            break
    
    return Flag

def Maximum(No1, No2):

    Max = No1
    
    if(Max < No2):
        Max = No2

    return Max

def main():

    Arr = list()
    print("Enter the size of list :")
    size = int(input())

    print("Enter the elements of list : ")
    Arr = Accept(Arr,size)

    FData = list(filter(ChkPrime,Arr))
    print("Data after filter()",FData)

    MData = list(map(lambda no : no *2 ,FData))
    print("Data after map() : ",MData)

    RData = functools.reduce(Maximum, MData)

    print("Output of reduce :",RData)


if __name__ == "__main__" :
    main()