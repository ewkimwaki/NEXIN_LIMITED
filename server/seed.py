from datetime import datetime
from databaseconfig import db
from client import Client
from admin import Admin
from tickets import PriorityLevel, TicketStatus, Tickets
from tasks import Task
from app import app


# Use the app's context for database operations
with app.app_context():
    # Create the database tables
    db.create_all()
    
    # Create Admins
    admin1 = Admin(first_name='Sang', last_name='Wicklif', user_name='sangw', position=1, phone_number='1234567890', email='sang@example.com')
    admin2 = Admin(first_name='Mary', last_name='Watiri', user_name='mw', position=2, phone_number='2345678901', email='mary.w@example.com')

    # Create clients
    client1 = Client(name='Mary Watiri', email='mary@example.com', phone_number='1234567890')
    client2 = Client(name='Samuel Omoding', email='sam@example.com', phone_number='0987654321')
    client1 = Client(name='Emmanuel Kimwaki', email='emman@example.com', phone_number='1235567890')
    client2 = Client(name='Sang Wicklife', email='sang@example.com', phone_number='0987653321')
    
    # Create tasks
    task1 = Task(title='Task 1', description='Description for Task 1')
    task2 = Task(title='Task 2', description='Description for Task 2')
    
    # Create tickets
    ticket1 = Tickets(status=TicketStatus.OPEN, priority=PriorityLevel.LOW, deadline=datetime.utcnow(), assign_to=client1.id, client_id=client1.id)
    ticket2 = Tickets(status=TicketStatus.OPEN, priority=PriorityLevel.URGENT, deadline=datetime.utcnow(), assign_to=client2.id, client_id=client2.id)

    # Add clients and tasks to the session
    db.session.add_all([admin1, admin2, client1, client2, task1, task2, ticket1, ticket2])

    # Commit the session to the database
    db.session.commit()
