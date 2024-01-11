# Training Keyboard commands #

*	Author: Ibrahim Hamadeh  
*	Contributors: cary rowen
*	Download [Stable Version 3.1][1]  
*	Download [Development Version 3.1.1][2]  
*	NVDA compatibility: 2019.3 and later  

This addon is aimed to train NVDA commands in a game like way, for either keyboard layout modes  
desktop or laptop layout  
All commands data is scraped from keyCommands.html file in locale documentation folder in NVDA.  
This addon does not have any default gesture or shortcut  
You have to assign a specific gesture to it via:  
NVDA menu>preferences>inputGestures>trainingKeyboardCommands.  

## Usage ##

*	you choose the keyboard layout mode you want to train, and begin play  
*	a question or command and it's description will be displayed, and you have to pick the right related keys or answer  
*	if you have chose the right answer, your score wi be added one point  
*	if the answer was wrong, the score will not change, and go on with no loose  
*	at any time if you want to exit, you will be asked if you want to save the remaining questions for next round  
*	if in later time you choose a layout wit saved questions, you will be asked if you want to resume the remaining questions from previous round  
*	answering all questions, about 129 for each layout, you will be declared a winner deserving NVDA addon's cup.  

### Changes for 3.1 ###

*	Update beautifulSoup package to version 4.12.2.
*	Use core.postNvdaStartup to start build addon data, instead upon addon loading. 

### Changes for 3.0 ###

*	Change index of scraped tables, according to changes in Commands Quick Reference.html file in latest NVDA 2023.3.
*	Now for command specific to certain applications, the first line of the question refers to that application.  
For instance in Microsoft word commands, the question is prefixed with "In Microsoft word:".

### Changes for 2.9 ###

*	Release first version to addon store.

### Changes for 2.8 ###

*	Update last tested version to 2023.1 to comply with NVDA 2023.1.

### Changes for 2.7 ###

*	Add Ukrainian translation for the addon.

### Changes for 2.6 ###

*	Update last tested version to 2022.1, to comply with latest NVDA addon's api.

### Changes for 2.5 ###

*	Added Turkish translation.
*	Use script decorators.

### Changes for 2.4 ###

*	Added simplified Chinese translation.  
*	Added new translatable strings.  

### Changes for 2.3 ###

*	Change sounds for various events with shorter sounds,makes possible to remove the sleeping time after the sound.  
*	use latest version of NVDA addon template.  
*	If the command is displayed as 'None' meaning unassigned, change it to 'Unassigned'.  

### Changes for 2.1 ###

*	Add Russian translation.

### Changes for 2.0 ###

*	Make the addon compatible with python3 only.  
*	Change index of scraped tables to accomodate with the changes in keyCommands.html file.  

### Changes for 1.2 ###

*	select current keyboard layout on start if game.
*	Add sounds to correct answer, wrong answer, and upon winning the game.

### Changes for 1.1 ###

*	Initial version.

### Contributions ###

*	Tanks a lot to cary-rowen, for his remarks and contributing the new sounds for the addon.  

[1]: https://github.com/ibrahim-s/trainingNvdaCommands/releases/download/3.1/trainingKeyboardCommands-3.1.nvda-addon

[2]: https://github.com/ibrahim-s/trainingNvdaCommands/releases/download/3.1.1/trainingKeyboardCommands-3.1.1.nvda-addon
