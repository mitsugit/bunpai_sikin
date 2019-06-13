from django.shortcuts import render
import pandas as pd
import numpy as np 
from datetime import datetime as dt
from time import sleep
import copy
# !pip install openpyxl
# import openpyxl
import urllib.request
from bs4 import BeautifulSoup
import time

import requests
# import lxml.html as parser
import re
import pprint

import lxml.html






def scraping():
    url = "https://race.netkeiba.com/?pid=race_list"
    html = urllib.request.urlopen(url)
    # xpath指定できるようにlxml用にhtml2を作成
    html2 = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    dom = lxml.html.fromstring(html2.read())

    target_kaisai = "東京"
    target_race = "11"

    kaisai_list = []
    kaisaidata = soup.select('p[class="kaisaidata"]')

    for i in range(len(kaisaidata)):
        kaisai_list.append((kaisaidata[i].text)) 

        print("kaisai_list",kaisai_list)

    return url,kaisai_list