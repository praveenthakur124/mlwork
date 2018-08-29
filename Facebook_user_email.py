import pandas as pd
import csv
import requests
import warnings
import codecs

warnings.filterwarnings(action='ignore')


class FbUserEmail(object):
    def __init__(self, input_file):
        self.input_file = input_file

    def email_extraction(self):
        token = 'EAAYTfjYsYEcBAK0LergGApzc8Ixw3A64lS1XavK8qAul1N4rIU4VGDGZCr2t34223oaPe7yAqnfB6U9WLjk2EdEjKoDYDTBS37fy3IQM7EO96cEOcZCawzEDVNIOAosrfBdk3wZClBdKNOTjfJL4fZBiTuRmdJsYMidURZBo87kMoYpjtV62M4ZBHzt7w0sIqzdJwvZBA4FXgZDZD'
        channel_info_file = pd.read_csv(self.input_file, header=None)
        data_list = []
        with codecs.open('/home/praveen/Working_files/Channel_Data_collection_Work/Korean_email_extraction.csv', 'w', encoding='utf-8') as output_file:
            csv_writer = csv.writer(output_file)

            for row in channel_info_file.values:
                channel_id = str(row[0])
                print(channel_id)
                data_list.append(channel_id)
                channel_title = str(row[1])
                print(channel_title)
                data_list.append(channel_title)
                channel_view = str(row[2])
                print(channel_view)
                data_list.append(channel_view)
                channel_subs = str(row[3])
                print(channel_subs)
                data_list.append(channel_subs)
                channel_cat = str(row[8])
                print(channel_cat)
                data_list.append(channel_cat)
                channel_fb_url = str(row[9])
                if channel_fb_url == " ":
                    data_list.append(None)
                else:
                    user = channel_fb_url.split("/")
                    fb_user_name = str(user[3])
                    data_list.append(fb_user_name)
                    print(fb_user_name)
                    try:
                        inp = requests.get("https://graph.facebook.com/v2.12/{}?fields=emails&access_token={}".format(fb_user_name, token))
                        print(inp.status_code)
                        resp = inp.json()

                        if 'emails' in resp:
                            print(resp['emails'])
                            data_list.append(resp['emails'])
                        else:
                            data_list.append(None)
                    except Exception as e:
                        print(e)
                csv_writer.writerow(data_list)
                data_list = []


obj = FbUserEmail("/home/praveen/Working_files/Channel_Data_collection_Work/channelinfo (29).csv")
obj.email_extraction()

