import requests
import csv
import codecs
import os


class FaceSimTest(object):
    def __init__(self, input_list1, input_list2):
        self.input_list1 = input_list1
        self.input_list2 = input_list2

    def face_sim_test(self):
        data_list = []
        image_list1 = os.listdir(self.input_list1)
        image_list2 = os.listdir(self.input_list2)
        with codecs.open("/home/praveen/Working_files/Age_Gender_Work/face_sim_pred1.csv", "w", encoding="utf-8") as output_file:
            csv_writer = csv.writer(output_file)
            count = 1
            for image1 in image_list1:
                count2 = 1
                for image2 in image_list2:
                    print("First image count = {}".format(count))
                    print("Second Image count = {}".format(count2))
                    image1_name = str(image1)
                    image2_name = str(image2)

                    image1_url = "https://s3.amazonaws.com/datascience-public/face/vidooly_office/f1/{}".format(image1_name)
                    print("Image1 URL : ", image1_url)
                    data_list.append(image1_url)
                    image2_url = "https://s3.amazonaws.com/datascience-public/face/vidooly_office/f2/{}".format(image2_name)
                    print("Image2 URL : ", image2_url)
                    data_list.append(image2_url)
                    api_url = "http://192.168.97.25/ml/result/face_comparison?method=v2&img_url1={}&img_url2={}".format(image1_url, image2_url)

                    try:
                        inp = requests.get(api_url)
                        print(inp.status_code)
                        resp = inp.json()
                        print(resp['status'])
                        if 'result' in resp:
                            print(resp['result'])
                            data_list.append(resp['result'])
                    except Exception as e:
                        print(e)
                    csv_writer.writerow(data_list)
                    data_list = []
                    count2 = count2 + 1
                count = count + 1


obj = FaceSimTest("/home/praveen/Working_files/Age_Gender_Work/Image_folder/Image1_files",
                  "/home/praveen/Working_files/Age_Gender_Work/Image_folder/Image2_files")
obj.face_sim_test()
