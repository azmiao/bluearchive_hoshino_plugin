'''碧蓝档案Blue Archive的游戏数据'''
'''数据更新日期21-02-08'''

'''角色名称

遵照格式： id: [中文直译, 日文原名, 英文名(罗马音), 中文直译（日文汉字姓氏+名）, 别称] （<-依此顺序）(全部格式参考原版hoshino)
日文用全角括号，英文用半角括号

说明：游戏解包资源没有官方id，只有官方英文名，所以下方Id按解包资源文件顺序排序，后续若有新角色应该就直接放在后面，不插队了
英文名来自游戏资源解包，日文名来自游戏内部，中文名为直译，中文姓氏为日文汉字

'''
CHARA_NAME = {
    1000: ["NPC_Null", "Null"],
    1001: ["爱莉", "アイリ", "Airi", "栗村爱莉"],
    # 1002: ["阿比多斯", "アビドス", "Abidosu"],
    1003: ["茜", "アカネ", "Akane", "室笠茜", "破甲女仆"],
    1004: ["明里", "アカリ", "Akari", "鰐渕明里", "吃货", "牛牛", "阿卡林", "手榴弹", "WTM"],
    # 1005: ["爱丽丝", "アリス", "Alice"], 
    1006: ["阿露", "アル", "Aru", "陸八魔阿露", "愉悦姐", "社长", "粉毛狙"],
    1007: ["明日奈", "アスナ", "Asuna", "一之瀬明日奈"],
    # 1008: ["", "", "Atsuko"],  #已有解包资源但暂未实装
    1009: ["绫音", "アヤネ", "Ayane", "奥空绫音", "会计", "眼镜奶"],
    # 1010: ["梓", "アズサ", "Azusa"],  #已有解包资源但暂未实装
    # 1011: ["琪莉诺", "チェリノ", "Cherino"],  #已有解包资源但暂未实装
    1012: ["千夏", "チナツ", "Chinatsu", "火宫千夏"],
    1013: ["千世", "チセ", "Chise", "和楽千世", "雷姆", "青鬼"],
    1014: ["艾米", "エイミ", "Eimi", "和泉元艾米", "爱米"],
    # 1015: ["绘梨香", "エリカ", "Erica"],
    1016: ["枫香", "フウカ", "Fuuka", "爱清枫香", "料理妹"],
    # 1017: ["格赫纳", "ゲヘナ", "Gehenna"],
    1018: ["花江", "ハナエ", "Hanae", "朝颜花江", "天使妹", "天使"],
    1019: ["晴", "ハレ", "Hare", "小钩晴", "无人机"],
    1020: ["春香", "ハルカ", "Haruka", "伊草春香"],
    1021: ["晴奈", "ハルナ", "Haruna", "黒舘晴奈", "美食会长", "神秘狙"],
    1022: ["莲见", "ハスミ", "Hasumi", "羽川莲见", "委员长", "女天狗"],
    1023: ["日引", "ヒビキ", "Hibiki", "猫塚日引", "鲁班"],
    1024: ["日富美", "ヒフミ", "Hihumi", "白富美"],
    1025: ["日奈", "ヒナ", "Hina", "空崎日奈", "魔王"],
    1026: ["星野", "ホシノ", "Hoshino", "小鳥遊星野", "粉毛", "粉毛盾", "霰弹盾"], # 她也叫hoshino可还行
    1027: ["伊织", "イオリ", "Iori", "銀鏡伊织", "佐仓", "佐仓狙"],
    1028: ["和泉", "イズミ", "Izumi", "獅子堂和泉", "汉堡妹"],
    1029: ["朱莉", "ジュリ", "Juli", "牛牧朱莉", "料理姐"],
    1030: ["花梨", "カリン", "Karin", "角楯花梨", "黑皮女仆", "黑皮狙", "女仆狙"],
    1031: ["佳代子", "カヨコ", "Kayoko", "鬼形佳代子", "恐惧姐"],
    # 1032: ["雾野", "キリノ", "Kirino"],
    # 1033: ["小春", "コハル", "Koharu"],
    1034: ["小玉", "コタマ", "Kotama", "音瀬小玉"],
    1035: ["柯托莉", "コトリ", "Kotori", "豊見柯托莉", "机枪盾"],
    1036: ["真希", "マキ", "Maki", "小塗真希", "破甲妹", "彩蛋妹"],
    # 1037: ["玛丽", "マリー", "Marie"],
    # 1038: ["益子", "マシロ", "Mashiro"],  #已有解包资源但暂未实装
    # 1039: ["绿", "ミドリ", "Midori"],
    # 1040: ["千禧", "ミレニアム", "Millennium"],
    # 1041: ["", "", "Miyako"],  #已有解包资源但暂未实装
    # 1042: ["桃井", "モモイ", "Momoi"],
    1043: ["睦月", "ムツキ", "Mutsuki", "浅黄睦月", "地雷妹"],
    1044: ["妮露", "ネル", "Neru", "美甘妮露", "暴躁姐"],
    1045: ["野宫", "ノノミ", "Nonomi", "十六夜野宫", "富婆", "机枪妹"],
    1046: ["菲娜", "フィーナ", "Fina", "朝比奈菲娜"],
    # 1047: ["莱德温达", "レッドウィンター", "Red winter],
    1048: ["纱绫", "サヤ", "Saya", "薬子紗綾", "老鼠妹", "鼠妹", "老鼠"],
    1049: ["芹香", "セリカ", "Serika", "黒見芹香", "黑猫", "战神", "梓猫", "梓喵", "阿梓喵"],
    1050: ["芹娜", "セリナ", "Serina", "鷲見芹娜", "护士妹", "护士"],
    1051: ["志美子", "シミコ", "Simiko ", "円堂志美子"],
    1052: ["白子", "シロコ", "Shiroko", "砂狼白子", "xcw", "小仓唯"],
    1053: ["瞬", "シュン", "Shun", "春原瞬", "教官"],
    1054: ["菫", "スミレ", "Sumire", "乙花菫", "堇", "运动部长", "运动妹"],
    1055: ["玲美", "スズミ", "Suzuki", "守月玲美"],
    # 1056: ["", "", "Suzumi"],  #已有解包资源但暂未实装
    # 1057: ["特立尼蒂", "トリニティ", "Trinity"],
    1058: ["椿", "ツバキ", "Tsubaki", "春日椿", "奈奈", "狗盾"],
    1059: ["鹤城", "ツルギ", "Tsurugi", "剣崎鹤城", "颜艺姐"],
    1060: ["歌原", "ウタハ", "Utaha", "白石歌原", "炮台妹"],
    # 1061: ["瓦尔古雷", "ヴァルキューレ", "Valkyrie"],
    # 1062: ["", "", "Wakamo"],  #已有解包资源但暂未实装
    1063: ["好美", "ヨシミ", "Yoshimi", "伊原木好美", "傲娇"],
    1064: ["佑香", "ユウカ", "Yuuka", "早瀬佑香", "女主", "蓝毛", "计算器"],
    1065: ["淳子", "ジュンコ", "Zunko", "赤司淳子", "琴里", "红毛"],


    # ================NPC================ #
    1901: ["阿罗那(NPC助理)", "アロナ", "Arona", "助理"],
    1902: ["莫莫香(NPC)", "もも化", "Momoka"],
    1903: ["凛(NPC)", "リン", "Rin"],


}
