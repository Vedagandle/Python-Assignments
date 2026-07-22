#Wap to implement a class named Bookstore
#class should contain 2 instance variables: Bookname, bookauthor
#class should contain 1 class variable: no of books initilaized to 0
#define constructor init that accepts name and author and initilaize instance variable
#inside constructor increment class variable by 1 whenever a new object is created
#implement instance method:
#display()=<bookname> by <authorname>. noofbooks:<noofbooks>

class bookstore:
    noofbooks=0

    def __init__(self,bookname,authorname):
        self.bookname=bookname
        self.authorname=authorname

        counter=0
        counter=bookstore.noofbooks
        counter=counter+1
        bookstore.noofbooks=counter

    def display(self):
        print(f"{self.bookname} by {self.authorname} number of books{bookstore.noofbooks}")

def main():
    
    book=(input("Enter Book name"))
    author=(input("Enter author name"))

    bobj1=bookstore(book,author)
    bobj1.display()

        
    book=(input("Enter Book name"))
    author=(input("Enter author name"))
    
    bobj2=bookstore(book,author)
    bobj2.display()
 

if __name__=="__main__":
    main()