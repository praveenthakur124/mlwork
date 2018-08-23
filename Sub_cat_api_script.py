import requests
import pandas as pd
import warnings
import codecs
import math
import csv

warnings.filterwarnings(action='ignore')


class CategoryTest(object):
    def __init__(self, input_file):
        self.input_file = input_file

    def api_test_category(self):
        data_list = []
        youtube_category_dict = {'1': 'Film & Animation',
                                 '2': 'Autos & Vehicles',
                                 '10': 'Music',
                                 '15': 'Pets & Animals',
                                 '17': 'Sports',
                                 '18': 'Short Movies',
                                 '19': 'Travel & Events',
                                 '20': 'Gaming',
                                 '21': 'Videoblogging',
                                 '22': 'People & Blogs',
                                 '23': 'Comedy',
                                 '24': 'Entertainment',
                                 '25': 'News & Politics',
                                 '26': 'How & Style',
                                 '27': 'Education',
                                 '28': 'Science & Technology',
                                 '29': 'Nonprofit & activism',
                                 '30': 'Movies',
                                 '31': 'Anime/Animation',
                                 '32': 'Action/Adventure',
                                 '33': 'Classics',
                                 '34': 'Comedy',
                                 '35': 'Documentary',
                                 '36': 'Drama',
                                 '37': 'Family',
                                 '38': 'Foreign',
                                 '40': 'Sci-Fi/Fantasy',
                                 '41': 'Thriller',
                                 '42': 'Shorts',
                                 '43': 'Shows',
                                 '44': 'Trailers',
                                 'nan': ''
                                 }
        meta_file = pd.read_csv(self.input_file, header=None)
        with codecs.open('/home/praveen/Working_files/Category_Work/sub_cat_api_result.csv', 'w', encoding='utf-8') as ouput_file:
            csv_writer = csv.writer(ouput_file)
            for row in meta_file.values:
                video_id = str(row[2])
                print(video_id)
                data_list.append(video_id)
                video_title = str(row[5])
                print(video_title)
                # data_list.append(video_title)
                video_desc = str(row[6])
                print(video_desc)
                # data_list.append(video_desc)
                video_tags = str(row[7])
                print(video_tags)
                # data_list.append(video_tags)

                if math.isnan(row[4]):
                    data_list.append('Nan')
                else:
                    cat_int = int(row[4])
                    video_cat_id = str(cat_int)
                    for k, v in youtube_category_dict.items():
                        if video_cat_id in k:
                            print(v)
                            data_list.append(v)

                description = video_title.strip() + video_desc.strip() + video_tags.strip()
                api_url = 'http://180.151.75.164:8080/ml/result/genre_classification?description={}'.format(description)
                try:
                    inp = requests.get(api_url)
                    print(inp.status_code)
                    resp = inp.json()
                    print(resp['status'])
                    if 'result' in resp:
                        print(resp['result'])
                        data_list.append(resp['result'])
                except Exception as e:
                    print(e)
                csv_writer.writerow(data_list)
                data_list = []


obj = CategoryTest('/home/praveen/Working_files/Category_Work/shuffle_cat_channel_meta.csv')
obj.api_test_category()



