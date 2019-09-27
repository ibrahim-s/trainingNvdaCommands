# -*- coding: utf-8 -*-
#Copyright (C) 2019 ibrahim hamadeh
#this addon is under GNU general public license2.0
#An addon like game to train nvda commands for desktop and labtop layouts.

import wx
import gui
import config
import winsound
import time
import os, sys
import pickle
import random
import addonHandler
addonHandler.initTranslation()

#current directory
CURRENT_DIR= os.path.abspath(os.path.dirname(__file__))
#locale path of keyCommands.html in Nvda documentation files.
keyCommands_path= gui.getDocFilePath("keyCommands.html")
current_lang= os.path.basename(os.path.dirname(keyCommands_path))
#file path of saved data if the user wishes to save remaining questions
filepath= os.path.join(CURRENT_DIR, 'savedData', current_lang, 'data.pickle')
#path of sound files
sound_path= os.path.join(os.path.dirname(__file__), "..", "..", "sounds")

class QuestionObj():
	def __init__(self, sublist=[]):
		self.question= sublist[0]
		tempChoices= sublist[1]
		self.answer= tempChoices[0]
		self.help= tempChoices

	@staticmethod
	def populateList(currentList):
		''' Make list of question objects out of the list containing the necessary informations for that. '''
		lst=[]
		tempList= currentList[:]
		for i in tempList:
			question= QuestionObj(i)
			lst.append(question)
		random.shuffle(lst)
		return lst

class Game(wx.Dialog):
	def __init__(self, parent):
		super(Game, self).__init__(parent, title='Training Nvda Commands', 
			size=(400, 450))

		self.allQuestions=[]
		self.question=None
		self.score=0
		self.savedData= {}
		self.layoutMode= ""

		panel = wx.Panel(self)
		vbox = wx.BoxSizer(wx.VERTICAL)
		hbox1 = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: label for the score value at the beginning of the game
		self.scoreText = wx.StaticText(panel, label=_('Your Score: 0'))
		hbox1.Add(self.scoreText)
		vbox.Add(hbox1, flag=wx.LEFT | wx.TOP, border=10)
		vbox.Add((-1, 10))
		hbox2 = wx.BoxSizer(wx.HORIZONTAL)
		self.tcQuestion = wx.TextCtrl(panel, -1, size=(350, 250), style=wx.TE_READONLY|wx.TE_MULTILINE)
		hbox2.Add(self.tcQuestion, proportion=1, flag=wx.EXPAND)
		vbox.Add(hbox2, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, border=10)
		vbox.Add((-1, 25))

		hbox3 = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: label for the cumbo box of options for correct answer
		staticListText=wx.StaticText(panel, -1, label= _('Choose Option'))
		self.answerObtionsCumbo= wx.Choice(panel, -1, choices= [])
		hbox3.Add(staticListText,0, wx.ALL, 10)
		hbox3.Add(self.answerObtionsCumbo, 1, flag=wx.RIGHT, border=10)
		vbox.Add(hbox3, flag=wx.LEFT, border=10)
		vbox.Add((-1, 25))

		hbox4 = wx.BoxSizer(wx.HORIZONTAL)
		# Translators: label for the two options of radio box, desktop and laptop layout
		layoutOptions=[_('Desktop layout commands'), _('Laptop layout commands')]
		self.layoutObtionsRadio=wx.RadioBox(panel, -1, 
		# Translators: label of radio box to choose type of keyboard commands to play
		_("Choose keyboard layout to train commands"), size= wx.DefaultSize,choices= layoutOptions, majorDimension=0, style= wx.RA_SPECIFY_COLS)
		hbox4.Add(self.layoutObtionsRadio, proportion=1)
		vbox.Add(hbox4, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)
		vbox.Add((-1, 10))

		hbox5 = wx.BoxSizer(wx.HORIZONTAL)
		self.ok = wx.Button(panel, 
		# Translators: label of OK button
		label=_('Ok'), size=(70, 30))
		hbox5.Add(self.ok)
		self.begin = wx.Button(panel, 
		# Translators: label ob Begin Play button
		label= _('Begin Play'), size=(70, 30))
		hbox5.Add(self.begin, flag=wx.EXPAND|wx.BOTTOM, border=5)
		exit= wx.Button(panel, wx.ID_CANCEL, 
		# Translators: label of Exit button
		_('Exit'), size=(70, 30))
		hbox5.Add(exit)
		vbox.Add(hbox5, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)
		panel.SetSizer(vbox)
#make binding
		self.Bind(wx.EVT_BUTTON, self.onBegin, self.begin)
		self.Bind(wx.EVT_BUTTON, self.onOk, self.ok)
		self.Bind(wx.EVT_BUTTON, self.onExit, exit)

	def postInit(self):
		self.hideControls(self.scoreText, self.tcQuestion, self.answerObtionsCumbo,  self.ok)
		self.retreaveData()
		self.begin.SetDefault()
		#setting the selected layout to the current layout of the computer
		current_layout= config.conf['keyboard']['keyboardLayout']
		selec= 0 if current_layout== 'desktop' else 1
		self.layoutObtionsRadio.SetSelection(selec) 
		self.layoutObtionsRadio.SetFocus()
		self.Centre()
		self.Raise()
		self.Show()  

	def retreaveData(self):
		try:
			with open(filepath, 'rb') as f:
				d= pickle.load(f)
				self.savedData= d
		except:
			 self.savedData= {}

	def onExit(self, e):
		if self.question and self.score !=0:
			# Translators: Message asking the user if he wishes to save remaining questions, to resume them in a later time.
			message= _("Do you want to save remaining questions from this round;\nso that you can resume them later?")
			if gui.messageBox(message, 
			# Translators: Title of message box.
			_("Save Game"),
			wx.YES|wx.NO|wx.ICON_QUESTION)== wx.YES:
				self.saveGame()
		self.Destroy()

	def saveGame(self):
		self.allQuestions.append(self.question)
		remainingQuestions= self.allQuestions
		entry= self.savedData
		entry[self.layoutMode]= {}
		entry[self.layoutMode]['score']= self.score
		entry[self.layoutMode]['remainingQuestions']= remainingQuestions
		entry[self.layoutMode]['totalScore']= self.totalScore
		#directory for saved data
		saving_path= os.path.join(CURRENT_DIR, 'savedData', current_lang)
		if not os.path.exists(saving_path):
			os.makedirs(saving_path)
		with open(filepath, 'wb') as f:
			pickle.dump(entry, f)

	def onOk(self, e):
		if self.answerObtionsCumbo.GetStringSelection()== self.question.answer and not self.allQuestions:
			winsound.PlaySound(os.path.join(sound_path, "congratulations.wav"), winsound.SND_ASYNC)
			time.sleep(9)
			self.endGameMessage()
			return
		if self.answerObtionsCumbo.GetStringSelection()== self.question.answer:
			winsound.PlaySound(os.path.join(sound_path, "correctAnswer.wav"), winsound.SND_ASYNC)
			time.sleep(3.5)
			self.score+=1
			# Translators: label for score value
			self.scoreText.SetLabel(_("Your Score: {}/{}").format(self.score, self.totalScore))
			self.displayQuestion()
		else:
			self.allQuestions.insert(0, self.question)
			winsound.PlaySound(os.path.join(sound_path, "incorrectAnswer.wav"), winsound.SND_ASYNC)
			time.sleep(1)
			self.errorMessage()

	def errorMessage(self):
		# Translators: Message displayed upon hitting the wrong answer.
		message= _("Wrong answer;\n No lose, go on.")
		gui.messageBox(message, 
		# Translators: Title of message dialog.
		_("Error Message"), 
		wx.OK)
		self.displayQuestion()

	def endGameMessage(self):
		self.tcQuestion.Clear()
		self.score=0
		# Translators: label of score
		self.scoreText.SetLabel(_("Your Score: %d")%self.score)
		if self.layoutMode in self.savedData:
			self.savedData.pop(self.layoutMode)
		if self.savedData:
			with open(filepath, 'wb') as f:
				pickle.dump(self.savedData, f)
		else:
			try: os.remove(filepath)
			except: pass
		# Translators: Message displayed upon ending any round of game.
		message= _("Congratulations;\n you have answered all questions and won;\n see you in another round or game.")
		gui.messageBox( message,
		# Translators: title of message dialog.
		_("End Of Game "), 
		wx.OK|wx.ICON_INFORMATION)
		self.hideControls(self.scoreText, self.tcQuestion, self.answerObtionsCumbo, self.ok)
		# Translators: label of radio box to play again
		self.layoutObtionsRadio.SetLabel(_("Choose layout and play again"))
		self.showControls(self.layoutObtionsRadio, self.begin)
		self.begin.SetDefault()
		self.layoutObtionsRadio.SetFocus()

	def onBegin(self, e):
		self.layoutMode= 'desktopLayout' if self.layoutObtionsRadio.GetSelection()==0 else 'laptopLayout'
		if self.layoutMode in self.savedData:
			# Translators: Message displayed asking the user, if he wants to resume the previous round or not.
			message= _("Questions preserved of previous round of same layout found,\nDo you want to resume the previous round?")
			if gui.messageBox(message, 
			# Translators: Title of message dialog
			_("Resume Game"), 
			wx.YES_NO|wx.ICON_QUESTION)== wx.YES:
				self.beginGame(resume= True)
				return
			self.beginGame(resume= False)
			return
		# Translators: message displayed at the begining of game, giving little informations about it.
		message= _("Welcome To training nvda commands like game;\nWe will ask you NVDA {} commands like questions;\nand you have to choose the right answer from the available options;\nLet us then begin!").format(self.layoutMode)
		if gui.messageBox(message, 
		# Translators: Title of welcome dialog.
		_("Welcome"),
		wx.OK|wx.CANCEL|wx.ICON_INFORMATION)== wx.CANCEL:
			return
		self.beginGame(resume=False)

	def beginGame(self, resume):
		if resume:
			self.allQuestions= self.savedData[self.layoutMode]['remainingQuestions']
			self.score= self.savedData[self.layoutMode]['score']
			self.totalScore= self.savedData[self.layoutMode]['totalScore']
			# Translators: label of score text upon resuming game
			self.scoreText.SetLabel(_("Your score: {}/{}").format(self.score, self.totalScore))
		else:
		# no resume,  starting game from scratch
			#importing commandLists that contains the required data
			from . import commandLists
			currentList= commandLists.desktopList if self.layoutObtionsRadio.GetSelection()== 0 else commandLists.laptopList
			self.totalScore= len(currentList)
			self.allQuestions= QuestionObj.populateList(currentList)
		self.hideControls(self.begin, self.layoutObtionsRadio)
		self.showControls(self.scoreText, self.tcQuestion, self.answerObtionsCumbo, self.ok)
		self.ok.SetDefault()
		self.displayQuestion()

	def displayQuestion(self):
		self.question= self.allQuestions.pop()
		self.tcQuestion.SetValue(self.question.question)
		self.tcQuestion.SetSelection(0,-1)
		choices= self.question.help[:]
		random.shuffle(choices)
		self.answerObtionsCumbo.Set(choices)
		self.answerObtionsCumbo.SetSelection(0)
		self.tcQuestion.SetFocus()

	def hideControls(self, *args):
		for control in args:
			control.Hide()

	def showControls(self, *args):
		for control in args:
			control.Show()
