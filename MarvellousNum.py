def Accept(Arr, size1):

    for value in range(size1):
        no = int(input())
        Arr.append(no)

    return Arr

def Addition(Arr):

    Sum = 0
    
    for value in range(len(Arr)):
       Sum = Sum + Arr[value] 

    return Sum

def Maximum(Arr):
    
    Max = 0

    for value in range(len(Arr)):
        if( Max < Arr[value]):
            Max = Arr[value]
    
    return Max

def Minimum(Arr):
    
    Min = Arr[0]

    for value in range(len(Arr)):
        if( Min > Arr[value]):
            Min = Arr[value]
    
    return Min

def Frequency(Arr,No):

    Cnt = 0

    for value in range(len(Arr)):
        if(Arr[value] == No):
            Cnt = Cnt + 1

    return Cnt

def ChkPrime(No):
    
    flag = True

    for cnt in range(2,int(No/2+1)):
        if(No % cnt == 0):
            flag = False
            break
    
    return flag
