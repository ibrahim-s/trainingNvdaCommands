# Allenamento nei comandi da tastiera #

*	Authore: Ibrahim Hamadeh  
*	Contributori: cary rowen
*	Scarica la [Versione stabile 3.2.1][1]  
*	Compatibilità di NVDA: 2019.3 e successive  

L'obbiettivo di questo componente aggiuntivo è quello di allenarsi sui comandi di NVDA, sia del layout desktop che per quello laptop, in forma di gioco
  Tutti i dati dei comandi vengono recuperati dal file keyCommands.html nella cartella della documentazione locale di NVDA.  
Questo componente aggiuntivo non ha alcun gesto o scorciatoia predefinita  
È necessario assegnarne uno specifico tramite:  
menu di NVDA>preferenze>gesti e tasti di immissione>Allenamento nei comandi da tastiera.  

## Uso ##

*	scegli il layout della tastiera sulla quale desideri allenarti e inizi a giocare  
*	verrà visualizzata una domanda o un comando e la sua descrizione e dovrai scegliere i tasti o la risposta corretta  
*	se hai scelto la risposta corretta, al tuo punteggio verrà aggiunto un punto  
*	se la risposta è sbagliata, il punteggio non cambierà, e si proseguirà senza perdere  
*	in qualsiasi momento, se vorrai uscire, ti verrà chiesto se desideri salvare le domande rimanenti per il round successivo  
*	se in un secondo momento sceglierai un layout con domande salvate, ti verrà chiesto se desideri riprendere  
*	rispondendo a tutte le domande, circa 136 per ogni layout, verrai dichiarato vincitore meritevole della NVDA addon's cup.  

### Modifiche nella versione 3.2.1 ###

*	Aggiunta la traduzione in lingua italiana, fornita da Leonardo Marenda.

### Modifiche nella versione 3.2 ###

*	Aggiornata l'ultima versione testata, quindi ora il componente aggiuntivo è compatibile con NVDA 2024.1.

### Modifiche nella versione 3.1 ###

*	Aggiornato il pacchetto beautifulSoup alla versione 4.12.2.
*	Utilizzato core.postNvdaStartup per avviare la creazione dei dati del componente aggiuntivo, anziché al suo caricamento. 

### Modifiche nella versione 3.0 ###

*	Modificato l'indice delle tabelle scraped, in base alle modifiche nel file Commands Quick Reference.html nell'ultimo NVDA 2023.3.
*	Ora, per il comando specifico di determinate applicazioni, la prima riga della domanda contiene un riferimento a quell'applicazione  
Ad esempio, nei comandi di Microsoft Word, la domanda ha il prefisso "In Microsoft Word:".

### Modifiche nella versione 2.9 ###

*	Rilasciata la prima versione nello store dei componenti aggiuntivi.

### Modifiche nella versione 2.8 ###

*	Aggiornata l'ultima versione testata alla 2023.1 per rendere compatibile il componente aggiuntivo con tale versione di NVDA.

### Modifiche nella versione 2.7 ###

*	Aggiunta la traduzione in lingua Ucraina.

### Modifiche nella versione 2.6 ###

*	Aggiornata l'ultima versione testata alla 2022.1 per rendere compatibile il componente aggiuntivo con tale versione di NVDA.

### Modifiche nella versione 2.5 ###

*	Aggiunta la traduzione in Turco.
*	Uso degli script decorators.

### Modifiche nella versione 2.4 ###

*	Aggiunta la traduzione in Cinese semplificato.  
*	Aggiunte nuove stringhe traducibili.  

### Modifiche nella versione 2.3 ###

*	Cambia i suoni per vari eventi con suoni più brevi, rende possibile rimuovere il tempo di pausa dopo il suono.  
*	utilizza l'ultima versione del modello di componenti aggiuntivi di NVDA.  
*	Se il comando viene visualizzato come "Nessuno", ovvero non assegnato, il componente lo modifica in "Non assegnato".  

### Modifiche nella versione 2.1 ###

*	Aggiunta la traduzione in lingua Russa.

### Modifiche nella versone 2.0 ###

*	Rende il componente aggiuntivo compatibile solo con Python3.  
*	Modifica l'indice delle tabelle scraped per adattarsi alle modifiche nel file keyCommands.html.  

### Modifiche nella versione 1.2 ###

*	selezione del layout corrente all'avvio del gioco.
*	Aggiunti suoni per risposta corretta, sbagliata ed alla vincita della partita.

### Modifiche nella versione 1.1 ###

*	Versione iniziale.

### Contributi ###

*	Ringrazio molto Cary-Rowen per le sue osservazioni e per il contributo ai nuovi suoni per l'add-on.  

[1]: https://github.com/ibrahim-s/trainingNvdaCommands/releases/download/3.2.1/trainingKeyboardCommands-3.2.1.nvda-addon
