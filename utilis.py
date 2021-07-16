import add_book_module
import list_books_module
import update_book_module
import share_book_module
import book_notes_module


def close_application():
    #  Close app function. The user will be asked after each menu entry if he wants to quit the app or return
    #  to main menu
    close_app = input('Do You want to quit the app? Y/N -> ').upper()
    if close_app == 'N':
        main_menu()
    else:
        print('The app will close.')


def main_menu():
    #  main menu as tuple.
    #  Tuple is a list that can not be modified.
    menu = ('1. Add Books', '2. List Books', '3. Update Books', '4. Share Books', '5. Book Start Date', '6. Book End '
                                                                                                        'Date',
            '7. Notes', '8. Close App')
    print(menu)
    option = int(input('Please select one option from the menu -> '))
    if option == 1:
        add_book_module.add_book()
        close_application()
    elif option == 2:
        list_books_module.list_books()
        close_application()
    elif option == 3:
        update_book_module.update_book()
        close_application()
    elif option == 4:
        share_book_module.share_book()
        close_application()
    elif option == 5:
        book_notes_module.book_notes()
        close_application()
    elif option == 6:
        close_application()
    else:
        print('Not a valid option')