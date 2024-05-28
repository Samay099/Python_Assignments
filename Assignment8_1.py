
class BookStore:
    NoOfBooks = 0

    def __init__(self,Name,Writer):
        self.Book = Name
        self.Author = Writer
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1
    
    def Display(self):
        print(self.Book,"by",self.Author,".Number of Books",BookStore.NoOfBooks)


def main():

    Obj1 = BookStore("Linux System Programming","Robert Love")
    Obj1.Display()
    Obj2 = BookStore("C Programming","Dennis Ritchie")
    Obj2.Display()

if __name__ == "__main__":
    main()