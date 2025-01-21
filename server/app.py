# server/app.py
#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Pet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def index():
    return make_response(
        '<h1>Welcome to the pet directory!</h1>',
        200
    )

@app.route('/demo_json')
def demo_json():
    pet = Pet.query.first()
    pet_dict = {'id': pet.id,
                'name': pet.name,
                'species': pet.species
                }

    return make_response(pet_dict, 200)

if __name__ == '__main__':
    app.run(port=5555, debug=True)