import utilis


def end_book():
    #  with this function we will enter the date
    #  when we finished reading the book

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
                                 'EndDate': row.get('EndDate'),
                                 'Notes': row.get('Notes')})


utilis.main_menu()
