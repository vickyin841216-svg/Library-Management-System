# 📚 Library Management System

A simple command-line **Library Management System** built in Python. It allows users to add books, view available titles, issue books to members, and return them — all through an interactive terminal menu.

---

## 🚀 Features

- **Add Books** — Add new titles to the library collection
- **Show Books** — View all currently available books
- **Issue Books** — Check out a book (supports multiple copies)
- **Return Books** — Return a previously issued book
- **Input Validation** — Handles invalid inputs gracefully throughout

---

## 📁 Project Structure

```
Library-Management-System/
│
├── main.py          # Entry point; main menu loop
├── add_books.py     # Logic for adding a new book
├── show_books.py    # Logic for displaying available books
├── issue_book.py    # Logic for issuing a book to a user
├── return_book.py   # Logic for returning an issued book
└── utils.py         # Shared data stores and helper functions
```

---

## ⚙️ Requirements

- Python 3.6 or higher
- No external libraries required

---

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/vickyin841216-svg/Library-Management-System.git
   cd Library-Management-System
   ```

2. **Run the application:**
   ```bash
   python main.py
   ```

---

## 📖 Usage

When you run `main.py`, you'll see the following menu:

```
1. Add Book
2. Show Book
3. Issue Book
4. Return Book
5. Exit
```

Enter the number corresponding to the action you'd like to perform. Book names are stored and matched in **uppercase** (case-insensitive input).

### Example Session

```
Enter your choice for using our library service: 1
Enter the Book name which you want to add in the library: The Great Gatsby
Book added successfully: THE GREAT GATSBY

Enter your choice for using our library service: 3
Enter the book name: the great gatsby
Book assigned successfully.
Thank you for using our library.
Have a nice day.
```

---

## 🗃️ Data Storage

All data is stored **in-memory** using Python dictionaries defined in `utils.py`:

| Variable      | Purpose                          |
|---------------|----------------------------------|
| `books`       | Currently available books        |
| `issue_books` | Books that have been issued out  |

> ⚠️ Note: Data is not persisted between sessions. Restarting the program resets all data.

---

## 🔧 How It Works

- Books are stored as `{id: title}` dictionaries.
- The `renumber_books()` utility function keeps IDs sequential after any add/remove operation.
- Issuing a book moves it from `books` → `issue_books`.
- Returning a book moves it back from `issue_books` → `books`.

---

## 🌱 Future Improvements

- [ ] Add file/database persistence (e.g., JSON or SQLite)
- [ ] Track which member has issued which book
- [ ] Add due dates and overdue notifications
- [ ] Add search functionality
- [ ] Build a GUI or web interface

---

## 👩‍💻 Author

**vickyin841216-svg**  
GitHub: [https://github.com/vickyin841216-svg](https://github.com/vickyin841216-svg)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
