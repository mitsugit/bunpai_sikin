from django.shortcuts import render

from . scraping import scraping
from . scraper import NetkeibaSpider
from .pre_load import pre_get_data
from .rafine import rafine


def bunpai(request):

    return render(request,'bunpai/bunpai.html')


# 開催日読み込み
def getkaisaibi(request):
    pre_scrape = pre_get_data()

    

    kaisaibi_list = pre_scrape.getkaisaibi()

    context={
        'kaisaibi_list':kaisaibi_list,
        }
   
    return render(request,'bunpai/bunpai.html',context)

def get_kaisai(request):

    target_kaisaibi = request.POST['kaisaibi']

    pre_scrape = pre_get_data()

    

    kaisai_list,target_kaisai_link = pre_scrape.get_kaisai(target_kaisaibi)

    # scraper = NetkeibaSpider()



    # target_url = scraper.shutuba_page(target_kaisai_link)

    # race_list = scraper.get_info(target_url)

    context={
        'kaisai_list':kaisai_list,
        'target_kaisaibi':target_kaisaibi,
        'target_kaisai_link':target_kaisai_link,
        
        }
   
    return render(request,'bunpai/bunpai.html',context)






# 開催日と開催場を読み込む
def preload(request):
    pre_scrape = pre_get_data()

    

    kaisai_dict,kaisaibi_list,kaisai_list = pre_scrape.parse()

    context={
        'kaisai_dict':kaisai_dict,
        'kaisaibi_list':kaisaibi_list,
        'kaisai_list':kaisai_list,
        }
   
    return render(request,'bunpai/bunpai.html',context)


# def select_kaisaibi(request):

#     target_kaisaibi = request.POST['kaisaibi']
#     # kaisai_dict = request.POST['kaisai_dict']

#     target_kaisai_list = kaisai_dict[target_kaisaibi]

#     context={'target_kaisai_list':target_kaisai_list}

#     return render(request,'bunpai/bunpai.html',context)



# def kaisai_select(request):

#     kaisaibi = request.POST['kaisaibi']



#     context={'kaisaibi':kaisaibi}

#     return render(request,'bunpai/bunpai.html',context)


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
    # target_kaisaibi=request.POST['target_kaisaibi']
    target_race=request.POST['target_race']

    ms7 = target_kaisai+" : "+ target_race + "上位６番人気"

    scraper = NetkeibaSpider()

    odds_list,umaban_list,ninki_list = scraper.parse(target_kaisai,target_race)

    
    context = {
        'target_kaisai':target_kaisai,
        # 'target_kaisaibi':target_kaisaibi,
        'target_race':target_race,

        'ms7':ms7,

        'odds_list':odds_list,
        'umaban_list':umaban_list,
        'ninki_list':ninki_list,

        # 'url':url,
        # 'kaisai_list':kaisai_list,
    }
    print(type(target_kaisai))
    print(type(target_race))
    return render(request,'bunpai/bunpai.html',context)



def sikinbunpai(request):

 

    odds_list = []
    umaban_list = []
    try:
        checkbox1 = request.POST['odds1check']
        val1 = request.POST['odds1']
        umaban1 = request.POST['umaban1']
        umaban_list.append(umaban1)

        odds_list.append(val1)
        
    except:
        checkbox1 = ""
        val1 = ""
        umaban1 = ""

    try:
        checkbox2 = request.POST['odds2check']
        val2 = request.POST['odds2']
        umaban2 = request.POST['umaban2']
        umaban_list.append(umaban2)

        odds_list.append(val2)
    except:
        checkbox2 = ""
        val2 = ""
        umaban2 = ""

    try:
        checkbox3 = request.POST['odds3check']
        val3 = request.POST['odds3']
        umaban3 = request.POST['umaban3']
        umaban_list.append(umaban3)

        odds_list.append(val3)
    except:
        checkbox3 = ""
        val3 = ""
        umaban3 = ""

    try:
        checkbox4 = request.POST['odds4check']
        val4 = request.POST['odds4']
        umaban4 = request.POST['umaban4']
        umaban_list.append(umaban4)

        odds_list.append(val4)
    except:
        checkbox4 = ""
        val4 = ""
        umaban4 = ""

    try:
        checkbox5 = request.POST['odds5check']
        val5 = request.POST['odds5']

        umaban5 = request.POST['umaban5']
        umaban_list.append(umaban5)

        odds_list.append(val5)
    except:
        checkbox5 = ""
        val5 = ""
        umaban5 = ""

    try:
        checkbox6 = request.POST['odds6check']
        val6 = request.POST['odds6']
        umaban6 = request.POST['umaban6']
        umaban_list.append(umaban6)

        odds_list.append(val6)
    except:
        checkbox6 = ""
        val6 = ""
        umaban6 = ""


    

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



    ms7 = "分配結果"

    context = {
        'ratio':ratio,
        'each_bet':each_bet,
        'return_list':return_list,
        'total_bet':total_bet,
        'profit_list':profit_list,
        'odds_list':odds_list,
        'errorms1':errorms1,
        'ms7':ms7,
        'umaban_list':umaban_list,
    }
    return render(request,'bunpai/bunpai.html',context)