from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models import db, bcrypt, User, Note
from config import SQLALCHEMY_DATABASE_URI, SECRET_KEY

app = Flask(__name__, static_folder='static')
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SECRET_KEY"] = SECRET_KEY

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        secret_word = request.form["secret_word"]

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return "<h3 style='color:red;'>Этот пользователь уже существует!</h3> <a href='/register'>Попробовать снова</a>"

        new_user = User(username=username, secret_word=secret_word)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()

        return redirect("/login")

    return render_template("register.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    app.logger.info(f"Попытка входа с именем пользователя: {username}")

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        app.logger.info(f"Пользователь {username} успешно вошел.")
        return render_template('code.html')

    app.logger.error(f"Ошибка входа для пользователя {username}. Неверный логин или пароль.")
    return "<h3 style='color:red;'>Ошибка входа!</h3> <a href='/'>Попробовать снова</a>"


@app.route("/code", methods=["POST"])
def verify_code():
    code = request.form["code"]
    user = User.query.filter_by(secret_word=code).first()

    if user:
        login_user(user)
        return redirect("/notes")
    return render_template("error.html")


@app.route("/notes")
@login_required
def notes():
    notes = Note.query.filter_by(user_id=current_user.id).all()
    return render_template("notes.html", notes=notes)


@app.route("/add_note", methods=["GET", "POST"])
@login_required
def add_note():
    if request.method == "POST":
        text = request.form["note"]
        new_note = Note(user_id=current_user.id, text=text)
        db.session.add(new_note)
        db.session.commit()
        return redirect("/notes")

    return render_template("add_note.html")


@app.route("/delete_note/<int:note_id>")
@login_required
def delete_note(note_id):
    note = Note.query.get(note_id)
    if note and note.user_id == current_user.id:
        db.session.delete(note)
        db.session.commit()
    return redirect("/notes")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
