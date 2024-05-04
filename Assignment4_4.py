
import functools

def Accept(Arr1, size):

    Value = 0
    for no in range(size):
        Value = int(input())
        Arr1.append(Value)
    
    return Arr1


def main():

    Arr = list()
    print("Enter the size of list :")
    size = int(input())

    print("Enter the elements of list : ")
    Arr = Accept(Arr,size)

    FData = list(filter(lambda no : (no%2 == 0) ,Arr))
    print("Data after filter()",FData)

    MData = list(map(lambda no : no*no ,FData))
    print("Data after map() : ",MData)

    RData = functools.reduce(lambda no1,no2 : no1 + no2,MData)

    print("Output of reduce :",RData)


if __name__ == "__main__" :
    main()