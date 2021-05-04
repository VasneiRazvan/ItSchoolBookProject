def add_book():
    book_name = input("Insert a book name -> ")
    author_name = input("Insert a author name -> ")
    # importing csv lib
    import csv
    #  open csv file in append mode so we can add more lines in the csv file
    with open('booksDB.csv', mode='a') as file:
        writer = csv.DictWriter(file, fieldnames=[
            'BookName', 'AuthorName', 'SharedWith', 'IsRead'
        ])
        writer.writerow({'BookName': book_name,
                         'AuthorName': author_name,
                         'SharedWith': 'None',
                         'IsRead': False,
                         'StartDate': None,
                         'EndDate': None})
        print('Book was added successfully')


def list_books():
    import csv
    with open('booksDB.csv', mode='r') as file:
        #  Step 1 take all the data from the DB(DataBase)
        rows = csv.DictReader(file, fieldnames=("BookName", "AuthorName", "SharedWith", "IsRead",
                                                "StartDate", "EndDate"))
        #  we are going through one line at a time
        for row in rows:
            print(f"Book name is: {row.get('BookName')}"
                  f" Author Name {row.get('AuthorName')}"
                  f" Is Shared {row.get('ShareWith')} "
                  f"Is Read  {row.get('IsRead', False)}"
                  f"Start book date {row.get('StartDate', None)}"
                  f"End book date {row.get('EndDate', None)}")


def update_book():
    book_name = input("Enter book name: ")
    book_read = input("Is the book read?(Y/N)?")
    if book_read == 'Y':
        book_read = True
    else:
        book_read = False
    import csv
    rows = []
    with open('booksDB.csv', mode='r') as file:
        rows = list(csv.DictReader(file))
        rows = list(csv.DictReader(file, fieldnames=("BookName", "AuthorName", "SharedWith", "IsRead",
                                                     "StartDate", "EndDate")))
        for row in rows:
            if row["BookName"] == book_name:
                row["IsRead"] = book_read
                break
        with open('booksDB.csv', mode='w') as file:
            csv_writer = csv.DictWriter(file, fieldnames=[
                "BookName", "AuthorName", "SharedWith", "IsRead", "Start Date", "End Date"
            ])
            csv_writer.writerow({"BookName": row.get("BookName"),
                                 "AuthorName": row.get("AuthorName"),
                                 "SharedWith": row.get("SharedWith"),
                                 "IsRead": book_read,
                                 'StartDate': row.get("StartDate"),
                                 "EndDate": row.get("EndDate")})
        print("Book was updated successfully")


def share_book():
    #  share book function witch will ask the user the name of the book and with who to share it with
    book_name = input('What is the name of the book you want to share? -> ')
    shared_with = input('With whom do you like to share? -> ')
    import csv
    with open('booksDB.csv', mode='r') as file:
        rows = list(csv.DictReader(file, fieldnames=('BookName', 'AuthorName', 'SharedWith', 'IsRead',
                                                     "StartDate", "EndDate")))
        for row in rows:
            if row['BookName'] == book_name:
                row['SharedWith'] = shared_with
                break
            else:
                print('Book is not in DB')
        with open('booksDB.csv', mode='w') as file:
            csv_writer = csv.DictWriter(file, fieldnames=['BookName', 'AuthorName', 'SharedWith', 'IsRead'])
            csv_writer.writerow({'BookName': row.get('BookName'),
                                 'AuthorName': row.get('AuthorName'),
                                 'SharedWith': shared_with,
                                 'IsRead': row.get('IsRead')})


def close_application():
    #  Close app function. The user will be asked after each menu entry if he wants to quit the app or return
    #  to main menu
    close_app = input('Do You want to quit the app? Y/N -> ')
    while close_app == 'N':
        main_menu()
        return
    print('The app will close.')


def start_book():
    #  with this function we will enter the date when we started
    #  reading the book
    start_date = input('When have you started to read the book? -> ')
    import csv
    with open('booksDB.csv', mode='r') as file:
        rows = list(csv.DictReader(file, fieldnames=('BookName', 'AuthorName', 'SharedWith', 'IsRead',
                                                     "StartDate", "EndDate")))
        for row in rows:
            if row['BookName'] == book_name:
                row['StartDate'] = start_date
                break
        with open('booksDB.csv', mode='w') as file:
            csv_writer = csv.DictWriter(file, fieldnames=['BookName', 'AuthorName', 'SharedWith', 'IsRead',
                                                          'StartDate', 'EndDate'])
            csv_writer.writerow({'BookName': row.get('BookName'),
                                 'AuthorName': row.get('AuthorName'),
                                 'SharedWith': row.get('SharedWith'),
                                 'IsRead': row.get('IsRead'),
                                 'StartDate': start_date,
                                 'EndDate': None})


def end_book():
    #  with this function we will enter the date
    #  when we finished reading the book
    end_date = input('When have you finished reading the book? -> ')
    import csv
    with open('booksDB.csv', mode='r') as file:
        rows = list(csv.DictReader(file, fieldnames=('BookName', 'AuthorName', 'SharedWith', 'IsRead',
                                                     "StartDate", "EndDate")))
        for row in rows:
            if row['BookName'] == book_name:
                row['EndDate'] = end_date
                break
        with open('booksDB.csv', mode='w') as file:
            csv_writer = csv.DictWriter(file, fieldnames=['BookName', 'AuthorName', 'SharedWith', 'IsRead',
                                                          'StartDate', 'EndDate'])
            csv_writer.writerow({'BookName': row.get('BookName'),
                                 'AuthorName': row.get('AuthorName'),
                                 'SharedWith': row.get('SharedWith'),
                                 'IsRead': row.get('IsRead'),
                                 'StartDate': row.get('StartDate'),
                                 'EndDate': end_date})


def main_menu():
    menu = ("""Main Menu:
    1. Add a book
    2. List books
    3. Update books
    4. Share books
    5. Book Record
    6. Close Application""")
    print(menu)
    option = int(input('Please select one option from the menu -> '))
    if option == 1:
        add_book()
        close_application()
    elif option == 2:
        list_books()
        close_application()
    elif option == 3:
        update_book()
        close_application()
    elif option == 4:
        share_book()
        close_application()
    elif option == 5:
        start_book()
        close_application()
    elif option == 6:
        end_book()
        close_application()
    elif option == 7:
        close_application()
    else:
        print('Not a valid option')


main_menu()
