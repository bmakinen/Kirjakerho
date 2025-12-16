import db

def add_book(title, author, review, user_id):
    sql = """INSERT INTO books (title, author, review, user_id)
            VALUES (?, ?, ?, ?)"""
    db.execute(sql, [title, author, review, user_id])