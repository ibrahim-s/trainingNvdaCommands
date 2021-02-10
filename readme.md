# Training Keyboard commands #

*	Author: Ibrahim Hamadeh  
*	Download [stable version][1]  
*	Download [development version][2]  
*	NVDA compatibility: 2019.3 to 2019.4  
*	Python compatibility: Python3 only  
*	For previous versions of NVDA, please use this [Link][3]  

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
*	answering all questions, about 88 for each layout, you will be declared a winner deserving NVDA cup.  

### Changes for 2.2 ###

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

[1]: https://github.com/ibrahim-s/trainingNvdaCommands/releases/download/2.2/trainingKeyboardCommands-2.2.nvda-addon

[2]: https://github.com/ibrahim-s/trainingNvdaCommands/releases/download/v2.1dev/trainingKeyboardCommands-2.1-dev.nvda-addon

[3]: https://github.com/ibrahim-s/trainingNvdaCommands/releases/download/v1.3dev/trainingKeyboardCommands-1.3-dev.nvda-addon