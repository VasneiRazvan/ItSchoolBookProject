import utilis


def start_book():
    #  with this function we will enter the date when we started
    #  reading the book
    start_date = input('When have you started to read the book? -> ')
    import csv
    with open('booksDB.csv', mode='r') as file:
        rows = list(csv.DictReader(file, fieldnames=('BookName', 'AuthorName', 'SharedWith', 'IsRead',
                                                     'StartDate', 'EndDate', 'Notes')))
        for row in rows:
            if row['BookName'] == 'BookName':
                row['StartDate'] = start_date
                break
        with open('booksDB.csv', mode='w'):
            csv_writer = csv.DictWriter(file, fieldnames=['BookName', 'AuthorName', 'SharedWith', 'IsRead',
                                                          'StartDate', 'EndDate', 'Notes'])
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
                                                     'StartDate', 'EndDate', 'Notes')))
        for row in rows:
            if row['BookName'] == 'BookName':
                row['EndDate'] = end_date
                break
        with open('booksDB.csv', mode='w'):
            csv_writer = csv.DictWriter(file, fieldnames=['BookName', 'AuthorName', 'SharedWith', 'IsRead',
                                                          'StartDate', 'EndDate', 'Notes'])
            csv_writer.writerow({'BookName': row.get('BookName'),
                                 'AuthorName': row.get('AuthorName'),
                                 'SharedWith': row.get('SharedWith'),
                                 'IsRead': row.get('IsRead'),
                                 'StartDate': row.get('StartDate'),
                                 'EndDate': end_date,
                                 'Notes': row.get('Notes')})


utilis.main_menu()