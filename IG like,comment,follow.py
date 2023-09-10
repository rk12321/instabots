from instagrapi import Client
import threading
from oauth2client.service_account import ServiceAccountCredentials
import gspread
import json
import requests
import time
import random

scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]


credentials = ServiceAccountCredentials.from_json_keyfile_name("helical-lantern-341505-97d7f2e3a202.json", scopes) #access the json key you downloaded earlier 
file = gspread.authorize(credentials) # authenticate the JSON key with gspread
ss = file.open("IGC BOT")  #open sheet
ws = ss.worksheet('Sheet3')#to open tab


cl1 = Client()
un1=ws.cell(2, 1).value;
pass1=ws.cell(3, 1).value;
cl1.login(un1, pass1)

'''
cl2 = Client()
un2=ws.cell(4, 1).value;
pass2=ws.cell(5, 1).value;
cl1.login(un2, pass2)

cl3 = Client()
un3=ws.cell(6, 1).value;
pass3=ws.cell(7, 1).value;
cl1.login(un3, pass3)
'''

while(1>0):
    def account1():
        n=2;
        for x in range(2):
            urltol = ws.cell(n, 2).value;
            urltoc = ws.cell(n, 3).value;
            lid = cl1.media_pk_from_url(urltol)
            #follow start
            un = ws.cell(n, 5).value;
            user = cl1.user_id_from_username(un)
            cl1.user_follow(user)
            print("done follow")
            time.sleep(33)
            #like start
            m = cl1.media_id(lid)
            cl1.media_like(m)
            print("done like")
            time.sleep(21)
            #comment start
            comments = ws.cell(n, 4).value;
            media_id = cl1.media_id(cl1.media_pk_from_url(urltoc))
            comment = cl1.media_comment(media_id, comments)
            comment.dict()
            print("done comment")
            time.sleep(31)
            n=n+1;
    '''
            #post start
            urltop = ws.cell(n, 6).value;
            path = cl1.photo_download(cl1.media_pk_from_url(urltop), folder='app')
            captions = ws.cell(n, 7).value;
            cl1.photo_upload(path)
            time.sleep(133)
    '''
            


          

    def account2():
        n=2;
        for x in range(2):
            urltol = ws.cell(n, 2).value;
            urltoc = ws.cell(n, 3).value;
            lid = cl2.media_pk_from_url(urltol)
            #follow start
            un = ws.cell(n, 5).value;
            user = cl2.user_id_from_username(un)
            cl2.user_follow(user)
            time.sleep(21)
            #like start
            m = cl2.media_id(lid)
            cl2.media_like(m)
            time.sleep(44)
            #comment start
            comments = ws.cell(n, 4).value;
            media_id = cl2.media_id(cl2.media_pk_from_url(urltoc))
            comment = cl2.media_comment(media_id, comments)
            comment.dict()
            time.sleep(12)
            n=n+1;
    '''
            #post start
            urltop = ws.cell(n, 6).value;
            path = cl1.photo_download(cl1.media_pk_from_url(urltop), folder='app')
            captions = ws.cell(n, 7).value;
            cl1.photo_upload(path)
            time.sleep(133)
    '''
            




    def account3():
        n=2;
        for x in range(2):
            urltol = ws.cell(n, 2).value;
            urltoc = ws.cell(n, 3).value;
            lid = cl3.media_pk_from_url(urltol)
            #follow start
            un = ws.cell(n, 5).value;
            user = cl3.user_id_from_username(un)
            cl3.user_follow(user)
            time.sleep(19)
            #like start
            m = cl3.media_id(lid)
            cl3.media_like(m)
            time.sleep(21)
            #comment start
            comments = ws.cell(n, 4).value;
            media_id = cl3.media_id(cl3.media_pk_from_url(urltoc))
            comment = cl3.media_comment(media_id, comments)
            comment.dict()
            time.sleep(32)
            n=n+1;
    '''
            #post start
            urltop = ws.cell(n, 6).value;
            path = cl1.photo_download(cl1.media_pk_from_url(urltop), folder='app')
            captions = ws.cell(n, 7).value;
            cl1.photo_upload(path)
            time.sleep(133)
    '''
            




    thread1 = threading.Thread(target=account1)
    thread1.start()
    #thread2 = threading.Thread(target=account2)
    #thread2.start()
    #thread3 = threading.Thread(target=account3)
    #thread3.start()
    thread1.join()
    gap = random.randint(93600,108000)
    time.sleep(gap)
    '''
    thread2.join()
    thread3.join()
    '''
    



