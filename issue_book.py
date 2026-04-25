from utils import books, issue_books, renumber_books

def issue():
    book_name = input("Enter the book name: ").upper()
    matches = [key for key, name in books.items() if name == book_name]
    if not matches:
        print("This Book is not available in our library.\nSorry for the inconvenience.\nThank you for using our library.\nHave a nice day.")
    elif len(matches) == 1:
        target_key = matches[0]
        issue_books[target_key] = books.pop(target_key)
        renumber_books()
        print("Book assigned successfully.\nThank you for using our library.\nHave a nice day.")
    else:
        print("Available copies:")
        for i, key in enumerate(matches, start=1):
            print(f"{i}. {books[key]}")
        while True:
            choice_input = input("Enter the number of the book you want to issue: ").strip()
            if not choice_input.isdigit():
                print("Invalid input. Please enter a number.")
                continue
            choice = int(choice_input)
            if 1 <= choice <= len(matches):
                target_key = matches[choice-1]
                issue_books[target_key] = books.pop(target_key)
                renumber_books()
                print("|->Book assigned successfully.\n|-> You have 15 days to return this book.\nThank you for using our library.\nHave a nice day.")
                break
            else:
                print(f"Invalid choice. Please enter a number between 1 and {len(matches)}.")
