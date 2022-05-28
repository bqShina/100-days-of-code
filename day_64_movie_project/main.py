from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests
import pprint
# import sqlite3
#
# db = sqlite3.connect("movies-collection.db")

MOVIES_API_KEY = "Your own api key"
MOVIES_ENDPOINT = "https://api.themoviedb.org/3/search/movie"
DETAILS_ENDPOINT = "https://api.themoviedb.org/3/movie"


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies-collection.db'
db = SQLAlchemy(app)
Bootstrap(app)


class MyForm(FlaskForm):
    rating = FloatField(label='Your Rating of 10. e.g. 7.5 ', validators=[DataRequired()])
    review = StringField(label='Your Review', validators=[DataRequired()])

    submit = SubmitField(label='Done')


class AddForm(FlaskForm):
    title = StringField(label='Movie Title', validators=[DataRequired()])

    submit = SubmitField(label='Add Movie')


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String)
    img_url = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'title: {self.title}, year: {self.year}'

# db.create_all()


@app.route("/")
def home():
    movies = db.session.query(Movie).order_by(Movie.rating)
    i = movies.count()
    for movie in movies:
        movie.ranking = i
        i -= 1
    return render_template("index.html", all_movies=movies)


@app.route("/edit", methods=['POST', 'GET'])
def edit():
    form = MyForm()
    movie_id = request.args.get('id')
    movie = Movie.query.get(movie_id)

    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=['POST', 'GET'])
def add():
    add_form = AddForm()
    if add_form.validate_on_submit():
        search_title = add_form.title.data
        response = requests.get(url=MOVIES_ENDPOINT, params={'api_key': MOVIES_API_KEY, 'query': search_title})
        data = response.json()
        movies_data = data['results']
        return render_template("select.html", movies=movies_data)
    return render_template("add.html", form=add_form)


@app.route("/movie")
def add_movie():
    movie_id = request.args.get('id')

    response = requests.get(url=f"https://api.themoviedb.org/3/movie/{movie_id}", params={"api_key": MOVIES_API_KEY,
                                                                                          "language": "en-US"})
    movie_data = response.json()

    new_movie = Movie(
            title=movie_data['title'],
            year=movie_data['release_date'][:4],
            description=movie_data['overview'],
            img_url=f"https://image.tmdb.org/t/p/w500{movie_data['poster_path']}"
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit', id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
