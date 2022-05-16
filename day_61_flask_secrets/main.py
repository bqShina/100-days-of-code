from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class MyForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired(), Email(message="Invalid email address.")])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8, message="Field must be 8 "
                                                                                                 "characters long.")])
    submit = SubmitField(label='Log In')


# def validate_password(field):
#     if len(field.data) < 8:
#         raise ValidationError('Field must be 8 characters long.')


app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm(meta={'csrf': False})
    if form.validate_on_submit():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)

