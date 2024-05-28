import threading

def EvenDisplay():
    
    print("First 10 even numbers are :")
    for no in range(1,11):
        print(no*2)
    

def OddDisplay():
    
    print("First 10 odd numbers are :")
    for no in range(1,11):
        print((no*2)+1)


def main():

    t1 = threading.Thread(target= EvenDisplay,args=())
    t2 = threading.Thread(target= OddDisplay,args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__" :
    main()