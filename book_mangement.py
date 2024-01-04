import book.py
c = 'y'
While c.lower() == 'y':
    print("Book Shop Management".center (89, '='))
    print('1. Register')
    print('2. Login')
    print('3. Exit')
    choice4 = int(input("Enter the serial number of your choice: "))
    if choice4 == 1:
        Book.clrscreen ()
        Book.add_user()
        elif choice4 == 2:
            Book.clrscreen ()
            if Book.login():
                var Book.clrscreen
                C = 'y'
                While C.lower() == 'y':
                    Book.clrscreen ()
                    print("Book Shop Management".center (89, '='))
                    print("1. Book Stock")
                    print("2. Book Selling")
                    print("3. Exit")
                    choice = int(input("Enter the serial number of your choice: "))
                    if choice == 1:
                        Book.clrscreen ()
                        print("Book Book".center (89, '='))
                        print("1. Add a new Stock")
                        print("2. View all Stock")
                        print("3. Update an existing Stock")
                        print("4. Exit")
                        choice2 = int(input("Enter the choice: "))
                        if choice2 == 1:
                            Book.clrscreen()
                            Book.add stock()
                            elif choice2 == 2:
                                Book.clrscreen ()
                                Book.view stock()
                                elif choice2 == 3:
                                    Book.clrscreen ()
                                    Book.update_stock()
                                    break
                                else:
                                    print("INVALID CHOICE")
                                    elif choice == 2:
                                        Book.clrscreen ()
                                        print('Book Selling'.center (89, '='))
                                        print('1. Sell a book')
                                        print('2. View Sales this month')
                                        print("3. Exit")
                                        choice3 int (input("Enter your choice: "))
                                        if choice3 == 1:
                                            Book.clrscreen ()
                                            Book.sell book() elif choice3 == 2:
                                                Book.clrscreen()
                                                Book.view sales ()
                                                elif choice3 == 3:
                                                    print("Good Bye")
                                                    break
                                                else:
                                                    print("INVALID CHOICE")
                                                    elif choice == 3:
                                                        print("Good Bye")
                                                        break
                                                    else:
                                                        print("INVALID CHOICE")
                                                        C = input("Do you want to continue (y/[n]): ")
                                                        else:
                                                            print("Good Bye")
                                                            else:
                                                                print("Either your username or password is incorrect")
                                                                elif choice4 == 3:
                                                                    print("Good Bye")
                                                                    break
                                                                else:
                                                                    print("INVALID CHOICE")
                                                                    c = input("Do you want to return to main menu (y/[n]): ")
                                                                    else:
                                                                        print("Good Bye")
                                                                        try:

                                                                            
def unique book_no():
    _cur.execute("select max (Book No) from stock")
    data = cur.fetchall()
    if bool (data[0][0]):
        11 [x for x in range((data[0] [0] + 1), (data[0] [0] + 10000))】
            shuffle (L1)
            return L1.pop(0)
        else:
            return False
        def view sales():
            print ('Overall Sales This Month')
            cur.execute(
                "select distinct (s. Book Name), s.qty purchased from stocks, purchased p where s. Book No p.Book No and p.purchased on between
                year= dt.date.today(). year, month= dt.date.today().month,
                date-last_month(dt.date.today().month, dt.date.today().year)))
            data = cur.fetchall()
            L1, L2 = [],口
            for row in data:
                11.append(row[0])
                12.append(row[1])
                plt.bar(L1, L2)
                plt.xlabel('Books')
                plt.ylabel('Sales')
                plt.title('Sales')
                plt.show()
                def login():
                    user = input("Enter the username: ") pwd input("Enter the password: ")
                    _cur.execute("select from users where username = '() and password = '()'".format (user, pwd))
                    return bool( cur.rowcount)
                def update stock():
                    cur.execute("select Book Name, Available_Stock from stock where Book No []".format (bno))
                    bno int (input("Enter the book number: "))
                    data =_cur.fetchall()
                    print("Book Name", data[0][0])
                    try:
                        import pymysql as entr
                        except ImportError:
                            import mysql.connector as entr
                            import datetime a dt
                            import matplotlib.pyplot as plt
                            from os import startfile
                            from random import shuffle
                            from tempfile import mktemp



                            
db cntr.connect (host='localhost', user='root', passwd='prajwall2', database='book shop')
cur = db.cursor()
if str(cntr) = "<module 'pymysql' from 'C:\\\\Program Files (x86)\\\\Python37\\\\lib\\\\site-packages\\\\pymysql\\\\_init__.py'>": _db.autocommit = True



def view stock():
    cur.execute("select Book No, Book Name, Available_Stock from stock")
    data = cur.fetchall()
    print("Book Number Book Name
          for row in data:
          if len (row[1]) >= 11:
          Stock")
          print(row[0], ', row[1], ', row[2])
          else: print(row[0], ', row[1], , row[2])
                      def add stock():
                          print('Add Stock'.center (89, '-'))
                          bno unique book_no()
                          11 bno:
                              print("Book Number: ", bno)
                              else:
                                  bno int(input("Enter book number: "))
                                  bname input("Enter the Book\'s Name: ")
                                  auth input ("Enter the Author of the Book: ")
                                  publ input ("Enter the Publisher of the Book: ")
                                  cost eval(input("Enter the Cost per Book: "))
                                  stock int (input("Enter the Quantity purchased: "))
                                  cur.execute()
                                  cur.execute (
                                      "insert into stock values ((), '0', '0', '{}', ()()(), '{}')".format (bno, bname, auth, publ, cost, stock, 0, dt.date.today ()))
                                  print("Inserted Sucessfully !!!")


                                  
def add user():
    user input("Enter the user name: ")
    passwd input("Enter a Password: ")
    passwd2 = input("Enter Password to confirm: ")
    If passwd passwd2:
        cur.execute("insert into users values('()', ()')".format (user, passwd))
        print ("Created Successfully!!!")
        elif passwd passwd2:
            print("You've entered different passwords")
            def sell book():
                print('Purchase')
                cname = input("Enter the Customer Name:") phnoint (input("Enter the phone number: "))
                bno int(input("Enter book number: "))
                bname input("Enter the name of the book: ")
                cost eval (input("Enter the cost of the book: "))
                cur.execute("insert into purchased values ([), ()')".format(bno, dt.date.today()))
                cur.execute("update stock set qty_purchased cur.execute("update stock set Available_Stock qty_purchased + 1 where Book No {}".format(bno)) Available Stock 1 where Book No ()".format (bno))
                print("Bought Successfully") qBook Shop\nName: {}\nPhone No: {}\nBook Number: {}\nBook Name: {}\nCost: {}\nDate Of Purchase: {}'.format(
                cname, phno, bno, bname, cost, dt.date.today())filename = mktemp('.txt')
                open (filename, 'w').write(g)
                startfile(filename, 'print')
                cur.execute('select Book Name, Book No, Author from stock where Available Stock 011
                            cur.rowcount == 1
                            print ("STOCK OF ")
                            print("Book Name:", cur.fetchall() [0] [0])
                            print("Book Number: ",cur.fetchall() [0] [1])
                            print("Author: ", cur.fetchall () [0] [2])
                            print("EXHAUSTED")
                            _cur.execute('delete from stock where Available Stock = 0)
                                         print("Either your username or password is incorrect")
                                         elif choice4 == 3:
                                             print("Good Bye")
                                             break
                                            else:
                                                print("INVALID CHOICE")
                                                c = input("Do you want to return to main menu (y/[n]): ")
                                                else:
                                                    print("Good Bye")
                                                    try:


                                                        
import pymysql as entr
except ImportError:
import mysql.connector as entr
db = cntr.connect (host='localhost', user='root', passwd='prajwall2')
if str(
cntr) == "<module 'pymysql' from 'C:\\\\Program Files (x86)\\\\Python37\\\\lib\\\\site-packages\\\\pymysql\\\\_init__.py'>":
db.autocommit = True
else:
var db.autocommit
cur db.cursor()
cur.execute("create database if not exists book shop")
cur.execute("use book shop") cur.execute("create table stock\
(Book No bigint primary key, \
Book Name varchar(255),\
Author varchar(255),\
Publisher varchar(255),\
Cost per Book float,\
Available Stock bigint, \
qty_purchased bigint, \
purchased on date)")
cur.execute("create table users (username varchar(255), password varchar(255))")
cur.execute(
"create table purchased (Book no bigint purchased on date foreign key (Book_no) references stock(Bock_No))")
cur.execute("create unique index Book Index on stock (Book No)")
print("Database and Tables created successfully")
c = input("Press any key to continue-----> ")
cur.close()
db.close()
