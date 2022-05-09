from flask import Flask, request

from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)



#making the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description}"

@app.route('/')
def index():
    return 'Hello!'

@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()

    output = []
    for drink in drinks:
        drink_data = {'name': drink.name, 'description': drink.description}

        output.append(drink_data)

    return {"drinks" : output}

#Accessing specific id's in the api. Although dicts, count from ), id's in the web start from 0
#So http://127.0.0.1:5000/drinks/0 return a 404 error,, whereas, http://127.0.0.1:5000/drinks/1 returns the first drink item from the database
@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return {"name": drink.name, "description": drink.description}

#Adding a new drink. POST is the API standard to add(Create from CRUD)
@app.route('/drinks', methods=['POST'])
def add_drink():
    drink = Drink(name=request.json['name'],
                   description=request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {'id': drink.id}

@app.route('/drinks/<id>', methods=['DELETE'])
def delete_drinl(id):
    drink = Drink.query.get(id)
    if drink is None:
        return {"error" : "drink not found"}
    db.session.delete(drink)
    db.session.commit()
    return {"message": "drink deleted"}