from hoshino import Service

sv_help = '''
[档案挖矿15001] 档案矿场余钻             # 这个还没整
[档案谁是xcw] 档案角色别称查询
'''.strip()

sv = Service('blue-query', help_=sv_help, bundle='bluearchive查询')

from .whois import *
# from .miner import *
