from flask import Flask, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import MetaData
from databaseconfig import db
from models import Client


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h3>Nexin LTD</h3>'

@app.route('/clients')
def clients():
    clients = Client.querry.all()
    client_list = []
    for client in clients:
        client_list.append({
            'id': client.id,
            'name': client.name,
            'email': client.email,
            'phone_number': client.phone_number
        })
    return jsonify(client_list)

if __name__ == '__main__':
    app.run(port=5555, debug=True)