#!/usr/bin/env python

import wx

class Frame(wx.Frame):
	
	def __init__(self, parent):
	
		wx.Frame.__init__(self, parent, wx.ID_ANY, "fancierHeightConverter")
		self.panel = wx.Panel(self)
		self.promptFeet = wx.StaticText(self.panel, label = "feet", pos = (40, 10))
		self.promptInches = wx.StaticText(self.panel, label = "inches", pos = (195, 10))
		self.feetBox = wx.TextCtrl(self.panel, pos = (75, 10))
		self.inchesBox = wx.TextCtrl(self.panel, pos = (245, 10))

		self.btnEnter = wx.Button(self.panel, label = "Enter", pos = (150, 50))
		self.btnEnter.Bind(wx.EVT_BUTTON, self.OnEnter)
		self.Show()
		
		self.response = wx.StaticText(self.panel, pos = (40, 100))
		
		
	def OnEnter(self, e):
		feet = self.feetBox.GetValue()
		inches = self.inchesBox.GetValue()
		
		try:
			feet = int(feet)
		except:
			wx.MessageBox("I'm sorry, but you didn't enter number for feet, so I will" \
			"assume that you are 0 feet!", "Info", wx.OK | wx.CANCEL)
			self.feetBox.SetValue(str(0))
			feet = 0
			
		try:
			inches = int(inches)
		except:
			wx.MessageBox("I'm sorry, but you didn't enter anything for inches, so I will" \
			"assume that you are 0 inch!", "Info", wx.OK | wx.CANCEL)
			self.inchesBox.SetValue(str(0))
			inches = 0
		
		if inches > 12:
			wx.MessageBox("I don't think inches can be bigger than 12, I will convert" \
			" 12 inches to 1 foot for you!", "Info", wx.OK | wx.CANCEL)
			extraFeet = inches / 12
			self.inchesBox.SetValue(str(inches - extraFeet * 12))
			inches -= extraFeet * 12
			self.feetBox.SetValue(str(feet + extraFeet))
			feet += extraFeet
				
		
		centimeters = 30.48 * feet + 2.54 * inches
		self.response.SetLabel("You height in centimeters is " + str(round(centimeters, 1)))
			
			
# ----------- Main Program Below -----------------

app = wx.App(False)

frame = Frame(None)

app.MainLoop()
