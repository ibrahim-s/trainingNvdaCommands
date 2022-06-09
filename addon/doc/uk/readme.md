# Training Keyboard commands (Тренажер клавіатурних команд) #

*	Автор: Ibrahim Hamadeh  
*	Учасники: cary rowen
*	Завантажити [стабільну версію][1]  
*	Завантажити [версію в розробці][2]  
*	Сумісність з NVDA: 2019.3 і новіші  

Цей додаток призначений для вивчення команд NVDA в ігровій формі як для режимів розкладки клавіатури Desktop, так і для розкладки Laptop.
Усі дані команд витягуються з файлу keyCommands.html у локальній папці з документацією NVDA.  
Цей додаток не має жодного початкового жесту або комбінації клавіш.  
Ви можете призначити для нього певний жест за допомогою:  
меню NVDA>налаштування>жести вводу>Тренажер клавіатурних команд.   

## Використання ##

*	Ви вибираєте режим розкладки клавіатури, який хочете вивчати і починаєте гру    
*	Відобразиться запитання чи команда та її опис, і ви повинні вибрати правильний варіант відповіді    
*	Якщо ви вибрали правильну відповідь, до вашої оцінки буде додано один бал    
*	Якщо відповідь була неправильною, рахунок не зміниться, тобто ви не програєте  
*	У будь-який час, якщо ви хочете вийти, вас запитають, чи хочете ви зберегти решту запитань для наступного раунду  
*	Якщо пізніше ви виберете розкладку зі збереженими запитаннями, вас запитають, чи хочете ви відновити запитання, що залишилися з попереднього раунду  
*	Відповідаючи на всі запитання, приблизно 95 для кожної розкладки, ви будете оголошені переможцем, який заслуговує на кубок додатка NVDA.  

### Зміни у версії 2.6 ###

*	Востаннє протестовану версію оновлено до 2022.1, щоб отримати сумісність з найновішим API NVDA.

### Зміни у версії 2.5 ###

*	Додано переклад на турецьку.
*	Використовуються скрипти-декоратори.

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

[1]: https://github.com/ibrahim-s/trainingNvdaCommands/releases/download/2.6/trainingKeyboardCommands-2.6.nvda-addon

[2]: https://github.com/ibrahim-s/trainingNvdaCommands/releases/download/2.6-dev/trainingKeyboardCommands-2.6-dev.nvda-addon
