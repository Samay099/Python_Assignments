
class Arithmetic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0
        
    
    def Accept(self):
        print("Enter first number :")
        self.Value1 = int(input())

        print("Enter second number :")
        self.Value2 = int(input())
    
        return 0

    def Addition(self):
        Sum = self.Value1 + self.Value2
        return Sum

    def Subtraction(self):
        Sub = self.Value1 - self.Value2
        return Sub

    def Multiplication(self):
        Mult = self.Value1 * self.Value2
        return Mult
    def Division(self):
        
        if(self.Value2 == 0):
            return -1

        Div = self.Value1 / self.Value2
        return Div


def main():

    Obj1 = Arithmetic()
    Obj2 = Arithmetic()
    Obj3 = Arithmetic()

    Obj1.Accept()
    print("Additon of",Obj1.Value1,"and",Obj1.Value2 ,"is",Obj1.Addition())

    print("Subtraction of",Obj1.Value1,"and",Obj1.Value2 ,"is",Obj1.Subtraction())

    print("Multiplication of",Obj1.Value1,"and",Obj1.Value2 ,"is",Obj1.Multiplication())

    Ret = Obj1.Division()
    if(Ret  == -1):
        print("Division by 0 is not possible")
        return
    else :
        print("Division of",Obj1.Value1,"and",Obj1.Value2 ,"is",Obj1.Division())

        
    Obj2.Accept()
    print("Additon of",Obj2.Value1,"and",Obj2.Value2 ,"is",Obj2.Addition())

    print("Subtraction of",Obj2.Value1,"and",Obj2.Value2 ,"is",Obj2.Subtraction())

    print("Multiplication of",Obj2.Value1,"and",Obj2.Value2 ,"is",Obj2.Multiplication())

    Ret = Obj2.Division()
    if(Ret  == -1):
        print("Division by 0 is not possible")
        return
    else :
        print("Division of",Obj2.Value1,"and",Obj2.Value2 ,"is",Obj2.Division())


    Obj3.Accept()
    print("Additon of",Obj3.Value1,"and",Obj3.Value2 ,"is",Obj3.Addition())

    print("Subtraction of",Obj3.Value1,"and",Obj3.Value2 ,"is",Obj3.Subtraction())

    print("Multiplication of",Obj3.Value1,"and",Obj3.Value2 ,"is",Obj3.Multiplication())

    Ret = Obj3.Division()
    if(Ret  == -1):
        print("Division by 0 is not possible")
        return
    else :
        print("Division of",Obj3.Value1,"and",Obj3.Value2 ,"is",Obj3.Division())



if __name__ == "__main__":
    main()