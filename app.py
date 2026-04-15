import sqlite3
from flask import Flask
from flask import abort, redirect, render_template, request, session
from werkzeug.security import check_password_hash, generate_password_hash
import config
import db
import books
import users

app = Flask(__name__)
app.secret_key = config.secret_key

def require_login():
    if "user_id" not in session:
        abort(403)

@app.route("/")
def index():
    all_books = books.get_books()
    return render_template("index.html", books=all_books)

@app.route("/user/<int:user_id>")
def show_user(user_id):
    user = users.get_user(user_id)
    if not user:
        abort(404)
    books = users.get_books(user_id)
    return render_template("show_user.html", user=user, books=books)

@app.route("/find_book")
def find_book():
    query = request.args.get("query")
    if query:
        results = books.find_books(query)
    else:
        query = ""
        results = []
    return render_template("find_book.html", query=query, results=results)

@app.route("/book/<int:book_id>")
def show_book(book_id):
    book = books.get_book(book_id)
    if not book:
        abort(404)
    classes = books.get_classes(book_id)
    return render_template("show_book.html", book=book, classes=classes)

@app.route("/new_book")
def new_book():
    require_login()
    classes = books.get_all_classes()
    return render_template("new_book.html", classes=classes)

@app.route("/create_book", methods=["POST"])
def create_book():
    require_login()

    title = request.form["title"]
    if len(title) > 50:
        abort(403)
    author = request.form["author"]
    if len(author) > 50:
        abort(403)
    review = request.form["review"]
    if len(review) > 1000:
        abort(403)
    user_id = session["user_id"]

    all_classes = books.get_all_classes()

    classes = []
    for entry in request.form.getlist("classes"):
        if entry:
            class_title, class_value = entry.split(":")
            if class_title not in all_classes:
                abort(403)
            if class_value not in all_classes[class_title]:
                abort(403)
            classes.append((class_title, class_value))

    books.add_book(title, author, review, user_id, classes)

    return redirect("/")

@app.route("/edit_book/<int:book_id>")
def edit_book(book_id):
    require_login()
    book = books.get_book(book_id)
    if not book:
        abort(404)
    if book["user_id"] != session["user_id"]:
        abort(403)

    all_classes = books.get_all_classes()
    classes = {}
    for my_class in all_classes:
        classes[my_class] = ""
    for entry in books.get_classes(book_id):
        classes[entry["title"]] = entry["value"]

    return render_template("edit_book.html", book=book, classes=classes, all_classes=all_classes)

@app.route("/update_book", methods=["POST"])
def update_book():
    require_login()
    book_id = request.form["book_id"]
    book = books.get_book(book_id)
    if not book:
        abort(404)
    if book["user_id"] != session["user_id"]:
        abort(403)

    review = request.form["review"]

    all_classes = books.get_all_classes()

    classes = []
    for entry in request.form.getlist("classes"):
        if entry:
            class_title, class_value = entry.split(":")
            if class_title not in all_classes:
                abort(403)
            if class_value not in all_classes[class_title]:
                abort(403)
            classes.append((class_title, class_value))

    books.update_book(book_id, review, classes)

    return redirect("/book/"+str(book_id))

@app.route("/remove_book/<int:book_id>", methods=["GET", "POST"])
def remove_book(book_id):
    require_login()
    book = books.get_book(book_id)

    if not book:
        abort(404)
    if book["user_id"] != session["user_id"]:
        abort(403)

    if request.method == "GET":
        return render_template("remove_book.html", book=book)
    
    if request.method == "POST":
        if "remove" in request.form:
            books.remove_book(book_id)
            return redirect("/")
        else:
            return redirect("/book/" + str(book_id))

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create", methods=["POST"])
def create():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        return "VIRHE: salasanat eivät ole samat"

    try:
        users.create_user(username, password1)
    except sqlite3.IntegrityError:
        return "VIRHE: tunnus on jo varattu"

    return "Tunnus luotu"

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":    
        username = request.form["username"]
        password = request.form["password"]

        user_id = users.check_login(username, password)
        if user_id:
            session["user_id"] = user_id
            session["username"] = username
            return redirect("/")
        else:
            return "VIRHE: väärä tunnus tai salasana"

@app.route("/logout")
def logout():
    if "user_id" in session:
        del session["user_id"]
        del session["username"]
    return redirect("/")
