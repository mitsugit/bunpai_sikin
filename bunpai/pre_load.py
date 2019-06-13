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

    def parse(self):
        print("pre_get_dataクラスのparse関数が実行されています")

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


        kaisai_list = []
        kaisaidata = soup.select('p[class="kaisaidata"]')

        for i in range(len(kaisaidata)):
            kaisai_list.append((kaisaidata[i].text))

        print("kaisai_list",kaisai_list)

        return kaisaibi_list,kaisai_list

if __name__ == "__main__":
    spider = pre_get_data()
    spider.parse()
else:
    print("__main__")