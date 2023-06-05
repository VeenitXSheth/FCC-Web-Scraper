import requests
from bs4 import BeautifulSoup
import csv

station_coords = []

with open("station.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            url = (
                "https://transition.fcc.gov/fcc-bin/tvq?call="
                + str(row[1])
                + "&fileno=&state=&city=&chan=0.0&cha2=51&serv=&type=&facid=&asrn=&list=0&dist=&dlat2=&mlat2=&slat2=&NS=N&dlon2=&mlon2=&slon2=&EW=W&size=9&NextTab=Results+to+Next+Page%2FTab"
            )

            requests_session = requests.Session()

            r = requests_session.get(url)

            soup = BeautifulSoup(r.content, "lxml")

            def scrape():
                print("a scrape has started!")
                coordinates = soup.find("td", class_="listtext")
                print(coordinates.text)
                station_coords.append(coordinates.text)

            scrape()

# KAAH is the first station with records
