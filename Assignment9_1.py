import os

def main():

    print("Enter file name: ",end="")
    Fname = input()

    if(os.path.exists(Fname)):
        print("File already exists")
    else :
        print("File does not exists")


if __name__ == "__main__":
    main()