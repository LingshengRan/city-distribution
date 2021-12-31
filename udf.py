# -*- coding: utf-8 -*-
"""
Created on 2021/12/14 16:14 

@author: R.ls
"""

import sys
import json


def read_input(file, separator):
    for line in file:
        try:
            yield line.strip().replace("\n", "").replace(" ", "").replace("\r", "").split('\t')
        except:
            print("error line")
            pass


def main(separator='\t'):
    line = read_input(sys.stdin, separator)
    # with open("C:/Users/admin/Desktop/temp_20211213", 'r', encoding='UTF-8-sig') as f:
    # line = read_input(f, separator)
    part = 0
    for dateline, areaid, cityarea, aiaccid, taskid, lag_dateline in line:

        # 超过30分钟 重新分组
        if int(dateline) >= int(lag_dateline) + 1800000:
            part += 1

        print("\t".join([dateline, areaid, cityarea, aiaccid, taskid, lag_dateline, str(part)]))


if __name__ == '__main__':
    main()
