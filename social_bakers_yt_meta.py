import requests
import re
import pandas as pd
from time import sleep
from random import randint


class SocialTwitter(object):
    def separator(self, input_dataframe):
        input_file = input_dataframe
        country_list = list(input_file['Country'])
        url_list = list(input_file['YT URL'])
        category_list = list(input_file['Category'])
        channel_id_list = list()
        username_list = list()
        for url in url_list:
            url = str(url)
            url = url.split("/")
            url = url[5]
            url_id = str(url[:24])
            channel_id_list.append(url_id)
            try:
                url_name = str(url[25:])
                url_name = url_name.strip()
                username_list.append(url_name.capitalize())
            except Exception as e:
                username_list.append(None)
        frame = pd.DataFrame({'Country': country_list, 'Category': category_list, 'YT URL': url_list,
                              'Channel ID': channel_id_list, 'UserName': username_list}, columns=['Country',
                                                                                                  'Category', 'YT URL',
                                                                                                  'Channel ID',
                                                                                                  'UserName'])
        output_dataframe = frame
        return output_dataframe

    def scraper(self):
        pagination_list = ['', 'page-1-2', 'page-1-3', 'page-1-4', 'page-1-5', 'page-2-6',
                           'page-3-7', 'page-4-8', 'page-5-9', 'page-6-10', 'page-7-11', 'page-8-12',
                           'page-9-13', 'page-10-14', 'page-11-15', 'page-12-16', 'page-13-17',
                           'page-14-18', 'page-15-19', 'page-16-20', 'page-17-21', 'page-18-22',
                           'page-19-23', 'page-20-24', 'page-21-25', 'page-22-26', 'page-23-27',
                           'page-24-28', 'page-25-29', 'page-26-30', 'page-27-31', 'page-28-32',
                           'page-29-33', 'page-30-34', 'page-31-35', 'page-32-36', 'page-33-37',
                           'page-34-38', 'page-35-39', 'page-36-40', 'page-37-41', 'page-38-42',
                           'page-39-43', 'page-40-44', 'page-41-45', 'page-42-46', 'page-43-47',
                           'page-44-48', 'page-45-49', 'page-46-50', 'page-47-51', 'page-48-52',
                           'page-49-53', 'page-50-54', 'page-51-55', 'page-52-56', 'page-53-57',
                           'page-54-58', 'page-55-59', 'page-56-60', 'page-57-61', 'page-58-62',
                           'page-59-63', 'page-60-64', 'page-61-65', 'page-62-66', 'page-63-67',
                           'page-64-68', 'page-65-69', 'page-66-70', 'page-67-71', 'page-68-72',
                           'page-69-73', 'page-70-74', 'page-71-75', 'page-72-76', 'page-73-77',
                           'page-74-78', 'page-75-79', 'page-76-80', 'page-77-81', 'page-78-82',
                           'page-79-83', 'page-80-84', 'page-81-85', 'page-82-86', 'page-83-87',
                           'page-84-88', 'page-85-89', 'page-86-90', 'page-87-91', 'page-88-92',
                           'page-89-93', 'page-90-94', 'page-91-95', 'page-92-96', 'page-93-97',
                           'page-94-98', 'page-95-99', 'page-96-100']

        category_list = ['brands/accommodation', 'brands/airlines', 'brands/alcohol/beer',
                         'brands/alcohol/spirits', 'brands/alcohol/wine', 'brands/auto/cars',
                         'brands/beauty', 'brands/beverages/coffee-tea',
                         'brands/beverages/soft-drink', 'brands/beverages/water',
                         'brands/conglomerate', 'brands/ecommerce/crowdfunding',
                         'brands/ecommerce/e-shop', 'brands/ecommerce/paid-music-video',
                         'brands/ecommerce/travel-booking', 'brands/electronics/appliance',
                         'brands/electronics/audio', 'brands/electronics/camera',
                         'brands/electronics/computer', 'brands/electronics/gaming-console',
                         'brands/electronics/phone', 'brands/fmcg-corporate',
                         'brands/fmcg-food/baby-food', 'brands/fmcg-food/confectionery',
                         'brands/fmcg-food/dairy', 'brands/fashion/accessories',
                         'brands/fashion/clothing', 'brands/fashion/jewelry',
                         'brands/finance/bank', 'brands/finance/insurance',
                         'brands/finance/payment', 'brands/gambling',
                         'brands/healthcare/medical-product', 'brands/home-living/children',
                         'brands/home-living/furniture', 'brands/home-living/home-maintenance',
                         'brands/home-living/toys-games', 'brands/home-living/utensils',
                         'brands/household-goods/chemicals', 'brands/household-goods/hygiene',
                         'brands/household-goods/pets', 'brands/household-goods/stationery',
                         'brands/industrial', 'brands/retail/auto-dealership',
                         'brands/retail/beauty-drug-stores', 'brands/retail/electronics-retailers',
                         'brands/retail/fashion-retailers', 'brands/retail/hypermarkets-supermarkets',
                         'brands/retail/sporting-goods-retailers', 'brands/retail-food',
                         'brands/services/agency', 'brands/services/housing',
                         'brands/services/mail-shipping', 'brands/services/transportation',
                         'brands/services/wellness', 'brands/software/game-developer',
                         'brands/software/programs', 'brands/sporting-goods', 'brands/telecom',
                         'celebrities/actor', 'celebrities/artist', 'celebrities/broadcast-star',
                         'celebrities/disc-jockey', 'celebrities/fashion-star', 'celebrities/musician',
                         'celebrities/singer', 'celebrities/writer', 'community/auto-interest',
                         'community/culture', 'community/film', 'community/fun', 'community/hobbies',
                         'community/life-style', 'community/music', 'community/personal',
                         'community/political', 'community/religion', 'community/sport-interest',
                         'community/wikipedia', 'entertainment/apps', 'entertainment/books',
                         'entertainment/broadcast-show', 'entertainment/computer-game',
                         'entertainment/event', 'entertainment/fictional-character',
                         'entertainment/film-music-industry/cinemas', 'entertainment/film-music-industry/movies',
                         'entertainment/film-music-industry/music-instruments',
                         'entertainment/film-music-industry/production-companies', 'entertainment/online-show',
                         'media/daily-news', 'media/magazines-journals/entertainment-news',
                         'media/media-house', 'media/radio-media', 'media/social-media', 'media/sports-media',
                         'media/tv-channels', 'media/web-portal', 'place/airport', 'place/city',
                         'place/country', 'place/cultural-center', 'place/medical-center', 'place/night-life',
                         'place/restaurant-cafe', 'place/shopping-center', 'society/csr', 'society/conference',
                         'society/education/university', 'society/governmental', 'society/ngo',
                         'society/politics', 'society/professional-association', 'society/science',
                         'sport/sport-club', 'sport/sport-event', 'sport/sport-organization']

        yt_regex = r'\/statistics\/youtube\/channels\/detail\/[A-z0-9\-]+'
        channel_id_list = list()
        country_name_list = list()
        cat_name_list = list()

        for cat in category_list:
            category = str(cat)

            for pagination in pagination_list[:5]:
                page_no = str(pagination)
                page_url = "https://www.socialbakers.com/statistics/youtube/channels/indonesia/{}/{}/".format(category, page_no)
                try:
                    inp = requests.get(page_url)
                    resp = inp.text

                    regex_compile = re.compile(yt_regex)
                    regex_search = regex_compile.findall(resp)

                    for row in regex_search:
                        print('Indonesia')
                        country_name_list.append('Indonesia')
                        print(cat)
                        cat_name_list.append(cat)
                        print(str(row))
                        channel_id_list.append(str(row))
                        print(category)
                except Exception as e:
                    print(e)
                    sleep(randint(1, 2))

        df = pd.DataFrame({'Country': country_name_list, 'YT URL': channel_id_list,
                           'Category': cat_name_list}, columns=['Country', 'YT URL',
                                                                'Category'])
        df1 = df.drop_duplicates(subset='YT URL')
        df1 = self.separator(df1)
        df1.to_csv("/home/praveen/Working_files/test_output.csv")


obj = SocialTwitter()
obj.scraper()
