# -*- coding: utf-8 -*-
#trainingKeyboardCommands, ibrahim hamadeh, copyright 2019
#this addon is under GNU general public license2.0, see copying.txt
#An addon like game to train nvda commands for desktop and labtop layouts.
#bs4 used in this addon is Copyright (c) 2004-2017 Leonard Richardson under MIT license.
#see copying.txt in bs4 package.

import globalPluginHandler
import os, sys
import threading
import random
import gui
import core
import documentationUtils
from scriptHandler import script
from .game import Game
from logHandler import log

# declared earlier, to be used in importing bs4.
CURRENT_DIR= os.path.abspath(os.path.dirname(__file__))

sys.path.append(CURRENT_DIR)
from bs4 import BeautifulSoup
del sys.path[-1]

import addonHandler
addonHandler.initTranslation()

#path of keyCommands.html in documentation files, taking into consideration nvda language
keyCommandsFile= documentationUtils.getDocFilePath("keyCommands.html")

def readFile(filepath):
	''' reading the file that contains the required data and returning its html source as a string.'''
	with open(filepath, 'r', encoding= 'utf-8') as f:
		html= f.read()
	return html

def populateOptionsAndReturnList(lst, lst_all):
	'''build the obtions or answers list as the second item of question tuple, that contains three random incorrect commands, beside the correct command .
	lst is a list of tuples, items of type string, first item of it is the question and the second item is the correct answer.
	lst_all is a lis of strings containing all scraped commands.
	'''
	result= []
	for question, rightAnswer in lst:
		#Instantiating options list, should contain three random incorrect commands, beside the right one.
		options= [rightAnswer]
		i=0
		while i<3:
			item= random.choice(lst_all)
			if any(j in options for j in (item, item.capitalize(), item.lower())): continue
			options.append(item)
			i+=1
		result.append((question, options))
	return result

appsOfInterest= (
	"Microsoft Word",
	"Microsoft Excel",
	"Microsoft PowerPoint",
	"Windows Console"
)

def getPrefixForTable(table):
	previousH3 = table.find_previous_sibling('h3')
	if previousH3 and previousH3.text in appsOfInterest:
		prefix= "In "+ previousH3.text + ":\n"
	else:
		prefix = ""
	return prefix

def scrapRequiredData():
	'''Establish three lists desktopQuestions, labtopQuestions, allCommands.'''
	soup = BeautifulSoup(readFile(keyCommandsFile), 'html.parser')
	desktopQuestions= []
	labtopQuestions= []
	allCommands= set()
	tables= soup.find_all('table')

	for table in tables[0:21]+tables[25: 42]:
		rows= table.find_all('tr')[1:]
		# The following two lines for debugging purposes.
		#tableStartsWith= rows[0].find_all('td')[0].text
		#log.info(f'table starts which:\n{tableStartsWith}')
		for row in rows:
			cells= row.find_all('td')
			if len(cells) in (4,5):
				commandName= cells[0].get_text()
				commandDescription= cells[-1].get_text()
				deskCommand= cells[1].get_text()
				lapCommand= cells[2].get_text()
				# If the gesture or command equals "None", replace it with "Unassigned"
				deskQuestion=(commandName + ';\n' + _("Description:") + '\n'+commandDescription, deskCommand if deskCommand.lower() != "none" else "Unassigned")
				labQuestion= (commandName +';\n' + _("Description:") +'\n'+commandDescription, lapCommand if lapCommand.lower() != "none" else "Unassigned")
				desktopQuestions.append(deskQuestion)
				labtopQuestions.append(labQuestion)
				allCommands.update({deskCommand, lapCommand})
			if len(cells)==3:
				# Prefix is the name of program under which the command is used.
				prefix= getPrefixForTable(table)
				commandName= cells[0].get_text()
				commandDescription= cells[-1].get_text()
				commandKey = cells[1].get_text()
				question = (prefix+ commandName + ';\n' +_("Description:") + '\n'+commandDescription, commandKey)
				desktopQuestions.append(question)
				labtopQuestions.append(question)
				allCommands.add(commandKey)
	# Remove from allCommands set the 2 strings 'None' and 'none'.
	allCommands= allCommands - {"None", "none"}
	# Convert allCommands from a set to a list.
	allCommands=list(allCommands)
	# Return the 3 lists.
	return desktopQuestions, labtopQuestions, allCommands

#writing the two lists to a file.
def writeListsToFile(l1, l2):
	with open(os.path.join(CURRENT_DIR, 'commandLists.py'), 'w', encoding= 'utf-8') as f:
		f.write('desktopList= '+str(l1))
		f.write('\n')
		f.write('laptopList= '+str(l2))

def buildDataAndWriteToFile():
	def startProcess():
		desktopQuestions, labtopQuestions, allCommands= scrapRequiredData()
		desktopLst= populateOptionsAndReturnList(desktopQuestions, allCommands)
		laptopLst= populateOptionsAndReturnList(labtopQuestions, allCommands)
		writeListsToFile(desktopLst, laptopLst)
	t= threading.Thread(target= startProcess)
	t.Daemon= True
	t.start()
	#log.info('starting building data for training keyboard commands ...')

# current instance
PLAYING = None

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	# Translators: Script category for Training Keyboard Commands addon in input gestures dialog.
	scriptCategory = _("Training Keyboard Commands")

	def __init__(self, *args, **kwargs):
		super(GlobalPlugin, self).__init__(*args, **kwargs)
		core.postNvdaStartup.register(buildDataAndWriteToFile)

	@script(
	# Translators: Message displayed in input help mode.
	description= _("Display training keyboard Commands game dialog.")
	)
	def script_startGame(self, gesture):
		global PLAYING
		if not PLAYING:
			PLAYING= Game(gui.mainFrame)
			PLAYING.postInit()
		else:
			PLAYING.Raise()
