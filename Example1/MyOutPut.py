from MyClass import ParaClass
from MyClass import PasClass
from MyClass import PathClass
import numpy as np

def pas(pas: PasClass):

    """
        print the two passengers
    :return:
    """
    outfile = "result_pas_path.csv"
    with open(outfile, "wt") as f:
        print("Pas,Path,Fare,Travel,Wait,W_Fare,W_Travel,W_Wait,WeightedCost,NonWeightCost",  file=f)
        for o in pas:
            for p in o.paths:
                print("{0},{1},{2},{3},{4},{5},{6},{7},{8},{9}".
                      format(o.id, p.id, p.att['Fare'], p.att['Travel'], p.att['Wait'], o.para.weight['Fare'],
                             o.para.weight['Travel'], o.para.weight['Wait'],
                             p.cost['Weight'], p.cost['NonWeight']), file=f)


def recommend_path(passengers: PasClass):

    with open("RecommendPath.txt", "wt") as f:
        for o in passengers:
            num = 1
            max_num = len(o.paths)
            print("Pas={0},shortest_non_weight=(".format(o.id), file=f, end='')
            for p in o.shortest_non_weight:
                if num < max_num:
                    print('{0},'.format(p.id), file=f, end='')
                else:
                    print('{0})'.format(p.id), file=f)
                num += 1
        for o in passengers:
            num = 1
            # max_num = len(list[ps for ps in o.paths:p.isCandy == True])
            max_num = len(o.paths)
            # max_num = len([ps for ps in o.paths]o.paths[where(o.paths.isCandy is True)])
            print("Pas={0},shortest_weight=(".format(o.id), file=f, end='')
            for p in o.shortest_weight :
                if num > max_num:
                    continue
                if num < max_num:
                    print('{0},'.format(p.id), file=f, end='')
                else:
                    print('{0})'.format(p.id), file=f)
                num += 1
        for o in passengers:
            num = 1
            max_num = len([ps for ps in o.paths if ps.isCandy is True])
            print("Pas={0},ordered_path=(".format(o.id), file=f, end='')
            for p in o.ordered_path:
                if num > max_num:
                    continue
                if num < max_num:
                    print('{0},'.format(p[0].id), file=f, end='')
                else:
                    print('{0})'.format(p[0].id), file=f)
                num += 1


def check_para(passengers:PasClass):

    with open("check_para.csv", "wt") as f:
        print("Weight,A,B", file=f)
        keys = passengers[0].para.weight.keys()
        for r in keys:
            print("{0},{1},{2}".format(r, passengers[0].para.weight[r], passengers[1].para.weight[r]), file=f)
    # with open("result_paths.csv", "wt") as f:
    #     print("Pas,Paht.B,non_weight,weight", file=f)
    #     nump = len(passengers[0].ordered_path)
    #     for p in range(0, nump):
    #         print("{0},{1},{2},{3},{4}".
    #               format(p, passengers[0].ordered_path[p].id, passengers[1].ordered_path[p][0].id,
    #                      passengers[0].ordered_path[p][0].cost['NonWeight'],
    #                      passengers[1].ordered_path[p][0].cost['Weight']), file=f)