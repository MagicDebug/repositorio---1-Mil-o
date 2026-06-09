Ajuda_plateia = 3
Ajuda_Universitarios = 5
Valor_Acumulado = 0.0

nome_usuario = (input("          [--| 🤖 CYBER MIND 🤖 |--] \n\n 🤖 Olá, seja bem-vindo ao Jogo CYBER MIND!!! \n\n Para começar, me diga seu nome: \n\n | DIGITE SEU NOME | \n | TECLA [ ENTER ] PARA PROSSEGUIR |\n\n 👤 "))

print (input("\n\n 🤖 Olá " + nome_usuario + ", Para prosseguir; \n selecione a matéria na qual deseja jogar o jogo CYBER MIND \n\n | TECLA [ ENTER ] PARA PROSSEGUIR| \n"))

Máteria_selecionada = (input(" 🤖 Matérias: \n (1) 📕 PORTUGUÊS📕 \n (2) 📦 FISICA📦 / ➕ MATEMÁTICA ➖ \n (3) 🪖 HISTORIA🪖 \n (4) 🌏 GEOGRAFIA🌏 \n (5) 🦠 BIOLOGIA🦠 \n (6) 👥 SOCIOLOGIA 👥 \n\n | DIGITE O NÚMERO DA MATÉRIA | \n | TECLA [ ENTER ] PARA PROSSEGUIR | \n\n 👤 "))

#===========================================================================================================
#===========================================================================================================
# LUIZ È AQUI QUE AS MATERIAS SERÂO ESCRITAS APARTIR DO QUE O USURARIO DIGITOU, UTILIZEI O IF PARA PORTUGUÊS
#===========================================================================================================
#===========================================================================================================
def gerenciar_pergunta(numero, enunciado, alternativas, alternativa_correta, valor):
    global Valor_Acumulado
    while True:
        print(f"\n 📝 PERGUNTA {numero} - VALENDO R$ {valor:,.2f} 📝")
        print(f"\n 🎤 {enunciado}\n")
        for letra, texto in alternativas.items():
            print(f" 🎤 Alternativa ({letra}) {texto}")
        
        resposta = input("\n 👤 Sua resposta [A/B/C/D/E]: ").upper()
        
        if resposta in ["A", "B", "C", "D", "E"]:
            if resposta == alternativa_correta:
                print("\n ✅ EXATA! PARABÉNS!!! ✅ \n")
                Valor_Acumulado += valor
                break
            else:
                print("\n ❌ !!!ERRADA!!! ❌ \n VOCÊ PERDEU TUDO! O jogo acabou. 💀 \n")
                Valor_Acumulado = 0.0
                exit()


if Máteria_selecionada == "1":
        print (input("\n 🤖 MATERIA DE PORTUGÊS SELECIONADA: \n\n | TECLA [ ENTER ] PARA PROSSEGUIR | \n"))

        print (input("\n 🎤 Bem vindo " + nome_usuario + ", as Instruções do Jogo são as seguintes: \n O Show será baseado na matéria de PORTUGUÊS e dividido em 5 temas do 😂 Mais Fácil até o, 🤬 Mais Difícil \n contendo 25 perguntas divididas para os diferentes 5 temas, podendo ter a ajuda da; \n\n 👨  Plateia 3 vezes \n 🎓 Universitários 5 vezes \n\n  | ENTER | \n"))

        print (input(" 🎤 Cada pergunta vale 💵 40,000,00 \n  Mas se você errar, o jogo acaba na hora e você perde tudo!!! \n\n | ENTER | \n"))

        print (input("\n 🎤 Seu Único Objetivo é responder todas as 25 Perguntas e tentar chegar ao 1 milhão \n\n  MAS ATENÇÃO!!! \n no fim das 25 perguntas você acertar tudo irá \n há uma Pergunta Bônus chamada \n\n 💀 ARRISCA TUDO 💀 \n\n  Pergunta na qual se você acertar leva seu 💵 Valor Acumulado 🤑  \n  Mas se Errar perde todo 💵 Valor Acumulado 💀 \n\n | ENTER | \n"))

        # AQUI É DANDO INÍCIO E COMEÇANDO O TEMA 1
        # TEMA 1: (NOTÍCIA E REPORTAGEM) DIFICULDADE: (😂 Mais Fácil😂)

        print (input(" 🎤 Vamos dar início: \n Primeiro Tema: Notícia e Reportagem \n Dificuldade: 😂 Mais Fácil😂 \n\n | ENTER | \n"))

        # PERGUNTA NÚMERO 1

        def RESPOSTAS_PERGUNTA_1 (pergunta_1_resposta):
            global Ajuda_plateia
            global Ajuda_Universitarios
            global Valor_Acumulado

            while True:
                pergunta_1_resposta = (input(" 🎤 PERGUNTA 1️:\n\n [ A prefeitura inaugurou uma nova escola nesta segunda-feira. ] \n\n Qual é a finalidade desse texto:❔ \n\n 🎤 Alternativa (A) Convencer o leitor \n 🎤 Alternativa (B) Informar um fato \n 🎤 Alternativa (C) Fazer uma crítica \n 🎤 Alternativa (D) Vender um produto \n 🎤 Alternativa (E) Contar uma piada \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 👨  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITÁRIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))
                
                pergunta_1_resposta = pergunta_1_resposta.upper()

                if pergunta_1_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não têm certeza de qual seja a certa, então boa sorte! \n\n | ENTER | "))
                        print (" 👨  É Alternativa (B)! \n 👨  Claro que é (B)! \n 👨  Óbvio que é (D)! \n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))
                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))



                elif pergunta_1_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        print (input("\n 🎤 Você pediu a ajuda do Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (B) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

                elif pergunta_1_resposta == "A":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Convencer o leitor), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou a primeira então saira com 💵 00,00 \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_1_resposta == "B":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Informar um fato), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 40,000,00!!! \n\n | ENTER | \n"))
                    Valor_Acumulado = 40,000,00
                    break

                elif pergunta_1_resposta == "C":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Fazer uma crítica), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou a primeira então saira com 💵 00,00 \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_1_resposta == "D":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Vender um produto), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou a primeira então saira com 💵 00,00 \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_1_resposta == "E":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Contar uma piada), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou a primeira então saira com 💵 00,00 \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

        RESPOSTAS_PERGUNTA_1(pergunta_1_resposta = "")

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 1️  \n Você pode ver em seu (👜 MENU) o quanto já acumulou do prêmio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 2️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSSEGUIR APENAS APERTE ENTER | \n\n | ENTER | \n "))
        menu = menu.upper()

        if menu == "M":
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acumulado: R$ " + str(Valor_Acumulado) + "\n 🥸   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

        # PERGUNTA NÚMERO 2

        def RESPOSTAS_PERGUNTA_2 (pergunta_2_resposta):
            global Ajuda_plateia
            global Ajuda_Universitarios
            global Valor_Acumulado

            while True:
                pergunta_2_resposta = (input(" 🎤 PERGUNTA 2️: \n\n [ Compre já o novo celular com desconto. ] \n\n Qual é a finalidade do texto:❔ \n\n 🎤 Alternativa (A) Narrar uma história \n 🎤 Alternativa (B) Informar um acontecimento \n 🎤 Alternativa (C) Convencer o consumidor \n 🎤 Alternativa (D) Fazer uma denúncia \n 🎤 Alternativa (E) Ensinar gramática \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 👨  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))
                
                pergunta_2_resposta = pergunta_2_resposta.upper()

                if pergunta_2_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 👨  É Alternativa (C)! \n 👨  Claro que é (E)! \n 👨  Obvio que é (C)! \n 👨  Nunca que seria (E)!\n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                elif pergunta_2_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (C) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

                elif pergunta_2_resposta == "A":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Narrar uma história), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou ntão saira com 💵 40,000,00 \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_2_resposta == "B":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Informar um acontecimento), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou ntão saira com 💵 40,000,00 \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_2_resposta == "C":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Convencer o consumidor), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ✅ exata ✅ \n Você acaba de chegar há 💵 80,000,00!!! \n\n | ENTER | \n"))
                    Valor_Acumulado = 80,000,00
                    break

                elif pergunta_2_resposta == "D":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Fazer uma denúncia), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou ntão saira com 💵 40,000,00 \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_2_resposta == "E":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Ensinar gramática), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit()

        RESPOSTAS_PERGUNTA_2(pergunta_2_resposta = "")

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 2️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 3️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
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
                pergunta_3_resposta = (input(" 🎤 PERGUNTA 3️: \n\n [ Ontem ocorreu uma forte chuva na cidade. ] \n\n A Esse trecho pertence mais provavelmente a:❔ \n\n 🎤 Alternativa (A) Propaganda \n 🎤 Alternativa (B) Receita \n 🎤 Alternativa (C) Poema \n 🎤 Alternativa (D) Notícia \n 🎤 Alternativa (E) Música \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                
                pergunta_3_resposta = pergunta_3_resposta.upper()

                # ALTERNATIVA DE AJUDA: 🥸PLATEIA🥸(P)
                if pergunta_3_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 🥸  É Alternativa (A)! \n 🥸  Claro que é (E)! \n 🥸  Obvio que é (D)! \n 🥸  Nunca que seria (D)! \n 🥸  Chuto que é (D)!\n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                # ALTERNATIVA DE AJUDA: 🎓UNIVERSITÁRIOS🎓 (U)
                
                elif pergunta_3_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))
                        
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
                pergunta_4_resposta = (input(" 🎤 PERGUNTA 4️: \n\n [ Beba mais água e cuide da sua saúde. ] \n\n A finalidade é:❔ \n\n 🎤 Alternativa (A) Informar um acidente \n 🎤 Alternativa (B) Narrar um fato histórico \n 🎤 Alternativa (C) Dar orientação \n 🎤 Alternativa (D) Fazer humor \n 🎤 Alternativa (E) Divulgar um filme \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                
                pergunta_4_resposta = pergunta_4_resposta.upper()

                # ALTERNATIVA DE AJUDA: 🥸PLATEIA🥸(P)
                if pergunta_4_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        
                        print (" 🥸  Não pode ser (D)! \n 🥸  Claro que é (C)! \n 🥸  Obvio que é (C)! \n 🥸  Nunca que seria (E)! \n 🥸  Chuto que é (C) \n 🥸  Claro que é (C)! \n 🥸  Eu iria na (A)! \n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                # ALTERNATIVA DE AJUDA: 🎓UNIVERSITÁRIOS🎓 (U)
                elif pergunta_4_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (C) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

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
                pergunta_5_resposta = (input(" 🎤 PERGUNTA 5️: \n\n [ Vacinação contra gripe começa na próxima semana. ] \n\n O objetivo principal é:❔ \n\n 🎤 Alternativa (A) Informar \n 🎤 Alternativa (B) Criticar uma ação pública \n 🎤 Alternativa (C) Convencer a comprar algo \n 🎤 Alternativa (D) Contar uma aventura \n 🎤 Alternativa (E) Entreter \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_5_resposta = pergunta_5_resposta.upper()

                if pergunta_5_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 🥸  Não pode ser (A)! \n 🥸  Claro que é (A)! \n 🥸  Vamos na (D)! \n 🥸  Nunca que seria (A)! \n 🥸  Chuto que é (A) \n 🥸  Claro que é (A)! \n 🥸  Eu não iria na (A)! \n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))
                    
                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                elif pergunta_5_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (A) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))
                
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
                
                pergunta_6_resposta = (input(" 🎤 PERGUNTA 6️:\n\n [ A cidade inaugurou um novo hospital. ] \n\n [ O novo hospital é uma excelente conquista para a população. ] \n\n Qual a diferença de um para o outro:❔ \n\n 🎤 Alternativa (A) Ambos informam apenas fatos \n 🎤 Alternativa (B) O primeiro informa e o segundo opina \n 🎤 Alternativa (C) Ambos são propagandas \n 🎤 Alternativa (D) Ambos são poemas \n 🎤 Alternativa (E) O segundo é uma receita \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_6_resposta = pergunta_6_resposta.upper()

                if pergunta_6_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 🥸  É Alternativa (B)! \n 🥸  Claro que é (C)! \n 🥸  Obvio que é (A)! \n 🥸  Obvio que é (E)! \n 🥸  Obvio que é (B)\n 🥸  É Alternativa (B)!\n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                elif pergunta_6_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (B) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

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
                pergunta_7_resposta = (input(" 🎤 PERGUNTA 7️: \n\n [ O trânsito aumentou 20% ] \n\n [ O aumento do trânsito mostra a falta de planejamento urbano. ] Os textos apresentam:❔ \n\n 🎤 Alternativa (A) Receita \n 🎤 Alternativa (B) Opinião \n 🎤 Alternativa (C) Propaganda \n 🎤 Alternativa (D) Entrevista \n 🎤 Alternativa (E) Fábula \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_7_resposta = pergunta_7_resposta.upper()

                if pergunta_7_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 🥸  É Alternativa (D)! \n 🥸  Claro que é (B)! \n 🥸  Obvio que é (D)! \n 🥸  Nunca que seria (B)! \n 🥸  Chuto que é (B)!\n 🥸  Acho que é (B)!\n 🥸  Com certeza é (B)!\n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                elif pergunta_7_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (B) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

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
                pergunta_8_resposta = (input(" 🎤 PERGUNTA 8️: \n\n [ Nova praça é inaugurada no centro. ] \n\n [ A praça deve melhorar o lazer dos moradores. ] \n\n Qual deles expressa opinião:❔ \n\n 🎤 Alternativa (A) Texto 1 \n 🎤 Alternativa (B) Texto 2 \n 🎤 Alternativa (C) Ambos \n 🎤 Alternativa (D) Nenhum \n 🎤 Alternativa (E) Não é possível saber \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_8_resposta = pergunta_8_resposta.upper()

                if pergunta_8_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 🥸  É Alternativa (C)! \n 🥸  Claro que é (B)! \n 🥸  Obvio que NÂO é (B)! \n 🥸  Nunca que seria (E)! \n 🥸  Chuto que é (A)! \n 🥸  Só poderia ser (A)! \n 🥸  Certeza que é (B)! \n 🥸  Com certeza é (B)!\n 🥸  Acho que é (B)!\n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                elif pergunta_8_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (B) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

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
                pergunta_9_resposta = (input(" 🎤 PERGUNTA 9️: \n\n [ Escola recebe novos computadores. ] \n\n [ Os novos computadores representam um avanço importante. ] \n\n O Texto 2:❔ \n\n 🎤 Alternativa (A) Faz uma avaliação \n 🎤 Alternativa (B) Informar um fato apenas \n 🎤 Alternativa (C) É uma propaganda \n 🎤 Alternativa (D) É uma receita \n 🎤 Alternativa (E) É uma notícia policial \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_9_resposta = pergunta_9_resposta.upper()

                if pergunta_9_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 🥸  É Alternativa (C)! \n 🥸  Claro que é (A)! \n 🥸  Obvio que NÂO é (A)! \n 🥸  Nunca que seria (E)! \n 🥸  Chuto que é (B)! \n 🥸  Só poderia ser (B)! \n 🥸  Certeza que é (A)! \n 🥸  Com certeza é (A)!\n 🥸  Acho que é (A)!\n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                elif pergunta_9_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (A) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

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

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 9️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 1️0️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
        menu = menu.upper()

        if menu == "M":
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 🥸   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

        # PERGUNTA NUMERO 10

        def RESPOSTAS_PERGUNTA_10 (pergunta_10_resposta):

            global Ajuda_plateia
            global Ajuda_Universitarios
            global Valor_Acumulado

            while True:
                pergunta_10_resposta = (input(" 🎤 PERGUNTA 1️0️: \n\n Qual habilidade está sendo usada ao comparar dois textos sobre o mesmo assunto: ❔ \n\n 🎤 Alternativa (A) Resolver contas \n 🎤 Alternativa (B) Reconhecer diferentes tratamentos da informação \n 🎤 Alternativa (C) Decorar palavras \n 🎤 Alternativa (D) Fazer desenhos \n 🎤 Alternativa (E) Traduzir idiomas \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_10_resposta = pergunta_10_resposta.upper()

                if pergunta_10_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 🥸  Claro que é (B)! \n 🥸  Chuto que é (A)! \n 🥸  Com certeza é (B)! \n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                elif pergunta_10_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (B) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

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

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 1️0️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 1️1️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
        menu = menu.upper()

        if menu == "M":
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 🥸   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 1️0️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 1️1️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
        menu = menu.upper()

        # AQUI È COMEÇANDO O TEMA 3

        # TEMA 3: (Artigo de Opinião) DIFICULDADE: (😢 Médio😢)

        print (input(" 🎤 Vamos dar inicio: \n Terceiro Tema: Artigo de Opinião \n Dificuldade: 😢 Médio😢  \n\n | ENTER | \n"))

        # PERGUNTA NUMERO 11

        def RESPOSTAS_PERGUNTA_11 (pergunta_11_resposta):

            global Ajuda_plateia
            global Ajuda_Universitarios
            global Valor_Acumulado

            while True:
                pergunta_11_resposta = (input(" 🎤 PERGUNTA 1️1️: \n\n [ Use protetor solar diariamente. ] \n\n A finalidade é:❔ \n\n 🎤 Alternativa (A) Convencer a proteger a saúde \n 🎤 Alternativa (B) Narrar um fato \n 🎤 Alternativa (C) Informar um acidente \n 🎤 Alternativa (D) Fazer humor \n 🎤 Alternativa (E) Contar uma lenda \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_11_resposta = pergunta_11_resposta.upper()

                if pergunta_11_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 🥸  É Alternativa (C)! \n 🥸  Claro que é (A)! \n 🥸  Obvio que NÂO é (A)! \n 🥸  Nunca que seria (E)! \n 🥸  Chuto que é (B)! \n 🥸  Só poderia ser (B)! \n 🥸  Certeza que é (A)! \n 🥸  Com certeza é (A)!\n 🥸  Acho que é (A)!\n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                elif pergunta_11_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (A) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

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

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 1️0️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 1️2️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
        menu = menu.upper()

        if menu == "M":
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 🥸   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

            # PERGUNTA NUMERO 12

        def RESPOSTAS_PERGUNTA_12 (pergunta_12_resposta):

            global Ajuda_plateia
            global Ajuda_Universitarios
            global Valor_Acumulado

            while True:
                pergunta_12_resposta = (input(" 🎤 PERGUNTA 1️2️: \n\n [ As inscrições terminam amanhã. ] \n\n A finalidade é:❔ \n\n 🎤 Alternativa (A) Informar \n 🎤 Alternativa (B) Criticar \n 🎤 Alternativa (C) Vender \n 🎤 Alternativa (D) Narrar \n 🎤 Alternativa (E) Entreter \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_12_resposta = pergunta_12_resposta.upper()

                if pergunta_12_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 🥸  Claro que é (A)! \n 🥸  Chuto que é (C)! \n 🥸  Com certeza é (A)! \n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                elif pergunta_12_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (A) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

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

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 1️2️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 1️3️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
        menu = menu.upper()

        if menu == "M":
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 🥸   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

        # PERGUNTA NUMERO 13

        def RESPOSTAS_PERGUNTA_13 (pergunta_13_resposta):

            global Ajuda_plateia
            global Ajuda_Universitarios
            global Valor_Acumulado

            while True:
                pergunta_13_resposta = (input(" 🎤 PERGUNTA 1️3️: \n\n [ O filme foi incrível e merece ser assistido. ] \n\n O autor está:❔ \n\n 🎤 Alternativa (A) Informando \n 🎤 Alternativa (B) Opinando \n 🎤 Alternativa (C) Vendendo \n 🎤 Alternativa (D) Entrevistando \n 🎤 Alternativa (E) Explicando \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_13_resposta = pergunta_13_resposta.upper()

                if pergunta_13_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 🥸  Claro que é (B)! \n 🥸  Chuto que é (A)! \n 🥸  Com certeza é (B)! \n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                elif pergunta_13_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (B) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

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

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 1️3️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 1️4️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
        menu = menu.upper()

        if menu == "M":
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 🥸   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

        # PERGUNTA NUMERO 14

        def RESPOSTAS_PERGUNTA_14 (pergunta_14_resposta):

            global Ajuda_plateia
            global Ajuda_Universitarios
            global Valor_Acumulado

            while True:
                pergunta_14_resposta = (input(" 🎤 PERGUNTA 1️4️: \n\n [ Promoçã! leve 2e pague 1. ] \n\n A finalidade é:❔ \n\n 🎤 Alternativa (A) Convencer o consumidor \n 🎤 Alternativa (B) Informar um acidente \n 🎤 Alternativa (C) Narrar uma aventura \n 🎤 Alternativa (D) Ensinar matemática \n 🎤 Alternativa (E) Fazer crítica \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_14_resposta = pergunta_14_resposta.upper()

                if pergunta_14_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 🥸  Claro que é (A)! \n 🥸  Chuto que é (D)! \n 🥸  Com certeza é (A)! \n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                elif pergunta_14_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (A) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

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

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                elif pergunta_15_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (A) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

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

        # PERGUNTA NUMERO 16

        def RESPOSTAS_PERGUNTA_16 (pergunta_16_resposta):

            global Ajuda_plateia
            global Ajuda_Universitarios
            global Valor_Acumulado

            while True:
                pergunta_16_resposta = (input(" 🎤 PERGUNTA 16: \n\n [Texto 1:\n\nO desemprego caiu 5%.\n\nTexto 2:\n\nA queda do desemprego mostra melhora da economia.] \n\n Qual contém opinião?❔ \n\n 🎤 Alternativa (A) Texto 1 \n 🎤 Alternativa (B) Texto 2 \n 🎤 Alternativa (C) Ambos \n 🎤 Alternativa (D) Nenhum \n 🎤 Alternativa (E) Não é possível saber \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_16_resposta = pergunta_16_resposta.upper()

                if pergunta_16_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 🥸  Claro que é (B)! \n 🥸  Chuto que é (A)! \n 🥸  Com certeza é (B)! \n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                elif pergunta_16_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (B) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

                elif pergunta_16_resposta == "A":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Texto 1), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_16_resposta == "B":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Texto 2), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 6,553,600,00!!! \n\n | ENTER | \n"))
                    Valor_Acumulado = 6553600.0
                    break

                elif pergunta_16_resposta == "C":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Ambos), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_16_resposta == "D":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Nenhum), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_16_resposta == "E":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Não é possível saber), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

        RESPOSTAS_PERGUNTA_16(pergunta_16_resposta = "")

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 16 \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 17 \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
        menu = menu.upper()

        if menu == "M":
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 🥸   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

        # PERGUNTA NUMERO 17

        def RESPOSTAS_PERGUNTA_17 (pergunta_17_resposta):

            global Ajuda_plateia
            global Ajuda_Universitarios
            global Valor_Acumulado

            while True:
                pergunta_17_resposta = (input(" 🎤 PERGUNTA 17: \n\n Qual texto normalmente tenta convencer o leitor? \n\n 🎤 Alternativa (A) Receita \n 🎤 Alternativa (B) Propaganda \n 🎤 Alternativa (C) Tabela \n 🎤 Alternativa (D) Dicionário \n 🎤 Alternativa (E) Calendário \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_17_resposta = pergunta_17_resposta.upper()

                if pergunta_17_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 🥸  Claro que é (B)! \n 🥸  Chuto que é (A)! \n 🥸  Com certeza é (B)! \n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                elif pergunta_17_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (B) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

                elif pergunta_17_resposta == "A":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Receita), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_17_resposta == "B":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Propaganda), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 13,107,200,00!!! \n\n | ENTER | \n"))
                    Valor_Acumulado = 13107200.0
                    break

                elif pergunta_17_resposta == "C":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Tabela), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_17_resposta == "D":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Dicionário), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_17_resposta == "E":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Calendário), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

        RESPOSTAS_PERGUNTA_17(pergunta_17_resposta = "")

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 17 \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 18 \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
        menu = menu.upper()

        if menu == "M":
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 🥸   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

        # PERGUNTA NUMERO 18

        def RESPOSTAS_PERGUNTA_18 (pergunta_18_resposta):

            global Ajuda_plateia
            global Ajuda_Universitarios
            global Valor_Acumulado

            while True:
                pergunta_18_resposta = (input(" 🎤 PERGUNTA 18: \n\n [Texto 1:\n\nChoveu durante toda a tarde.\n\nTexto 2:\n\nA chuva trouxe transtornos para a população.] \n\n O Texto 2:❔ \n\n 🎤 Alternativa (A) Apenas informa \n 🎤 Alternativa (B) Acrescenta interpretação \n 🎤 Alternativa (C) É poema \n 🎤 Alternativa (D) É receita \n 🎤 Alternativa (E) É propaganda \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_18_resposta = pergunta_18_resposta.upper()

                if pergunta_18_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 🥸  Claro que é (B)! \n 🥸  Chuto que é (A)! \n 🥸  Com certeza é (B)! \n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                elif pergunta_18_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (B) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

                elif pergunta_18_resposta == "A":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Apenas informa), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_18_resposta == "B":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Acrescenta interpretação), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 26,214,400,00!!! \n\n | ENTER | \n"))
                    Valor_Acumulado = 26214400.0
                    break

                elif pergunta_18_resposta == "C":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (É poema), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_18_resposta == "D":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (É receita), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_18_resposta == "E":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (É propaganda), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

        RESPOSTAS_PERGUNTA_18(pergunta_18_resposta = "")

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 18 \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 19 \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
        menu = menu.upper()

        if menu == "M":
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 🥸   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

        # PERGUNTA NUMERO 19

        def RESPOSTAS_PERGUNTA_19 (pergunta_19_resposta):

            global Ajuda_plateia
            global Ajuda_Universitarios
            global Valor_Acumulado

            while True:
                pergunta_19_resposta = (input(" 🎤 PERGUNTA 19: \n\n Uma notícia e um artigo de opinião sobre o mesmo tema costumam diferir porque: \n\n 🎤 Alternativa (A) Ambos só opinam \n 🎤 Alternativa (B) Ambos só informam \n 🎤 Alternativa (C) Um informa e o outro argumenta \n 🎤 Alternativa (D) Ambos vendem produtos \n 🎤 Alternativa (E) Ambos contam histórias \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_19_resposta = pergunta_19_resposta.upper()

                if pergunta_19_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 🥸  Claro que é (C)! \n 🥸  Chuto que é (B)! \n 🥸  Com certeza é (C)! \n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                elif pergunta_19_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (C) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

                elif pergunta_19_resposta == "A":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Ambos só opinam), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_19_resposta == "B":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Ambos só informam), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_19_resposta == "C":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Um informa e o outro argumenta), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 52,428,800,00!!! \n\n | ENTER | \n"))
                    Valor_Acumulado = 52428800.0
                    break

                elif pergunta_19_resposta == "D":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Ambos vendem produtos), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_19_resposta == "E":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Ambos contam histórias), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

        RESPOSTAS_PERGUNTA_19(pergunta_19_resposta = "")

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 19 \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 20 \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
        menu = menu.upper()

        if menu == "M":
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 🥸   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

        # PERGUNTA NUMERO 20

        def RESPOSTAS_PERGUNTA_20 (pergunta_20_resposta):

            global Ajuda_plateia
            global Ajuda_Universitarios
            global Valor_Acumulado

            while True:
                pergunta_20_resposta = (input(" 🎤 PERGUNTA 20: \n\n Qual gênero textual geralmente tem intenção persuasiva? \n\n 🎤 Alternativa (A) Notícia \n 🎤 Alternativa (B) Propaganda \n 🎤 Alternativa (C) Relatório técnico \n 🎤 Alternativa (D) Ata \n 🎤 Alternativa (E) Certidão \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_20_resposta = pergunta_20_resposta.upper()

                if pergunta_20_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 🥸  Claro que é (B)! \n 🥸  Chuto que é (A)! \n 🥸  Com certeza é (B)! \n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                elif pergunta_20_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (B) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

                elif pergunta_20_resposta == "A":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Notícia), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_20_resposta == "B":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Propaganda), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 104,857,600,00!!! \n\n | ENTER | \n"))
                    Valor_Acumulado = 104857600.0
                    break

                elif pergunta_20_resposta == "C":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Relatório técnico), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_20_resposta == "D":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Ata), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_20_resposta == "E":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Certidão), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

        RESPOSTAS_PERGUNTA_20(pergunta_20_resposta = "")

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 20 \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 21 \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
        menu = menu.upper()

        if menu == "M":
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 🥸   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

        # AQUI È COMEÇANDO O TEMA 5

        # TEMA 5: (Complementos Verbais) DIFICULDADE: (😡 MUITO DIFICIL😡)

        print (input(" 🎤 Vamos dar inicio: \n Quarto e ultimo Tema: Complementos Verbais \n Dificuldade: 😡 MUITO DIFICIL😡  \n\n | ENTER | \n"))

        def RESPOSTAS_PERGUNTA_21 (pergunta_21_resposta):

            global Ajuda_plateia
            global Ajuda_Universitarios
            global Valor_Acumulado

            while True:
                pergunta_21_resposta = (input(" 🎤 PERGUNTA 21: \n\n [Texto 1:\n\nA prefeitura construiu uma ponte.\n\nTexto 2:\n\nA construção da ponte foi uma decisão acertada.] \n\n Qual apresenta julgamento?❔ \n\n 🎤 Alternativa (A) Texto 1 \n 🎤 Alternativa (B) Texto 2 \n 🎤 Alternativa (C) Ambos \n 🎤 Alternativa (D) Nenhum \n 🎤 Alternativa (E) Não é possível saber \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_21_resposta = pergunta_21_resposta.upper()

                if pergunta_21_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 🥸  Claro que é (B)! \n 🥸  Chuto que é (A)! \n 🥸  Com certeza é (B)! \n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                elif pergunta_21_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (B) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

                elif pergunta_21_resposta == "A":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Texto 1), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_21_resposta == "B":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Texto 2), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 209,715,200,00!!! \n\n | ENTER | \n"))
                    Valor_Acumulado = 209715200.0
                    break

                elif pergunta_21_resposta == "C":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Ambos), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_21_resposta == "D":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Nenhum), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_21_resposta == "E":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Não é possível saber), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

        RESPOSTAS_PERGUNTA_21(pergunta_21_resposta = "")

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 21 \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 22 \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
        menu = menu.upper()

        if menu == "M":
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 🥸   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

        # PERGUNTA NUMERO 22

        def RESPOSTAS_PERGUNTA_22 (pergunta_22_resposta):

            global Ajuda_plateia
            global Ajuda_Universitarios
            global Valor_Acumulado

            while True:
                pergunta_22_resposta = (input(" 🎤 PERGUNTA 22: \n\n Ao comparar dois textos sobre o mesmo fato, devemos observar: \n\n 🎤 Alternativa (A) Apenas o tamanho \n 🎤 Alternativa (B) Apenas o título \n 🎤 Alternativa (C) O modo como a informação é apresentada \n 🎤 Alternativa (D) Apenas as imagens \n 🎤 Alternativa (E) Apenas o autor \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_22_resposta = pergunta_22_resposta.upper()

                if pergunta_22_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 🥸  Claro que é (C)! \n 🥸  Chuto que é (E)! \n 🥸  Com certeza é (C)! \n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                elif pergunta_22_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (C) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

                elif pergunta_22_resposta == "A":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Apenas o tamanho), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_22_resposta == "B":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Apenas o título), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_22_resposta == "C":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (O modo como a informação é apresentada), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 419,430,400,00!!! \n\n | ENTER | \n"))
                    Valor_Acumulado = 419430400.0
                    break

                elif pergunta_22_resposta == "D":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Apenas as imagens), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_22_resposta == "E":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Apenas o autor), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

        RESPOSTAS_PERGUNTA_22(pergunta_22_resposta = "")

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 22 \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 23 \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
        menu = menu.upper()

        if menu == "M":
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 🥸   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

        # PERGUNTA NUMERO 23

        def RESPOSTAS_PERGUNTA_23 (pergunta_23_resposta):

            global Ajuda_plateia
            global Ajuda_Universitarios
            global Valor_Acumulado

            while True:
                pergunta_23_resposta = (input(" 🎤 PERGUNTA 23: \n\n Qual texto apresenta mais frequentemente opiniões? \n\n 🎤 Alternativa (A) Notícia \n 🎤 Alternativa (B) Artigo de opinião \n 🎤 Alternativa (C) Certidão \n 🎤 Alternativa (D) Boletim \n 🎤 Alternativa (E) Manual \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_23_resposta = pergunta_23_resposta.upper()

                if pergunta_23_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 🥸  Claro que é (B)! \n 🥸  Chuto que é (A)! \n 🥸  Com certeza é (B)! \n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                elif pergunta_23_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (B) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

                elif pergunta_23_resposta == "A":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Notícia), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_23_resposta == "B":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Artigo de opinião), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 838,860,800,00!!! \n\n | ENTER | \n"))
                    Valor_Acumulado = 838860800.0
                    break

                elif pergunta_23_resposta == "C":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Certidão), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_23_resposta == "D":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Boletim), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_23_resposta == "E":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Manual), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

        RESPOSTAS_PERGUNTA_23(pergunta_23_resposta = "")

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 23 \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 24 \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
        menu = menu.upper()

        if menu == "M":
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 🥸   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

        # PERGUNTA NUMERO 24

        def RESPOSTAS_PERGUNTA_24 (pergunta_24_resposta):

            global Ajuda_plateia
            global Ajuda_Universitarios
            global Valor_Acumulado

            while True:
                pergunta_24_resposta = (input(" 🎤 PERGUNTA 24: \n\n A frase:\n\n\"Na minha opinião, o projeto foi excelente.\"\n\nindica:❔ \n\n 🎤 Alternativa (A) Informação neutra \n 🎤 Alternativa (B) Opinião do autor \n 🎤 Alternativa (C) Propaganda \n 🎤 Alternativa (D) Receita \n 🎤 Alternativa (E) Entrevista \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_24_resposta = pergunta_24_resposta.upper()

                if pergunta_24_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 🥸  Claro que é (B)! \n 🥸  Chuto que é (A)! \n 🥸  Com certeza é (B)! \n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))
                    
                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                elif pergunta_24_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (B) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

                elif pergunta_24_resposta == "A":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Informação neutra), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_24_resposta == "B":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Opinião do autor), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 1,677,721,600,00!!! \n\n | ENTER | \n"))
                    Valor_Acumulado = 1677721600.0
                    break

                elif pergunta_24_resposta == "C":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Propaganda), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_24_resposta == "D":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Receita), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_24_resposta == "E":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Entrevista), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

        RESPOSTAS_PERGUNTA_24(pergunta_24_resposta = "")

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 24 \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 25 \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
        menu = menu.upper()

        if menu == "M":
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 🥸   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

        # PERGUNTA NUMERO 25

        def RESPOSTAS_PERGUNTA_25 (pergunta_25_resposta):

            global Ajuda_plateia
            global Ajuda_Universitarios
            global Valor_Acumulado

            while True:
                pergunta_25_resposta = (input(" 🎤 PERGUNTA 25: \n\n Por que é importante comparar textos sobre o mesmo tema? \n\n 🎤 Alternativa (A) Para decorar palavras \n 🎤 Alternativa (B) Para perceber diferentes pontos de vista \n 🎤 Alternativa (C) Para aprender matemática \n 🎤 Alternativa (D) Para traduzir idiomas \n 🎤 Alternativa (E) Para copiar textos \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_25_resposta = pergunta_25_resposta.upper()

                if pergunta_25_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 🥸  Claro que é (B)! \n 🥸  Chuto que é (A)! \n 🥸  Com certeza é (B)! \n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                elif pergunta_25_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (B) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

                elif pergunta_25_resposta == "A":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Para decorar palavras), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_25_resposta == "B":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Para perceber diferentes pontos de vista), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 3,355,443,200,00!!! \n\n | ENTER | \n"))
                    Valor_Acumulado = 3355443200.0
                    break

                elif pergunta_25_resposta == "C":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Para aprender matemática), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_25_resposta == "D":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Para traduzir idiomas), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_25_resposta == "E":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Para copiar textos), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

        RESPOSTAS_PERGUNTA_25(pergunta_25_resposta = "")

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 25 \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA BONUS \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
        menu = menu.upper()

        if menu == "M":
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 🥸   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

        # PREPARAÇÂO PARA A ULTIMA PERGUNTA

        print (input(" 🎤 " + nome_usuario + ", Parabens por conseguir chegar até aqui!!! \n Você conseguiu acomular um total de... | \n\n | ENTER | \n"))
        print (input(" 🎤 " + nome_usuario + ", 💵  !!!3,355,443,200,00!!! 💵 \n\n 🎤 Agora para por fim encerrar nosso programa, você enfim chegou na legitima ultima pergunta\n esta pergunta é definitiva para saber se você sai daqui com seu; \n\n | 💵  valor acumulado em dobro 💵 ou \n | 💀 se saira daqui sem nada 💀 \n\n 🎤 Vamos para á: \n\n | ENTER | \n"))

        # PERGUNTA 26

        def PERGUNTA_26_ARRISCA_TUDO_ (resposta_bonus):

            global Valor_Acumulado

            while True:
                resposta_bonus = (input(" 💀 ARRISCA TUDO 💀 \n Pergunta 26: \n\n 🎤 [Texto 1] \n A inteligência artificial automatiza tarefas e amplia a produtividade, liberando o ser humano para o pensamento estratégico. \n\n 🎤 [Texto 2] \n Ao assumir as escolhas estratégicas com base em dados históricos, os algoritmos moldam as decisões humanas de forma imperceptível. \n\n Confrontando os dois textos, conclui-se que o Texto 2:❔ \n\n 🎤 Alternativa (A) Corrobora a tese do Texto 1 sobre a total liberdade humana \n 🎤 Alternativa (B) Problematiza o Texto 1 ao sugerir uma perda sutil de autonomia \n 🎤 Alternativa (C) Limita-se a descrever o funcionamento técnico de um algoritmo \n 🎤 Alternativa (D) Desmente o Texto 1 ao provar que a produtividade diminuiu \n 🎤 Alternativa (E) Trata de um assunto completamente diferente do Texto 1 \n\n | SE VOCÊ ACERTAR: SEU PRÊMIO DOBRA PARA 💵 6,710,886,400,00!!! 🤑 | \n | SE VOCÊ ERRAR: PERDE TUDO E SAI COM R$ 0.00! 💀 | \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n\n | ENTER | \n\n 👤 "))

                resposta_bonus = resposta_bonus.upper()

                if resposta_bonus == "A":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é a (A), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ !!!ERRADA!!! ❌ \n VOCÊ ARRISCOU TUDO E PERDEU!!! O jogo acabou na última linha! 💀  😂 \n\n | ENTER | \n"))
                    Valor_Acumulado = 0.0
                    exit() 

                elif resposta_bonus == "B":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é a (B), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ✅ EXATA! PARABÉNS!!! ✅ \n VOCÊ DOBROU SEU PRÊMIO E SE TORNOU O MAIOR CAMPEÃO DO SHOW DO MILHÃO!!! 🤑 \n Você acaba de receber: 💵 R$ 6.710.886.400,00!!! \n\n | ENTER | \n"))
                    Valor_Acumulado = 6710886400.0
                    break

                elif resposta_bonus == "C":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é a (C), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ !!!ERRADA!!! ❌ \n VOCÊ ARRISCOU TUDO E PERDEU!!! O jogo acabou na última linha! 💀  😂 \n\n | ENTER | \n"))
                    Valor_Acumulado = 0.0
                    exit() 

                elif resposta_bonus == "D":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é a (D), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ !!!ERRADA!!! ❌ \n VOCÊ ARRISCOU TUDO E PERDEU!!! O jogo acabou na última linha! 💀  😂 \n\n | ENTER | \n"))
                    Valor_Acumulado = 0.0
                    exit() 

                elif resposta_bonus == "E":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é a (E), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ !!!ERRADA!!! ❌ \n VOCÊ ARRISCOU TUDO E PERDEU!!! O jogo acabou na última linha! 💀  😂 \n\n | ENTER | \n"))
                    Valor_Acumulado = 0.0
                    exit() 

                    PERGUNTA_26_ARRISCA_TUDO_(resposta_bonus = "")

                    print (input(" 🎤 " + nome_usuario + ", Obrigado por jogar e testar nosso primeiro show \n 🎤 Gostaria de dizer no lugar do criador do meu papai, responsavel por criar o codigo deste Show, que foi um trabalho de muita dedicação dele. \n\n | ENTER | \n"))

elif Máteria_selecionada == "4" :
    input("\n 🤖 MATERIA DE GEOGRAFIA SELECIONADA: \n\n | TECLA [ ENTER ] PARA PROSSEGUIR | \n")

    input("\n 🎤 Bem vindo " + nome_usuario + ", o Show será baseado na matéria de GEOGRAFIA.\n\n | ENTER | \n")
    
    # ==========================================
    # BLOCO DE PERGUNTAS (1 A 15)
    # GEOGRAFIA
    # ==========================================

    # --- TEMA 1 ---
    input(" 🎤 Vamos dar início: \n Primeiro Tema: Demografia e População \n Dificuldade: 😊 Fácil 😊 \n\n | ENTER | \n")

    gerenciar_pergunta(1, "O que a Demografia estuda?",
                       {"A": "Os fenômenos climáticos", "B": "A população humana", "C": "Os recursos minerais", "D": "Os oceanos", "E": "As indústrias"}, "B", 100.0)

    gerenciar_pergunta(2, "Qual indicador representa o número de nascimentos em uma população?",
                       {"A": "Mortalidade", "B": "Migração", "C": "Natalidade", "D": "Urbanização", "E": "Densidade"}, "C", 200.0)

    gerenciar_pergunta(3, "O aumento da expectativa de vida significa que:",
                       {"A": "As pessoas vivem menos", "B": "A população diminui rapidamente", "C": "As pessoas vivem mais tempo", "D": "Há mais nascimentos", "E": "Há menos cidades"}, "C", 400.0)

    gerenciar_pergunta(4, "A densidade demográfica corresponde:",
                       {"A": "Ao número de idosos", "B": "Ao número de habitantes por área", "C": "Ao número de nascimentos", "D": "Ao tamanho das cidades", "E": "Ao número de migrantes"}, "B", 800.0)

    gerenciar_pergunta(5, "Quando o número de nascimentos é maior que o de mortes, ocorre:",
                       {"A": "Crescimento vegetativo positivo", "B": "Êxodo rural", "C": "Migração internacional", "D": "Urbanização", "E": "Redução populacional"}, "A", 1600.0)

    # --- TEMA 2 ---
    input(" 🎤 Vamos avançar: \n Segundo Tema: Migração e Urbanização \n Dificuldade: 😐 Média 😐 \n\n | ENTER | \n")

    gerenciar_pergunta(6, "O deslocamento de pessoas de um lugar para outro recebe o nome de:",
                       {"A": "Industrialização", "B": "Urbanização", "C": "Migração", "D": "Globalização", "E": "Colonização"}, "C", 3200.0)

    gerenciar_pergunta(7, "Quando uma pessoa entra em um país para morar nele, ocorre:",
                       {"A": "Emigração", "B": "Imigração", "C": "Êxodo rural", "D": "Natalidade", "E": "Urbanização"}, "B", 6400.0)

    gerenciar_pergunta(8, "Quando uma pessoa deixa seu país de origem para viver em outro, ocorre:",
                       {"A": "Imigração", "B": "Urbanização", "C": "Natalidade", "D": "Emigração", "E": "Industrialização"}, "D", 12800.0)

    gerenciar_pergunta(9, "O êxodo rural corresponde:",
                       {"A": "À saída da cidade para o campo", "B": "À chegada de estrangeiros", "C": "À saída do campo para a cidade", "D": "Ao crescimento industrial", "E": "À redução da população"}, "C", 25600.0)

    gerenciar_pergunta(10, "Um dos principais motivos do êxodo rural é:",
                       {"A": "Busca por empregos e serviços urbanos", "B": "Aumento das áreas agrícolas", "C": "Redução das cidades", "D": "Crescimento da natalidade", "E": "Mudança climática global"}, "A", 51200.0)

    # --- TEMA 3 ---
    input(" 🎤 Vamos avançar: \n Terceiro Tema: Desigualdade Econômica e IDH \n Dificuldade: 😡 Difícil 😡 \n\n | ENTER | \n")

    gerenciar_pergunta(11, "O IDH significa:",
                       {"A": "Índice de Desenvolvimento Habitacional", "B": "Índice de Desenvolvimento Humano", "C": "Indicador Demográfico Humano", "D": "Instituto de Desenvolvimento Humano", "E": "Índice de Distribuição Habitacional"}, "B", 102400.0)

    gerenciar_pergunta(12, "Qual dos fatores abaixo é utilizado no cálculo do IDH?",
                       {"A": "Quantidade de rios", "B": "Produção agrícola", "C": "Educação", "D": "Número de montanhas", "E": "Extensão territorial"}, "C", 204800.0)

    gerenciar_pergunta(13, "Uma medida que pode ajudar a reduzir as desigualdades econômicas é:",
                       {"A": "Diminuir o acesso à educação", "B": "Reduzir empregos", "C": "Investir em educação e qualificação", "D": "Aumentar a exclusão social", "E": "Fechar escolas públicas"}, "C", 409600.0)

    gerenciar_pergunta(14, "Além da educação, o IDH também considera:",
                       {"A": "Saúde e renda", "B": "Vegetação e clima", "C": "Relevo e hidrografia", "D": "Mineração e agricultura", "E": "Comércio e turismo"}, "A", 819200.0)

    gerenciar_pergunta(15, "Um país com alto IDH geralmente apresenta:",
                       {"A": "Baixa qualidade de vida", "B": "Pouco acesso à educação", "C": "Baixa expectativa de vida", "D": "Melhores condições de vida", "E": "Ausência de serviços públicos"}, "D", 1638400.0)
        # --- TEMA 4 ---
    print (input(" 🎤 Vamos dar início: \n Quarto Tema: Meio Ambiente \n Dificuldade: 😡 Difícil 😡 \n\n | ENTER | \n"))

    gerenciar_pergunta(16, "Qual é o principal gás responsável pelo efeito estufa intensificado?",
                        {"A": "Oxigênio", "B": "Nitrogênio", "C": "Dióxido de Carbono (CO₂)", "D": "Hidrogênio", "E": "Hélio"}, "C", 3276800.0)

    gerenciar_pergunta(17, "O desmatamento da Amazônia contribui principalmente para:",
                        {"A": "Aumento da biodiversidade", "B": "Redução das chuvas", "C": "Formação de geleiras", "D": "Diminuição do efeito estufa", "E": "Resfriamento global"}, "B", 6553600.0)

    gerenciar_pergunta(18, "Qual prática contribui para o desenvolvimento sustentável?",
                        {"A": "Desperdício de água", "B": "Queimadas frequentes", "C": "Reciclagem de materiais", "D": "Poluição dos rios", "E": "Desmatamento"}, "C", 13107200.0)

    gerenciar_pergunta(19, "O aquecimento global está relacionado principalmente:",
                        {"A": "Ao aumento dos gases de efeito estufa", "B": "À diminuição da população", "C": "Ao aumento da pesca", "D": "À formação de vulcões", "E": "À redução das cidades"}, "A", 26214400.0)

    gerenciar_pergunta(20, "Qual dos problemas abaixo é considerado um impacto ambiental urbano?",
                        {"A": "Poluição do ar", "B": "Formação de montanhas", "C": "Movimento das placas tectônicas", "D": "Erosão glacial", "E": "Marés oceânicas"}, "A", 52428800.0)


    # --- TEMA 5 ---
    print (input(" 🎤 Vamos dar início: \n Quinto Tema: Cartografia e Geopolítica \n Dificuldade: 😡 MUITO DIFÍCIL 😡 \n\n | ENTER | \n"))

    gerenciar_pergunta(21, "Qual instrumento é utilizado para determinar coordenadas geográficas por satélite?",
                        {"A": "Bússola", "B": "GPS", "C": "Barômetro", "D": "Termômetro", "E": "Altímetro"}, "B", 104857600.0)

    gerenciar_pergunta(22, "Os paralelos são linhas imaginárias utilizadas para medir:",
                        {"A": "Longitude", "B": "Altitude", "C": "Latitude", "D": "Distância", "E": "Profundidade"}, "C", 209715200.0)

    gerenciar_pergunta(23, "O Meridiano de Greenwich corresponde a:",
                        {"A": "Latitude 0°", "B": "Longitude 0°", "C": "Trópico de Capricórnio", "D": "Linha do Equador", "E": "Polo Norte"}, "B", 419430400.0)

    gerenciar_pergunta(24, "A disputa por territórios, recursos e influência entre países é estudada principalmente pela:",
                        {"A": "Meteorologia", "B": "Cartografia", "C": "Demografia", "D": "Geopolítica", "E": "Oceanografia"}, "D", 838860800.0)

    gerenciar_pergunta(25, "Qual bloco econômico é formado por Brasil, Argentina, Paraguai e Uruguai?",
                        {"A": "União Europeia", "B": "NAFTA", "C": "Mercosul", "D": "APEC", "E": "OTAN"}, "C", 1677721600.0)
    
    def PERGUNTA_26_ARRISCA_TUDO_(resposta_bonus):
        global Valor_Acumulado

        while True:
            resposta_bonus = (input(" 💀 ARRISCA TUDO 💀 \n Pergunta 26: \n\n"
            "🎤 O conceito de globalização refere-se principalmente a:\n\n"
            "🎤 Alternativa (A) Isolamento econômico entre países\n"
            "🎤 Alternativa (B) Ampliação das conexões econômicas, culturais e tecnológicas entre diferentes regiões do mundo\n"
            "🎤 Alternativa (C) Extinção das fronteiras nacionais\n"
            "🎤 Alternativa (D) Diminuição do comércio internacional\n"
            "🎤 Alternativa (E) Substituição dos governos por empresas privadas\n\n"
            "| SE VOCÊ ACERTAR: SEU PRÊMIO DOBRA! 🤑 |\n"
            "| SE VOCÊ ERRAR: PERDE TUDO! 💀 |\n\n"
            "| PARA RESPONDER DIGITE [A/B/C/D/E] |\n\n 👤 "))
            resposta_bonus = resposta_bonus.upper()

            if resposta_bonus == "B":
                print(input("\n 🎤 ✅ EXATA! PARABÉNS!!! ✅ \n VOCÊ DOBROU SEU PRÊMIO!!! \n\n | ENTER | "))
                Valor_Acumulado = 6710886400.0
                break

            elif resposta_bonus in ["A", "C", "D", "E"]:
                print(input("\n 🎤 ❌ ERRADA! ❌ \n VOCÊ PERDEU TUDO! 💀 \n\n | ENTER | "))
                Valor_Acumulado = 0.0
                sys.exit()

                        

                

            #print (input(" CREDITOS: \n\n Matéria de Português: Leonardo Matias de Souza Fonseca \n Matéria de Fisica: Arthur Marques \n Matéria de Geografia: Luís Fernando \n Matéria de Química: Fernanda Mariah \n Matéria de História: Joel \n Materia de Matemática: Heitor Ribeiro n\n | ENTER | \n"))

