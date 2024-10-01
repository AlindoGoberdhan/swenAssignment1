from App.database import db
from App.models import Employer
from App.models import Job
from sqlalchemy.exc import IntegrityError

def create_employer(username, password,firstName,lastName):
    try:
        employer = Employer(username, password,firstName,lastName)
        db.session.add(employer)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return "Employer could not be created"
    return "Employer was successfully created"

def view_applicants(jobCode):
    job = Job.query.get(jobCode)
    if job:
        for applicant in job.applicants:
            print(applicant)
    else:
        print("The job does not exist")
    