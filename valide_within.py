# -*- coding: utf-8 -*-
"""
Created on 2021/11/19 17:15 

@author: R.ls
"""
from matplotlib import pyplot as plt

def isRayIntersectsSegment(poi,s_poi,e_poi): #[x,y] [lng,lat]
    #输入：判断点，边起点，边终点，都是[lng,lat]格式数组
    if s_poi[1]==e_poi[1]: #排除与射线平行、重合，线段首尾端点重合的情况
        return False
    if s_poi[1]>poi[1] and e_poi[1]>poi[1]: #线段在射线上边
        return False
    if s_poi[1]<poi[1] and e_poi[1]<poi[1]: #线段在射线下边
        return False
    if s_poi[1]==poi[1] and e_poi[1]>poi[1]: #交点为下端点，对应spoint
        return False
    if e_poi[1]==poi[1] and s_poi[1]>poi[1]: #交点为下端点，对应epoint
        return False
    if s_poi[0]<poi[0] and e_poi[1]<poi[1]: #线段在射线左边
        return False

    xseg=e_poi[0]-(e_poi[0]-s_poi[0])*(e_poi[1]-poi[1])/(e_poi[1]-s_poi[1]) #求交
    if xseg<poi[0]: #交点在射线起点的左侧
        return False
    return True  #排除上述情况之后

def isPoiWithinPoly(poi,poly):
    #输入：点，多边形三维数组
    #poly=[[[x1,y1],[x2,y2],……,[xn,yn],[x1,y1]],[[w1,t1],……[wk,tk]]] 三维数组

    #可以先判断点是否在外包矩形内
    #if not isPoiWithinBox(poi,mbr=[[0,0],[180,90]]): return False
    #但算最小外包矩形本身需要循环边，会造成开销，本处略去
    sinsc=0 #交点个数
    for epoly in poly: #循环每条边的曲线->each polygon 是二维数组[[x1,y1],…[xn,yn]]
        for i in range(len(epoly)-1): #[0,len-1]
            s_poi=epoly[i]
            e_poi=epoly[i+1]
            if isRayIntersectsSegment(poi,s_poi,e_poi):
                sinsc+=1 #有交点就加1

    return True if sinsc%2==1 else  False

if __name__ == '__main__':
    poi=[540.4, 1051.8]
    poly=[[[720.0, 1280.0], [720.0, 1480.0], [960.0, 1480.0], [960.0, 1040.0], [520.0, 1040.0], [520.0, 1280.0], [720.0, 1280.0]]]
    within_poly= isPoiWithinPoly(poi, poly)
    if isPoiWithinPoly((540.4, 1051.8), poly):
        print("=============")
    plt.figure()
    outer_x=list()
    outer_y=list()
    for list_p in poly:
        for p in list_p:
            outer_x.append(p[0])
            outer_y.append(p[1])
    plt.plot(outer_x, outer_y, c='r')
    plt.scatter(540.4, 1051.8, marker='o', c='r')
    print(within_poly)
    plt.show()


