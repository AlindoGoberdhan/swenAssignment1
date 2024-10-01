from App.database import db
from .user import User

class Applicant(User):
    id = db.Column (db.Integer, db.ForeignKey ('user.id'),primary_key=True)     
    phoneNumber = db.Column(db.String(10),nullable=False)
    applications = db.Relationship('Job', secondary = 'application', backref = 'applicants')

    mapper_args = {
        'polymorphic_identity': 'applicant'
    }
    
    def __init__(self,username, password,firstName,lastName,phoneNumber):
         super().__init__(username, password,firstName,lastName)
         self.phoneNumber = phoneNumber

         
    def __repr__(self):
        return f'ID: {self.id} {self.firstName} {self.lastName}'

    