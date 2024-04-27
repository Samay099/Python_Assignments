def Accept(Arr1, size1):

    for value in range(size1):
        no = int(input())
        Arr1.append(no)

    return Arr1

def Addition(Arr1):

    Sum = 0
    
    for value in range(len(Arr1)):
       Sum = Sum + Arr1[value] 

    return Sum

def Maximum(Arr2):
    
    Max = 0

    for value in range(len(Arr2)):
        if( Max < Arr2[value]):
            Max = Arr2[value]
    
    return Max

def Minimum(Arr2):
    
    Min = Arr2[0]

    for value in range(len(Arr2)):
        if( Min > Arr2[value]):
            Min = Arr2[value]
    
    return Min

def main():

    Arr = list()
    print("Enter the size of list")
    size = int(input())

    print("Enter the elements of List :")
    Arr = Accept(Arr,size)
    
    Ret = Minimum(Arr)
    print("Minimum elemnt is : ",Ret)    

if __name__ == "__main__" :
    main()