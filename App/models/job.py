from App.database import db

class Job(db.Model):
    jobCode = db.Column(db.Integer, primary_key=True)
    jobName = db.Column(db.String(200),nullable=False)
    jobDescription = db.Column(db.String(200), nullable=False)

    def __init__(self,jobName,jobDescription):
        self.jobName = jobName
        self.jobDescription = jobDescription

    def __repr__(self):
        return f'Job Code- {self.jobCode} Job Name- {self.jobName} Job Description- {self.jobDescription}'
    