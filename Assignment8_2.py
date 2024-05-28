
class BankAccount:
    ROI = 10.5

    def __init__(self,Str,Value):
        self.Name = Str
        self.Amount = Value
    
    def Deposit(self):
        print("Enter the amount you want to Deposit")
        Value1 = float(input())
        if(Value1 < 0):
            return -1
        
        self.Amount = self.Amount + Value1
    def Withdraw(self):
        print("Enter the amount you want to withdraw")
        Value1 = float(input())
        if(Value1 < 0):
            return -1
        
        if(Value1 > self.Amount):
            return -2

        self.Amount = self.Amount - Value1

    def CalculateIntrest(self):

        FinalA = self.Amount * (1+((BankAccount.ROI / 100) * 1))
        print(FinalA)
        
        Interest = FinalA - self.Amount

        return Interest

        
    def Display(self):
        print("Name :",self.Name)
        print("Amount :",self.Amount)
    

def main():

    Obj1 = BankAccount("Marvellous",11000)
    Obj1.Display()
    Obj1.Deposit()
    Ret = Obj1.Withdraw()
    if(Ret == -1):
        print("Enter a positive value")
        return
    elif(Ret == -2):
        print("Not Enough Balance")

    Ret = Obj1.CalculateIntrest()
    print("Intrest for a period of one Year is :",Ret)
    Obj1.Display()

    print("-----------------------------------------------------------")

    Obj2 = BankAccount("Infosystems",21000)
    Obj2.Display()
    Obj2.Deposit()
    Ret = Obj2.Withdraw()
    if(Ret == -1):
        print("Enter a positive value")
        return
    elif(Ret == -2):
        print("Not Enough Balance")

    Ret = Obj2.CalculateIntrest()
    print("Intrest for a period of one Year is :",Ret)
    Obj2.Display()


if __name__ == "__main__":
    main()