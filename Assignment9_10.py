import os
import sys

def main():
    Fname = sys.argv[1]
    Str = sys.argv[2]

    if(os.path.exists(Fname)):

        fobj = open(Fname,'r')
        Cnt = 0

        for line in fobj:
            
            lst = line.split()
            
            for Str2 in lst: 
                
                if(Str2 == Str):
                    Cnt = Cnt+1
                    
        print("Frequency of",Str,"in",Fname,"is :",Cnt)

    elif(os.path.exists(Fname) == False):
        print(Fname,"Does not exist")
    
        

if __name__ == "__main__":
    main()