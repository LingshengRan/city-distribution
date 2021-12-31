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

def deal_path(outer_boundary, p2p_safe_distance, center_point_distance, request_num):
    zoom_dict = {}
    find_dict = {}
    sample_num = 1

    for center_point in turning_point:
        result_view.plt.figure()
        find_array = list()
        # 主城区
        city_list = list()
        city_list.append((center_point[0] - 10, center_point[1] - 13))
        city_list.append((center_point[0] + 10, center_point[1] - 13))
        city_list.append((center_point[0] + 10, center_point[1] + 13))
        city_list.append((center_point[0] - 10, center_point[1] + 13))
        city_list.append((center_point[0] - 10, center_point[1] - 13))

        path_array = path_point.get(center_point)
        zoom_array = list()
        boundary = turning_point.get(center_point)
        try:
            zoom_x, zoom_y = zoom_out.sample(boundary, outer_boundary)
            for i in range(len(zoom_x)):
                zoom_array.append((zoom_x[i], zoom_y[i]))
            # 外边界安全范围内的坐标数据
            zoom_dict[center_point] = zoom_array

            # 求出终点坐标 e_x = d * cos; e_y = d * sin
            r = 90  # 角度
            find_cnt, find_array = find_point(center_point, r, zoom_array, center_point_distance, request_num, p2p_safe_distance, path_array, city_list,find_array)
            while len(find_array) < 4 and r > 0:
                r = r - 1
                # print(r)
                find_cnt, find_array = find_point(center_point, r, zoom_array, center_point_distance, request_num, p2p_safe_distance, path_array, city_list,find_array)

            if len(find_array) != 4:
                # 缩小 center_point_distance 重新按角度查找
                center_point_distance2 = center_point_distance - 3.25
                # 求出终点坐标 e_x = d * cos; e_y = d * sin
                r = 90  # 角度
                find_cnt, find_array = find_point(center_point, r, zoom_array, center_point_distance2, request_num,p2p_safe_distance, path_array, city_list,find_array)
                while len(find_array) < 4 and r > 0:
                    r = r - 1
                    # print(r)
                    find_cnt, find_array = find_point(center_point, r, zoom_array, center_point_distance2, request_num, p2p_safe_distance, path_array, city_list,find_array)

            if len(find_array) != 4:
                # 缩小 center_point_distance 重新按角度查找
                center_point_distance3 = center_point_distance + 3
                # 求出终点坐标 e_x = d * cos; e_y = d * sin
                r = 90  # 角度
                find_cnt, find_array = find_point(center_point, r, zoom_array, center_point_distance3, request_num,p2p_safe_distance, path_array, city_list,find_array)
                while len(find_array) < 4 and r > 0:
                    r = r - 1
                    # print(r)
                    find_cnt, find_array = find_point(center_point, r, zoom_array, center_point_distance3, request_num, p2p_safe_distance, path_array, city_list,find_array)

            if len(find_array) != 4:
                result_view.sample(boundary, outer_boundary, find_array, center_point, sample_num, path_array)
                result_view.plt.savefig("C:/Users/admin/Desktop/test/" + str(sample_num) + ".png", dpi=1000)
                # result_view.plt.show()
                print(sample_num)
                # print(r, len(find_array))

            # {"城池ID": ["坐标X,坐标Y", "坐标X,坐标Y", "坐标X,坐标Y", "坐标X,坐标Y"]}
            find_list=list()
            for i in find_array:
                find_list.append(str(i[0])+','+str(i[1]))
            find_dict[str(sample_num)] = find_list

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


def find_point(center_point, r, zoom_array, center_point_distance, request_num, p2p_safe_distance, path_array, city_list, find_array):
    re = 0  # 起始角度
    find_cnt = len(find_array)
    # max = int(360 / r)
    max = 360
    for seg in range(1, max):
        if find_cnt < request_num:
            e_x = round(center_point[0] + center_point_distance * math.cos(math.radians(re)), 1)
            e_y = round(center_point[1] + center_point_distance * math.sin(math.radians(re)), 1)
            re += r
            # 不在主城区内 且在势力安全范围内 # 点与点之间的最小距离为4米 已选的点+路径上的点
            if valide_within.isPoiWithinPoly((e_x, e_y), [city_list]) is False and valide_within.isPoiWithinPoly((e_x, e_y), [zoom_array]) and safe_verify((e_x, e_y), find_array, p2p_safe_distance, path_array):
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
    # 1、长方形：长度距离中心点10米，宽度距离中心点13米
    # 2、距离势力范围边框5米
    # 3、点与点之间的最小距离为4米
    # 4、点的数量更变为了4个。
    # 5、去除路上的点位，以路上的坐标点半径4米内，不要生成点。


    center_point_distance = 16.5  # 1、长方形：长度距离中心点10米，宽度距离中心点13米
    outer_boundary = 4  # 2、距离势力范围边框2米
    p2p_safe_distance = 4  # 3、点与点之间的最小距离为4米
    request_num = 4  # 4、点的数量更变为了4个。

    find_dict = deal_path(outer_boundary, p2p_safe_distance, center_point_distance, request_num)
    # print(len(find_dict))
    result_dict = {}
    tmp = list()
    with open("C:/Users/admin/Desktop/city_distribute.txt", "w") as fw:
        fw.write(str(json.dumps(find_dict)))
