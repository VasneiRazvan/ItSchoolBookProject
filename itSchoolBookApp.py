def add_book():
    book_name = input("Insert a book name -> ")
    author_name = input("Insert a author name -> ")
    # importing csv lib
    import csv
    #  open csv file in append mode
    with open('booksDB.csv', mode='a') as file:
        writer = csv.DictWriter(file, fieldnames=[
            'BookName', 'AuthorName', 'SharedWith', 'IsRead'
        ])
        writer.writerow({'BookName': book_name,
                         'AuthorName': author_name,
                         'SharedWith': 'None',
                         'IsRead': False})
        print('Book was added successfully')


def list_books():
    import csv
    with open('booksDB.csv', mode='r') as file:
        #  Step 1 take all the data from the DB(DataBase)
        rows = csv.DictReader(file, fieldnames=("BookName", "AuthorName", "SharedWith", "IsRead"))
        #  we are going through one line at a time
        for row in rows:
            print(f"Book name is: {row.get('BookName')}"
                  f" Auth Name {row.get('AuthorName')}"
                  f" Is Shared {row.get('ShareWith')} "
                  f"Is Read  {row.get('IsRead', False)}")


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
        rows = list(csv.DictReader(file, fieldnames=("BookName", "AuthorName", "SharedWith", "IsRead")))
        for row in rows:
            if row["BookName"] == book_name:
                row["IsRead"] = book_read
                break
        with open('booksDB.csv', mode='w') as file:
            csv_writer = csv.DictWriter(file, fieldnames=[
                "BookName", "AuthorName", "SharedWith", "IsRead"
            ])
            csv_writer.writerow({"BookName": row.get("BookName"),
                                 "AuthorName": row.get("AuthorName"),
                                 "SharedWith": row.get("SharedWith"),
                                 "IsRead": book_read}
                                )
        print("Book was updated successfully")


def share_book():
    book_name = input('What is the name of the book you want to share? -> ')
    shared_with = input('With whom do you like to share? -> ')
    import csv
    with open('booksDB.csv', mode='r') as file:
        rows = list(csv.DictReader(file, fieldnames=('BookName', 'AuthorName', 'SharedWith', 'IsRead')))
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
                                 'IsRead': row.get('IsRead')}
                                )


def close_application():
    close_app = input('Do You want to quit the app? Y/N -> ')
    while close_app == 'N':
        main_menu()
        return
    print('The app will close.')


def main_menu():
    menu = ("""Main Menu:
    1. Add a book
    2. List books
    3. Update books
    4. Share books
    5. Close Application
    """)
    for option in menu:
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
            close_application()
        else:
            print('Not a valid option')


main_menu()

