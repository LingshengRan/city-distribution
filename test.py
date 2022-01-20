from settings import *
import zoom_out
import result_view
import valide_within
import numpy as np
import math
import time
import random
import json
from matplotlib import pyplot as plt

if __name__ == '__main__':

    slot_outer = list()
    slot_inner = list()
    # 全局无效区域范围内外 20 米 注意：顺时针和逆时针的方向不一致，缩进方向不一致
    for slot in invalid_area:
        print("=============")
        outer_x, outer_y = zoom_out.sample(invalid_area.get(slot), 20)
        inner_x, inner_y = zoom_out.sample(invalid_area.get(slot), -20)
        for out in range(len(outer_x)):
            slot_outer.append((outer_x[out], outer_y[out]))
        # print(outer_x,outer_y)
        for inn in range(len(inner_x)):
            slot_inner.append((inner_x[inn], inner_y[inn]))

        # "540.4,1051.8"
        # "541.1,1022.7"
        # "531.1,1054.0"
        # "525.6,1021.2"
    print([slot_outer])

    point_x=list()
    point_y = list()

    with open("C:/Users/admin/Desktop/city_distribute.txt", 'r', encoding='UTF-8-sig') as f:
        for line in f.readlines():
            result_point = eval(line.strip().replace("\n", "").replace("\r", "").split('\t')[0])
            for key in result_point:
                for p in result_point.get(key):
                    point_x.append(float(str(p).split(",")[0]))
                    point_y.append(float(str(p).split(",")[1]))
    plt.scatter(point_x, point_y, marker='.', c='g', s=1)
    plt.savefig("C:/Users/admin/Desktop/test/" + "验证图" + ".png", dpi=1000)
    plt.show()


