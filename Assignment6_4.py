import threading

def Capital(Str1):

    Cnt = 0

    for no in range(len(Str1)):
        if ((Str1[no] >= 'A') and (Str1[no] <= 'Z')):
            Cnt = Cnt + 1

    print("Number of Capital Characters :",Cnt)
    print("Thread id of Capital thread : ",threading.get_ident())


def Small(Str1):

    Cnt = 0

    for no in range(len(Str1)):
        if ((Str1[no] >= 'a') and (Str1[no] <= 'z')):
            Cnt = Cnt + 1

    print("Number of Small Characters :",Cnt)
    print("Thread id of Small thread : ",threading.get_ident())

def Digits(Str1):

    Cnt = 0

    for no in range(len(Str1)):
        if ((Str1[no] >= '0') and (Str1[no] <= '9')):
            Cnt = Cnt + 1

    print("Number of Digit Characters :",Cnt)   
    print("Thread id of Digits thread : ",threading.get_ident()) 


def main():

    print("Enter a String  : ",end="")
    Str = input()
    
    t1 = threading.Thread(target= Capital,args=(Str,))
    t2 = threading.Thread(target= Small,args=(Str,))
    t3 = threading.Thread(target= Digits,args=(Str,))

    print("Thread :",t1.name)
    t1.start()
    print("Thread :",t2.name)
    t2.start()
    print("Thread :",t3.name)
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__" :
    main()