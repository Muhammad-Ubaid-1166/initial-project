def display_menu():
    print("1. Add Book")  # Complete
    print("2. Remove Book")
    print("3. Display All Books")
    print("4. Search Book")
    print("5. Statistics")
    print("6. Borrow Book")
    print("7. Exit")
    return input("Enter your choice: ")

def add_books(library):
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    date = input("Enter the published date: ")
    read_status = input("Have you read it? (yes/no): ").strip().lower() == 'yes'

    book = {
        'title': title,
        'author': author,
        'date': date,
        'read_status': read_status
    }
    library.append(book)
    print("--------------------------------")
    print("Book added successfully!")
    print("--------------------------------")
    print()

def borrow_books(library):
    already = {
        'title': "Improve Your Vision",
        'author': "Martin Brofman",
        'date': 1999,
        'read_status': True
    }
    library.append(already)
    print("--------------------------------")
    print(f"The book '{already['title']}' is available.")
    print("--------------------------------")
    print()

    already = {
        'title': "Current Affairs",
        'author': "S. Chand",
        'date': 2020,
        'read_status': True
    }
    library.append(already)
    print("--------------------------------")
    print(f"The book '{already['title']}' is available.")
    print("--------------------------------")
    print()

    already = {
        'title': "The Art of War",
        'author': "Sun Tzu",
        'date': 2000,
        'read_status': True
    }
    library.append(already)
    print("--------------------------------")
    print(f"The book '{already['title']}' is available.")
    print("--------------------------------")
    print()

    book_borrowed = input("Enter the title of the book: ")

    for already in library:
        if book_borrowed.lower() == already['title'].lower():
            already['read_status'] = True
            library.append(already)
            print("--------------------------------")
            print("Book borrowed successfully!")
            print("--------------------------------")
            print()
            return
        else:
            print("--------------------------------")
            print("Invalid title.")
            print("--------------------------------")
            print()
    # -----------------x-----------------x---------------------

def remove_books(library):
    search_term = input("Enter the title of the book: ")
    for i, book in enumerate(library, 1):
        print(f"{i}. {book['title']}")
        if book['title'].lower() == search_term.lower():
            question = input("Have you read it? (yes/no): ")
            if question.lower() == 'yes':
                book['read_status'] = True
            library.remove(book)
            print("--------------------------------")
            print("Book removed successfully!")
            print("--------------------------------")
            print()
            return
    print("--------------------------------")
    print("Invalid title.")
    print("--------------------------------")
    print()

def display_books(library):
    print("All Books:")
    if library:
        for i, book in enumerate(library, 1):
            print(f"{i}. {book['title']}")
            status = 'Read' if book['read_status'] else 'Unread'
            print(f"Status: {status}")
    else:
        print("--------------------------------")
        print("The library is empty.")
    print("--------------------------------")
    print()

def search_books(library):
    search_book = input("Enter the title of the book: ")
    for i, book in enumerate(library, 1):
        status = 'Read' if book['read_status'] else 'Unread'
        if book['title'].lower() == search_book.lower():
            print(f"The book '{search_book}' is available and is {status}.")
            return
        else:
            print("--------------------------------")
            print("The book isn't found.")
            print("--------------------------------")
            print()

def statics(library):
    total_number = len(library)
    reading_status = 0
    for book in library:
        if book['read_status']:
            reading_status += 1
    print(f"Total books: {total_number}")
    if reading_status:
        print(f"Percentage of read books: {total_number / reading_status * 100}%")
    else:
        print("--------------------------------")
        print("Try again.")
        print("--------------------------------")
        print()

def main():
    library = []
    while True:
        choice = int(display_menu())
        if choice == 1:
            add_books(library)
        elif choice == 2:
            remove_books(library)
        elif choice == 3:
            display_books(library)
        elif choice == 4:
            search_books(library)
        elif choice == 5:
            statics(library)
        elif choice == 6:
            borrow_books(library)
        elif choice == 7:
            print("Goodbye!")
            break
        else:
            print("--------------------------------")
            print("Invalid number.")
            print("--------------------------------")
            print()

if __name__ == "__main__":
    main()