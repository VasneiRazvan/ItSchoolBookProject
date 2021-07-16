def update_book():
    book_name = input("Enter book name: ")
    book_read = input("Is the book read?(Y/N)?")
    if book_read == 'Y'.upper():
        book_read = True
    else:
        book_read = False
    rows = []
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