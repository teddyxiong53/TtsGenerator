# coding: utf-8
from __future__ import print_function
import wx
import wx_windows
import logging
from logging import debug, error, info

# from Config import *
import Config

import sys, os

from aip import AipSpeech

APP_ID = '11234074'
API_KEY = 'wNqEyF2KysMTiOcSt3HEZYhcvb0hjriX'
SECRET_KEY = '97UrqLeyNXhjtLeqL5XNPxYvAEQsGb7S'

TEXT_IS_EMPTY = '请在输入框输入要合成的文字内容再试'
TTS_GEN_FAIL = 'TTS合成出错了，请重试'

TTS_GEN_OK = 'TTS合成成功'

# 这个是快速切换打印跟日志的方式
# debug = print

# 创建mainWin类并传入wx_windows.MainFrame
class mainWin(wx_windows.MainFrame):
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    def getPerson(self):
        person = (0,'普通女声')
        if Config.globalParam['person'] == 0:
            person = (0,'普通女声')
        elif Config.globalParam['person'] == 1:
            person = (1,'普通男声')
        elif Config.globalParam['person'] == 2:
            person = (3, '情感女声')
        elif Config.globalParam['person'] == 3:
            person = (4, '情感男声')
        elif Config.globalParam['person'] == 4: #后面的都没有权限。界面上去掉了。
            person = (5, '度小娇')
        elif Config.globalParam['person'] == 5:
            person = (103, '度米朵')
        elif Config.globalParam['person'] == 6:
            person = (111,'度小萌')
        elif Config.globalParam['person'] == 7:
            person = (110,'度小童')
        elif Config.globalParam['person'] == 8:
            person = (106,'度博文')
        elif Config.globalParam['person'] == 9:
            person = (5118,'度小鹿')
        elif Config.globalParam['person'] == 10:
            person = (5003,'度逍遥')
        else:
            person = (0,'普通女声')
        return person
    def getFormat(self):
        format = 6

        if Config.globalParam['format'] == 0:
            format = 3
        else:
            format = 6
        return format

    def initUi(self):
        # 这个是为了把界面参数显示正确
        self.m_choicePerson.SetSelection(Config.globalParam['person'])
        self.m_sliderSpeed.SetValue(Config.globalParam['speed'])
        self.m_sliderTone.SetValue(Config.globalParam['tone'])
        self.m_sliderVolume.SetValue(Config.globalParam['volume'])
        self.m_choiceFormat.SetSelection(Config.globalParam['format'])

    def OnButtonGenTts(self, event):

        # 先判断文本是否为空
        # 为空则提示错误
        text = self.m_textCtrlInputText.GetValue().strip()

        if len(text) == 0:
            self.m_statusBar1.SetStatusText(TEXT_IS_EMPTY)
            return

        person = self.getPerson()[0]
        format = self.getFormat()

        result = self.client.synthesis(text, 'zh', 1, {
            'vol': int(Config.globalParam['volume']),
            'per': int(person),
            'spd': int(Config.globalParam['speed']),
            'pit': int(Config.globalParam['tone']),
            'aue': int(format)
        })

        debug("len of result:", len(result))
        debug("type of result", isinstance(result, dict))
        # 判断是否合成出错
        if not isinstance(result, dict):
            filename = Config.AUDIO_OUTPUT_DIR
            # 文件名，需要跟参数配合起来。这样方便进行各种参数测试时对比。
            filename += "发音人_" + str(self.getPerson()[1]) + '-' \
                + '语速_' + str(Config.globalParam['speed']) + '-' \
                + '音调_' + str(Config.globalParam['tone']) + '-' \
                + '音量_' + str(Config.globalParam['volume'])
            if Config.globalParam['format'] == 0:
                filename += '.mp3'
            else:
                filename += '.wav'
            with open(filename, 'wb') as f:
                f.write(result)
        else:
            print(result)
            self.m_statusBar1.SetStatusText(TTS_GEN_FAIL)
            return
        self.m_statusBar1.SetStatusText(TTS_GEN_OK)

    def OnButtonOpenDir(self, event):
        os.system("explorer.exe " + os.path.abspath(Config.AUDIO_OUTPUT_DIR))

    def OnMenuExit(self, event):
        self.OnClose(event)
    def OnClose( self, event ):
        debug('关闭软件')
        Config.writeConfig()
        wx.Exit()

    def OnMenuAbout(self, event):
        dialogAbout = wx_windows.DialogAbout(self)
        dialogAbout.m_staticText1.SetLabel(
            Config.SOFTWARE_NAME + Config.SOFTWARE_VERSION + '\n' + Config.SOFTWARE_AUTHOR)
        dialogAbout.ShowModal()

    def OnChoicePerson(self, event):
        selection = self.m_choicePerson.GetSelection()
        print(selection)
        # 得到的是数字
        # 可以写入到参数文件。
        Config.globalParam['person'] = selection
        # 不宜在这里写入，因为拖动的时候，会连续改动。
        # 在退出时进行写入就好了。
        # Config.writeConfig()

    def OnScrollSpeed(self, event):
        val = self.m_sliderSpeed.GetValue()
        print(val)
        Config.globalParam['speed'] = val

    def OnScrollTone(self, event):
        val = self.m_sliderTone.GetValue()
        print(val)
        Config.globalParam['tone'] = val

    def OnScrollVolume(self, event):
        val = self.m_sliderVolume.GetValue()
        print(val)
        Config.globalParam['volume'] = val

    def OnChoiceFormat(self, event):
        selection = self.m_choiceFormat.GetSelection()
        print(selection)
        # 得到的是数字
        # 可以写入到参数文件。
        Config.globalParam['format'] = selection


def initDir():
    # 如果没有audio_output目录。创建
    if not os.path.exists(Config.AUDIO_OUTPUT_DIR):
        os.mkdir(Config.AUDIO_OUTPUT_DIR)


def initLog():
    logging.basicConfig(filename='TtsGenerator.log', level=logging.DEBUG, format=Config.LOG_FORMAT)


if __name__ == '__main__':
    initLog()
    Config.readConfig()
    initDir()

    info('打开软件')
    # 下面是使用wxPython的固定用法
    # 这个是把输出重定向到文件里。
    # app = wx.App(redirect=True, filename="output.log")
    app = wx.App()
    main_win = mainWin(None)
    main_win.SetTitle(Config.SOFTWARE_NAME + Config.SOFTWARE_VERSION)
    main_win.initUi()
    main_win.Show()
    wx.Yield()
    app.MainLoop()
