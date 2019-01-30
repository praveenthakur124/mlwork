import pandas as pd
import csv
import requests
import codecs


class FoodDetection(object):
    def __init__(self, input_file):
        self.input_file = input_file

    def tags_to_text(self, y):
        try:
            return " ".join(eval(y))
        except Exception as e:
            return ""

    def api_crawl(self):

        df = pd.read_csv(self.input_file, header=None)
        base_url = "http://ds.vidooly.com/result/food_topics"

        with codecs.open("/home/praveen/Working_files/food_test.csv", "a", encoding='utf-8') as output_file:
            csv_writer = csv.writer(output_file)
            csv_writer.writerow(['Text', 'Result'])
            data_list = []

            for row in df.values[:5]:
                title = str(row[4])
                desc = str(row[5])
                tags = row[6]
                tags = self.tags_to_text(tags)
                tags = str(tags)

                final_desc = title.strip() + " " + desc.strip() + " " + tags.strip()
                data = {'description': final_desc}

                try:
                    inp = requests.post(base_url, data=data)
                    resp = inp.json()

                    if 'text' in resp:
                        print(resp['text'])
                        data_list.append(resp['text'])
                    else:
                        data_list.append("")

                    if 'result' in resp:
                        print(resp['result'])
                        data_list.append(resp['result'])
                    else:
                        data_list.append("")

                except Exception as e1:
                    print(e1)
                    data_list.append("")
                    data_list.append("")

                csv_writer.writerow(data_list)
                data_list = []


obj = FoodDetection("/home/praveen/Working_files/Category_Work/Australia_channel_meta.csv")
obj.api_crawl()


