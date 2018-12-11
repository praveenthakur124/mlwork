import requests
import csv
import pandas as pd
from time import sleep
from random import randint
import codecs
import re


class InstagramId(object):
    def __init__(self, input_file):
        self.input_file = input_file

    def scraper(self):
        df = pd.read_csv(self.input_file)
        userfile = df[df['Instagram User'].notnull()]

        with codecs.open("/home/praveen/Working_files/instagram_unique_id.csv", "a", encoding="utf-8") as output_file:
            csv_writer = csv.writer(output_file)
            data_list = []
            for user in userfile['Instagram User'].values:
                username = str(user)
                print(username)
                data_list.append(username)
                id_regex = r"profilePage_[0-9]+"
                try:
                    inp = requests.get("https://www.instagram.com/{}/".format(username))
                    resp = inp.text
                    regex_compile = re.compile(id_regex)
                    regex_search = regex_compile.findall(resp)
                    regex_search = str(regex_search)
                    ins_id = re.sub("[A-z\-]+", "", regex_search)
                    print(ins_id)
                    data_list.append(ins_id)
                    csv_writer.writerow(data_list)
                    data_list = []
                    sleep(randint(1, 3))
                except Exception as e:
                    print(e)


obj = InstagramId("/home/praveen/Working_files/input_file.csv")
obj.scraper()
