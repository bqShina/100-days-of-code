from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
# Line below only required once, when creating DB.
# db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        new_email = request.form['email']
        if User.query.filter_by(email=new_email).first():
            flash("You have already signed up with that email. Please log in instead.")
            return redirect(url_for('login'))
        hash_password = generate_password_hash(password=request.form['password'],
                                               method="pbkdf2:sha256",
                                               salt_length=8)

        new_user = User(email=new_email,
                        name=request.form['name'],
                        password=hash_password)
        db.session.add(new_user)
        db.session.commit()

        return render_template("secrets.html", name=new_user.name)

    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        user_to_login = User.query.filter_by(email=request.form['email']).first()
        if not user_to_login:
            flash("The email doesn't exist. Please try again.")
            return redirect(url_for('login'))
        elif check_password_hash(pwhash=user_to_login.password, password=request.form['password']):
            login_user(user_to_login)
            return redirect(url_for('secrets'))
        else:
            flash("Incorrect password. Please try again.")
            return redirect(url_for('login'))

    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', filename='files/cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
