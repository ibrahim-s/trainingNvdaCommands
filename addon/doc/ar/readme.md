# التدرُب على أوامر NVDA #

*	مصمم الإضافة: ابراهيم حمادة  
*	المساهِمون: Cary Rowen  
*	رابط [stable version][1]  
*	رابط [development version][2]  
*	التوافُق مع NVDA: 2019.3 فما فوق  
*	التوافُق مع بايثون: Python3 فقط.  
*	للإصدارات القديمة مِن NVDA, يمكن استخدام هذه النسخة [Link][3]  

هذه الإضافة تتيح لك التدرب على أوامر NVDA, على طريقة لعبة  
سواء بالنسبة لاختصارات الحاسوب المكتبي أو المحمول  
معلومات و بيانات الأسءلة قد تم استخلاصها من ملف keyCommands.html, الخاص بكل لغة, و الموجود في مجلد documentation في NVDA.  
هذه الإضافة ليس لها اختصار بشكل افتراضي خاص بها  
عليك عمل اختصار خاص بها من خلال:  
قائمةْ NVDA>تفضيلات>تخصيص إختصارات NVDA>التدرب على أوامر NVDA.    

## طريقةْ الإستخدام ##

*	إختر نوع الإختصارات التي تريد التدرب عليها, و ابدأ باللعبة  
*	ستعرض عليك وظيفة و شرح لها, و عليك اختيار المفاتيح أو الأوامر الخاصة بها  
*	إذا اخترت الجواب الصحيح, سيزيد رصيدك نقطة واحدة  
*	إذا كانت الإجابة خاطءة, لن ينقص رصيدك, و هكذا تستمر في اللعبة بغير خسارة  
*	في أي وقت إذا أردت الخروج من اللعبة قبل النهاية, ستُسأل إذا ما كنت تريد حفظ الأسءلة المتبقية أم لا
*	و في وقت لاحق, إذا اخترت نوع إختصاراتيوجد أسءلة محفوظة لها, ستُسأل ما إذا كنت تريد استءناف تلك الجولة السابقة أم لا  
*	و في حال الإجابة على جميع الأسءلة, خوالي 88 بالنسبة لكل نمط, سيتم إعلان فوزك, و استحقاقك لكأس إضافات NVDA.  

### التغييرات في 2.4 ###

*	إضافةْ الترجمة إلى اللغة الصينية المُبسطة.  
*	إضافةْ كلمات أو عِبارات جديدة إلى nvda.po لإمكانيةْ ترجمتها.  

### التغييرات في 2.3 ###

*	استبدال الأصوات المُستخدمة في مناسبات معينة بأصوات أقصر , مما يتيح لنا التخلص من فترةْ توقف بعد الصوت.  
*	استخدام أحدث إصدار مِن نموذج إضافات NVDA, NVDA addon template.  
*	عندما يكون الأمر "None", يعني بدون اختصار, نستبدل "None" بِ "Unassigned".  

### التغييرات في 2.1 ###

*	ترجمةْ الإضافة للغة الروسية.

### Changes for 2.0 ###

*	جعل الإضافة تتوافق مع بايثون3, بايثون3 فقط.  
*	Change index of scraped tables to accomodate with the changes in keyCommands.html file.  

### Changes for 1.2 ###

*	select current keyboard layout on start of game.
*	Add sounds to correct answer, wrong answer, and upon winning the game.

### Changes for 1.1 ###

*	Initial version.

### المساهمات ###

*	الشكر الكبير لِ cary-rowen, لملاحظاته و تزويد الإضافة بالأصوات الجديدة.  

[1]: https://github.com/ibrahim-s/trainingNvdaCommands/releases/download/2.4/trainingKeyboardCommands-2.4.nvda-addon

[2]: https://github.com/ibrahim-s/trainingNvdaCommands/releases/download/2.4-dev/trainingKeyboardCommands-2.4-dev.nvda-addon

[3]: https://github.com/ibrahim-s/trainingNvdaCommands/releases/download/v1.3dev/trainingKeyboardCommands-1.3-dev.nvda-addon