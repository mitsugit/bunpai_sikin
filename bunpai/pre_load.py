import pandas as pd
import numpy as np
from datetime import datetime as dt
from time import sleep
import copy
# !pip install openpyxl
import openpyxl
import urllib.request
from bs4 import BeautifulSoup
import time

import requests
# import lxml.html as parser
import re
import pprint

# import urllib2
# import pandas as pd

import lxml.html


class pre_get_data:

    print("pre_get_dataが読み込まれています")

    def getkaisaibi(self):

        print("pre_get_dataクラスのgetkaisaibi関数が実行されています")

        url = "https://race.netkeiba.com/?pid=race_list"

        html = urllib.request.urlopen(url)

        # xpath指定できるようにlxml用にhtml2を作成

        html2 = urllib.request.urlopen(url)

        soup = BeautifulSoup(html, "html.parser")

        dom = lxml.html.fromstring(html2.read())

        pre_kaisaibi_list=soup.select(".DateList_Box")[0].select("a")

        kaisaibi_list = []
        for i in pre_kaisaibi_list:
            kaisaibi_list.append(i.text)

        return kaisaibi_list




    def get_kaisai(self,target_kaisaibi):
        print("pre_get_dataクラスのget_kaisai関数が実行されています")

        target_kaisaibi = target_kaisaibi

        url = "https://race.netkeiba.com/?pid=race_list"

        html = urllib.request.urlopen(url)

        # xpath指定できるようにlxml用にhtml2を作成

        html2 = urllib.request.urlopen(url)

        soup = BeautifulSoup(html, "html.parser")

        dom = lxml.html.fromstring(html2.read())

        raceday_list = soup.select( "#race_list_header")[0].select("a")

        for i in raceday_list:
           if i.text == target_kaisaibi:
               target_kaisai_link =   "https://race.netkeiba.com" + i.get("href")

        target_kaisai_list = self.get_kaisaidata(target_kaisai_link)


        return target_kaisai_list,target_kaisai_link


    def get_kaisaidata(self,kaisai_link):
        x = kaisai_link
    
        html = urllib.request.urlopen(x)
        soup = BeautifulSoup(html, "html.parser")

        day_kaisai_list = []
        kaisaidata = soup.select('p[class="kaisaidata"]')
        day_kaisai_list = [i.text  for i in  kaisaidata]
    
        return day_kaisai_list
    


if __name__ == "__main__":
    spider = pre_get_data()
    spider.parse()
else:
    print("__main__")