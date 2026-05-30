Ajuda_plateia = 3
Ajuda_Universitarios = 5
Valor_Acumulado = 0.0

# AQUI É A INTRODUÇÃO DO JOGO COM O TÍTULO
print (input("\n\n 💰!!! O SHOW DO MILHÃO !!!💰  | ENTER |"))

# AQUI É ONDE O APRESENTADOR/MÁQUINA QUE SE IDENTIFICA PELO MICROFONE (🎤) DÁ AS BOAS-VINDAS AO USUÁRIO E PEDE PARA ELE SE APRESENTAR, USUÁRIO SENDO (👤)
print ("\n 🎤 Seja Bem-Vindo ao Show Do Milhão! ")
nome_usuario = (input(" Vamos dar início ao Grande Show. Por Favor, Se Apresente nos dizendo seu nome de usuário | DIGITE SEU NOME | \n\n | ENTER | \n\n 👤 "))

# AQUI ESTÃO AS EXPLICAÇÕES DE COMO SÃO AS REGRAS DO JOGO, SOBRE O VALOR DAS PERGUNTAS, AS AJUDAS E O OBJETIVO DO JOGO QUE É CHEGAR AO 1 MILHÃO
print (input("\n 🎤 " + nome_usuario + ", as Instruções do Jogo são as seguintes: \n  O Show será baseado na matéria de PORTUGUÊS e dividido em 5 temas do 😂 Mais Fácil até o, 🤬 Mais Difícil \n contendo 25 perguntas divididas para os diferentes 5 temas, podendo ter a ajuda da; \n\n 🥸  Plateia 3 vezes \n 🎓 Universitários 5 vezes \n\n  | ENTER | \n"))
print (input(" 🎤 Cada pergunta vale 💵 200,00 \n  A cada acerto o valor da próxima pergunta dobra, aumentando o resultado acumulado \n  Mas se você errar, o jogo acaba na hora! \n\n | ENTER | \n"))
print (input("\n 🎤 Seu Único Objetivo é responder todas as 25 Perguntas e tentar chegar ao 1 milhão \n\n  MAS ATENÇÃO!!! \n  Se até o final da pergunta Número 25 você tiver acumulado 1 milhão ou mais, você tem direito a uma Pergunta Bônus chamada \n\n 💀 ARRISCA TUDO 💀 \n\n  Pergunta na qual se você acertar leva seu 💵 Valor Acumulado ao Dobro🤑  \n  Mas se Errar perde todo 💵 Valor Acumulado 💀 \n\n | ENTER | \n"))

# AQUI É DANDO INÍCIO E COMEÇANDO O TEMA 1
# TEMA 1: (NOTÍCIA E REPORTAGEM) DIFICULDADE: (😂 Mais Fácil😂)
print (input(" 🎤 Vamos dar início: \n Primeiro Tema: Notícia e Reportagem \n Dificuldade: 😂 Mais Fácil😂 \n\n | ENTER | \n"))

# PERGUNTA NÚMERO 1

def RESPOSTAS_PERGUNTA_1 (pergunta_1_resposta):
    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_1_resposta = (input(" 🎤 PERGUNTA 1️:\n\n [A prefeitura inaugurou uma nova escola nesta segunda-feira.] \n\n Qual é a finalidade desse texto:❔ \n\n 🎤 Alternativa (A) Convencer o leitor \n 🎤 Alternativa (B) Informar um fato \n 🎤 Alternativa (C) Fazer uma crítica \n 🎤 Alternativa (D) Vender um produto \n 🎤 Alternativa (E) Contar uma piada \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITÁRIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))
        
        # .upper() serve para aceitar letras minúsculas digitadas pelo usuário
        pergunta_1_resposta = pergunta_1_resposta.upper()

        if pergunta_1_resposta == "P":
            if Ajuda_plateia > 0:
                Ajuda_plateia -= 1
                print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não têm certeza de qual seja a certa, então boa sorte! \n\n | ENTER | "))
                print (" 🥸  É Alternativa (B)! \n 🥸  Claro que é (B)! \n 🥸  Óbvio que é (D)! \n\n")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

        elif pergunta_1_resposta == "U":
            if Ajuda_Universitarios > 0:
                Ajuda_Universitarios -= 1
                print (input("\n 🎤 Você pediu a ajuda do Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (B) \n\n ")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

        elif pergunta_1_resposta == "A":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Convencer o leitor), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

        elif pergunta_1_resposta == "B":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Informar um fato), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 200,00!!! \n\n | ENTER | \n"))
            Valor_Acumulado = 200.0
            break

        elif pergunta_1_resposta == "C":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Fazer uma crítica), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

        elif pergunta_1_resposta == "D":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Vender um produto), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

        elif pergunta_1_resposta == "E":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Contar uma piada), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

RESPOSTAS_PERGUNTA_1(pergunta_1_resposta = "")

menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 1 \n Você pode ver em seu (👜 MENU) o quanto já acumulou do prêmio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 2 \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSSEGUIR APENAS APERTE ENTER | \n\n | ENTER | \n "))
menu = menu.upper()

if menu == "M":
    menu = (input("\n 👜 MENU: \n\n 💵  Valor acumulado: R$ " + str(Valor_Acumulado) + "\n 🥸   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

# PERGUNTA NÚMERO 2

def RESPOSTAS_PERGUNTA_2 (pergunta_2_resposta):
    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_2_resposta = (input(" 🎤 PERGUNTA 2️: \n\n [Compre já o novo celular com desconto] \n\n Qual é a finalidade do texto:❔ \n\n 🎤 Alternativa (A) Narrar uma história \n 🎤 Alternativa (B) Informar um acontecimento \n 🎤 Alternativa (C) Convencer o consumidor \n 🎤 Alternativa (D) Fazer uma denúncia \n 🎤 Alternativa (E) Ensinar gramática \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))
        
        pergunta_2_resposta = pergunta_2_resposta.upper()

        if pergunta_2_resposta == "P":
            if Ajuda_plateia > 0:
                Ajuda_plateia -= 1
                print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                print (" 🥸  É Alternativa (C)! \n 🥸  Claro que é (E)! \n 🥸  Obvio que é (C)! \n 🥸  Nunca que seria (E)!\n\n")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

        elif pergunta_2_resposta == "U":
            if Ajuda_Universitarios > 0:
                Ajuda_Universitarios -= 1
                print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (C) \n\n ")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

        elif pergunta_2_resposta == "A":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Narrar uma história), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

        elif pergunta_2_resposta == "B":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Informar um acontecimento), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

        elif pergunta_2_resposta == "C":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Convencer o consumidor), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ✅ exata ✅ \n Você acaba de chegar há 💵 400,00!!! \n\n | ENTER | \n"))
            Valor_Acumulado = 400
            break

        elif pergunta_2_resposta == "D":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Fazer uma denúncia), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

        elif pergunta_2_resposta == "E":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Ensinar gramática), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit()

RESPOSTAS_PERGUNTA_2(pergunta_2_resposta = "")

menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 2️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 2️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
menu = menu.upper()

if menu == "M":
    menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 🥸   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

# PERGUNTA NUMERO 3

def RESPOSTAS_PERGUNTA_3 (pergunta_3_resposta):

    # VARIAVEIS GLOBAL PARA AS AJUDAS
    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_3_resposta = (input(" 🎤 PERGUNTA 3️: \n\n [Ontem ocorreu uma forte chuva na cidade.] \n\n A Esse trecho pertence mais provavelmente a:❔ \n\n 🎤 Alternativa (A) Propaganda \n 🎤 Alternativa (B) Receita \n 🎤 Alternativa (C) Poema \n 🎤 Alternativa (D) Notícia \n 🎤 Alternativa (E) Música \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

        
        pergunta_3_resposta = pergunta_3_resposta.upper()

        # ALTERNATIVA DE AJUDA: 🥸PLATEIA🥸(P)
        if pergunta_3_resposta == "P":
            if Ajuda_plateia > 0:
                Ajuda_plateia -= 1
                
                print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                print (" 🥸  É Alternativa (A)! \n 🥸  Claro que é (E)! \n 🥸  Obvio que é (D)! \n 🥸  Nunca que seria (D)! \n 🥸  Chuto que é (D)!\n\n")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

        # ALTERNATIVA DE AJUDA: 🎓UNIVERSITÁRIOS🎓 (U)
        
        elif pergunta_3_resposta == "U":
            if Ajuda_Universitarios > 0:
                Ajuda_Universitarios -= 1
                
                print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (D) \n\n ")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

        # ALTERNATIVA A (❌ ERRADA ❌)
         
        elif pergunta_3_resposta == "A":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Propaganda), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit()

        # ALTERNATIVA B (❌ ERRADA ❌)

        elif pergunta_3_resposta == "B":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Receita), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit()

        # ALTERNATIVA C (❌ ERRADA ❌)

        elif pergunta_3_resposta == "C":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Poema), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit()

        # ALTERNATIVA D (✅ CORRETA ✅)

        elif pergunta_3_resposta == "D":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Notícia), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ✅ exata ✅ \n Você acaba de chegar há 💵  800,00!!! \n\n | ENTER | \n"))
            Valor_Acumulado = 800.0
            break

        # ALTERNATIVA E (❌ ERRADA ❌)

        elif pergunta_3_resposta == "E":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Música), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit()

RESPOSTAS_PERGUNTA_3(pergunta_3_resposta = "")

menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 3️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 4️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
menu = menu.upper()

if menu == "M":
    menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 🥸   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

# PERGUNTA NUMERO 4

def RESPOSTAS_PERGUNTA_4 (pergunta_4_resposta):

    # VARIAVEIS GLOBAL PARA AS AJUDAS

    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_4_resposta = (input(" 🎤 PERGUNTA 4️: \n\n [Beba mais água e cuide da sua saúde] \n\n A finalidade é:❔ \n\n 🎤 Alternativa (A) Informar um acidente \n 🎤 Alternativa (B) Narrar um fato histórico \n 🎤 Alternativa (C) Dar orientação \n 🎤 Alternativa (D) Fazer humor \n 🎤 Alternativa (E) Divulgar um filme \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

        
        pergunta_4_resposta = pergunta_4_resposta.upper()

        # ALTERNATIVA DE AJUDA: 🥸PLATEIA🥸(P)
        if pergunta_4_resposta == "P":
            if Ajuda_plateia > 0:
                Ajuda_plateia -= 1
                
                print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                # AJUSTADO: Agora a maioria dos palpites indica a alternativa correta (C) para o jogador interpretar
                print (" 🥸  Não pode ser (D)! \n 🥸  Claro que é (C)! \n 🥸  Obvio que é (C)! \n 🥸  Nunca que seria (E)! \n 🥸  Chuto que é (C) \n 🥸  Claro que é (C)! \n 🥸  Eu iria na (A)! \n\n")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

        # ALTERNATIVA DE AJUDA: 🎓UNIVERSITÁRIOS🎓 (U)
        elif pergunta_4_resposta == "U":
            if Ajuda_Universitarios > 0:
                Ajuda_Universitarios -= 1
                
                print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                
                print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (C) \n\n ")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

        # ALTERNATIVA A (❌ ERRADA ❌)
        elif pergunta_4_resposta == "A":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Informar um acidente), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit()

        # ALTERNATIVA B (❌ ERRADA ❌)
        elif pergunta_4_resposta == "B":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Narrar um fato histórico), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 𫫵  😂 \n\n | ENTER | \n"))
            exit()

        # ALTERNATIVA C (✅ CORRETA ✅)
        elif pergunta_4_resposta == "C":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Dar orientação), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ✅ exata ✅ \n Você acaba de chegar há 💵  1,600,00!!! 𫫵  😂 \n\n | ENTER | \n"))
            Valor_Acumulado = 1600.0
            break

        # ALTERNATIVA D (❌ ERRADA ❌)
        elif pergunta_4_resposta == "D":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Fazer humor), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 𫫵  😂 \n\n | ENTER | \n"))
            exit()

        # ALTERNATIVA E (❌ ERRADA ❌)
        elif pergunta_4_resposta == "E":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Divulgar um filme), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 𫫵  😂 \n\n | ENTER | \n"))
            exit()

RESPOSTAS_PERGUNTA_4(pergunta_4_resposta = "")

menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 4️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 5️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
menu = menu.upper()

if menu == "M":
    menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 🥸   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))


# PERGUNTA NUMERO 5

def RESPOSTAS_PERGUNTA_5 (pergunta_5_resposta):

    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_5_resposta = (input(" 🎤 PERGUNTA 5️: \n\n [Vacinação contra gripe começa na próxima semana] \n\n O objetivo principal é:❔ \n\n 🎤 Alternativa (A) Informar \n 🎤 Alternativa (B) Criticar uma ação pública \n 🎤 Alternativa (C) Convencer a comprar algo \n 🎤 Alternativa (D) Contar uma aventura \n 🎤 Alternativa (E) Entreter \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

        pergunta_5_resposta = pergunta_5_resposta.upper()

        if pergunta_5_resposta == "P":
            if Ajuda_plateia > 0:
                Ajuda_plateia -= 1
                
                print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                print (" 🥸  Não pode ser (A)! \n 🥸  Claro que é (A)! \n 🥸  Vamos na (D)! \n 🥸  Nunca que seria (A)! \n 🥸  Chuto que é (A) \n 🥸  Claro que é (A)! \n 🥸  Eu não iria na (A)! \n\n")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

        elif pergunta_5_resposta == "U":
            if Ajuda_Universitarios > 0:
                Ajuda_Universitarios -= 1
                
                print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (A) \n\n ")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))
         
        elif pergunta_5_resposta == "A":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Informar), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ✅ exata ✅ \n Você acaba de chegar há 💵  3,200,00!!! 🫵  😂 \n\n | ENTER | \n"))
            Valor_Acumulado = 3200.0
            break

        elif pergunta_5_resposta == "B":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Criticar uma ação pública), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit()

        elif pergunta_5_resposta == "C":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Convencer a comprar algo), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit()

        elif pergunta_5_resposta == "D":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Contar uma aventura), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 𫫵  😂 \n\n | ENTER | \n"))
            exit()

        elif pergunta_5_resposta == "E":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Entreter), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 𫫵  😂 \n\n | ENTER | \n"))
            exit()

RESPOSTAS_PERGUNTA_5(pergunta_5_resposta = "")

menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 5️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 6️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
menu = menu.upper()

if menu == "M":
    menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 🥸   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))


# AQUI È COMEÇANDO O TEMA 2

# TEMA 2: (Barroco e Arcadismo) DIFICULDADE: (😊 Facil😊)

print (input(" 🎤 Vamos dar inicio: \n Segundo Tema: Barroco e Arcadismo \n Dificuldade: 😊 Mais Facil😊  \n\n | ENTER | \n"))

def RESPOSTAS_PERGUNTA_6 (pergunta_6_resposta):

    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        
        pergunta_6_resposta = (input(" 🎤 PERGUNTA 6️:\n\n [A cidade inaugurou um novo hospital.] \n\n [O novo hospital é uma excelente conquista para a população.] \n\n Qual a diferença de um para o outro:❔ \n\n 🎤 Alternativa (A) Ambos informam apenas fatos \n 🎤 Alternativa (B) O primeiro informa e o segundo opina \n 🎤 Alternativa (C) Ambos são propagandas \n 🎤 Alternativa (D) Ambos são poemas \n 🎤 Alternativa (E) O segundo é uma receita \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

        pergunta_6_resposta = pergunta_6_resposta.upper()

        if pergunta_6_resposta == "P":
            if Ajuda_plateia > 0:
                Ajuda_plateia -= 1
                print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                print (" 🥸  É Alternativa (B)! \n 🥸  Claro que é (C)! \n 🥸  Obvio que é (A)! \n 🥸  Obvio que é (E)! \n 🥸  Obvio que é (B)\n 🥸  É Alternativa (B)!\n\n")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

        elif pergunta_6_resposta == "U":
            if Ajuda_Universitarios > 0:
                Ajuda_Universitarios -= 1
                print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (B) \n\n ")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

        elif pergunta_6_resposta == "A":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Ambos informam apenas fatos), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

        elif pergunta_6_resposta == "B":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (O primeiro informa e o segundo opina), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 6,400,00!!! \n\n | ENTER | \n"))
            Valor_Acumulado = 6400.0
            break

        elif pergunta_6_resposta == "C":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Ambos são propagandas), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

        elif pergunta_6_resposta == "D":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Ambos são poemas), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

        elif pergunta_6_resposta == "E":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (O segundo é uma receita), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

RESPOSTAS_PERGUNTA_6(pergunta_6_resposta = "")

menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 6️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 7️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
menu = menu.upper()

if menu == "M":
    menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 🥸   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

# PERGUNTA NUMERO 7

def RESPOSTAS_PERGUNTA_7 (pergunta_7_resposta):

    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_7_resposta = (input(" 🎤 PERGUNTA 7️: \n\n [O trânsito aumentou 20%] \n\n [O aumento do trânsito mostra a falta de planejamento urbano] Os textos apresentam:❔ \n\n 🎤 Alternativa (A) Receita \n 🎤 Alternativa (B) Opinião \n 🎤 Alternativa (C) Propaganda \n 🎤 Alternativa (D) Entrevista \n 🎤 Alternativa (E) Fábula \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

        pergunta_7_resposta = pergunta_7_resposta.upper()

        if pergunta_7_resposta == "P":
            if Ajuda_plateia > 0:
                Ajuda_plateia -= 1
                
                print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                print (" 🥸  É Alternativa (D)! \n 🥸  Claro que é (B)! \n 🥸  Obvio que é (D)! \n 🥸  Nunca que seria (B)! \n 🥸  Chuto que é (B)!\n 🥸  Acho que é (B)!\n 🥸  Com certeza é (B)!\n\n")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

        elif pergunta_7_resposta == "U":
            if Ajuda_Universitarios > 0:
                Ajuda_Universitarios -= 1
                print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (B) \n\n ")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

        elif pergunta_7_resposta == "A":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Receita), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

        elif pergunta_7_resposta == "B":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Opinião), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 12,800,00!!! \n\n | ENTER | \n"))
            Valor_Acumulado = 12800.0
            break

        elif pergunta_7_resposta == "C":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Propaganda), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

        elif pergunta_7_resposta == "D":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Entrevista), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

        elif pergunta_7_resposta == "E":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Fábula), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 𫫵  😂 \n\n | ENTER | \n"))
            exit() 

RESPOSTAS_PERGUNTA_7(pergunta_7_resposta = "")

menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 7️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 8️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
menu = menu.upper()

if menu == "M":
    menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 🥸   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

# PERGUNTA NUMERO 8

def RESPOSTAS_PERGUNTA_8 (pergunta_8_resposta):

    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_8_resposta = (input(" 🎤 PERGUNTA 8️: \n\n [Nova praça é inaugurada no centro] \n\n [A praça deve melhorar o lazer dos moradores] Qual deles expressa opinião:❔ \n\n 🎤 Alternativa (A) Receita \n 🎤 Alternativa (B) Opinião \n 🎤 Alternativa (C) Propaganda \n 🎤 Alternativa (D) Entrevista \n 🎤 Alternativa (E) Fábula \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

        pergunta_8_resposta = pergunta_8_resposta.upper()

        if pergunta_8_resposta == "P":
            if Ajuda_plateia > 0:
                Ajuda_plateia -= 1
                
                print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                print (" 🥸  É Alternativa (C)! \n 🥸  Claro que é (B)! \n 🥸  Obvio que NÂO é (B)! \n 🥸  Nunca que seria (E)! \n 🥸  Chuto que é (A)! \n 🥸  Só poderia ser (A)! \n 🥸  Certeza que é (B)! \n 🥸  Com certeza é (B)!\n 🥸  Acho que é (B)!\n\n")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

        elif pergunta_8_resposta == "U":
            if Ajuda_Universitarios > 0:
                Ajuda_Universitarios -= 1
                print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (B) \n\n ")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

        elif pergunta_8_resposta == "A":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Texto 1), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

        elif pergunta_8_resposta == "B":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Texto 2), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 25,600,00!!! \n\n | ENTER | \n"))
            Valor_Acumulado = 25600.0
            break

        elif pergunta_8_resposta == "C":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Ambos), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

        elif pergunta_8_resposta == "D":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Nenhum), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

        elif pergunta_8_resposta == "E":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Não é possível saber), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

RESPOSTAS_PERGUNTA_8(pergunta_8_resposta = "")

menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 8️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 9️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
menu = menu.upper()

if menu == "M":
    menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 🥸   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

# PERGUNTA NUMERO 9

def RESPOSTAS_PERGUNTA_9 (pergunta_9_resposta):

    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_9_resposta = (input(" 🎤 PERGUNTA 9️: \n\n [Texto 1:\n\nEscola recebe novos computadores.\n\nTexto 2:\n\nOs novos computadores representam um avanço importante.] \n\n O Texto 2:❔ \n\n 🎤 Alternativa (A) Faz uma avaliação \n 🎤 Alternativa (B) Informar um fato apenas \n 🎤 Alternativa (C) É uma propaganda \n 🎤 Alternativa (D) É uma receita \n 🎤 Alternativa (E) É uma notícia policial \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

        pergunta_9_resposta = pergunta_9_resposta.upper()

        if pergunta_9_resposta == "P":
            if Ajuda_plateia > 0:
                Ajuda_plateia -= 1
                
                print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                print (" 🥸  É Alternativa (C)! \n 🥸  Claro que é (A)! \n 🥸  Obvio que NÂO é (A)! \n 🥸  Nunca que seria (E)! \n 🥸  Chuto que é (B)! \n 🥸  Só poderia ser (B)! \n 🥸  Certeza que é (A)! \n 🥸  Com certeza é (A)!\n 🥸  Acho que é (A)!\n\n")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

        elif pergunta_9_resposta == "U":
            if Ajuda_Universitarios > 0:
                Ajuda_Universitarios -= 1
                print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (A) \n\n ")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

        elif pergunta_9_resposta == "A":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Faz uma avaliação), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 51,400,00!!! \n\n | ENTER | \n"))
            Valor_Acumulado = 51200.0
            break

        elif pergunta_9_resposta == "B":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Informar um fato apenas), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

        elif pergunta_9_resposta == "C":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (É uma propaganda), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

        elif pergunta_9_resposta == "D":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (É uma receita), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

        elif pergunta_9_resposta == "E":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (É uma notícia policial), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

RESPOSTAS_PERGUNTA_9(pergunta_9_resposta = "")

menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 9️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 10️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
menu = menu.upper()

if menu == "M":
    menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 🥸   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

# PERGUNTA NUMERO 10

def RESPOSTAS_PERGUNTA_10 (pergunta_10_resposta):

    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_10_resposta = (input(" 🎤 PERGUNTA 10️: \n\n Qual habilidade está sendo usada ao comparar dois textos sobre o mesmo assunto? \n\n 🎤 Alternativa (A) Resolver contas \n 🎤 Alternativa (B) Reconhecer diferentes treatments da informação \n 🎤 Alternativa (C) Decorar palavras \n 🎤 Alternativa (D) Fazer desenhos \n 🎤 Alternativa (E) Traduzir idiomas \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

        pergunta_10_resposta = pergunta_10_resposta.upper()

        if pergunta_10_resposta == "P":
            if Ajuda_plateia > 0:
                Ajuda_plateia -= 1
                
                print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                print (" 🥸  Claro que é (B)! \n 🥸  Chuto que é (A)! \n 🥸  Com certeza é (B)! \n\n")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

        elif pergunta_10_resposta == "U":
            if Ajuda_Universitarios > 0:
                Ajuda_Universitarios -= 1
                print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (B) \n\n ")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

        elif pergunta_10_resposta == "A":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Resolver contas), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

        elif pergunta_10_resposta == "B":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Reconhecer diferentes tratamentos da informação), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 102,400,00!!! \n\n | ENTER | \n"))
            Valor_Acumulado = 102400.0
            break

        elif pergunta_10_resposta == "C":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Decorar palavras), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

        elif pergunta_10_resposta == "D":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Fazer desenhos), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

        elif pergunta_10_resposta == "E":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Traduzir idiomas), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

RESPOSTAS_PERGUNTA_10(pergunta_10_resposta = "")

menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 10 \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 11️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
menu = menu.upper()

if menu == "M":
    menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 🥸   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 10 \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 11️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
menu = menu.upper()

# AQUI È COMEÇANDO O TEMA 3

# TEMA 3: (Artigo de Opinião) DIFICULDADE: (😢 Facil😢)

print (input(" 🎤 Vamos dar inicio: \n Terceiro Tema: Artigo de Opinião \n Dificuldade: 😢 Médio😢  \n\n | ENTER | \n"))

# PERGUNTA NUMERO 11

def RESPOSTAS_PERGUNTA_11 (pergunta_11_resposta):

    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_11_resposta = (input(" 🎤 PERGUNTA 11️: \n\n \"Use protetor solar diariamente.\" \n\n A finalidade é:❔ \n\n 🎤 Alternativa (A) Convencer a proteger a saúde \n 🎤 Alternativa (B) Narrar um fato \n 🎤 Alternativa (C) Informar um acidente \n 🎤 Alternativa (D) Fazer humor \n 🎤 Alternativa (E) Contar uma lenda \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

        pergunta_11_resposta = pergunta_11_resposta.upper()

        if pergunta_11_resposta == "P":
            if Ajuda_plateia > 0:
                Ajuda_plateia -= 1
                
                print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                print (" 🥸  É Alternativa (C)! \n 🥸  Claro que é (A)! \n 🥸  Obvio que NÂO é (A)! \n 🥸  Nunca que seria (E)! \n 🥸  Chuto que é (B)! \n 🥸  Só poderia ser (B)! \n 🥸  Certeza que é (A)! \n 🥸  Com certeza é (A)!\n 🥸  Acho que é (A)!\n\n")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

        elif pergunta_11_resposta == "U":
            if Ajuda_Universitarios > 0:
                Ajuda_Universitarios -= 1
                print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (A) \n\n ")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

        elif pergunta_11_resposta == "A":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Convencer a proteger a saúde), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 204,800,00!!! \n\n | ENTER | \n"))
            Valor_Acumulado = 204800.0
            break

        elif pergunta_11_resposta == "B":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Narrar um fato), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

        elif pergunta_11_resposta == "C":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Informar um acidente), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

        elif pergunta_11_resposta == "D":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Fazer humor), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

        elif pergunta_11_resposta == "E":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Contar uma lenda), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

RESPOSTAS_PERGUNTA_11(pergunta_11_resposta = "")

menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 11 \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 12️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
menu = menu.upper()

if menu == "M":
    menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 🥸   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

    # PERGUNTA NUMERO 12

def RESPOSTAS_PERGUNTA_12 (pergunta_12_resposta):

    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_12_resposta = (input(" 🎤 PERGUNTA 12️: \n\n \"As inscrições terminam amanhã.\" \n\n O texto pretende:❔ \n\n 🎤 Alternativa (A) Informar \n 🎤 Alternativa (B) Criticar \n 🎤 Alternativa (C) Vender \n 🎤 Alternativa (D) Narrar \n 🎤 Alternativa (E) Entreter \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

        pergunta_12_resposta = pergunta_12_resposta.upper()

        if pergunta_12_resposta == "P":
            if Ajuda_plateia > 0:
                Ajuda_plateia -= 1
                
                print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                print (" 🥸  Claro que é (A)! \n 🥸  Chuto que é (C)! \n 🥸  Com certeza é (A)! \n\n")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

        elif pergunta_12_resposta == "U":
            if Ajuda_Universitarios > 0:
                Ajuda_Universitarios -= 1
                print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (A) \n\n ")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

        elif pergunta_12_resposta == "A":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Informar), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 409,600,00!!! \n\n | ENTER | \n"))
            Valor_Acumulado = 409600.0
            break

        elif pergunta_12_resposta == "B":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Criticar), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

        elif pergunta_12_resposta == "C":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Vender), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

        elif pergunta_12_resposta == "D":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Narrar), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 𫫵  😂 \n\n | ENTER | \n"))
            exit() 

        elif pergunta_12_resposta == "E":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Entreter), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 𫫵  😂 \n\n | ENTER | \n"))
            exit() 

RESPOSTAS_PERGUNTA_12(pergunta_12_resposta = "")

menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 12 \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 13 \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
menu = menu.upper()

if menu == "M":
    menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 🥸   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

# PERGUNTA NUMERO 13

def RESPOSTAS_PERGUNTA_13 (pergunta_13_resposta):

    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_13_resposta = (input(" 🎤 PERGUNTA 13: \n\n \"O filme foi incrível e merece ser assistido.\" \n\n O autor está:❔ \n\n 🎤 Alternativa (A) Informando \n 🎤 Alternativa (B) Opinando \n 🎤 Alternativa (C) Vendendo \n 🎤 Alternativa (D) Entrevistando \n 🎤 Alternativa (E) Explicando \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

        pergunta_13_resposta = pergunta_13_resposta.upper()

        if pergunta_13_resposta == "P":
            if Ajuda_plateia > 0:
                Ajuda_plateia -= 1
                
                print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                print (" 🥸  Claro que é (B)! \n 🥸  Chuto que é (A)! \n 🥸  Com certeza é (B)! \n\n")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

        elif pergunta_13_resposta == "U":
            if Ajuda_Universitarios > 0:
                Ajuda_Universitarios -= 1
                print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (B) \n\n ")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

        elif pergunta_13_resposta == "A":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Informando), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

        elif pergunta_13_resposta == "B":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Opinando), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 819,200,00!!! \n\n | ENTER | \n"))
            Valor_Acumulado = 819200.0
            break

        elif pergunta_13_resposta == "C":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Vendendo), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

        elif pergunta_13_resposta == "D":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Entrevistando), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

        elif pergunta_13_resposta == "E":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Explicando), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

RESPOSTAS_PERGUNTA_13(pergunta_13_resposta = "")

menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 13 \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 14 \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
menu = menu.upper()

if menu == "M":
    menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 🥸   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

# PERGUNTA NUMERO 14

def RESPOSTAS_PERGUNTA_14 (pergunta_14_resposta):

    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_14_resposta = (input(" 🎤 PERGUNTA 14: \n\n \"Promoção: leve 2 e pague 1.\" \n\n A finalidade é:❔ \n\n 🎤 Alternativa (A) Convencer o consumidor \n 🎤 Alternativa (B) Informar um acidente \n 🎤 Alternativa (C) Narrar uma aventura \n 🎤 Alternativa (D) Ensinar matemática \n 🎤 Alternativa (E) Fazer crítica \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

        pergunta_14_resposta = pergunta_14_resposta.upper()

        if pergunta_14_resposta == "P":
            if Ajuda_plateia > 0:
                Ajuda_plateia -= 1
                
                print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                print (" 🥸  Claro que é (A)! \n 🥸  Chuto que é (D)! \n 🥸  Com certeza é (A)! \n\n")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

        elif pergunta_14_resposta == "U":
            if Ajuda_Universitarios > 0:
                Ajuda_Universitarios -= 1
                print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (A) \n\n ")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

        elif pergunta_14_resposta == "A":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Convencer o consumidor), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 1,638,400,00!!! \n\n | ENTER | \n"))
            Valor_Acumulado = 1638400.0
            break

        elif pergunta_14_resposta == "B":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Informar um acidente), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

        elif pergunta_14_resposta == "C":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Narrar uma aventura), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

        elif pergunta_14_resposta == "D":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Ensinar matemática), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

        elif pergunta_14_resposta == "E":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Fazer crítica), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

RESPOSTAS_PERGUNTA_14(pergunta_14_resposta = "")

menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 14 \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 15 \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
menu = menu.upper()

if menu == "M":
    menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 🥸   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

# PERGUNTA NUMERO 15

def RESPOSTAS_PERGUNTA_15 (pergunta_15_resposta):

    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_15_resposta = (input(" 🎤 PERGUNTA 15: \n\n \"A dengue aumentou 30% neste ano.\" \n\n Esse trecho busca:❔ \n\n 🎤 Alternativa (A) Informar \n 🎤 Alternativa (B) Fazer humor \n 🎤 Alternativa (C) Vender \n 🎤 Alternativa (D) Narrar ficção \n 🎤 Alternativa (E) Opinar \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

        pergunta_15_resposta = pergunta_15_resposta.upper()

        if pergunta_15_resposta == "P":
            if Ajuda_plateia > 0:
                Ajuda_plateia -= 1
                
                print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                print (" 🥸  Claro que é (A)! \n 🥸  Chuto que é (E)! \n 🥸  Com certeza é (A)! \n\n")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

        elif pergunta_15_resposta == "U":
            if Ajuda_Universitarios > 0:
                Ajuda_Universitarios -= 1
                print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (A) \n\n ")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

        elif pergunta_15_resposta == "A":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Informar), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 3,276,800,00!!! \n\n | ENTER | \n"))
            Valor_Acumulado = 3276800.0
            break

        elif pergunta_15_resposta == "B":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Fazer humor), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

        elif pergunta_15_resposta == "C":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Vender), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

        elif pergunta_15_resposta == "D":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Narrar ficção), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

        elif pergunta_15_resposta == "E":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Opinar), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() 

RESPOSTAS_PERGUNTA_15(pergunta_15_resposta = "")

menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 15 \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 16 \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
menu = menu.upper()

if menu == "M":
    menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 🥸   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

# AQUI È COMEÇANDO O TEMA 4

# TEMA 4: (Textos Publicitários) DIFICULDADE: (😡 Dificil😡)

print (input(" 🎤 Vamos dar inicio: \n Quarto Tema: Textos Publicitários \n Dificuldade: 😡 Dificil😡  \n\n | ENTER | \n"))