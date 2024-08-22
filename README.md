这个python文件利用azure语音转文字，文字转语音服务生成wav格式的语音播报文件


ipod文件方法如下：
使用电脑链接ipod
在\iPod_Control\Speakable中有各种voiceover语音
Track文件下，里边包含每个歌曲的歌名信息（使用脚本更换语音）
Messgaes下包含各种系统提示如电量提醒，回复模式等（可使用脚本更换语音）

其他文件夹下有音量声音，关机提示音等，也可自行更换


脚本使用指南：

首先注册azure账号，开通speech stdio，获取密钥（请查阅b站教程，也可以联系我帮你转换）

在python中替换你的密钥

将想要更换语音的wav文件放置到input文件下
运行python
将output中的文件替换到ipod原位置中
大功告成


测试环境：
Windows11
iPod shuffle4
python3.6






第一次做项目，如果哪里有问题欢迎提问，如果可以帮到你也可以点个star
