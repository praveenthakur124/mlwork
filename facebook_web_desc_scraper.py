import bs4
import requests
from scrapy import Selector
import pandas as pd
from random import randint
from time import sleep
import re
import json


class FacebookMoreData(object):
    def __init__(self, input_file):
        self.input_file = input_file

    def scraper(self):
        df = pd.read_csv(self.input_file)
        for idx, row in df['Facebook Page ID'].iteritems():
            print(idx)
            dic = {'id': '', 'about': '', 'products': '', 'web_url': '', 'web_url1': '', 'web_url2': '',
                   'category': ''}
            fb_id = str(row)
            fb_id = fb_id.split("'")
            fb_id = str(fb_id[1])
            print(fb_id)
            dic['id'] = fb_id
            url = "https://www.facebook.com/{}/about/".format(fb_id)
            header = {'accept-language': 'en-US,en;q=0.9'}
            try:
                resp = requests.get(url, headers=header)
                soup = bs4.BeautifulSoup(resp.text, 'html.parser')
                obj_list = soup.find_all('div', {'class': ['_50f4', '_3-8w']})
                for val in obj_list:
                    try:
                        if 'About'.lower() in val.getText().strip().lower():
                            about_data = val.find_next().getText()
                            print(about_data)
                            dic['about'] = about_data
                    except Exception as e:
                        print(e)

                for val1 in obj_list:
                    try:
                        if 'Products'.lower() in val1.getText().strip().lower():
                            product_data = val1.find_next().getText()
                            print(product_data)
                            dic['products'] = product_data
                    except Exception as e:
                        print(e)

                try:
                    data = Selector(text=resp.text)
                    web_url = data.xpath('//*[@id="u_0_p"]/div')
                    web_url = web_url.get('data')
                    web_url = str(web_url)
                    web_url = web_url.split(">")
                    web_url = str(web_url[1])
                    web_url = web_url.split("<")
                    web_url = web_url[0]
                    print(web_url)
                    dic['web_url'] = web_url
                except Exception as e:
                    print(e)

                try:
                    data1 = Selector(text=resp.text)
                    web_url1 = data1.xpath('//*[@id="u_0_q"]/div')
                    web_url1 = web_url1.get('data')
                    web_url1 = str(web_url1)
                    web_url1 = web_url1.split(">")
                    web_url1 = str(web_url1[1])
                    web_url1 = web_url1.split("<")
                    web_url1 = web_url1[0]
                    print(web_url1)
                    dic['web_url1'] = web_url1
                except Exception as e:
                    print(e)

                try:
                    data2 = Selector(text=resp.text)
                    web_url2 = data2.xpath('//*[@id="u_0_o"]/div')
                    web_url2 = web_url2.get('data')
                    web_url2 = str(web_url2)
                    web_url2 = web_url2.split(">")
                    web_url2 = str(web_url2[1])
                    web_url2 = web_url2.split("<")
                    web_url2 = web_url2[0]
                    print(web_url2)
                    dic['web_url2'] = web_url2
                except Exception as e:
                    print(e)

                try:
                    category_regex = r'\/pages\/category\/[0-9A-z-]+'
                    regex_compile = re.compile(category_regex)
                    search_category = regex_compile.findall(resp.text)[0]
                    search_category = str(search_category)
                    search_category = search_category.split("/")
                    search_category = str(search_category[3])
                    print(search_category)
                    dic['category'] = search_category
                except Exception as e:
                    print(e)
            except Exception as e:
                print(e)

            sleep(randint(5, 8))
            with open('/home/praveen/Working_files/Social_bakers_collection/Indian_top_facebook_brand_output.json', 'a') as output:
                json.dump(dic, output)
                output.write('\n')


obj = FacebookMoreData("/home/praveen/Working_files/Social_bakers_collection/Indian_top_facebook_brand.csv")
obj.scraper()
