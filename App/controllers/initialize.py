from .user import create_user
from .job import create_job
from .employer import create_employer
from .applicant import create_applicant
from App.database import db


def initialize():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass','bob','smith')
    create_job("Janitor","Clean thing")
    create_employer("John","johnpass","John","The baptist")
    create_applicant("Dave", 'davepass', "Dave", "d tire man", '282-1694')
    
