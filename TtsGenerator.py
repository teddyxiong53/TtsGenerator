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

# 创建mainWin类并传入wx_windows.MainFrame
class mainWin(wx_windows.MainFrame):
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    def OnButtonGenTts(self, event):
        # 先判断文本是否为空
        # 为空则提示错误
        text = self.m_textCtrlInputText.GetValue().strip()

        if len(text) == 0:
            self.m_statusBar1.SetStatusText(TEXT_IS_EMPTY)
            return
        debug("person:",Config.PERSON)

        result = self.client.synthesis(text, 'zh', 1, {
            'vol': int(Config.VOLUME),
            'per': int(Config.PERSON),
            'spd': int(Config.SPEED),
            'pit': int(Config.TONE),
            'aue': int(Config.AUE)
        })

        debug("len of result:",len(result))
        debug("type of result", isinstance(result, dict))
        # 判断是否合成出错
        if not isinstance(result, dict):
            with open(Config.AUDIO_OUTPUT_DIR+'tts.wav', 'wb') as f:
                f.write(result)
        else:
            debug(result)
            self.m_statusBar1.SetStatusText(TTS_GEN_FAIL)
            return
        self.m_statusBar1.SetStatusText(TTS_GEN_OK)
    def OnButtonOpenDir(self, event):
        os.system("explorer.exe " + os.path.abspath(Config.AUDIO_OUTPUT_DIR))

    def OnMenuExit(self, event):
        self.OnClose(event)

    def OnMenuAbout(self, event):
        dialogAbout = wx_windows.DialogAbout(self)
        dialogAbout.m_staticText1.SetLabel(Config.SOFTWARE_NAME+Config.SOFTWARE_VERSION+'\n'+Config.SOFTWARE_AUTHOR)
        dialogAbout.ShowModal()

def initDir():
    # 如果没有audio_output目录。创建
    if not os.path.exists(Config.AUDIO_OUTPUT_DIR):
        os.mkdir(Config.AUDIO_OUTPUT_DIR)
def initLog():
    logging.basicConfig(filename='TtsGenerator.log', level=logging.DEBUG, format=Config.LOG_FORMAT)

if __name__ == '__main__':
    initLog()
    Config.initConfig()
    initDir()

    info('打开软件')
    # 下面是使用wxPython的固定用法
    # 这个是把输出重定向到文件里。
    # app = wx.App(redirect=True, filename="output.log")
    app = wx.App()
    main_win = mainWin(None)
    main_win.SetTitle(Config.SOFTWARE_NAME + Config.SOFTWARE_VERSION)
    main_win.Show()
    app.MainLoop()
