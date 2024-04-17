from databaseconfig import db

class Client(db.Model):
    __tablename__ = 'clients'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self):
        return f"<Client(name='{self.name}', email='{self.email}', phone_number='{self.phone_number}')>"