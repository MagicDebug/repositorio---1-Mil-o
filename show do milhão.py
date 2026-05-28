# AQUI É A INTRODUÇÂO DO JOGO COM O TITULO

print (input("\n\n 💰!!! O SHOW DO MILHÃO !!!💰  | ENTER |"))

# AQUI É AONDE O APRESENTADOR/MAQUINA QUE SE IDENTIFICA PELO MICROFONE (🎤) DA AS BOAS VINDAS AO USUÁRIO E PEDE PARA ELE SE APRESENTAR, USUARIO SENDO (👤)

print ("\n 🎤 Seja Bem Vindo ao Show Do Milhão! ")
nome_usuario = (input(" Vamos dar inicio ao Grande Show, Por Favor Se Apresente nos dizendo seu nome de usuario | DIGITE SEU NOME | ENTER | \n\n 👤 "))

# AQUI ESTA AS EXPLICAÇÕES DE COMO SÂO AS REGRAS DO JOGO, SOBRE O VALOR DAS PERGUNTAS, AS AJUDAS E O OBJETIVO DO JOGO QUE É CHEGAR AO 1 MILHÃO

print (input("\n 🎤 " + nome_usuario + ", as Instruções do Jogo são as seguintes: \n  O Show será baseado na matéria de PORTUGUÊS e dividido em 5 temas do 😂 Mais Facil até o, 🤬 Mais Dificil, contendo 25 perguntas divididas para os diferentes 5 temas, podendo ter a ajuda dá; \n\n 🥸  Plateia 3 vezes \n 🎓 Universitarios 5 vezes \n\n  | ENTER | \n"))

print (input(" 🎤 Cada pergunta vale 💵 200,00 \n  A cada acerto o valor da proxima pergunta dobra, aumentando o resultado acumulado \n  Mas cuidado: a cada erro você perde 💵 um quarto do valor acumulado! \n\n | ENTER | \n"))

print (input("\n 🎤 Seu Unico Objetivo é responder todas as 25 Perguntas e tentar chegar ao 1 milhão \n\n  MAS ATENÇÃO!!! \n  Se até o final da pergunta Numero 25 você tiver acumulado 1 milhão ou mais, você tem direito uma Pergunta Bonus chamada \n\n 💀 ARRISCA TUDO 💀 \n\n  Pergunta na qual se você acerta leva seu 💵 Valor Acumulado ao Dobro🤑  \n  Mas se Errar perde todo 💵 Valor Acumulado 💀 \n\n | ENTER | \n"))

# AQUI È DANDO INICIO E COMEÇANDO O TEMA 1
# TEMA 1: (NOTICIA E REPORTAGEM) DIFICULDADE: (😂 Mais Facil😂)

print (input(" 🎤 Vamos dar inicio: \n Primeiro Tema: Noticia e Reportagem \n Dificuldade: 😂 Mais Facil😂 \n\n | ENTER | \n"))

# AQUI È  PRIMERIA PERGUNTA

def RESPOSTAS_PERGUNTA_1 (pergunta_1_resposta):

    pergunta_1_resposta = (input(" 🎤 PERGUNTA 1️: O que é uma noticia:❔ \n\n 🎤 Alternativa (A) Um texto Teatral \n 🎤 Alternativa (B) Um texto que informa fatos \n 🎤 Alternativa (C) Uma poesia \n 🎤 Alternativa (D) Uma receita \n 🎤 Alternativa (E) Um conto ficticio \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] \n\n | ENTER | \n\n 👤 "))

    # ALTERNATIVA A (❌ ERRADA ❌) 

    if pergunta_1_resposta == "A":
        print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Um texto Teatral), sua resposta está eee... \n\n | ENTER | "))
        print (input(" 🎤 ❌ errada ❌ \n Você não ganhou nada  💵 0,00!!! 🫵  😂 \n\n | ENTER | \n"))

        # ALTERNATIVA B (✅ CORRETA ✅)

    elif pergunta_1_resposta == "B":
        print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Um texto que informa fatos), sua resposta está eee... \n\n | ENTER | "))
        print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 200,00!!! \n\n | ENTER | \n"))

        # ALTERNATIVA C (❌ ERRADA ❌)

    elif pergunta_1_resposta == "C":
        print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Uma poesia), sua resposta está eee... \n\n | ENTER | "))
        print (input(" 🎤 ❌ errada ❌ \n Você não ganhou nada  💵 0,00!!! 🫵  😂 \n\n | ENTER | \n"))

        # ALTERNATIVA D (❌ ERRADA ❌)

    elif pergunta_1_resposta == "D":
        print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Uma receita), sua resposta está eee... \n\n | ENTER | "))
        print (input(" 🎤 ❌ errada ❌ \n Você não ganhou nada  💵 0,00!!! 🫵  😂 \n\n | ENTER | \n"))

        # ALTERNATIVA E (❌ ERRADA ❌)

    elif pergunta_1_resposta == "E":
        print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Um conto ficticio), sua resposta está eee... \n\n | ENTER | "))
        print (input(" 🎤 ❌ errada ❌ \n Você não ganhou nada  💵 0,00!!! 🫵  😂 \n\n | ENTER | \n"))

        # ALTERNATIVA P (🥸 PLATEIA)

    elif pergunta_1_resposta == "P":
        plateia = (input(""))


RESPOSTAS_PERGUNTA_1(pergunta_1_resposta = "")