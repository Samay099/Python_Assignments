
class Numbers:

    def __init__(self,No):
        self.Value = No
    
    def ChkPrime(self):

        Flag = True

        for cnt in range(2,int(self.Value/2)):
            if(self.Value % cnt == 0):
                Flag = False
                break
        
        return Flag
    
    def SumFactors(self):

        Sum = 0

        for cnt in range(1,int(self.Value/2+1)):
            if(self.Value % cnt == 0):
                Sum = Sum + cnt
        
        return Sum

    def Factors(self):

        print("Factors of",self.Value,"are :",end=" ")
        for cnt in range(1,int(self.Value/2+1)):
            if(self.Value % cnt == 0):
                print(cnt,end="\t")

        print(end = "\n")

    def ChkPerfect(self):

        Sum = 0

        for cnt in range(1,int(self.Value/2+1)):
            if(self.Value % cnt == 0):
                Sum = Sum + cnt
        
        if(Sum == self.Value):
            return True
        else:
            return False

def main():

    print("Enter a number : ",end="")
    No = int(input())

    obj1 = Numbers(No)
    obj1.Factors()

    Ret = obj1.SumFactors()
    print("Sum of all factors of",No,"is :",Ret)

    Ret = obj1.ChkPrime()
    if(Ret == True):
        print(No,"is Prime")
    else:
        print(No,"is not Prime")

    Ret = obj1.ChkPerfect()
    if(Ret == True):
        print(No,"is Perfect")
    else:
        print(No,"is not Perfect")


if __name__ == "__main__":
    main()