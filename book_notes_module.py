def book_notes():
    book_note = str(input("Please write your notes about the book here -> "))
    import csv
    with open('booksDB.csv', mode='r') as file:
        rows = list(csv.DictReader(file, fieldnames=('BookName', 'AuthorName', 'SharedWith', 'IsRead',
                                                     'StartDate', 'EndDate', 'Notes')))
        for row in rows:
            if row['BookName'] == 'BookName':
                row['Notes'] = book_note
                break
        with open('booksDB.csv', mode='w'):
            csv_writer = csv.DictWriter(file, fieldnames=['BookName', 'AuthorName', 'SharedWith', 'IsRead',
                                                          'StartDate', 'EndDate', 'Notes'])
            csv_writer.writerow({'BookName': row.get('BookName'),
                                 'AuthorName': row.get('AuthorName'),
                                 'SharedWith': row.get('SharedWith'),
                                 'IsRead': row.get('IsRead'),
                                 'StartDate': row.get('StartDate'),
                                 'EndDate': row.get('EndDate'),
                                 'Notes': book_note})
