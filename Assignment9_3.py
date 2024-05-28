import os
import sys

def main():
    Fname = sys.argv[1]

    if(os.path.exists("Demo.txt")):
        print("Demo.txt already exists")
        return
    else:
        fobj1= open("Demo.txt",'x')
        fobj2 = open(Fname,'r')

        fobj1.write(fobj2.read())

if __name__ == "__main__":
    main()