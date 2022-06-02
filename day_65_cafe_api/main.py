from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(cafes)
    print(random_cafe)
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all")
def get_all_cafes():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafe=[cafe.to_dict() for cafe in cafes])


@app.route("/search")
def search_cafes():
    loc = request.args.get('loc')
    cafes_searched = Cafe.query.filter_by(location=loc)
    if cafes_searched.count() != 0:
        return jsonify(cafe=[cafe.to_dict() for cafe in cafes_searched])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})


## HTTP POST - Create Record
@app.route("/add", methods=['POST'])
def add_cafe():
    print(request.form.get('name'))
    new_cafe = Cafe(
        name=request.form.get('name'),
        map_url=request.form.get('map_url'),
        img_url=request.form.get('img_url'),
        location=request.form.get('loc'),
        seats=request.form.get('seats'),
        has_toilet=bool(request.form.get('toilet')),
        has_wifi=bool(request.form.get('wifi')),
        has_sockets=bool(request.form.get('sockets')),
        can_take_calls=bool(request.form.get('calls')),
        coffee_price=request.form.get('price')
    )
    # try:

    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={'success': 'Successfully added the new cafe.'})
    # except:
    #     db.session.rollback()
    # finally:
    #     db.session.close()
    # return jsonify(response={'fail': 'Unsuccessfully added the new cafe.'})


## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=['PATCH'])
def update_price(cafe_id):
    cafe_to_update = Cafe.query.get(cafe_id)
    if cafe_to_update:
        cafe_to_update.coffee_price = request.form.get('new_price')
        print(cafe_to_update.to_dict())
        db.session.commit()
        return jsonify(success='Successfully updated the price.'), 200
    else:
        return jsonify(error={'Not Found': 'Sorry the cafe with that id was not found in the database.'}), 404


## HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=['DELETE'])
def report_closed_cafe(cafe_id):
    api_key = request.args.get('api_key')
    if api_key == 'TopSecretAPIKey':
        cafe_to_delete = Cafe.query.get(cafe_id)
        if cafe_to_delete:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            return jsonify(success='Successfully deleted the cafe.'), 200
        else:
            return jsonify(error={'Not Found': 'Sorry the cafe with that id was not found in the database.'}), 404
    else:
        return jsonify(error={'Forbidden': 'Sorry, that\'s not allowed. Make sure you have the correct api_key.'}), 403


if __name__ == '__main__':
    app.run(debug=True)
