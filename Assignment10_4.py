import os
import sys
import time

def DirectoryCopyExt(SrcDir,DstDir,Ext):

    flag  = os.path.isabs(SrcDir) 
    flag_1 = os.path.exists(DstDir)

    
    if(flag == False):
        SrcDir = os.path.abspath(SrcDir)
       
    exist = os.path.isdir(SrcDir)

    if(flag_1  == False):
        os.mkdir(DstDir)
    
    if(exist == True):
        for dirname,subdirs,filenames in os.walk(SrcDir):
            for name in filenames:
                if(name.lower().endswith(Ext)):
                    DstPath = os.path.abspath(DstDir)

                    fobj = open(name,'r')
                    nobj = open(os.path.join(DstPath,name),'w')

                    nobj.write(fobj.read())

    else : 
        print("There is no such directory")

def main():
    Dir = sys.argv[1]
    Str = sys.argv[2]

    print("---------------- Directory Files Copy -------------------")

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is used to copy Files of named Extention form one directory to another")
            exit()

        if(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage of the script : ")
            print("Src_Directory  Dst_Directory  File_Extention")
            exit()

    if(len(sys.argv) == 4):
        try:
            starttime = time.time()
            DirectoryCopyExt(sys.argv[1],sys.argv[2],sys.argv[3])
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