# NVDA命令终结者

*	作者： Ibrahim Hamadeh Ibrahim Hamadeh  
*	下载[稳定版][1]  
*	下载[开发版][2]  
*	NVDA兼容性： 2019.3至2019.4。 
*	Python兼容性。仅Python3  
*	旧版 NVDA，请使用这个[链接][3]  

此插件可以让您以类似游戏的形式，练习 NVDA 台式机或笔记本布局中的键盘命令。
所有的命令数据都抽取自 NVDA 安装目录的 documentation 中的 keyCommands.html。 
该插件没有分配默认的手势快捷键，你必须通过以下方式设置一个：
NVDA菜单 > 选项 > 输入手势 > NVDA命令终结者。 

## 使用方法 ##

*	打开游戏对话框后选择您要练习的键盘布局，然后开始游戏。   
*	然后会显示一个包含了命令、描述和选项的问题，您必须从选项中选择一个正确答案。   
*	如果答对了则增加一分。 
*	如果答错了，分数不便，仍然可以继续作答下一题。 
*	您随时可以退出游戏，退出时，您可以按照提示选择是否保存游戏记录。 
*	日后您如果选择了一个包含记录的键盘布局，会提示您是否从已保存的记录开始游戏。
*	正确回答每个键盘布局中的大约 88 个问题后，您将被宣布获胜并取得“NVDA杯”冠军称号。


### 2.3版更新日志 ###

*	更改了各种声音事件的音效，以取消在游戏过程中因播放音效而产生的延时。
*	使用最新的 NVDA 插件模板。
*	如果命令显示为'None'，表示未分配，现在将显示为'Unassigned'。

### 2.1版更新日志 ###

*	增加了俄语翻译。

### 2.0版更新日志 ###

*	使插件仅兼容 Python3。
*	更改了 scraped 表索引以适配 keyCommands.html 文件的变更。 

### 1.2版更新日志 ###

*	在游戏开始时默认选中当前键盘布局
*	在回答正确，回答错误和游戏结束时添加音效

### 1.1版更新日志 ###
*	初始版本。

[1]: https://github.com/ibrahim-s/trainingNvdaCommands/releases/download/v2.13/trainingKeyboardCommands-2.13.nvda-addon

[2]: https://github.com/ibrahim-s/trainingNvdaCommands/releases/download/v2.1dev/trainingKeyboardCommands-2.1-dev.nvda-addon

[3]: https://github.com/ibrahim-s/trainingNvdaCommands/releases/download/v1.3dev/trainingKeyboardCommands-1.3-dev.nvda-addon

**简体中文译者： Cary-rowen**