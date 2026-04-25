
books = {}
show_books = {}
issue_books = {}
add_books = {}
return_books = {}

def renumber_books():
    """Keep available book IDs sequential after delete/add operations."""
    titles = list(books.values())
    books.clear()
    for i, title in enumerate(titles, start=1):
        books[i] = title