from django.shortcuts import render

def index(request):

    return render(request,'calculator/index.html')

def calc(request):

    val1 = int(request.POST['val1'])

    val2 = int(request.POST['val2'])

    answer = val1 + val2

    context={

        'answer':answer,
    }

    return render(request,'calculator/index.html',context)

# calc1で得た計算結果の２乗を計算する関数
def calc2(request):
    
    val3 = int(request.POST['val3'])

    answer2 = val3 * val3

    context={
            'answer2':answer2,
        }

    

    return render(request,'calculator/index.html',context)

def gouseiodds(request):
    return render(request,'calculator/gouseiodds.html')
    

def gouseiodds_calc(request):
    val1 = int(request.POST['val1'])
    val2 = int(request.POST['val2'])
    val3 = int(request.POST['val3'])
    val4 = int(request.POST['val4'])
    val5 = int(request.POST['val5'])

    answer = val1 * val2 * val3 * val4 * val5


    context={
        'answer':answer,
    }

    

    return render(request,'calculator/gouseiodds.html',context)





def test(request):

    test_list = []

    # チェックボックスになっていないと、request.POSTがエラーになることを利用
    # して、エラーにならない時だけ、test_listに追加する。
    try:
        checkbox1 = request.POST['odds1check']
        val1 = request.POST['odds1']

        test_list.append(val1)
    except:
        checkbox1 = ""
        val1 = ""

    try:
        checkbox2 = request.POST['odds2check']
        val2 = request.POST['odds2']

        test_list.append(val2)
    except:
        checkbox2 = ""
        val2 = ""

    context={
        'checkbox1':checkbox1,
        'checkbox2':checkbox2,
        'val1':val1,
        'val2':val2,
        'test_list':test_list,
    }

    return render(request,'calculator/index.html',context)