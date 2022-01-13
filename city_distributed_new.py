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

def deal_path(outer_boundary, p2p_safe_distance, request_num):
    zoom_dict = {}
    find_dict = {}
    sample_num = 1

    slot_outer = list()
    slot_inner = list()

    with open("C:/Users/admin/Desktop/turning_point.txt", 'r', encoding='UTF-8-sig') as f:
        for line in f.readlines():
            turning_point = eval(line.strip().replace("\n", "").replace("\r", "").split('\t')[0])

    with open("C:/Users/admin/Desktop/path_point.txt", 'r', encoding='UTF-8-sig') as f:
        for line in f.readlines():
            path_point = eval(line.strip().replace("\n", "").replace("\r", "").split('\t')[0])

    # 全局无效区域范围内外 8 米
    for slot in invalid_area:
        outer_x, outer_y = zoom_out.sample(invalid_area.get(slot), -8)
        for out in range(len(outer_x)):
            slot_outer.append((outer_x[out], outer_y[out]))

        inner_x, inner_y = zoom_out.sample(invalid_area.get(slot), 8)
        for inn in range(len(inner_x)):
            slot_inner.append((inner_x[inn], inner_y[inn]))

    for center_point in turning_point:

        if sample_num not in (62,228,766,1183,1335,1695,1700,1863,2024,2153,2264,2324,2484,2623,2771,2798,2960,3085,3223,3432,3502,3540,3684,3752,3859,3880):
            sample_num += 1
            continue

        center_point_distance = 10
        result_view.plt.figure()
        find_array = list()
        # 主城区
        city_list = list()
        city_list.append((center_point[0] - 10, center_point[1] - 11))
        city_list.append((center_point[0] + 10, center_point[1] - 11))
        city_list.append((center_point[0] + 10, center_point[1] + 11))
        city_list.append((center_point[0] - 10, center_point[1] + 11))
        city_list.append((center_point[0] - 10, center_point[1] - 11))

        path_array = path_point.get(center_point)
        zoom_array = list()
        # 势力范围
        boundary = turning_point.get(center_point)
        try:
            zoom_x, zoom_y = zoom_out.sample(boundary, outer_boundary)
            for i in range(len(zoom_x)):
                zoom_array.append((zoom_x[i], zoom_y[i]))
            # 外边界安全范围内的坐标数据
            zoom_dict[center_point] = zoom_array

            # 求出终点坐标 e_x = d * cos; e_y = d * sin
            while len(find_array) < 4 and center_point_distance > 0 and center_point_distance<50:
                r = 90  # 角度
                while len(find_array) < 4 and r > 0:
                    r -= 89.5
                    # print(r)
                    find_cnt, find_array = find_point(center_point, r, zoom_array, center_point_distance, request_num, p2p_safe_distance, path_array, city_list, find_array, slot_outer, slot_inner)
                center_point_distance += 0.1 #每0.1米搜索一次

            if len(find_array) != 4:
                result_view.sample(boundary, outer_boundary, find_array, center_point, sample_num, path_array)
                result_view.plt.savefig("C:/Users/admin/Desktop/test/" + str(sample_num) + ".png", dpi=1000)
                # result_view.plt.show()
                print(sample_num)
                # print(r, len(find_array))
            else:
                # {"城池ID": ["坐标X,坐标Y", "坐标X,坐标Y", "坐标X,坐标Y", "坐标X,坐标Y"]}

                find_list=list()
                for i in find_array:
                    find_list.append(str(i[0])+','+str(i[1]))
                find_dict[str(sample_num)] = find_list
            # if sample_num%100==0:
            #     print(sample_num)

            # result_view.sample(boundary, outer_boundary, find_array, center_point, sample_num, path_array)

            # print(find_dict)
            # result_view.plt.close()
            # result_view.plt.savefig("C:/Users/admin/Desktop/test/" + str(sample_num) + ".png", dpi=1000)
            # result_view.plt.show()
            sample_num += 1
            result_view.plt.close()
        except Exception as e:
            print("================",e)
    return find_dict

def find_point(center_point, r, zoom_array, center_point_distance, request_num, p2p_safe_distance, path_array, city_list, find_array, slot_outer, slot_inner):
    re = 0  # 起始角度
    find_cnt = len(find_array)
    # max = int(360 / r)
    max = 721
    for seg in range(1, max):
        if find_cnt < request_num:
            e_x = round(center_point[0] + center_point_distance * math.cos(math.radians(re)), 1)
            e_y = round(center_point[1] + center_point_distance * math.sin(math.radians(re)), 1)
            re += r
            # 不在主城区内 且在势力安全范围内 # 点与点之间的最小距离为4米 已选的点+路径上的点
            if valide_within.isPoiWithinPoly((e_x, e_y), [city_list]) is False and valide_within.isPoiWithinPoly((e_x, e_y), [zoom_array]) and safe_verify((e_x, e_y), find_array, p2p_safe_distance, path_array):
                # 不在区块无效区域
                if (valide_within.isPoiWithinPoly((e_x, e_y), [slot_outer]) and (valide_within.isPoiWithinPoly((e_x, e_y), [slot_inner]) is False)) is False:
                    find_array.append((e_x, e_y))
                    find_cnt += 1
    return find_cnt, find_array


def safe_verify(e_p, find_array, p2p_safe_distance, path_array):
    """
    两点之间的距离
    :param p1:
    :param p2:
    :return:
    """
    for find_p in find_array:
        mid = np.array(find_p) - np.array(e_p)
        if math.hypot(mid[0], mid[1]) <= p2p_safe_distance:
            return False

    for path_p in path_array:
        mid = np.array(path_p) - np.array(e_p)
        if math.hypot(mid[0], mid[1]) <= p2p_safe_distance:
            return False
    return True


if __name__ == '__main__':
    # 资源点刷新规则：
    # 1、长方形：长度距离中心点10米，宽度距离中心点13米 可调至11米
    # 2、距离势力范围边框4米
    # 3、点与点之间的最小距离为4米
    # 4、点的数量更变为了4个。
    # 5、去除路上的点位，以路上的坐标点半径4米内，不要生成点。
    # 6、区块里外8米不可刷点

    # center_point_distance = 10.1  # 1、长方形：长度距离中心点10米，宽度距离中心点13米 可调至11米
    outer_boundary = 4  # 2、距离势力范围边框4米 不可调
    p2p_safe_distance = 4  # 3、点与点之间的最小距离为4米
    request_num = 4  # 4、点的数量更变为了4个。



    find_dict = deal_path(outer_boundary, p2p_safe_distance, request_num)
    # print(len(find_dict))
    result_dict = {}
    tmp = list()
    with open("C:/Users/admin/Desktop/city_distribute_26.txt", "w") as fw:
        fw.write(str(json.dumps(find_dict)))
