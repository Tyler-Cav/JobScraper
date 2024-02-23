import requests
import smtplib

URL = "https://boards-api.greenhouse.io/v1/boards/listrak/departments"
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
    