from add_books import add
from issue_book import issue
from show_books import show
from return_book import return_book

def library():
    while True:
        print("\n1. Add Book")
        print("2. Show Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")
        choice_input = input("Enter your choice for using our library service: ").strip()
        if not choice_input.isdigit():
            print("Oops -_- you entered wrong input\n|-> Please enter a number between 1 and 5.")
            continue
        choice = int(choice_input)
        
        if choice == 1:
            add()
        elif choice == 2:
            show()
        elif choice == 3:
            issue()
        elif choice == 4:
            return_book()
        elif choice == 5:
            print("__|^-^|__Thank you for using our library service.\nHave a nice day.")
            break
        else:
            print("For using our library service, you have to choose from the given options.\nThank you.")
            
library()