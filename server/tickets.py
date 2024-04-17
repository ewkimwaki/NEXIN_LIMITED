from databaseconfig import db


class Tickets(db.Model):
    __tablename__ = 'tickets'
    
    id = db.Column(db.Integer, primary_key=True)
    ticket = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)