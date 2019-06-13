from django.shortcuts import render

from . scraping import scraping
from . scraper import NetkeibaSpider
from .pre_load import pre_get_data
from .rafine import rafine


def bunpai(request):

    return render(request,'bunpai/bunpai.html')


# 開催日と開催場を読み込む
def preload(request):
    pre_scrape = pre_get_data()

    

    kaisaibi_list,kaisai_list = pre_scrape.parse()

    context={
        'kaisaibi_list':kaisaibi_list,
        'kaisai_list':kaisai_list,
        }
   
    return render(request,'bunpai/bunpai.html',context)



def select(request):

    kaisai = request.POST['kaisai']
    race = request.POST['race']

    ms = kaisai
    ms2 = race+"Rがセットされました"

    context={
        'kaisai':kaisai,
        'race':race,
        'ms':ms,
        'ms2':ms2,

    }
    return render(request,'bunpai/bunpai.html',context)


def get_data(request):



    # scraper = NetkeibaSpider()
    # odds_list = scraper.parse()

    target_kaisai=request.POST['target_kaisai']
    target_race=request.POST['target_race']

    scraper = NetkeibaSpider()
    odds_list = scraper.parse(target_kaisai,target_race)

    
    context = {
        'target_kaisai':target_kaisai,
        'target_race':target_race,

        'odds_list':odds_list,

        # 'url':url,
        # 'kaisai_list':kaisai_list,
    }
    print(type(target_kaisai))
    print(type(target_race))
    return render(request,'bunpai/bunpai.html',context)



def sikinbunpai(request):

    odds_list = []

    try:
        checkbox1 = request.POST['odds1check']
        val1 = request.POST['odds1']

        odds_list.append(val1)
    except:
        checkbox1 = ""
        val1 = ""

    try:
        checkbox2 = request.POST['odds2check']
        val2 = request.POST['odds2']

        odds_list.append(val2)
    except:
        checkbox2 = ""
        val2 = ""

    try:
        checkbox3 = request.POST['odds3check']
        val3 = request.POST['odds3']

        odds_list.append(val3)
    except:
        checkbox3 = ""
        val3 = ""

    try:
        checkbox4 = request.POST['odds4check']
        val4 = request.POST['odds4']

        odds_list.append(val4)
    except:
        checkbox4 = ""
        val4 = ""

    budget = request.POST['budget']
    print("budget",budget)
    print("odds_list",odds_list)

    if odds_list != []:
        odds_list,ratio,each_bet,return_list,total_bet,profit_list = rafine(budget,odds_list)
        errorms1 = ""
    else:
        errorms1 = "分配するオッズを選択してください!!!"

        odds_list = [request.POST['odds1'],request.POST['odds2'],request.POST['odds3'],request.POST['odds4'],request.POST['odds5']]

        ratio=each_bet=return_list=total_bet=profit_list = ""

    context = {
        'ratio':ratio,
        'each_bet':each_bet,
        'return_list':return_list,
        'total_bet':total_bet,
        'profit_list':profit_list,
        'odds_list':odds_list,
        'errorms1':errorms1,
    }
    return render(request,'bunpai/bunpai.html',context)