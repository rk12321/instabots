from instagrapi import Client
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import json
import requests
import time
import random


#open cmd and write
#ek ek krke daalio bsdk, pehle line 1 and usko donload hone dio, ek hi wala banake deta but time kam hai
'''
1) pip install instagrapi
2) pip install oauth2client
3) pip install gspread
4) pip install json
5) pip install requests
6) pip install time
7) pip install random
'''

#import imageio
#imageio.plugins.ffmpeg.download()


scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]


cl = Client()
cl.login('Masteruber', '8447391024')

credentials = ServiceAccountCredentials.from_json_keyfile_name("dotted-hope-341616-4e5d44b7775e.json", scopes) #access the json key you downloaded earlier 
file = gspread.authorize(credentials) # authenticate the JSON key with gspread
ss = file.open("IGRP")  #open sheet
ws = ss.worksheet('Sheet1')#to open tab

#time gap between two posts btw 30 mins to 60 mins
gap = random.randint(1800,3600)

#random comment to select btw row 1 to 10
captionnumber = random.randint(1,10)

#to download and upload reel
def downloadandupload_reel():
    n=2;
    for x in range(1):
        url = ws.cell(n, 1).value;
        path = cl.clip_download(cl.media_pk_from_url(url), folder='app')
        captions = ws.cell(captionnumber, 3).value;
        cl.clip_upload(path, caption=captions)
        ws.update_cell(n, 2, "done")
        n=n+1;
        time.sleep(gap)


#to upload posts
def upload_post():
    media = cl.photo_upload(
        "app/hhh.jpg",
        "Test caption for photo with #hashtags #gym #demo",
    )


while(1):
    print("Click 1 to download and then upload reels\nClick 2 to upload a post\nClick 3 to terminate the program\nClick 4 if you can't decide anything")
    task = input();
    if(task == "1"):
        downloadandupload_reel()
    if(task == "2"):
        upload_post()
    if(task == "3"):
        break;
    if(task == "4"):
        continue;
