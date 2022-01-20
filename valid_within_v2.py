# -*- coding: utf-8 -*-
"""
Created on 2022/1/19 16:34 

@author: R.ls
"""


# -*- coding:utf-8 -*-

def rayCasting(p, poly):
    px = p[0]
    py = p[1]
    flag = False

    i = 0
    l = len(poly)
    j = l - 1
    # for(i = 0, l = poly.length, j = l - 1; i < l; j = i, i++):
    while i < l:
        sx = poly[i][0]
        sy = poly[i][1]
        tx = poly[j][0]
        ty = poly[j][1]

        # 点与多边形顶点重合
        if (sx == px and sy == py) or (tx == px and ty == py):
            return (px, py)

        # 判断线段两端点是否在射线两侧
        if (sy < py and ty >= py) or (sy >= py and ty < py):
            # 线段上与射线 Y 坐标相同的点的 X 坐标
            x = sx + (py - sy) * (tx - sx) / (ty - sy)
            # 点在多边形的边上
            if x == px:
                return (px, py)
            # 射线穿过多边形的边界
            if x > px:
                flag = not flag
        j = i
        i += 1

    # 射线穿过多边形边界的次数为奇数时点在多边形内
    return (px, py) if flag else 'out'


# 根据输入的点循环判断芝麻是否在多边形里面，如果全部在外面则输出no,否则输出芝麻的坐标
def rs(zm, dbx):
    count = 0
    for point in zm:
        rs = rayCasting(point, dbx)
        if rs == 'out':
            count += 1
        else:
            return True
    if count == len(zm):
        return False

if __name__ == '__main__':
    zm=[[540.4, 1051.8]]
    duobianxing=[[720.0, 1280.0], [720.0, 1480.0], [960.0, 1480.0], [960.0, 1040.0], [520.0, 1040.0], [520.0, 1280.0], [720.0, 1280.0]]
    print(rs(zm, duobianxing))