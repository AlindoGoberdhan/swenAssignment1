from App.database import db
from App.models import Job
from sqlalchemy.exc import IntegrityError

def create_job(jobName, jobDescription):
    try:
        job = Job(jobName,jobDescription)
        db.session.add(job)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return "Job could not be created"
    return "Job created Successfully"





