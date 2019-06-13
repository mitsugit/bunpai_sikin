import numpy as np
import math
import decimal


def rafine(budget,odds_list):

    odds_list = [float(i) for i in odds_list]
    odds = odds_list
    print("odds",odds)
    each_bet = []

    C = 0

    # リスト内の最小値を取得し、１００を乗じる
    A = min(odds) * 100

    print(A)
    # 資金を分配する


    budget = int(budget)

    # オッズの最小値を各オッズで割ったものをリスト化する
    B_list = [A / i for i in odds]

    # 小数切り捨て
    B_list = list(map(lambda x: math.floor(x), B_list))

    print(B_list)

    C = sum(B_list)

    print("C", C)
    ratio = [B_list[i] / C * 100 for i in range(0, len(B_list))]

    ratio = np.round(ratio, 1)


    print("ratio", ratio)

    # ratio = [float(i) for i in ratio]

    # print("ratio", ratio)

    # for i in ratio:
    #     each_bet.append(np.round(budget*i/100,-2))

    each_bet = [np.round(budget * i / 100, -2) for i in ratio]


    return_list = [xx * yy for (xx,yy) in zip(each_bet,odds)]
    return_list = list(map(lambda x: math.floor(x), return_list))


    print(each_bet)

    print(sum(each_bet))

    total_bet = sum(each_bet)

    profit_list = [x-total_bet for x in return_list]

    print(profit_list)

    return odds_list,ratio,each_bet,return_list,total_bet,profit_list




