import re
import requests
import pandas as pd
import csv
import codecs
from time import sleep
from random import randint
import xlrd


class Blade(object):
    def __init__(self, input_file):
        self.input_file = input_file

    def scraper(self):
        df = pd.read_csv(self.input_file)
        base_url = "https://socialblade.com/youtube/channel/"

        with codecs.open("/home/praveen/Working_files/Sharechat_work/ShareChat_3rd_Cut_output.csv", 'a', encoding='utf-8') as output_file:
            csv_writer = csv.writer(output_file)
            csv_writer.writerow(["Channel ID", "Min. Estimated Monthly Earnings",
                                 "Max. Estimated Monthly Earnings"])
            data_list = []
            count = 1
            for values in df['Channel ID'].values:
                print("count = {}".format(count))
                earn_regex = r'\$\d+ - \$\d+[\.\d+KM]*'
                earn_compile = re.compile(earn_regex)
                channel_id = str(values)
                print(channel_id)
                data_list.append(channel_id)

                try:
                    inp = requests.get(base_url + '{}'.format(channel_id))
                    resp = inp.text

                    result = earn_compile.findall(resp)
                    print(result[0])
                    earn_result = str(result[0])
                    earning = earn_result.split("-")

                    min_earning = str(earning[0])
                    min_earning = re.sub("\$", "", min_earning)
                    min_earning = min_earning.strip()

                    if 'K' in min_earning:
                        val = re.sub("K", "", min_earning)
                        int_val = float(val)
                        int_val = int_val * 1000
                        int_val = int_val + randint(10, 99)
                        print("Min Earning = {}".format(int_val))
                        data_list.append(int_val)
                    else:
                        print("Min Earning = {}".format(min_earning))
                        data_list.append(min_earning)

                    max_earning = str(earning[1])
                    max_earning = re.sub("\$", "", max_earning)
                    max_earning = max_earning.strip()

                    if 'K' in max_earning:
                        value = re.sub("K", "", max_earning)
                        int_value = float(value)
                        int_value = int_value * 1000
                        int_value = int_value + randint(10, 99)
                        print("Max Earning = {}".format(int_value))
                        data_list.append(int_value)
                    else:
                        print("Max Earning = {}".format(max_earning))
                        data_list.append(max_earning)
                    # data_list.append(result[0])

                except Exception as e:
                    data_list.append("")
                    data_list.append("")
                    print(e)
                sleep(randint(1, 2))
                csv_writer.writerow(data_list)
                data_list = []
                count += 1


obj = Blade("/home/praveen/Working_files/Sharechat_work/ShareChat_3rd_Cut.csv")
obj.scraper()
