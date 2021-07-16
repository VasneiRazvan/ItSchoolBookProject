def list_books():
    import csv
    with open('booksDB.csv', mode='r') as file:
        #  Step 1 take all the data from the DB(DataBase)
        rows = csv.DictReader(file, fieldnames=('BookName', 'AuthorName', 'SharedWith', 'IsRead',
                                                'StartDate', 'EndDate', 'Notes'))
        #  we are going through one line at a time
        for row in rows:
            print(f"The book name is: {row.get('BookName')}"
                  f" writen by: {row.get('AuthorName')}"
                  f" the book is shared: {row.get('ShareWith')} "
                  f" Is Read:  {row.get('IsRead', False)}")