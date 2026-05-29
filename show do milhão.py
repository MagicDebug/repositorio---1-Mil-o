Ajuda_plateia = 3
Ajuda_Universitarios = 5
Valor_Acumulado = 0.0

# AQUI É A INTRODUÇÂO DO JOGO COM O TITULO
print (input("\n\n 💰!!! O SHOW DO MILHÃO !!!💰  | ENTER |"))

# AQUI É AONDE O APRESENTADOR/MAQUINA QUE SE IDENTIFICA PELO MICROFONE (🎤) DA AS BOAS VINDAS AO USUÁRIO E PEDE PARA ELE SE APRESENTAR, USUARIO SENDO (👤)
print ("\n 🎤 Seja Bem Vindo ao Show Do Milhão! ")
nome_usuario = (input(" Vamos dar inicio ao Grande Show, Por Favor Se Apresente nos dizendo seu nome de usuario | DIGITE SEU NOME | \n\n | ENTER | \n\n 👤 "))

# AQUI ESTA AS EXPLICAÇÕES DE COMO SÂO AS REGRAS DO JOGO, SOBRE O VALOR DAS PERGUNTAS, AS AJUDAS E O OBJETIVO DO JOGO QUE É CHEGAR AO 1 MILHÃO
print (input("\n 🎤 " + nome_usuario + ", as Instruções do Jogo são as seguintes: \n  O Show será baseado na matéria de PORTUGUÊS e dividido em 5 temas do 😂 Mais Facil até o, 🤬 Mais Dificil, contendo 25 perguntas divididas para os diferentes 5 temas, podendo ter a ajuda dá; \n\n 🥸  Plateia 3 vezes \n 🎓 Universitarios 5 vezes \n\n  | ENTER | \n"))
print (input(" 🎤 Cada pergunta vale 💵 200,00 \n  A cada acerto o valor da proxima pergunta dobra, aumentando o resultado acumulado \n  Mas se você errar, o jogo acaba na hora! \n\n | ENTER | \n"))
print (input("\n 🎤 Seu Unico Objetivo é responder todas as 25 Perguntas e tentar chegar ao 1 milhão \n\n  MAS ATENÇÃO!!! \n  Se até o final da pergunta Numero 25 você tiver acumulado 1 milhão ou mais, você tem direito uma Pergunta Bonus chamada \n\n 💀 ARRISCA TUDO 💀 \n\n  Pergunta na qual se você acerta leva seu 💵 Valor Acumulado ao Dobro🤑  \n  Mas se Errar perde todo 💵 Valor Acumulado 💀 \n\n | ENTER | \n"))

# AQUI È DANDO INICIO E COMEÇANDO O TEMA 1
# TEMA 1: (NOTICIA E REPORTAGEM) DIFICULDADE: (😂 Mais Facil😂)
print (input(" 🎤 Vamos dar inicio: \n Primeiro Tema: Noticia e Reportagem \n Dificuldade: 😂 Mais Facil😂 \n\n | ENTER | \n"))

# PERGUNTA NUMERO 1
def RESPOSTAS_PERGUNTA_1 (pergunta_1_resposta):
    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_1_resposta = (input(" 🎤 PERGUNTA 1️: O que é uma noticia:❔ \n\n 🎤 Alternativa (A) Um texto Teatral \n 🎤 Alternativa (B) Um texto que informa fatos \n 🎤 Alternativa (C) Uma poesia \n 🎤 Alternativa (D) Uma receita \n 🎤 Alternativa (E) Um conto ficticio \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

        if pergunta_1_resposta == "P":
            if Ajuda_plateia > 0:
                Ajuda_plateia -= 1
                print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                print (" 🥸  É Alternativa (B)! \n 🥸  Claro que é (B)! \n 🥸  Obvio que é (D)! \n\n")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

        elif pergunta_1_resposta == "U":
            if Ajuda_Universitarios > 0:
                Ajuda_Universitarios -= 1
                print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (B) \n\n ")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

        elif pergunta_1_resposta == "A":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Um texto Teatral), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() # <--- ALTERADO: Encerra o programa imediatamente

        elif pergunta_1_resposta == "B":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Um texto que informa fatos), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 200,00!!! \n\n | ENTER | \n"))
            Valor_Acumulado = 200
            break

        elif pergunta_1_resposta == "C":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Uma poesia), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() # <--- ALTERADO: Encerra o programa imediatamente

        elif pergunta_1_resposta == "D":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Uma receita), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() # <--- ALTERADO: Encerra o programa imediatamente

        elif pergunta_1_resposta == "E":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Um conto ficticio), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() # <--- ALTERADO: Encerra o programa imediatamente

RESPOSTAS_PERGUNTA_1(pergunta_1_resposta = "")

menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 1 \n Você pode ver em seu (👜 MENU) o quanto já acumulou do prêmio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 2 \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSSEGUIR | \n\n | ENTER | \n "))

if menu == "M":
    menu = (input("\n 👜 MENU: \n\n 💵  Valor acumulado: " + str(Valor_Acumulado) + "\n 🥸   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

# PERGUNTA NUMERO 2   
def RESPOSTA_SPERGUNTA_2 (pergunta_2_resposta):
    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_2_resposta = (input(" 🎤 PERGUNTA 2️: Qual a função principal da reportagem:❔ \n\n 🎤 Alternativa (A) Inventar histórias \n 🎤 Alternativa (B) Criar humor \n 🎤 Alternativa (C) Aprofundar informações \n 🎤 Alternativa (D) Fazer propagandas \n 🎤 Alternativa (E) Criar poemas \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

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
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Inventar histórias), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() # <--- ALTERADO: Encerra o programa imediatamente

        elif pergunta_2_resposta == "B":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Criar humor), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() # <--- ALTERADO: Encerra o programa imediatamente

        elif pergunta_2_resposta == "C":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Aprofundar informações), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ✅ exata ✅ \n Você acaba de chegar há 💵 400,00!!! \n\n | ENTER | \n"))
            Valor_Acumulado = 400
            break

        elif pergunta_2_resposta == "D":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Fazer propagandas), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit() # <--- ALTERADO: Encerra o programa imediatamente

        elif pergunta_2_resposta == "E":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Criar poemas), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit()

RESPOSTA_SPERGUNTA_2(pergunta_2_resposta = "")

# MENU DA PRIMEIRA RESPOSTA NUMERO 2

menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 2️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 2️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))

if menu == "M":

    menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 🥸   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

# PERGUNTA NUMERO 3

def RESPOSTA_SPERGUNTA_3 (pergunta_3_resposta):

    # VARIAVEIS GLOBAL PARA AS AJUDAS
    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_3_resposta = (input(" 🎤 PERGUNTA 3️: A notícia apresenta opinião do autor:❔ \n\n 🎤 Alternativa (A) Sempre \n 🎤 Alternativa (B) Nunca informa fatos \n 🎤 Alternativa (C) Somente em poemas \n 🎤 Alternativa (D) Busca imparcialidade \n 🎤 Alternativa (E) Somente em romances \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

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
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Inventar histórias), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit()

        # ALTERNATIVA B (❌ ERRADA ❌)

        elif pergunta_3_resposta == "B":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Criar humor), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit()

        # ALTERNATIVA C (❌ ERRADA ❌)

        elif pergunta_3_resposta == "C":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Aprofundar informações), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit()

        # ALTERNATIVA D (✅ CORRETA ✅)

        elif pergunta_3_resposta == "D":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Fazer propagandas), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ✅ exata ✅ \n Você acaba de chegar há 💵  800,00!!! \n\n | ENTER | \n"))
            Valor_Acumulado = Valor_Acumulado * 2
            break

        # ALTERNATIVA E (❌ ERRADA ❌)

        elif pergunta_3_resposta == "E":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Criar poemas), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit()

RESPOSTA_SPERGUNTA_3(pergunta_3_resposta = "")

menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 3️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 4️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))

if menu == "M":

    menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 🥸   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

# PERGUNTA NUMERO 4

def RESPOSTA_SPERGUNTA_4️ (pergunta_4_resposta):

    # VARIAVEIS GLOBAL PARA AS AJUDAS
    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_4_resposta = (input(" 🎤 PERGUNTA 4️: Qual texto costuma ser mais aprofundado \n notícia ou reportagem:❔ \n\n 🎤 Alternativa (A) Charge \n 🎤 Alternativa (B) Piada \n 🎤 Alternativa (C) Reportagem \n 🎤 Alternativa (D) Bilhete \n 🎤 Alternativa (E) Anúncio \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

        # ALTERNATIVA DE AJUDA: 🥸PLATEIA🥸(P)
        if pergunta_4_resposta == "P":
            if Ajuda_plateia > 0:
                Ajuda_plateia -= 1
                
                print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                print (" 🥸  Não pode ser (D)! \n 🥸  Claro que é (E)! \n 🥸  Obvio que é (D)! \n 🥸  Nunca que seria (E)! \n 🥸  Chuto que é (C) \n 🥸  Claro que é (C)! \n 🥸  Eu iria na (C)! \n\n")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

        # ALTERNATIVA DE AJUDA: 🎓UNIVERSITÁRIOS🎓 (U)
        
        elif pergunta_4_resposta == "U":
            if Ajuda_Universitarios > 0:
                Ajuda_Universitarios -= 1
                
                print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (D) \n\n ")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

        # ALTERNATIVA A (❌ ERRADA ❌)
          
        elif pergunta_4_resposta == "A":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Inventar histórias), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit()

        # ALTERNATIVA B (❌ ERRADA ❌)

        elif pergunta_4_resposta == "B":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Criar humor), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit()

        # ALTERNATIVA C (✅ CORRETA ✅)

        elif pergunta_4_resposta == "C":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Aprofundar informações), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ✅ exata ✅ \n Você acaba de chegar há 💵  1,600,00!!! 🫵  😂 \n\n | ENTER | \n"))
            Valor_Acumulado = Valor_Acumulado * 2
            break

        # ALTERNATIVA D (❌ ERRADA ❌)

        elif pergunta_4_resposta == "D":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Fazer propagandas), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit()

        # ALTERNATIVA E (❌ ERRADA ❌)

        elif pergunta_4_resposta == "E":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Criar poemas), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit()

RESPOSTA_SPERGUNTA_4️(pergunta_4_resposta = "")

menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 4️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 5️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
if menu == "M":

    menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 🥸   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

# PERGUNTA NUMERO 5

def RESPOSTA_SPERGUNTA_5 (pergunta_5_resposta):

    # VARIAVEIS GLOBAL PARA AS AJUDAS
    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_5_resposta = (input(" 🎤 PERGUNTA 5️: Onde geralmente encontramos notícias:❔ \n\n 🎤 Alternativa (A) Jornais e sites \n 🎤 Alternativa (B) Receitas médicas \n 🎤 Alternativa (C) Músicas \n 🎤 Alternativa (D) Jogos \n 🎤 Alternativa (E) Poemas \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

        # ALTERNATIVA DE AJUDA: 🥸PLATEIA🥸(P)
        if pergunta_5_resposta == "P":
            if Ajuda_plateia > 0:
                Ajuda_plateia -= 1
                
                print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                print (" 🥸  Não pode ser (A)! \n 🥸  Claro que é (A)! \n 🥸  Vamos na (D)! \n 🥸  Nunca que seria (A)! \n 🥸  Chuto que é (A) \n 🥸  Claro que é (A)! \n 🥸  Eu não iria na (A)! \n\n")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

        # ALTERNATIVA DE AJUDA: 🎓UNIVERSITÁRIOS🎓 (U)
        
        elif pergunta_5_resposta == "U":
            if Ajuda_Universitarios > 0:
                Ajuda_Universitarios -= 1
                
                print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (A) \n\n ")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

        # ALTERNATIVA A (✅ CORRETA ✅)

        elif pergunta_5_resposta == "A":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Jornais e sites), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ✅ exata ✅ \n Você acaba de chegar há 💵  3,200,00!!! 🫵  😂 \n\n | ENTER | \n"))
            Valor_Acumulado = Valor_Acumulado * 2
            break

        # ALTERNATIVA B (❌ ERRADA ❌)

        elif pergunta_5_resposta == "B":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Criar humor), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit()

        # ALTERNATIVA C (❌ ERRADA ❌)

        elif pergunta_5_resposta == "C":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Aprofundar informações), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit()

        # ALTERNATIVA D (❌ ERRADA ❌)

        elif pergunta_5_resposta == "D":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Fazer propagandas), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
            exit()

        # ALTERNATIVA E (❌ ERRADA ❌)

        elif pergunta_5_resposta == "E":
            print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Criar poemas), sua resposta está eee... \n\n | ENTER | "))
            print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))

RESPOSTA_SPERGUNTA_5(pergunta_5_resposta = "")

menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 5️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 6️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))

if menu == "M":

    menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 🥸   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))