from hoshino.typing import CQEvent, MessageSegment
from hoshino.util import FreqLimiter

from .. import chara
from . import sv

lmt = FreqLimiter(5)

@sv.on_prefix(('档案谁是'))
async def whois(bot, ev: CQEvent):
    uid = ev.user_id
    if not lmt.check(uid):
        await bot.send(ev, f'这是bug：查询技能冷却中(剩余 {int(lmt.left_time(uid)) + 1}秒)', at_sender=True)
        return
#    lmt.start_cd(uid)

    name = ev.message.extract_plain_text().strip()
    if not name:
        await bot.send(ev, '请发送"档案谁是"+别称，如"档案谁是xcw"')
        return
    id_ = chara.name2id(name)
    confi = 100
    if id_ == chara.UNKNOWN:
        id_, guess_name, confi = chara.guess_id(name)
    c = chara.fromid(id_)
    
    msg = ''
    if confi < 100:
        #lmt.start_cd(uid, 120)
        msg = f'碧蓝档案似乎没有叫"{name}"的人欸'
        await bot.send(ev, msg)
        msg = f'\n您有{confi}%的可能在找{guess_name} '

    if confi > 60:
        msg += f'{c.icon.cqcode} {c.name}'
        await bot.send(ev, msg, at_sender=True)
