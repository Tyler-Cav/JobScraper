import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
jobElements = results.find_all('div', class_="card-content")

for jobElement in jobElements:
    title_element = jobElement.find("h2", class_="title")
    company_element = jobElement.find("h3", class_="company")
    location_element = jobElement.find("p", class_="location")
    print('Title: ' + title_element.text)
    print('Company: ' + company_element.text)
    print('Location: ' + location_element.text.strip())
    print()
    print('------------')
    print()