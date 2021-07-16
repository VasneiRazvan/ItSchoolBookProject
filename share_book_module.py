def share_book():
    #  share book function witch will ask the user the name of the book and with who to share it with
    book_name = input('What is the name of the book you want to share? -> ')
    shared_with = input('With whom do you like to share? -> ')
    import csv
    with open('booksDB.csv', mode='r') as file:
        rows = list(csv.DictReader(file, fieldnames=('BookName', 'AuthorName', 'SharedWith', 'IsRead',
                                                     'StartDate', 'EndDate', 'Notes')))
        for row in rows:
            if row['BookName'] == book_name:
                row['SharedWith'] = shared_with
                break
            else:
                print('Book is not in DB')
            with open('booksDB.csv', mode='w'):
                csv_writer = csv.DictWriter(file, fieldnames=['BookName', 'AuthorName', 'SharedWith', 'IsRead'])
                csv_writer.writerow({'BookName': row.get('BookName'),
                                     'AuthorName': row.get('AuthorName'),
                                     'SharedWith': shared_with,
                                     'IsRead': row.get('IsRead')})
