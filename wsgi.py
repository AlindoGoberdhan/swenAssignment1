import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup

from App.database import db, get_migrate
from App.models import User
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize,applyToJob, view_applicants, create_job, view_jobs )


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

@user_cli.command('viewJob')
def job_list():
    view_jobs()

app.cli.add_command(user_cli) # add the group to the cli


employer_cli = AppGroup('Employer', help='Employer object commands')

@employer_cli.command('create_job')
@click.argument('job_name')
@click.argument('job_description')
def job_create(job_name,job_description):
    print(create_job(job_name,job_description))

@employer_cli.command('view_applicants')
@click.argument('job_code')
def applicant_listing(job_code):
    view_applicants(job_code)

app.cli.add_command(employer_cli)

applicant_cli = AppGroup('Applicant', help='Employer object commands')

@applicant_cli.command('applyToJob')
@click.argument('applicant_id')
@click.argument('job_code')
def jobApply(applicant_id,job_code):
    applyToJob(applicant_id,job_code)
app.cli.add_command(applicant_cli)


'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)