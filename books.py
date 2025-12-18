import db

def add_book(title, author, review, user_id):
    sql = """INSERT INTO books (title, author, review, user_id)
            VALUES (?, ?, ?, ?)"""
    db.execute(sql, [title, author, review, user_id])


def get_books():
    sql = "SELECT id, title, author FROM books ORDER BY id DESC"
    return db.query(sql)


def get_book(book_id):
    sql = """SELECT books.id,
                    books.title,
                    books.author,
                    books.review,
                    users.id user_id,
                    users.username
            FROM books, users
            WHERE books.user_id = users.id AND
                  books.id = ?"""
    return db.query(sql, [book_id])[0]


def update_book(book_id, review):
    sql = """UPDATE books SET review = ?
                          WHERE id = ?"""
    db.execute(sql, [review, book_id])