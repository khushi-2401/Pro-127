from selenium import webdriver
from bs4 import BeautifulSoup
import time 
import csv

start_url="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("Chromedriver.exe")
browser.get(start_url)
time.sleep(100)

def scrapper():
    headers=["name","distance","mass","radius"]
    star_data=[]
    for i in range(0,1):
        bs=BeautifulSoup(browser.page_source,"html.parser")
        for j in bs.find_all("ul",attrs={"class","exoplanet"}):
            li_tags = j.find_all("li")
            temp_list=[]
            
            for index,k in enumerate(li_tags):
                if index==0:
                    temp_list.append(k.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(k.contents[0])
                    except:
                        temp_list.append("")
            star_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("data.csv","w") as f:
        writer=csv.writer(f)
        writer.writerow(headers)
        writer.writerows(star_data)
        writer.writerow("")

scrapper()