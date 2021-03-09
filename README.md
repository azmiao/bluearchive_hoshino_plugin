
## 插件代码非原创，只是由ICE咖啡大佬的hoshinobot修改而来，已经他本人授权
原版链接：https://github.com/Ice-Cirno/HoshinoBot/

## 本插件仅供研究学习使用，请勿用于商业用途

## 03-09正式弃坑档案，问就是沉迷赛马娘

02-24
前端时间一直较忙，这两天突然对档案没啥兴趣了，应该不会经常更新了，虽然没改完，有兴趣的大佬可以自己把剩下的改改完
档案的新闻网页是可以直连的，他的10026端口是开放的，页面转码一下就行，我试过了正则表达式也能匹配出正确的链接，
匹配成item形式应该就好整了（门外汉的想法，大佬勿喷），链接https://bluearchive.jp:10026/news/detail

## 更新日志

21-02-24    release 里更新了一个万一报错的解决方案（原因是大家Hoshino版本不一样）

21-02-08    v1.0    先用着吧

## bluearchive_hoshino_plugin
一个适用hoshinobot的碧蓝档案Blue Archive插件
功能如下：

-非指令类：

  竞技场结算提醒blue-arena-reminder

-指令类相关：

  [@bot档案十连] 十连转蛋

  [@bot档案单抽] 单抽转蛋

  [@bot档案来一井] 一井

  [档案查看卡池] 查看现在的卡池

  [档案谁是xxx] 查询档案角色

其他hoshino的功能还没改完，啥时候有空再改吧

## 项目地址：
https://github.com/azmiao/bluearchive_hoshino_plugin/

## 食用教程

### step 1
在 HoshinoBot\hoshino\modules 目录下使用以下命令拉取本项目
```
git clone https://github.com/azmiao/bluearchive_hoshino_plugin
```
### step 2
在 HoshinoBot\hoshino\config_bot_.py 文件的 MODULES_ON 加入 ‘bluearchive_hoshino_plugin’

### step 3
放置图片资源包
将步骤1中拉取的bluearchive_hoshino_plugin文件夹中的bluearchive文件夹剪贴到\HoshinoBot\res\img目录下

### step 4
重启hoshinobot即可使用

### 额外
在群内发送
```
开启 blue-arena-reminder
```
即可开启碧蓝档案竞技场提醒
