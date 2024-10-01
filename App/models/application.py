from App.database import db

class Application(db.Model):
    appID = db.Column(db.Integer, primary_key=True)
    applicantID = db.Column(db.Integer, db.ForeignKey('applicant.id'))
    jobCode = db.Column(db.Integer, db.ForeignKey('job.jobCode'))

    def __init__(self,applicantID,jobCode):
        self.applicantID = applicantID
        self.jobCode = jobCode

    def __repr__(self):
        return f"Applicant ID- {self.applicantID} Job Code - {self.jobCode}"
    
    