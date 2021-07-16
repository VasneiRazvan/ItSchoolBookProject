def update_book():
    book_name = input("Enter book name: ")
    book_read = input("Is the book read?(Y/N)?")
    if book_read == 'Y'.upper():
        book_read = True
    else:
        book_read = False
    import csv
    with open('booksDB.csv', mode='r') as file:
        rows = list(csv.DictReader(file, fieldnames=('BookName', 'AuthorName', 'SharedWith', 'IsRead', 'StartDate',
                                                     'EndDate', 'Notes')))
        for row in rows:
            if row["BookName"] == book_name:
                row["IsRead"] = book_read
                break
            with open('booksDB.csv', mode='w'):
                csv_writer = csv.DictWriter(file, fieldnames=[
                    "BookName", "AuthorName", "SharedWith", "IsRead"])
                csv_writer.writerow({"BookName": row.get("BookName"),
                                     "AuthorName": row.get("AuthorName"),
                                     "SharedWith": row.get("SharedWith"),
                                     "IsRead": book_read})
        print("Book was updated successfully")
        if book_read == "Y".upper():
            start_date = input('When have you started to read the book? -> ')
            end_date = input('When have you finished reading the book? -> ')
            with open('booksDB.csv', mode='r') as isfile:
                rows = list(csv.DictReader(isfile, fieldnames=('BookName', 'AuthorName', 'SharedWith', 'IsRead',
                                                               'StartDate', 'EndDate', 'Notes')))
                for row in rows:
                    if row['BookName'] == 'BookName':
                        row['StartDate'] = start_date
                        row['EndDate'] = end_date
                        break
                with open('booksDB.csv', mode='w'):
                    csv_writer = csv.DictWriter(file, fieldnames=['BookName', 'AuthorName', 'SharedWith', 'IsRead',
                                                                  'StartDate', 'EndDate', 'Notes'])
                    csv_writer.writerow({'BookName': row.get('BookName'),
                                         'AuthorName': row.get('AuthorName'),
                                         'SharedWith': row.get('SharedWith'),
                                         'IsRead': row.get('IsRead'),
                                         'StartDate': start_date,
                                         'EndDate': end_date})
