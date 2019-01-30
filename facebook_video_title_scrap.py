import csv
import codecs
import pandas as pd
import bs4
import requests
from random import randint
from time import sleep


class FacebookTitle(object):
    def __init__(self, input_file):
        self.input_file = input_file

    def crawl(self):
        df = pd.read_csv(self.input_file, header=None)

        with codecs.open("/home/praveen/Working_files/Facebook_work/fb_title.csv", "a", encoding='utf-8') as output_file:
            csv_writer = csv.writer(output_file)
            data_list = []

            for row in df.values:
                url = str(row[0])
                print(url)
                data_list.append(url)
                try:
                    inp = requests.get(url)
                    resp = inp.content
                    soup = bs4.BeautifulSoup(resp, 'lxml')
                    title = soup.find('title', {'id': 'pageTitle'}).getText()
                    title = str(title)
                    title_split = title.split("-")
                    publish = title_split[0]
                    data_list.append(publish)
                    print(publish)
                    original_title = " ".join(title_split[1:])
                    data_list.append(original_title)
                    print(original_title)
                except Exception as e:
                    data_list.append("")
                    print(e)
                csv_writer.writerow(data_list)
                data_list = []
                # sleep(randint(1, 2))


obj = FacebookTitle("/home/praveen/Working_files/Facebook_work/facebook_title_scrap.csv")
obj.crawl()

