# -*- coding: utf-8 -*-
"""
Created on 2022/1/12 15:33 

@author: R.ls
"""

import sys
import json


def read_input(file, separator):
    for line in file:
        try:
            yield line.strip().replace("\n", "").replace("\r", "").split('\t')
        except:
            print("error line")
            pass


def main(separator='\t'):
    with open("C:/Users/admin/Downloads/battle.log", 'r', encoding='UTF-8-sig') as f:
        for line in f.readlines():
            dateline, batchno, userid, accid, areaid, battle_info, userpowermap, logindate = line.strip().replace("\n", "").replace("\r", "").split('\t')
            userpowermap = json.loads(userpowermap)
            battle = json.loads(battle_info)
            # 英雄信息
            userHero = battle.get("userHero")
            # 关卡级别
            userExtends = battle.get("userExtends")
            if userHero is not None:
                for hero in userHero:
                    # 英雄id
                    heroId = str(hero.get("heroId"))
                    # 英雄战力
                    ce = userpowermap.get(heroId)
                    # 英雄等级
                    heroLevel = hero.get("heroLevel")
                    # 英雄星级
                    heroStar = hero.get("heroStar")
                    # 皮肤
                    heroSkin = hero.get("heroSkin")

                    # 装备
                    equipments = hero.get("equipments")
                    # if equipments is not None and equipments.size()>0:
                    #     for e in equipments:

                    # #武器
                    # equipmentWeapon = hero.get("equipments")[0]
                    # #铠甲
                    # equipmentArmor = hero.get("equipments")[1]
                    # #头盔
                    # equipmentHelmet = hero.get("equipments")[2]
                    # #鞋子
                    # equipmentShoe = hero.get("equipments")[3]

                    # 突破
                    upgradePriority = hero.get("upgradePriority")
                    # 天赋等级
                    weaponLevel = hero.get("weaponLevel")
                    # 天赋洗炼
                    weaponUpInfo = hero.get("weaponUpInfo")
                    print("\t".join(
                        [dateline, batchno, userid, accid, areaid, logindate, heroId, str(ce), str(heroLevel), str(heroStar),
                         str(heroSkin), str(upgradePriority), str(weaponLevel),str(weaponUpInfo)]))

    # line = read_input(sys.stdin, separator)
    # for dateline,opponent,appver,gametype,status,gameid,hero2,dt in line:
    #     hero = ''
    #     #hero2_arr = json.loads(hero2)
    #     hero2_arr = eval(hero2)
    #     for data in hero2_arr:
    #         if hero == '':
    #             hero = str(data)
    #         else:
    #             hero = hero + '#' + str(data)
    #     print("\t".join([dateline,opponent,appver,gametype,status,gameid,hero,dt]))


if __name__ == '__main__':
    main()
