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
                         'IsRead': False})
        print('Book was added successfully')