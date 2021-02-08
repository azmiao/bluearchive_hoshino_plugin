from hoshino.service import Service

svblare = Service('blue-arena-reminder', enable_on_default=False, help_='战术对抗时间提醒', bundle='blue订阅')
msg = '老师，该上碧蓝档案啦，准备好被刺了吗？'

@svblare.scheduled_job('cron', hour='12', minute='45')
async def blue_reminder():
    await svblare.broadcast(msg, 'blue-reminder', 0.2)
