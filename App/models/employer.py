from App.database import db
from .user import User

class Employer(User):
    
    id = db.Column (db.Integer, db.ForeignKey ('user.id'),primary_key=True)  
    
    __mapper_args__ = {
        'polymorphic_identity': 'employer'
    }
