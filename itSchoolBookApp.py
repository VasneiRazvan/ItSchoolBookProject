def add_book():
    book_name = input("Insert a book name -> ")
    author_name = input("Insert a author name -> ")
    # importing csv lib
    import csv
    with open('booksDB.csv', mode='w') as file:
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
    print("Update book option")


def share_book():
    print("Share book option")


# Main menu for user
print("Menu:")
print("1 : Add a book")
print("2 : List books")
print("3 : Update book")
print("4 : Share book")
option = int(input("Select one option -> "))

if option == 1:
    add_book()
elif option == 2:
    list_books()
elif option == 3:
    update_book()
elif option == 4:
    share_book()
else:
    print('Not a valid option')
