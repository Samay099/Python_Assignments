import os
import sys
import time

def DirectoryFileSearch(Dname, ext):

    Flag  = os.path.isabs(Dname)    
    
    if(Flag == False):
        Dname = os.path.abspath(Dname)
    
    exist = os.path.isdir(Dname)

    if(exist == True):
        
        for dirname,subdirs,filenames in os.walk(Dname):
            for name in filenames:
                if(name.lower().endswith(ext)):
                    print(name)

    else : 
        print("There is no such directory")

def main():
    Dir = sys.argv[1]
    Str = sys.argv[2]

    print("---------------- Directory File Search -------------------")

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is used to search Files of the named Extention in a named directory")
            exit()

        if(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage of the script : ")
            print("Name_Of_Directory  Extention_Of_File")
            exit()

    if(len(sys.argv) == 3):
        try:
            starttime = time.time()
            DirectoryFileSearch(sys.argv[1],sys.argv[2])
            endtime = time.time()

            print("Time required to execute the script is : ",endtime-starttime)

        except Exception as obj2:
            print("Unable to perform the task due to ", obj2)
            
    else:
        print("Invalid option")
        print("Use --h option to get the help and use --u option to get the usage of application")
        exit()

    
            
if __name__ == "__main__":
    main()