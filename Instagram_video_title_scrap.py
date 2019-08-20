import pandas as pd
import requests
import csv
import codecs
import bs4
import re
from time import sleep
from random import randint


class InstagramTitle(object):
    def __init__(self, input_file):
        self.input_file = input_file

    def crawl(self):
        df = pd.read_csv(self.input_file, header=None)

        with codecs.open("/home/praveen/Working_files/Instagram_work/Instagram_title.csv", "a", encoding='utf-8') as output_file:
            csv_writer = csv.writer(output_file)
            data_list = []

            for row in df.values:
                url = str(row[0])
                print(url)
                data_list.append(url)

                try:
                    inp = requests.get(url)
                    resp = inp.text
                    soup = bs4.BeautifulSoup(resp, 'lxml')
                    title = soup.find("meta", property="og:title")
                    title = title.get('content')
                    print(title)
                    data_list.append(title)
                except Exception as e:
                    print(e)
                    data_list.append("")

                try:
                    instagram_regex = r"http[s]?:\/\/[www.]*[instagram]*.com\/[A-z 0-9 _]+\/?"
                    instagram_compile = re.compile(instagram_regex)
                    instagram_search = instagram_compile.search(resp)[0]
                    instagram_user = str(instagram_search)
                    instagram_user = instagram_user.split("/")
                    instagram_user = instagram_user[3]
                    print(instagram_user)
                    data_list.append(instagram_user)
                except Exception as e1:
                    print(e1)
                    data_list.append("")

                csv_writer.writerow(data_list)
                data_list = []
                sleep(randint(2, 4))


obj = InstagramTitle("/home/praveen/Working_files/Instagram_work/Instagram_url_file.csv")
obj.crawl()





