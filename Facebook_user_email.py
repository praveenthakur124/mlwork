import pandas as pd
import csv
import requests
import warnings
import codecs
from time import sleep
from random import randint
import xlrd
import numpy as np
import math

warnings.filterwarnings(action='ignore')


class FbUserEmail(object):
    def __init__(self, input_file):
        self.input_file = input_file

    def email_extraction(self):
        token = 'EAAQuJfslG8ABAB5nUjXj0uOt40xx3gbfKwOZAHvvzoGa87YjrOTaI3mWpS4sdvR0pNXjbLl6mKQUKOfgkZCLZB70dc5a7UaVNt2A0vQJNJ7yV8yn6VhohdlRQlpULDXinssjHs5ZCd86XUJZBH1jduhmB9pEZCwlFnRKwJFXpqpgZDZD'
        channel_info_file = pd.read_csv(self.input_file)
        data_list = []
        with codecs.open('/home/praveen/Working_files/Test1.csv', 'a', encoding='utf-8') as output_file:
            csv_writer = csv.writer(output_file)
            # csv_writer.writerow(['Channel ID', 'FB URL', 'FB Username', 'FB Email'])

            for row in channel_info_file.values:
                try:
                    channel_fb_url = row[0]
                    if math.isnan(channel_fb_url):
                        data_list.append(None)
                        data_list.append(None)
                except Exception as e:
                    print(e)
                    channel_fb_url = str(row[0])
                    # channel_fb_url = str(channel_fb_url)
                    # data_list.append(channel_fb_url)
                    # print(channel_fb_url)
                    # user = channel_fb_url.split("/")
                    # fb_user_name = str(user[3])
                    fb_user_name = channel_fb_url
                    data_list.append(fb_user_name)
                    print(fb_user_name)
                    inp = requests.get("https://graph.facebook.com/v2.12/{}?fields=emails&access_token={}".format(fb_user_name, token))
                    print(inp.status_code)
                    resp = inp.json()

                    if 'emails' in resp:
                        print(resp['emails'])
                        data_list.append(resp['emails'])
                    else:
                        data_list.append(None)
                csv_writer.writerow(data_list)
                data_list = []
                sleep(randint(1, 2))


obj = FbUserEmail("/home/praveen/Working_files/test.csv")
obj.email_extraction()

