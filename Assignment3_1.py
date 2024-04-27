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

def main():

    Arr = list()
    print("Enter the size of list")
    size = int(input())

    print("Enter the elements of List :")
    Arr = Accept(Arr,size)
    
    Ret = Addition(Arr)
    print("Sum of all the elemnts is : ",Ret)    

if __name__ == "__main__" :
    main()