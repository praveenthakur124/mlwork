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
        with codecs.open('/home/praveen/Working_files/Category_Work/Australia_channel_category_test.csv', 'w', encoding='utf-8') as ouput_file:
            csv_writer = csv.writer(ouput_file)
            for row in meta_file.values:
                channel_id = str(row[0])
                print(channel_id)
                data_list.append(channel_id)
                video_id = str(row[1])
                print(video_id)
                data_list.append(video_id)
                video_title = str(row[4])
                print(video_title)
                # data_list.append(video_title)
                video_desc = str(row[5])
                print(video_desc)
                # data_list.append(video_desc)
                video_tags = str(row[6])
                print(video_tags)
                # data_list.append(video_tags)

                if math.isnan(row[3]):
                    data_list.append("Nan")
                else:
                    cat_int = int(row[3])
                    video_cat_id = str(cat_int)
                    for k, v in youtube_category_dict.items():
                        if video_cat_id in k:
                            print(v)
                            data_list.append(v)

                description = video_title.strip() + video_desc.strip() + video_tags.strip()
                api_url = 'http://180.151.75.164:8080/ml/result/genre_classification'
                data = {'method': 'newcategory', 'description': description}
                try:
                    inp = requests.post(api_url, data=data)
                    print(inp.status_code)
                    resp = inp.json()
                    print(resp['status'])
                    if 'result1' in resp:
                        print(resp['result1'])
                        data_list.append(resp['result1'])
                    else:
                        data_list.append("")
                    if 'result2' in resp:
                        print(resp['result2'])
                        data_list.append(resp['result2'])
                    else:
                        data_list.append("")
                    if 'result3' in resp:
                        print(resp['result3'])
                        data_list.append(resp['result3'])
                    else:
                        data_list.append("")
                    if 'desc_func1' in resp:
                        print(resp['desc_func1'])
                        data_list.append(resp['desc_func1'])
                    else:
                        data_list.append("")
                    if 'desc_func2' in resp:
                        print(resp['desc_func2'])
                        data_list.append(resp['desc_func2'])
                    else:
                        data_list.append("")
                    if 'desc_func3' in resp:
                        print(resp['desc_func3'])
                        data_list.append(resp['desc_func3'])
                    else:
                        data_list.append("")
                    if 'miss_vocab' in resp:
                        print(resp['miss_vocab'])
                        data_list.append(resp['miss_vocab'])
                    else:
                        data_list.append("")
                    if 'text' in resp:
                        print(resp['text'])
                        data_list.append(resp['text'])
                    else:
                        data_list.append("")
                    if 'confidence' in resp:
                        print(resp['confidence'])
                        data_list.append(resp['confidence'])
                    else:
                        data_list.append("")
                    if 'total_words' in resp:
                        print(resp['total_words'])
                        data_list.append(resp['total_words'])
                    else:
                        data_list.append("")
                    if 'language_barrier' in resp:
                        print(resp['language_barrier'])
                        data_list.append(resp['language_barrier'])
                    else:
                        data_list.append("")
                except Exception as e:
                    print(e)
                csv_writer.writerow(data_list)
                data_list = []


obj = CategoryTest('/home/praveen/Working_files/Category_Work/Australia_channel_meta.csv')
obj.api_test_category()



