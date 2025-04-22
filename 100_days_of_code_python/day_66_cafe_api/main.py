from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
        # return self.__dict__

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route('/random', methods=['GET'])
def get_random_cafe():
    # GET a random cafe
    random_cafe = db.session.execute(db.select(Cafe).order_by(func.random())).scalars().first()
    if request.method == 'GET':
        return jsonify(cafe=random_cafe.to_dict())

@app.route('/all', methods=['GET'])
def get_all_cafes():
    # GET all cafes
    result = db.session.execute(db.select(Cafe).order_by(Cafe.name)).scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in result])


@app.route('/search', methods=['GET'])
def search_cafe():
    #get a cafe location
    cafe_location = request.args.get('loc')
    # return cafe_location
    result = db.session.execute(db.select(Cafe).where(Cafe.location == cafe_location)).scalars().all()
    if result:
        return jsonify(cafe=[cafe.to_dict() for cafe in result])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404
# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def patch_new_price(cafe_id):
    new_price = request.args.get("new_price")
    try:
        cafe = db.get(Cafe, cafe_id)
    except AttributeError:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
