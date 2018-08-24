import requests
import csv
import os
import codecs

class AgeGenderTest(object):
    def __init__(self, input_folder):
        self.input_folder = input_folder

    def test_script(self):
        data_list = []
        image_list = os.listdir(self.input_folder)
        with codecs.open("/home/praveen/Working_files/Age_Gender_Work/age_gender_pred.csv", "w", encoding="utf-8") as output_file:
            csv_writer = csv.writer(output_file)
            for image in image_list:
                image_name = str(image)
                image_path = "https://s3.amazonaws.com/datascience-public/face/vidooly_office/f1/{}".format(image_name)
                print(image_path)
                data_list.append(image_path)
                api_url = "http://180.151.75.164:8080/ml/result/age_gender?img_url={}".format(image_path)
                try:
                    inp = requests.get(api_url)
                    resp = inp.json()
                    print(resp['status'])
                    if 'result' in resp:
                        print(resp['result'])
                        data_list.append(resp['result'])
                except Exception as e:
                    print(e)
                csv_writer.writerow(data_list)
                data_list = []


obj = AgeGenderTest("/home/praveen/Working_files/Age_Gender_Work/Image_folder/Image1_files")
obj.test_script()
