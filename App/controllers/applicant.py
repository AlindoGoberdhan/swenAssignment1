from App.models import Applicant
from .application import create_application
from App.database import db
from sqlalchemy.exc import IntegrityError

def create_applicant(username,password,firstName,lastName,phoneNumber):
    print("DSDS")
    try:
        applicant = Applicant(username,password,firstName,lastName,phoneNumber)
        db.session.add(applicant)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return("The applicant could not be created")
    return("The applicant was created successfully")

def applyToJob(applicantID,jobCode):
    print(create_application(applicantID,jobCode))
    