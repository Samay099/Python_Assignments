import MarvellousNum

def Display(Arr):

    for value in range(len(Arr)):
        print(Arr[value], end="\t")

def ListPrime(Arr):

    primeArr = list()

    for value in range(len(Arr)):
        if(MarvellousNum.ChkPrime(Arr[value]) == True):
            primeArr.append(Arr[value])
    
    return primeArr

def main():

    Arr = list()
    print("Enter the size of list")
    size = int(input())

    print("Enter the elements of List :")
    Arr = MarvellousNum.Accept(Arr,size)

    RetArr = list()

    RetArr = ListPrime(Arr)

    print("All prime numbers are : ",end="")
    Display(RetArr)
    print(end="\n")

    Ret = MarvellousNum.Addition(RetArr)
    print("Additon of All Prime Numbers : ",Ret)


if __name__ == "__main__" :
    main()