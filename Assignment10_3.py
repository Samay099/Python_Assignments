import os
import sys
import time

def DirectoryCopy(SrcDir,DstDir):

    flag  = os.path.isabs(SrcDir) 
    flag_1 = os.path.exists(DstDir)

    if(flag_1  == True):
        print("Destination Directory already exists")
        return

    
    if(flag == False):
        SrcDir = os.path.abspath(SrcDir)
       
    exist = os.path.isdir(SrcDir)

    os.mkdir(DstDir)

    if(exist == True):
        
        for dirname,subdirs,filenames in os.walk(SrcDir):
            for name in filenames:
                DstPath = os.path.abspath(DstDir)

                fobj = open(name,'r')
                nobj = open(os.path.join(DstPath,name),'w')

                nobj.write(fobj.read())

    else : 
        print("There is no such directory")

def main():
    Dir = sys.argv[1]
    Str = sys.argv[2]

    print("---------------- Directory Copy -------------------")

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is used to copy Files form one directory to another")
            exit()

        if(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage of the script : ")
            print("Src_Directory  Dst_Directory")
            exit()

    if(len(sys.argv) == 3):
        try:
            starttime = time.time()
            DirectoryCopy(sys.argv[1],sys.argv[2])
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