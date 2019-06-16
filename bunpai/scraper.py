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





class NetkeibaSpider:

	# name = 'netkeiba'
    print("NetkeibaSpiderクラスが読み込まれています")
	# start_urls = ['https://race.netkeiba.com/?pid=race_list']
    
    def parse(self,target_kaisai,target_race):
        print("NetkeibaSpiderのparse関数が実行されています")

        url = "https://race.netkeiba.com/?pid=race_list"

        html = urllib.request.urlopen(url)

        # xpath指定できるようにlxml用にhtml2を作成

        html2 = urllib.request.urlopen(url)

        soup = BeautifulSoup(html, "html.parser")

        dom = lxml.html.fromstring(html2.read())

        target_kaisai = target_kaisai
        target_race = target_race

        kaisai_list = []
        kaisaidata = soup.select('p[class="kaisaidata"]')

        for i in range(len(kaisaidata)):
            kaisai_list.append((kaisaidata[i].text)) 

        print("kaisai_list",kaisai_list)

        counter = 0

        for i in kaisai_list:
            if target_kaisai in i:
                kai = counter
                break
            else:
                kai = 0 
            counter += 1

        


        if kai != "":
            print(kai)
            

        kai += 1

        kai = str(kai)

        kai


        base_left = '//*[@id="race_list_body"]/div[1]/dl['
        base_middle = ']/dd/ul/li['
        base_right = ']/dl/dt/a/img/@alt'

        base_href = ']/dl/dd/div[1]/a/@href'



        # 平日に実行すると、４レースしか表示されない等になるため、対象の開催場のレース数を確認する
        howmany_race = len(dom.xpath('//*[@id="race_list_body"]/div[1]/'+'dl['+kai+']//div[@class="racename"]/a/@href'))

        # 　現時点で表示されているレースのリストを作成

        number_race_list = []
        for i in range(howmany_race):
            print(str(i+1))
            position = str(i+1)
            print(dom.xpath(base_left + kai + base_middle + position + base_right)[0])
            number_race = dom.xpath(base_left + kai + base_middle + position + base_right)[0]
            number_race_list.append(number_race)



        # レースからRの文字を取り除く
        number_race_list = [i.replace("R","") for i in number_race_list]

        #　target_race がリストの何番目にあるかを表示

        nanbanme = number_race_list.index(target_race) + 1
        nanbanme = str(nanbanme)



        # 対象レースのURLを取得する
        race_url = dom.xpath(base_left + kai + base_middle + nanbanme + base_href )[0]

        race_link="https://race.netkeiba.com/"+race_url

        race_link

        race_link

        url2 = race_link

        # url3 = self.odds_page(url2)


        # self.get_info(url3)

        odds_list = self.get_info(url2)

   

        # print(odds_list)

        return odds_list

    # def odds_page(self,url2):
    #     html3 = urllib.request.urlopen(url2)

    #     soup = BeautifulSoup(html3, "html.parser")

    #     odds_page=soup.select('.race_navi_odds')[0].a.get("href")

    #     url3 = "https://race.netkeiba.com/"+ odds_page

    #     print(url3)

    #     return url3

    


    def get_info(self, url2):
        # html2 = urllib.request.urlopen(url2)


        dfs = pd.read_html(url2,header=1 )
        tan_odds_list = dfs[0]["単勝オッズ"].values.tolist()

        # if "除外" in tan_odds_list:
        #     tan_odds_list.remove("除外")
        # else:
        #      print("除外なし")

        tan_odds_list = [e for e in tan_odds_list if e  != "除外"]

        print(tan_odds_list)

        # 文字列　→ float型へ
        tan_odds_list = [float(i) for i in tan_odds_list]

        # 並び替え
        tan_odds_list.sort()
       

        print(tan_odds_list)
        

        return tan_odds_list

        

if __name__ == "__main__":
    spider = NetkeibaSpider()
    spider.parse()