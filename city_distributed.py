# -*- coding: utf-8 -*-
"""
Created on 2021/11/19 16:40 

@author: R.ls
"""

from settings import *
import zoom_out
import result_view
import valide_within
import numpy as np
import math
import time
import random
import json


def deal_path(sd, d):
    zoom_dict = {}
    find_dict = {}
    n = 0
    for point in turning_point:
        zoom_array = list()
        boundary = turning_point.get(point)

        try:
            zoom_x, zoom_y = zoom_out.sample(boundary, sd)
            for i in range(len(zoom_x)):
                zoom_array.append((zoom_x[i], zoom_y[i]))
            # 安全范围内的字典数据
            zoom_dict[point] = zoom_array

            # 求出终点坐标 e_x = d * cos; e_y = d * sin
            r = 60
            find_cnt, find_array = find_six(point, r, zoom_array, d, boundary)

            while len(find_array) < 6 and r > 0:
                r = r - 5
                # print(r)
                find_cnt, find_array = find_six(point, r, zoom_array, d, boundary)

            if len(find_array) != 6:
                print(r, len(find_array))
                # print(zoom_array)

            find_dict[str(point)] = find_array

            if len(boundary[0])>4:
                print(n)
                result_view.sample(boundary, sd, find_array, point, n)

            n += 1

            # print(find_dict)
        except Exception as e:
            print(point)
    return find_dict


def find_six(point, r, zoom_array, d, boundary):
    find_array = list()
    re = 0
    find_cnt = 0
    max = int(360 / r)
    for seg in range(1, max):
        if find_cnt >= 6:
            continue
        e_x = round(point[0] + d * math.cos(math.radians(re)), 1)
        e_y = round(point[1] + d * math.sin(math.radians(re)), 1)
        re += r
        # 是否在势力范围内
        if valide_within.isPoiWithinPoly((e_x, e_y), [zoom_array]) :
            find_array.append((e_x, e_y))
            find_cnt += 1
    return find_cnt, find_array


if __name__ == '__main__':
    sd = 5
    d = 12.5
    find_dict = deal_path(sd, d)
    # print(len(find_dict))
    result_dict={}
    tmp = list()
    # with open("C:/Users/admin/Desktop/city_distribute.txt", "w") as fw:
        # fw.write(str(json.dumps(find_dict)))
        # fw.write(str(find_dict))