import threading

def Count50():
    
    for no in range(1,51):
        print(no,end="\t")

    print(end="\n")

def CountRev50():
    
    for no in range(50,0,-1):
        print(no,end="\t")

    print(end="\n")

def main():
    
    t1 = threading.Thread(target= Count50,args=(),name= "Thread1")
    t2 = threading.Thread(target= CountRev50,args=(),name= "Thread2")

    print(t1.name)
    t1.start()
    t1.join()
    print(t2.name)
    t2.start()
    t2.join    
  

if __name__ == "__main__" :
    main()