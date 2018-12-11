import pandas as pd
import requests
import csv
import codecs


class ChannelPrediction(object):
    def __init__(self, input_file):
        self.input_file = input_file

    def test_script(self):
        channel_file = pd.read_csv(self.input_file, header=None)

        with codecs.open('/home/praveen/Working_files/Category_Work/channel_cat_predict.csv', 'w', encoding='utf-8') as output_file:
            csv_writer = csv.writer(output_file)
            data_list = []

            for i in channel_file.values:
                channel_id = str(i[0])
                data_list.append(channel_id)
                inp = requests.get('http://api.vidooly.com/getcustomcategory?channelid={}'.format(channel_id))
                resp = inp.json()

                if 'primary' in resp['finalArray']:
                    print(resp['finalArray']['primary'])
                    data_list.append(resp['finalArray']['primary'])
                else:
                    data_list.append("")

                if 'primaryscore' in resp['finalArray']:
                    print(resp['finalArray']['primaryscore'])
                    data_list.append(resp['finalArray']['primaryscore'])
                else:
                    data_list.append("")
                csv_writer.writerow(data_list)
                data_list = []


obj = ChannelPrediction('/home/praveen/Working_files/Category_Work/Australia_channel_ids.csv')
obj.test_script()
