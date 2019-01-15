# -*- coding: UTF-8 -*-

# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

# Full getext (please don't change)
_ = lambda x : x

# Add-on information variables
addon_info = {
	# for previously unpublished addons, please follow the community guidelines at:
	# https://bitbucket.org/nvdaaddonteam/todo/raw/master/guideLines.txt
	# add-on Name, internal for nvda
	"addon_name" : "trainingKeyboardCommands",
	# Add-on summary, usually the user visible name of the addon.
	# Translators: Summary for this add-on to be shown on installation and add-on information.
	"addon_summary" : _("Training Keyboards Commands"),
	# Add-on description
	# Translators: Long description to be shown for this add-on on add-on information from add-ons manager
	"addon_description" : _("""This addon allows you to train NVDA commands in game like way, for either desktop or laptop layout mode.
For every commands and it's description, you have to choose the right keys or answer specific to it.
And if exiting before the end, you can save the remaining questions to resume them in later time.
In order to use the addon, you have to assign a gesture to it via NVDAmenu>preferences>inputGestures>trainingKeyboardCommands."""),
	# version
	"addon_version" : "1.1-dev",
	# Author(s)
	"addon_author" : u"ibrahim hamadeh <ibra.hamadeh@hotmail.com>",
	# URL for the add-on documentation support
	"addon_url" : "https://github.com/ibrahim-s/trainingNvdaCommands.git",
	# Documentation file name
	"addon_docFileName" : "readme.html",
	# Minimum NVDA version supported (e.g. "2018.3")
	"addon_minimumNVDAVersion" : "2017.3",
	# Last NVDA version supported/tested (e.g. "2018.4", ideally more recent than minimum version)
	"addon_lastTestedNVDAVersion" : "2019.1",
	# Add-on update channel (default is stable or None)
	"addon_updateChannel" : None,
}


import os.path

# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = [os.path.join("addon", "globalPlugins", "trainingNvdaCommands", "*.py"), ]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py"]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
excludedFiles = []
