import pandas as pd
import warnings
import csv
import codecs
import requests
warnings.filterwarnings(action='ignore')


class MetaData(object):
    def __init__(self, input_file, api_key):
        self.input_file = input_file
        self.api_key = api_key

    def crawling(self):
        with codecs.open('/home/praveen/Working_files/test.csv', 'a', encoding='utf-8') as output_file:
            csv_writer = csv.writer(output_file)
            channel_id_file = pd.read_csv(self.input_file, header=None)

            for channel in channel_id_file.values[:12]:
                channel_id = str(channel[0])

                base_video_url = 'https://www.youtube.com/watch?v='
                base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

                first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=50'.format(self.api_key, channel_id)
                url = first_url
                videos_link = []

                while True:
                    try:
                        inp = requests.get(url)
                        resp = inp.json()
                    except Exception as e:
                        print(e)

                    for i in resp['items']:
                        if i['id']['kind'] == 'youtube#video':
                            videos_link.append(i['id']['videoId'])  # append videos id corresponding to a channel id
                            # Fetch video id meta data call video id one by one from video link list
                        for video_id in videos_link:
                            meta_list = []

                            # create url to get video meta data
                            url_video = "https://www.googleapis.com/youtube/v3/videos?part=id%2C+snippet&id={}&key={}".format(video_id, self.api_key)
                            try:
                                inp1 = requests.get(url_video)  # requests on video meta api
                                video_resp = inp1.json()  # assign video api json to video_resp variable

                                for j in video_resp['items']:
                                    if j['kind'] == 'youtube#video':  # checking kind is equal to given string
                                        if 'channelId' in j['snippet']:
                                            print(video_id, j['snippet']['channelId'])
                                            meta_list.append(j['snippet']['channelId'])  # append video belonging channel id
                                        else:
                                            meta_list.append("")
                                        print(video_id)
                                        meta_list.append(video_id)
                                        if 'channelTitle' in j['snippet']:
                                            print(video_id, j['snippet']['channelTitle'])
                                            meta_list.append(j['snippet']['channelTitle'])  # append video channel title in list
                                        else:
                                            meta_list.append("")
                                        if 'categoryId' in j['snippet']:
                                            print(video_id, j['snippet']['categoryId'])
                                            meta_list.append(j['snippet']['categoryId'])  # append video categoryId in list
                                        else:
                                            meta_list.append("")
                                        if 'title' in j['snippet']:
                                            print(video_id, j['snippet']['title'])
                                            meta_list.append(j['snippet']['title'])  # append video title in list
                                        else:
                                            meta_list.append("")
                                        if 'description' in j['snippet']:
                                            print(video_id, j['snippet']['description'])
                                            meta_list.append(j['snippet']['description'])  # append video description in list
                                        else:
                                            meta_list.append("")
                                        if 'tags' in j['snippet']:
                                            print(video_id, list(j['snippet']['tags']))
                                            meta_list.append(list(j['snippet']['tags']))  # append video tags in list
                                        else:
                                            meta_list.append("")
                                        if 'publishedAt' in j['snippet']:
                                            print(video_id, j['snippet']['publishedAt'])
                                            meta_list.append(j['snippet']['publishedAt'])  # append video published date
                                        else:
                                            meta_list.append("")
                            except Exception as e:
                                print(e)
                            # Write video meta in csv file
                            csv_writer.writerow(meta_list)
                        videos_link = []
                    # Try to get next page token for getting next page videos
                    try:
                        next_page_token = resp['nextPageToken']
                        url = first_url + '&pageToken={}'.format(next_page_token)

                    except Exception as e:
                        print(e)
                        break


obj = MetaData('/home/praveen/Working_files/example.csv',
               'AIzaSyC54MhoGU4G3XjIqeTFrmqhENNFPyCyXOk')
obj.crawling()
