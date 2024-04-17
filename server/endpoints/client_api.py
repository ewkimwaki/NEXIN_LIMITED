from models import Client
from flask import jsonify

def clients():
    clients = Client.query.all()
    client_list = []
    for client in clients:
        client_list.append({
            'id': client.id,
            'name': client.name,
            'email': client.email,
            'phone_number': client.phone_number
        })
    return jsonify(client_list)