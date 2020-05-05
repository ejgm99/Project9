from selenium import webdriver
import csv
import time
#
# driver=webdriver.Chrome()
# place_url="https://www.google.com/maps/search/?api=1&query="
#
# with open('restaurants.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter='|')
#     for row in csv_reader:
#         print("Searching for: ", row[0], " at ",row[1])
#         row=row[0].strip().replace("#","")+" "+row[1].strip()
#         row=row.split(" ")
#         search_query = "%s" % '+'.join([i for i in row if len(i)>0])
#         print("using url: "+place_url+search_query)
#         driver.get(place_url+search_query)
#         time.sleep(5)
#         elements = driver.find_elements("css selector",'button.widget-pane-link')
#         for elem in elements:
#             if len(elem.text)>5:
#                 print("Category: ",elem.text)
#                 print(driver.current_url)
#                 url=driver.current_url
#                 coordinates = [i for i in url.split('/') if i.find("@")==0][0].split(",")
#                 print(coordinates[0][1:],coordinates[1])

class GoogleMapsParser:#this class handles the upload of a csv while iterating through it
    def __init__(self):
        #user = input("Username: ")
        #secret = getpass.getpass()
        self.driver = driver=webdriver.Chrome()
        self.base_url = "https://www.google.com/maps/search/?api=1&query="
    def createQuery(self, row):
        self.current_name=row[0].strip()
        self.current_address=row[1].strip()
        row=row[0].strip().replace("#","")+" "+row[1].strip()
        row=row.split(" ")
        self.search_query = "%s" % '+'.join([i for i in row if len(i)>0])
        print(self.search_query)
    def SearchMap(self):
        self.driver.get(self.base_url+self.search_query)
        time.sleep(5)
        elements = self.driver.find_elements("css selector",'button.widget-pane-link')
        for elem in elements:
            if len(elem.text)>5: #only return actual values here since a category was found
                category=elem.text
                # print(self.driver.current_url)
                url=self.driver.current_url
                coordinates = [i for i in url.split('/') if i.find("@")==0][0].split(",")
                latitude = coordinates[0][1:]
                longitude = coordinates[1]
                star_rating = self.driver.find_elements("css selector",'span.section-star-display')[0].text
                print(self.current_name,self.current_address, category, latitude, longitude)

g= GoogleMapsParser()

with open('restaurants.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='|')
    for row in csv_reader:
        g.createQuery(row)
        g.SearchMap()
