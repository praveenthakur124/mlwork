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
        channel_info_file = pd.read_excel(self.input_file)
        data_list = []
        with codecs.open('/home/praveen/Working_files/Facebook_work/Test5.csv', 'a', encoding='utf-8') as output_file:
            csv_writer = csv.writer(output_file)
            # csv_writer.writerow(['Channel ID', 'FB URL', 'FB Username', 'FB Email'])

            for row in channel_info_file.values:
                channel_id = str(row[0])
                print(channel_id)
                data_list.append(channel_id)
                channel_title = str(row[1])
                print(channel_title)
                data_list.append(channel_title)
                channel_view = str(row[2])
                print(channel_view)
                data_list.append(channel_view)
                channel_subs = str(row[3])
                print(channel_subs)
                data_list.append(channel_subs)
                video_count = str(row[4])
                print(video_count)
                data_list.append(video_count)
                language = str(row[5])
                print(language)
                data_list.append(language)
                sub_cat = str(row[6])
                data_list.append(sub_cat)
                contact_id = str(row[7])
                data_list.append(contact_id)
                phone_number = str(row[8])
                data_list.append(phone_number)
                subs_cat = str(row[9])
                data_list.append(subs_cat)
                try:
                    channel_fb_url = row[10]
                    if math.isnan(channel_fb_url):
                        data_list.append(None)
                        data_list.append(None)
                except Exception as e:
                    channel_fb_url = str(row[10])
                    print(e)
                    channel_fb_url = str(channel_fb_url)
                    data_list.append(channel_fb_url)
                    print(channel_fb_url)
                    user = channel_fb_url.split("/")
                    fb_user_name = str(user[3])
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


obj = FbUserEmail("/home/praveen/Working_files/Facebook_work/For fb, contactid, phne number_output.xlsx")
obj.email_extraction()

