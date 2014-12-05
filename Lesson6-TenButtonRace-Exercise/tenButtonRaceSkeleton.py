#! /usr/bin/evn python

import wx #import the graphical library
import time #import the time module
from random import randint


class TenButtonFrame(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Ten Button Race")
		
		#Make a new Panel
		self.panel = wx.Panel(self)
		
		#Make the start button
		self.btnStartButton = wx.Button(self.panel, label = "start", pos = (150, 90))
		self.btnStartButton.Bind(wx.EVT_BUTTON, self.OnStart)
		#Make the other ten buttons
		
		self.buttons = []
		
		for i in range(10):
			a = randint(0, 275)
			b = randint(0, 190)
			self.buttons.append(wx.Button(self.panel, label = "button " + str(i + 1), pos = (a, b)))
			self.buttons[i].Show(False)
			self.buttons[i].Bind(wx.EVT_BUTTON, self.OnButtons)

		
	# Event handler for the start button
	def OnStart(self, e):
		self.btnStartButton.Show(False) #Make the start button disappear
		self.startTime = time.time()
		self.buttons[0].Show(True) #Make Button One appear
		

	def OnButtons(self, e):
		clickedButton = e.GetEventObject()
		clickedButton.Show(False)
		for i in range(10):
			if clickedButton == self.buttons[i]:
				if i <= 8:
					self.buttons[i + 1].Show(True)
				if i == 9:
					self.endTime = time.time()
					resultTime = self.endTime - self.startTime
					resultTime = round(resultTime, 2)
					self.result = wx.StaticText(self.panel, label = \
					"Your total time to finish click is {}s".format(resultTime), \
					pos = (76, 7))

	
	#Remember the last event handler needs to print the final time.
	
	
# -------- Main Program Below ------------

app = wx.App(False)
frame = TenButtonFrame(None)
frame.Show()
app.MainLoop()