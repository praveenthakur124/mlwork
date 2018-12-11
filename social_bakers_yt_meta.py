import requests
import csv
import codecs
import re
from time import sleep
from random import randint


class SocialTwitter(object):

    def scraper(self):
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

        with codecs.open("/home/praveen/Working_files/Social_bakers_collection/indo_yt_data.csv", "a", encoding='utf-8') as output_file:
            csv_writer = csv.writer(output_file)
            twitter_regex = r'\/statistics\/youtube\/channels\/detail\/[A-z0-9\-]+'
            data_list = []

            for cat in category_list:
                category = str(cat)
                page_url = "https://www.socialbakers.com/statistics/youtube/channels/indonesia/{}/page-1-5/".format(category)
                try:
                    inp = requests.get(page_url)
                    resp = inp.text

                    regex_compile = re.compile(twitter_regex)
                    regex_search = regex_compile.findall(resp)

                    for row in regex_search:
                        print('Indonesia')
                        data_list.append('Indonesia')
                        print(str(row))
                        data_list.append(str(row))
                        print(category)
                        data_list.append(category)
                        csv_writer.writerow(data_list)
                        data_list = []
                    sleep(randint(2, 4))
                except Exception as e:
                    print(e)


obj = SocialTwitter()
obj.scraper()
