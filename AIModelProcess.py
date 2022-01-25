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
            print ("error line")
            pass


def main(separator='\t'):
    with open("C:/Users/admin/Desktop/ai_model_skin_mid", 'r', encoding='UTF-8-sig') as f:
        for line in f.readlines():
            dateline, batchno, userid, accid, areaid, battle_info = line.strip().replace("\n", "").replace("\r", "").split('\t')
            if dateline=='1642660273849':
                print("--")
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
                    ce = ""
                    # 英雄等级
                    heroLevel = hero.get("heroLevel")
                    # 英雄星级
                    heroStar = hero.get("heroStar")
                    # 皮肤
                    heroSkin = hero.get("heroSkin")
                    # 装备
                    equipments = hero.get("equipments")

                    # 初始化装备
                    equipment_weapon = '0,0,0'
                    equipment_head = '0,0,0'
                    equipment_body = '0,0,0'
                    equipment_shoe = '0,0,0'

                    for e in equipments:
                        # 1手 2头 3身 4脚
                        if e.get("eqpPart")==1:
                            equipment_weapon=str(e.get("quality"))+','+str(e.get("eqpLv"))+','+str(e.get("starLv"))
                        elif e.get("eqpPart")==2:
                            equipment_head=str(e.get("quality"))+','+str(e.get("eqpLv"))+','+str(e.get("starLv"))
                        elif e.get("eqpPart")==3:
                            equipment_body=str(e.get("quality"))+','+str(e.get("eqpLv"))+','+str(e.get("starLv"))
                        elif e.get("eqpPart")==4:
                            equipment_shoe=str(e.get("quality"))+','+str(e.get("eqpLv"))+','+str(e.get("starLv"))
                    # 突破
                    heroStep = hero.get("heroStep")
                    # 天赋等级
                    weaponLevel = hero.get("weaponLevel")
                    # 天赋洗炼
                    weaponUpInfo = hero.get("weaponUpInfo")
                    print("\t".join(
                        [dateline, batchno, userid, accid, areaid, heroId, str(ce), str(heroLevel), str(heroStar),
                         str(heroSkin), str(heroStep), str(weaponLevel), str(weaponUpInfo), equipment_weapon, equipment_head, equipment_body, equipment_shoe]))
    # line = read_input(sys.stdin, separator)
    # for dateline, batchno, userid, accid, areaid, battle_info, userpowermap, logindate in line:
    #     userpowermap = json.loads(userpowermap)
    #     battle = json.loads(battle_info)
    #     # 英雄信息
    #     userHero = battle.get("userHero")
    #     # 关卡级别
    #     userExtends = battle.get("userExtends")
    #     if userHero is not None:
    #         for hero in userHero:
    #             # 英雄id
    #             heroId = str(hero.get("heroId"))
    #             # 英雄战力
    #             ce = ""
    #             # 英雄等级
    #             heroLevel = hero.get("heroLevel")
    #             # 英雄星级
    #             heroStar = hero.get("heroStar")
    #             # 皮肤
    #             heroSkin = hero.get("heroSkin")
    #             # 装备
    #             equipments = hero.get("equipments")
    #
    #             # 初始化装备
    #             equipment_weapon = '0,0,0'
    #             equipment_head = '0,0,0'
    #             equipment_body = '0,0,0'
    #             equipment_shoe = '0,0,0'
    #
    #             for e in equipments:
    #                 # 1手 2头 3身 4脚
    #                 if e.get("eqpPart") == 1:
    #                     equipment_weapon = str(e.get("quality")) + ',' + str(e.get("eqpLv")) + ',' + str(
    #                         e.get("starLv"))
    #                 elif e.get("eqpPart") == 2:
    #                     equipment_head = str(e.get("quality")) + ',' + str(e.get("eqpLv")) + ',' + str(e.get("starLv"))
    #                 elif e.get("eqpPart") == 3:
    #                     equipment_body = str(e.get("quality")) + ',' + str(e.get("eqpLv")) + ',' + str(e.get("starLv"))
    #                 elif e.get("eqpPart") == 4:
    #                     equipment_shoe = str(e.get("quality")) + ',' + str(e.get("eqpLv")) + ',' + str(e.get("starLv"))
    #             # 突破
    #             heroStep = hero.get("heroStep")
    #             # 天赋等级
    #             weaponLevel = hero.get("weaponLevel")
    #             # 天赋洗炼
    #             weaponUpInfo = hero.get("weaponUpInfo")
    #             print("\t".join(
    #                 [dateline, batchno, userid, accid, areaid, heroId, str(ce), str(heroLevel), str(heroStar),
    #                  str(heroSkin), str(heroStep), str(weaponLevel), str(weaponUpInfo), equipment_weapon,
    #                  equipment_head, equipment_body, equipment_shoe]))

if __name__ == '__main__':
    main()
