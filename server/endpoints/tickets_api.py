from models import Tickets
from flask import jsonify, request
from databaseconfig import db

def tickets():
    if request.method == 'GET':
        tickets = Tickets.query.all()
        ticket_list = []
        for ticket in tickets:
            ticket_list.append({
                'id' : ticket.id,
                'status' : ticket.status,
                'priority' : ticket.priority,
                'deadline' : ticket.deadline,
                'assign_to' : ticket.assign_to,
                'client_id' : ticket.id
            })
        return jsonify(ticket_list)
    elif request.method == 'POST':
        data = request.get_json()
        status = data.get('status')
        priority = data.get('priority')
        deadline = data.get('deadline')
        assign_to = data.get('assign_to')
        client_id = data.get('client_id')
        ticket = Tickets(status = status, priority = priority, deadline = deadline, assign_to = assign_to, client_id = client_id)
        db.session.add(ticket)
        db.session.commit()
        inserted_ticket = {
            'status' : ticket.status,
            'priority' : ticket.priority,
            'deadline' : ticket.deadline,
            'assign_to' : ticket.assign_to,
            'client_id' : ticket.id
            }
        return jsonify(inserted_ticket)
    elif request.method == 'DELETE':
        ticket_id = request.args.get('id')
        ticket = Tickets.query.get(ticket_id)
        if ticket:
            db.session.delete(ticket)
            db.session.commit()
            return f"Ticket with ID {client_id} deleted"
        else:
            return f"Ticket with ID {client_id} not found", 404