import os
import requests
import smtplib
from dotenv import load_dotenv, dotenv_values
load_dotenv()

URL = os.getenv('MY_SECRET_URL')

response = requests.get(URL)

data = response.json()

departments = data.get('departments', [])

def productJobs(jobs):
    for job in jobs:
        print()
        print(job['title'])
        print(job['absolute_url'])
        print()
        print('---')
        
for department in departments:
    if department['id'] == 17858:
        productJobs(department['jobs'])


print(os.getenv('MY_SECRET_NAME'))