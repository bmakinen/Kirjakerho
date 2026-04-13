CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT, 
    review TEXT,
    user_id INTEGER REFERENCES users
);

CREATE TABLE book_classes (
    id INTEGER PRIMARY KEY,
    book_id INTEGER REFERENCES books,
    title TEXT,
    value TEXT
);