import pandas as pd
import requests
import json
import os
import traceback
import time


import socket


def is_connected():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

keys = ["AIzaSyBLuKB_DU4NmGca6XGW5-BcYSxBB_2OmiA"]
key_index=0

class Youtube_extract:
    
    def __init__(self):
        self.hit= 0
    ##To extract Channel Details
    def get_channel_details(self,chan_ids_list,part='snippet',key="AIzaSyBLuKB_DU4NmGca6XGW5-BcYSxBB_2OmiA"):
        url_c = "https://www.googleapis.com/youtube/v3/channels"
        responses = dict()
        for ind,chan in enumerate(chan_ids_list):
            try:
                querystring = {"id":chan ,"part":part,
                               "key":key}
                response = requests.request("GET", url_c, params=querystring)
                if response.json().get('error'):
                    responses.update({chnlid:[response,response.text]})
                    if response.json()['error']['errors']['reason']=='keyInvalid':
                        return [{chnlid:[response,response.text]}]
                    break
                responses[chan] = response.json()['items']
            except Exception as e:
                responses[chan] = {'error': [e,response,response.text]}
            if ind%100==0:
                print(ind)
        return (responses)
    #To get video Details
    def get_video_details(self,vid_ids_list,part='snippet',key="AIzaSyBLuKB_DU4NmGca6XGW5-BcYSxBB_2OmiA"):
        url_v = "https://www.googleapis.com/youtube/v3/videos"
        responses = dict()
        for ind,vid in enumerate(vid_ids_list):
            try:
                querystring = {"id":vid ,"part":part,
                               "key":key}
                response = requests.request("GET", url_v, params=querystring)
                if response.json().get('error'):
                    responses.update({chnlid:[response,response.text]})
                    if response.json()['error']['errors']['reason']=='keyInvalid':
                        return [{chnlid:[response,response.text]}]
                    break
                responses[vid] = response.json()['items']
            except Exception as e:
                # responses[chan] = [e,response,response.text]
                responses[vid] = {'error': [e,response,response.text]}
            if ind%100==0:
                print(ind)
        return (responses)

    #to get all videos of a channel
    def playlist(self,channel_list,limit,part='contentDetails',key='AIzaSyDOWd9zD98l4cpfNVG2UufPM2sZbHFt3XA',only_id=1):
        playlist_url = 'https://www.googleapis.com/youtube/v3/playlistItems/'
        if limit<=50 and limit>0:
            maxResults=limit
        else:
            maxResults=50
        all_result = {}
        for chnlid in channel_list:
            vidcount = initial = 0
            nextPageToken =''
            results=[]
            # print('UU'+chnlid[2:])
            try:
                while nextPageToken or initial==0:
                    query = {
                        'playlistId':'UU'+chnlid[2:],
                        'part':part,
                        'key':key,
                        'pageToken':nextPageToken,
                        'maxResults':maxResults
                    }
                    response = requests.get(url = playlist_url,params = query)
                    # print(response,response.text)
                    if response.json().get('error'):
                        print(response.json())
#                         all_result.update({chnlid:[response,response.text]})
                        if response.json()['error'].get('errors'):
                            if response.json()['error']['errors'].get('reason'):
                                if response.json()['error']['errors']['reason']=='keyInvalid':
                                    print("InvalidKey")
                                    return [{chnlid:{'error':[response,response.text]}}]
                        break
                    if limit==-1:
                        limit = response.json()['pageInfo']['totalResults']
                    # print(response,response.text)
                    
                    if only_id==1:
                        for i in range(response.json()['pageInfo']['resultsPerPage']):
                            try:
                                results.append(response.json()['items'][i]['contentDetails']['videoId'])
                            except:
                                pass
                    else:
                        results.append(response.json()['items'])
                    nextPageToken = response.json().get('nextPageToken')
                    vidcount = vidcount+ len(response.json()['items'])
                    if vidcount>=limit:
                        break
                    print("Completed:",vidcount)
                    
                    
                    initial = 1
                all_result.update({chnlid:results})
            except Exception as e:
                all_result[chnlid] = {'error': [e,traceback.print_exc(),response,response.text]}
                break
        return all_result
    
    #To get stats of videos of a channel
    def all_channel_video_data(self,channel_list,limit,vid_part='snippet'):
        all_result={}
        for chanlid in channel_list:
            result = self.playlist([chanlid],limit)
            all_result.update({chanlid:self.get_video_details(result[chanlid],part=vid_part)})
        return all_result


if __name__ =='__main__':
    data = Youtube_extract()
    result = data.all_channel_video_data(['UCAGzeRhIE9NUASlH_X5MDEQ'],limit=-1,vid_part='snippet')
    print(len(result['UCAGzeRhIE9NUASlH_X5MDEQ']))
    json.dump(result,open(os.curdir+'/output.json','w+'))