import pandas as pd
import requests
import csv
import codecs


class Topic(object):
    def __init__(self, input_file):
        self.input_file = input_file

    def scraper(self):
        df = pd.read_csv(self.input_file, header=None)
        base_url = "http://180.151.75.164:8080/ml/result/food_modeling?description="

        with codecs.open("/home/praveen/Working_files/Topic_Work/Indian_food_text_result.csv", "a", encoding="utf-8") as output_file:
            csv_writer = csv.writer(output_file)
            data_list = []
            count = 1

            for row in df.values:
                print("count = {}".format(count))
                desc = str(row[4])
                url = "{}{}".format(base_url, desc)

                try:

                    inp = requests.get(url)
                    resp = inp.json()
                    print(resp['status'])

                    if 'text' in resp:
                        # print(resp['text'])
                        data_list.append(resp['text'])
                    else:
                        data_list.append("")

                    if 'result' in resp:
                        # print(resp['result'])
                        # print(resp['result'])
                        data_list.append(resp['result'])
                    else:
                        data_list.append("")

                    csv_writer.writerow(data_list)
                    data_list = []

                except Exception as e:
                    print(e)
                count = count + 1


obj = Topic("/home/praveen/Working_files/Topic_Work/Indian_dishes_file.csv")
obj.scraper()



