import pandas as pd
import bs4
import requests
from time import sleep
from random import randint
import csv
import codecs


class TwitterData(object):
    def __init__(self, input_file):
        self.input_file = input_file

    def scraper(self):
        df = pd.read_csv(self.input_file)
        # country_list = list(df['Country'])
        # category_list = list(df['Category'])
        # profile_url_list = list(df['Twitter Profile URL'])
        # id_list = list(df['Twitter ID'])
        # # name_list = list(df['Twitter Name'])
        # handle_list = list(df['Twitter Handle'])
        # status_list = list(df['Verification Status'])
        # tags_list = list(df['Tags (Comma separated)'])
        # twitter_profile_name_list = list()
        # twitter_profile_website_list = list()
        with codecs.open("/home/praveen/Working_files/Top_indian_twitter_brand.csv", 'a', encoding='utf-8') as output_file:
            csv_writer = csv.writer(output_file)
            data_list = list()
            for val in df['Twitter Handle'].values:
                # country = str(val[0])
                # data_list.append(country)
                # category = str(val[1])
                # data_list.append(category)
                # profile = str(val[2])
                # data_list.append(profile)
                # twitter_id = str(val[3])
                # data_list.append(twitter_id)
                # handle = str(val)
                # data_list.append(handle)
                # status = str(val[6])
                # data_list.append(status)
                # tags = str(val[7])
                # data_list.append(tags)

                try:
                    handle = str(val)
                    print(handle)
                    data_list.append(handle)
                    url = "https://twitter.com/{}".format(handle)
                    print(url)
                    inp = requests.get(url)
                    resp = inp.text
                    soup = bs4.BeautifulSoup(resp, 'lxml')
                    name = soup.find('a', {'class': 'ProfileHeaderCard-nameLink u-textInheritColor js-nav'}).getText()
                    name = str(name)
                    twitter_profile_name = name.strip()
                    data_list.append(twitter_profile_name)
                    print(twitter_profile_name)
                    website = soup.find('a', {'class': 'u-textUserColor', 'rel': 'me nofollow noopener'}).getText()
                    website = str(website)
                    twitter_profile_website = website.strip()
                    data_list.append(twitter_profile_website)
                    print(twitter_profile_website)
                except Exception as e:
                    print(e)
                csv_writer.writerow(data_list)
                data_list = []
                sleep(randint(2, 4))
        # print(twitter_profile_name_list)
        # print(twitter_profile_website_list)

        # df1 = pd.DataFrame({'Country': country_list, 'Category': category_list,
        #                     'Twitter Profile URL': profile_url_list, 'Twitter ID': id_list,
        #                     'Twitter Name': twitter_profile_name_list, 'Twitter Handle': handle_list,
        #                     'Verification Status': status_list, 'Tags (Comma separated)': tags_list,
        #                     'Website URL': twitter_profile_website_list}, columns=['Country',
        #                                                                            'Category',
        #                                                                            'Twitter Profile URL',
        #                                                                            'Twitter ID',
        #                                                                            'Twitter Name',
        #                                                                            'Twitter Handle',
        #                                                                            'Verification Status',
        #                                                                            'Tags (Comma separated)',
        #                                                                            'Website URL'])
        # df1 = pd.DataFrame({'Twitter handle': handle_list, 'Twitter Name': twitter_profile_name_list,
        #                     'Website URL': twitter_profile_website_list})

        # df1.to_csv('/home/praveen/Working_files/Top_indian_twitter_brand.csv')


obj = TwitterData('/home/praveen/Working_files/Social_bakers_collection/Indian_top_twitter_brand1.csv')
obj.scraper()
