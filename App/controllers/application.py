from App.models import Application
from App.database import db
from sqlalchemy.exc import IntegrityError

def create_application(applicantID,jobCode):
    
    if Application.query.filter_by(jobCode=jobCode,applicantID=applicantID).first() != None:
        return "An application for this job already exists"

    try:
        application = Application(applicantID,jobCode)
        db.session.add(application)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return "The application could not successfuly be created"
    return "The application was created successfully"