# -*- coding: utf-8 -*-
#trainingKeyboardCommands, ibrahim hamadeh, copyright 2019
#this addon is under GNU general public license2.0, see copying.txt
#An addon like game to train nvda commands for desktop and labtop layouts.
#bs4 used in this addon is Copyright (c) 2004-2017 Leonard Richardson under MIT license.
#see copying.txt in bs4 package.

from .game import Game
import globalPluginHandler
#from logHandler import log
import os, sys
import addonHandler
addonHandler.initTranslation()

CURRENT_DIR= os.path.abspath(os.path.dirname(__file__))
#importing bs4 is borrowed from textInformation addon by Carter Temm.
sys.path.append(CURRENT_DIR)
import imp
a, b, c=imp.find_module("bs4")
BeautifulSoup=imp.load_module("bs4", a, b, c).BeautifulSoup
del sys.path[-1]
import random
import gui

#path of keyCommands.html in documentation files, taking into consideration nvda language
keyCommandsFile= gui.getDocFilePath("keyCommands.html")

def readFile(filepath):
	with open(filepath, 'r') as f:
		html= f.read()
	return html

def populateOptionsAndReturnList(lst, lst_all):
	"""Adding to obtions or answers list three random incorrect commands, beside the correct command already there.
	lst is a list of questions data, each element of it is a tuple, first item of it is the question and the second item is a list containing one item which is the correct answer.
	lst_all is a lis containing all scraped commands.
	"""
	result= []
	for question in lst:
		#the lis containing only the right command, and we want to add to it 3 incorrect command
		options= question[1]
		i=0
		while i<3:
			item= random.choice(lst_all)
			if any(i in options for i in (item, item.capitalize(), item.lower())): continue
			options.append(item)
			i+=1
		result.append(question)
	return result

def scrapCommandsAndMakeFile(filename):
	"""filename is the fi we want to write in it the two lists desktop and laptop scraped data.
	"""
	soup = BeautifulSoup(readFile(keyCommandsFile), 'html.parser')
	allCommands= []
	desktopQuestions= []
	labtopQuestions= []
	tables= soup.find_all('table')

	for table in tables[0:14]+tables[22: 32]:
		rows= table.find_all('tr')[1:]
		for row in rows:
			cells= row.find_all('td')
			if len(cells) in (4,5):
				deskQuestion=(cells[0].string+';\nDescription:\n'+cells[-1].string, [cells[1].string])
				labQuestion= (cells[0].string +';\nDescription:\n'+cells[-1].string, [cells[2].string])
				desktopQuestions.append(deskQuestion)
				labtopQuestions.append(labQuestion)
				allCommands.append(cells[1].string)
				allCommands.append(cells[2].string)
			if len(cells)==3:
				desktopQuestions.append((cells[0].string+';\nDescription:\n'+cells[-1].string, [cells[1].string]))
				labtopQuestions.append((cells[0].string+';\nDescription:\n'+cells[-1].string, [cells[1].string]))
				allCommands.append(cells[1].string)
	s=set(allCommands)
	allCommands=list(s)
	l1= populateOptionsAndReturnList(desktopQuestions, allCommands)
	l2= populateOptionsAndReturnList(labtopQuestions, allCommands)
	#writing the two lists to a file.
	with open(os.path.join(CURRENT_DIR, filename), 'wb') as f:
		f.write('desktopList= '+str(l1))
		f.write('\n')
		f.write('laptopList= '+str(l2))

PLAYING = None

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	scriptCategory = _("Training Nvda Commands")

	def __init__(self, *args, **kwargs):
		super(GlobalPlugin, self).__init__(*args, **kwargs)
		scrapCommandsAndMakeFile('commandLists.py')

	def script_startGame(self, gesture):
		global PLAYING
		if not PLAYING:
			PLAYING= Game(gui.mainFrame)
			PLAYING.postInit()
		else:
			PLAYING.Raise()
	# Translators: Message displayed in input help mode.
	script_startGame.__doc__= _("Displays trainingNvdaCommands game dialog.")
