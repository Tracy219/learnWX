#! /usr/bin/evn python

import wx #import the graphical library
import time #import the time module
from random import randint
from specialInput import *


class TenButtonFrame(wx.Frame):
	
	def __init__(self, parent, buttonNumber):
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Click Button Race")
		
		#Make a new Panel
		self.panel = wx.Panel(self)
		
		#Make the start button
		self.btnStartButton = wx.Button(self.panel, label = "start", pos = (150, 90))
		self.btnStartButton.Bind(wx.EVT_BUTTON, self.OnStart)
		#Make the other ten buttons
		
		self.buttons = []
		
		for i in range(buttonNumber):
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
		for i in range(buttonNumber):
			if clickedButton == self.buttons[i]:
				if i <= buttonNumber - 2:
					self.buttons[i + 1].Show(True)
				if i == buttonNumber - 1:
					self.endTime = time.time()
					resultTime = self.endTime - self.startTime
					resultTime = round(resultTime, 2)
					self.result = wx.StaticText(self.panel, label = \
					"Your total time to finish click is {}s".format(resultTime), \
					pos = (76, 7))

	
	#Remember the last event handler needs to print the final time.
	
	
# -------- Main Program Below ------------

app = wx.App(False)
buttonNumber = int_input("How many buttons wolud you like to be in this race? ")
frame = TenButtonFrame(None, buttonNumber)
frame.Show()
app.MainLoop()