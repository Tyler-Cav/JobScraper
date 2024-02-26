import os
import requests
from email.message import EmailMessage
import ssl
import smtplib
from dotenv import load_dotenv, dotenv_values
load_dotenv()

# Setting URL to the Listrak department API
URL = os.getenv('MY_SECRET_URL')

# Using the request python dependecy to call on that API
response = requests.get(URL)

# Concerting the API into a readable JSON format
data = response.json()

# Getting the departments Object Array
departments = data.get('departments', [])

# Creating a callback loop function for the list of jobs under the product department. Then placing the jobs in an object and returning that object as a string.
def productJobs(jobs):
    currentJobs = {}
    for job in jobs:
        currentJobs[(job['title'])] = (job['absolute_url'])
    print(currentJobs)
    return f"Listrak Jobs {currentJobs}"

# Looping over all the departments until it matches the product departments ID. Then passing its data to the callback function above.
for department in departments:
    if department['id'] == 17858:
        body = productJobs(department['jobs'])

# Email Subject
subject = "Current Listrak Product Jobs"

# imported email to create email setup
em = EmailMessage()
em['From'] = os.getenv('emailSender')
em['To'] = os.getenv('emailReceiver')
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(os.getenv('emailSender'), os.getenv('appPassword'))
    smtp.sendmail(os.getenv('emailSender'), os.getenv('emailReceiver'), em.as_string())