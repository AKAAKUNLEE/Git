# 1.导入需要使用的包
import pandas as pd
import json

# 2.读取数据
# GB2312/utf9/ISO-8859-1/GB18030
with open('HeroRaceCfg.json', 'r', encoding="ISO-8859-1") as fp:
    datas = json.load(fp)
    print('这是文件中的json数据：', datas)
    print('这是读取到文件数据的数据类型：', type(datas))
    datas_string = json.dumps(datas)
    datas_string.replace("'\x80", '')
    print(type(datas_string))
    print(datas_string)

# 3.做数据变量方便后续引用
data = datas['data']
data_records_list = data['records']

# 4.原数据储存到列表中，接着映射列名，再用pd.DataFrame展示出
erp_adsList = []
for y in range(len(data_records_list)):
    Id = data_records_list[y]['Id']
    RaceID = data_records_list[y]['RaceID']
    RaceLevel = data_records_list[y]['RaceLevel']
    SpineID = data_records_list[y]['SpineID']
    RaceReward = data_records_list[y]['RaceReward']
    RaceName = data_records_list[y]['RaceName']
    Desc = data_records_list[y]['Desc']
    Icon = data_records_list[y]['Icon']
    LifeTime = data_records_list[y]['LifeTime']
    HPMax = data_records_list[y]['HPMax']
    MPMax = data_records_list[y]['MPMax']
    Resume = data_records_list[y]['Resume']
    Damage = data_records_list[y]['Damage']
    Defence = data_records_list[y]['Defence']
    Magic = data_records_list[y]['Magic']
    Knowledge = data_records_list[y]['Knowledge']
    Speed = data_records_list[y]['Speed']
    Critical = data_records_list[y]['Critical']
    Accuracy = data_records_list[y]['Accuracy']
    Dodge = data_records_list[y]['Dodge']
    ResistCritical = data_records_list[y]['ResistCritical']
    MoneyLuck = data_records_list[y]['MoneyLuck']
    Lucky = data_records_list[y]['Lucky']
    InitGold = data_records_list[y]['InitGold']
    Talent1 = data_records_list[y]['Talent1']
    Talent2 = data_records_list[y]['Talent2']
    Talent3 = data_records_list[y]['Talent3']
    Talent4 = data_records_list[y]['Talent4']
    Talent5 = data_records_list[y]['Talent5']
    Talent6 = data_records_list[y]['Talent6']
    SkillCard = data_records_list[y]['SkillCard']
    NeedSilverTurnip = data_records_list[y]['NeedSilverTurnip']
    NeedGoldTurnip = data_records_list[y]['NeedGoldTurnip']
    FragmentId = data_records_list[y]['FragmentId']
    lists = {'角色ID': Id, '种族ID': RaceID, '种族等级': RaceLevel, '脊柱ID': SpineID, '种族奖励': RaceReward,
             '种族名称': RaceName,
             '描述': Desc, '图标': Icon, '生命周期': LifeTime, '最大生命值': HPMax, '最大法力值': MPMax,
             '恢复能力': Resume,
             '伤害': Damage, '防御': Defence, '魔法': Magic, '知识': Knowledge, '速度': Speed, '爆击率': Critical,
             '精确度': Accuracy,
             '闪避率': Dodge, '闪避暴击率': ResistCritical, '钱运': MoneyLuck, '运气': Lucky, '初始金币': InitGold,
             '天赋1': Talent1,
             '天赋2': Talent2, '天赋3': Talent3, '天赋4': Talent4, '天赋5': Talent5, '天赋6': Talent6,
             '技能卡': SkillCard,
             '需要银币萝卜': NeedSilverTurnip, '需要金币萝卜': NeedGoldTurnip, '片段ID': FragmentId}
    erp_adsList.append(lists)
erpTotalData = pd.DataFrame(erp_adsList)
'''# 5.将数据里的值映射成更明确的含义
state_name = {0: '启用',
              1: '暂停'}
servingStatus_name = {'CAMPAIGN_OUT_OF_BUDGET': '广告活动超出预算',
                      'AD_GROUP_STATUS_ENABLED': '正在投放',
                      'CAMPAIGN_PAUSED': '广告活动已暂停'}
tactic_name = {'T00030': '-',
               'T00020': '商品投放'}
erpTotalData['有效'] = erpTotalData['有效'].map(state_name)
erpTotalData['状态'] = erpTotalData['状态'].map(servingStatus_name)
erpTotalData['投放类型'] = erpTotalData['投放类型'].map(tactic_name)
erpTotalData
'''
# 6.保存到Excel
erpTotalData.to_excel('HeroRaceCfg.xlsx', sheet_name='数据', index=False)
