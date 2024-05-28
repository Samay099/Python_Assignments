
class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0
    
    def Accept(self):
        print("Enter Radius of Circle :")

        self.Radius = float(input())

        if (self.Radius < 0):
            print("Enter a positive Radius")
            return -1

        return 0

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print("Radius of Circle :",self.Radius)
        print("Area of Circle :",self.Area)
        print("Circumference of Circle :",self.Circumference)



def main():

    Obj1 = Circle()
    Obj2 = Circle()
    Obj3 = Circle()

    Ret = Obj1.Accept()
    if(Ret  == -1):
        return
    Obj1.CalculateArea()
    Obj1.CalculateCircumference()
    Obj1.Display()
        
    Ret = Obj2.Accept()
    if(Ret  == -1):
        return
    Obj2.CalculateArea()
    Obj2.CalculateCircumference()
    Obj2.Display()

    Ret = Obj3.Accept()
    if(Ret  == -1):
        return
    Obj3.CalculateArea()
    Obj3.CalculateCircumference()
    Obj3.Display()


if __name__ == "__main__":
    main()