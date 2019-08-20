import os

path = 
files = os.listdir('/home/praveen/Working_files/tvf_txt_files/')

for file in files:
    f = open(file, 'r')
    print(f)

