# -*- coding: utf-8 -*-
"""
Created on 2022/1/20 16:07 

@author: R.ls
"""
import math

import pandas as pd
import sys
import numpy as np
from scipy.optimize import curve_fit

ai_model_main_city_feature = sys.argv[1]
ai_model_pve_feature = sys.argv[2]
ai_model_soldier_lv_feature = sys.argv[3]
ai_model_soldier_star_feature = sys.argv[4]
file_path = sys.argv[5]
varhh = sys.argv[6]

def fun_soldier_level(x, a, b):
    y = a * x + 1
    return y


def fun_soldier_star(x, a, b):
    y = a * np.power(x, b)
    return y


def fun_main_line(x, a, b):
    y = a * x + 1
    return y


def fun_base_city(x, a, b):
    y = a * np.log(x) + b
    return y


def train(xdata, ydata, func_name):
    # Fit for the parameters a, b, c of the function func:
    popt, pcov = curve_fit(func_name, xdata, ydata)
    return popt+'\t'+pcov


if __name__ == "__main__":
    func_names = {'士兵等级': fun_soldier_level,
                  '士兵星级': fun_soldier_star,
                  '主线关卡': fun_main_line,
                  '主城等级': fun_base_city}

    df_base_city = pd.read_table(file_path+"/"+ai_model_main_city_feature+"_"+varhh, sep='\t', names=['1', '2', '3'], dtype=int)
    df_main_line = pd.read_table(file_path+"/"+ai_model_pve_feature+"_"+varhh, sep='\t')
    df_soldier_level = pd.read_table(file_path+"/"+ai_model_soldier_lv_feature+"_"+varhh, sep='\t')
    df_soldier_star = pd.read_table(file_path+"/"+ai_model_soldier_star_feature+"_"+varhh, sep='\t')


    train1 = train(df_main_line['2'], df_main_line['3'], func_names['主线关卡'])
    train2 = train(df_base_city['2'], df_base_city['3'], func_names['主城等级'])
    train3 = train(df_soldier_level['2'], df_soldier_level['3'], func_names['士兵等级'])
    train4 = train(df_soldier_star['2'], df_soldier_star['3'], func_names['士兵星级'])

    with open(file_path+"/ai_model_pve_"+varhh, "w") as fw:
        fw.write(train1)
    with open(file_path+"/ai_model_main_city_"+varhh, "w") as fw:
        fw.write(train2)
    with open(file_path+"/ai_model_soldier_lv_"+varhh, "w") as fw:
        fw.write(train3)
    with open(file_path+"/ai_model_soldier_star_"+varhh, "w") as fw:
        fw.write(train4)
