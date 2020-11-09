# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 700,400 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE|wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( -1,-1 ), wx.Size( -1,-1 ) )

		self.m_statusBar1 = self.CreateStatusBar( 1, wx.STB_SIZEGRIP, wx.ID_ANY )
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItemExit = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"退出", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItemExit )

		self.m_menubar1.Append( self.m_menu1, u"文件" )

		self.m_menu3 = wx.Menu()
		self.m_menuItemAbout = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"关于", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.Append( self.m_menuItemAbout )

		self.m_menubar1.Append( self.m_menu3, u"帮助" )

		self.SetMenuBar( self.m_menubar1 )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"发声人", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer4.Add( self.m_staticText2, 0, wx.ALL, 5 )

		m_choicePersonChoices = [ u"普通女声", u"普通男声", u"情感女声", u"情感男声" ]
		self.m_choicePerson = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choicePersonChoices, 0 )
		self.m_choicePerson.SetSelection( 0 )
		bSizer4.Add( self.m_choicePerson, 0, wx.ALL, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"语速", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer4.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.m_sliderSpeed = wx.Slider( self, wx.ID_ANY, 5, 0, 9, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL|wx.SL_MIN_MAX_LABELS|wx.SL_VALUE_LABEL )
		bSizer4.Add( self.m_sliderSpeed, 0, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"音调", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer4.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.m_sliderTone = wx.Slider( self, wx.ID_ANY, 5, 0, 9, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL|wx.SL_MIN_MAX_LABELS|wx.SL_VALUE_LABEL )
		bSizer4.Add( self.m_sliderTone, 0, wx.ALL, 5 )

		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"音量", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		bSizer4.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.m_sliderVolume = wx.Slider( self, wx.ID_ANY, 5, 0, 15, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL|wx.SL_MIN_MAX_LABELS|wx.SL_VALUE_LABEL )
		bSizer4.Add( self.m_sliderVolume, 0, wx.ALL, 5 )

		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"格式", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		bSizer4.Add( self.m_staticText6, 0, wx.ALL, 5 )

		m_choiceFormatChoices = [ u"mp3", u"wav" ]
		self.m_choiceFormat = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceFormatChoices, 0 )
		self.m_choiceFormat.SetSelection( 1 )
		bSizer4.Add( self.m_choiceFormat, 0, wx.ALL, 5 )


		bSizer2.Add( bSizer4, 1, wx.EXPAND, 5 )

		bSizer21 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_buttonGenTts = wx.Button( self, wx.ID_ANY, u"生成音频文件", wx.DefaultPosition, wx.Size( 400,50 ), 0 )
		bSizer21.Add( self.m_buttonGenTts, 0, wx.ALL, 5 )

		self.m_buttonOpenDir = wx.Button( self, wx.ID_ANY, u"打开文件目录", wx.DefaultPosition, wx.Size( 300,50 ), 0 )
		bSizer21.Add( self.m_buttonOpenDir, 0, wx.ALL, 5 )


		bSizer2.Add( bSizer21, 1, wx.EXPAND, 5 )

		gSizer2 = wx.GridSizer( 1, 1, 0, 0 )

		self.m_textCtrlInputText = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 680,200 ), 0 )
		gSizer2.Add( self.m_textCtrlInputText, 0, wx.ALL, 5 )


		bSizer2.Add( gSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()
		self.m_toolBar1 = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY )
		self.m_toolBar1.Realize()


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.OnClose )
		self.Bind( wx.EVT_MENU, self.OnMenuExit, id = self.m_menuItemExit.GetId() )
		self.Bind( wx.EVT_MENU, self.OnMenuAbout, id = self.m_menuItemAbout.GetId() )
		self.m_choicePerson.Bind( wx.EVT_CHOICE, self.OnChoicePerson )
		self.m_sliderSpeed.Bind( wx.EVT_SCROLL, self.OnScrollSpeed )
		self.m_sliderTone.Bind( wx.EVT_SCROLL, self.OnScrollTone )
		self.m_sliderVolume.Bind( wx.EVT_SCROLL, self.OnScrollVolume )
		self.m_choiceFormat.Bind( wx.EVT_CHOICE, self.OnChoiceFormat )
		self.m_buttonGenTts.Bind( wx.EVT_BUTTON, self.OnButtonGenTts )
		self.m_buttonOpenDir.Bind( wx.EVT_BUTTON, self.OnButtonOpenDir )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnClose( self, event ):
		event.Skip()

	def OnMenuExit( self, event ):
		event.Skip()

	def OnMenuAbout( self, event ):
		event.Skip()

	def OnChoicePerson( self, event ):
		event.Skip()

	def OnScrollSpeed( self, event ):
		event.Skip()

	def OnScrollTone( self, event ):
		event.Skip()

	def OnScrollVolume( self, event ):
		event.Skip()

	def OnChoiceFormat( self, event ):
		event.Skip()

	def OnButtonGenTts( self, event ):
		event.Skip()

	def OnButtonOpenDir( self, event ):
		event.Skip()


###########################################################################
## Class DialogAbout
###########################################################################

class DialogAbout ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"关于", pos = wx.DefaultPosition, size = wx.Size( 400,150 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"版本：V1.0\n作者：熊汉良", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		bSizer3.Add( self.m_staticText1, 0, wx.ALL, 5 )

		m_sdbSizer1 = wx.StdDialogButtonSizer()
		self.m_sdbSizer1OK = wx.Button( self, wx.ID_OK )
		m_sdbSizer1.AddButton( self.m_sdbSizer1OK )
		m_sdbSizer1.Realize();

		bSizer3.Add( m_sdbSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


