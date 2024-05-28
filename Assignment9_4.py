import os
import sys

def main():
    Fname1 = sys.argv[1]
    Fname2 = sys.argv[2]

    if(os.path.exists(Fname1) and os.path.exists(Fname2)):

        fobj1 = open(Fname1,'r')
        fobj2 = open(Fname2,'r')

        if(fobj1.read() == fobj2.read()):
            print("Success")
        else:
            print("Failure")

    elif(os.path.exists(Fname1) == False):
        print(Fname1,"Does not exist")

    elif(os.path.exists(Fname2) == False):
        print(Fname2,"Does not exist")
    
        

if __name__ == "__main__":
    main()