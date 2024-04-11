# Treinar comandos do teclado #

* Autor: Ibrahim Hamadeh
* Contribuição de : Cary Rowen
* descarregar [versão estável 3.2.1] [1]
* Compatibilidade com NVDA: 2019.3 e posteriores

Este extra tem como objetivo treinar comandos do NVDA de maneira semelhante a um jogo, tanto para tipos de teclado
de computadores de secretária como de computadores portáteis.
Todos os dados dos comandos são extraídos do ficheiro keyCommands.html na pasta de documentação local no NVDA.
Este extra não possui nenhum comando ou atalho padrão
Deve atribuir-lhe um atalho específico por meio de:
Menu do NVDA>preferências>definir comandos>treinar comandos de teclado.

## Uso ##

* Escolhe o tipo de do teclado que deseja treinar e começa a jogar
* uma pergunta ou comando e a sua descrição serão mostrados, e deve escolher as teclas ou respostas corretas relacionadas
* se escolheu a resposta certa, a sua pontuação será aumentada em um ponto
* se a resposta estiver errada, a pontuação não mudará, e seguirá sem perder
* a qualquer momento, se desejar sair, será perguntado se deseja guardar as questões restantes para a próxima rodada
* se posteriormente escolher um tipo de teclado com perguntas guardadas, será perguntado se deseja retomar as perguntas restantes da rodada anterior
* Se responder a todas as perguntas, cerca de 136 para cada tipo de teclado, será declarado um vencedor merecedor do prémio do extra do NVDA.

### Modificações em 3.2.1 ###

* Adicionada tradução para o idioma italiano, contribuição de Leonardo Marenda.

### Alterações em  3.2 ###

* Atualizada a última versão testada, para que agora o extra seja compatível com NVDA 2024.1.

### Alterações para 3.1 ###

* Atualizado o pacote beautifulSoup para a versão 4.12.2.
* Usa o core.postNvdaStartup para iniciar a construção de dados de extra, em vez de carregar o extra.

### Mudanças para 3.0 ###

* Alterado o índice das tabelas extraídas, de acordo com as alterações no arquivo Commands Quick Reference.html no NVDA 2023.3 mais recente.
* Agora, para comandos específicos de determinadas aplicações, a primeira linha da pergunta refere-se a essa aplicação.
Por exemplo, em comandos do Microsoft Word, a pergunta é prefixada com "No Microsoft Word:".

### Mudanças para 2.9 ###

* Lançada a primeira versão na loja de extras.

### Mudanças para 2.8 ###

* Atualizada a última versão testada para 2023.1 para estar em conformidade com o NVDA 2023.1.

### Mudanças para 2.7 ###

* Adicionada tradução ucraniana para o addon.

### Mudanças para 2.6 ###

* Atualizada a última versão testada para 2022.1, para estar em conformidade com a API do extra do NVDA mais recente.

### Mudanças para 2.5 ###

* Adicionada tradução para turco.
* Usa decoradores de script.

### Mudanças para 2.4 ###

* Adicionada tradução para chinês simplificado.
* Adicionadas novas strings traduzíveis.

### Mudanças para 2.3 ###

* Alterados sons para vários eventos com sons mais curtos, possibilitando remover o tempo de pausa após o som.
* usa a versão mais recente do modelo adicional do NVDA.
* Se o comando for mostrado como 'Nenhum', significando não atribuído, altere-o para 'Não atribuído'.

### Mudanças para 2.1 ###

* Adicionada tradução para o russo.

### Mudanças para 2.0 ###

* Torna o extra compatível apenas com python3.
* Alterado o índice das tabelas extraídas para acomodar as alterações no ficheiro keyCommands.html.

### Mudanças para 1.2 ###

* seleciona o tipo atual do teclado ao iniciar o jogo.
* Adicionados sons para respostas corretas, respostas erradas e ao vencer o jogo.

### Mudanças para 1.1 ###

*tVersão inicial.

### Contribuições ###

* Agradeço muito a Cary-rowen, por seus comentários e pela contribuição com os novos sons para o addon.

[1]: https://github.com/ibrahim-s/trainingNvdaCommands/releases/download/3.2.1/trainingKeyboardCommands-3.2.1.nvda-addon