import requests
import pandas as pd
import codecs
import csv


class KeywordTesting(object):

    def __init__(self, input_file):
        self.input_file = input_file

    def api_request(self):
        df = pd.read_csv(self.input_file)
        api_url = 'http://192.168.100.25/ml/result/topic_keyword_mapper'
        with codecs.open("/home/praveen/Working_files/Topic_Work/Food_file_keyword_result.csv", 'a', encoding='utf-8') as output_file:
            csv_writer = csv.writer(output_file)
            for row in df.values:
                data_list = list()
                video_title = str(row[2])
                video_desc = str(row[3])
                video_tags = row[4]
                final_desc = str(video_title) + " " + str(video_desc) + " " + str(video_tags)
                data_list.append(final_desc)
                data = {'title': video_title, 'description': video_desc, 'tags': video_tags}
                inp = requests.post(api_url, data=data)
                resp = inp.json()
                print(resp)

                if 'result' in resp:
                    for i in resp['result']:
                        data_list.append(i)

                else:
                    data_list.append(None)
                csv_writer.writerow(data_list)


obj = KeywordTesting("/home/praveen/Working_files/Topic_Work/Food_file_keyword.csv")
obj.api_request()

