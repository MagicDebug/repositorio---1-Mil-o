Ajuda_plateia = 99
Ajuda_Universitarios = 99
Valor_Acumulado = 0


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
    global Ajuda_plateia
    global Ajuda_Universitarios

    while True:
        print(f"\n 📝 PERGUNTA {numero} - VALENDO R$ {valor:,.2f} 📝")
        print(f"\n 🎤 {enunciado}\n")

        for letra, texto in alternativas.items():
            print(f" 🎤 Alternativa ({letra}) {texto}")

        resposta = input(
            "\n | RESPONDA [A/B/C/D/E] |"
            "\n | PLATEIA [P] |"
            "\n | UNIVERSITÁRIOS [U] |"
            "\n\n 👤 "
        ).upper()

        if resposta == "P":
            if Ajuda_plateia > 0:
                Ajuda_plateia -= 1

                print("\n 👨 AJUDA DA PLATEIA 👨")
                print(f" 👨 Acho que é ({alternativa_correta})")
                print(" 👨 Talvez seja (A)")
                print(f" 👨 Tenho quase certeza que é ({alternativa_correta})")
            else:
                print("\n ❌ Você não possui mais ajudas da plateia!")

        elif resposta == "U":
            if Ajuda_Universitarios > 0:
                Ajuda_Universitarios -= 1

                print("\n 🎓 AJUDA DOS UNIVERSITÁRIOS 🎓")
                print(f" 🎓 Nossa resposta é ({alternativa_correta})")
            else:
                print("\n ❌ Você não possui mais ajudas dos universitários!")

        elif resposta in ["A", "B", "C", "D", "E"]:

            if resposta == alternativa_correta:
                print("\n ✅ EXATA! PARABÉNS!!! ✅\n")
                Valor_Acumulado += valor
                break

            else:
                print("\n ❌ !!!ERRADA!!! ❌")
                print(" 💀 VOCÊ PERDEU TUDO!")
                Valor_Acumulado = 0.0
                exit()

        else:
            print("\n ⚠️ Digite apenas A, B, C, D, E, P ou U.")


if Máteria_selecionada == "1":
        print (input("\n 🤖 MATERIA DE PORTUGÊS SELECIONADA: \n\n | TECLA [ ENTER ] PARA PROSSEGUIR | \n"))

        print (input("\n 🎤 Bem vindo " + nome_usuario + ", as Instruções do Jogo são as seguintes: \n O Show será baseado na matéria de PORTUGUÊS e dividido em 5 temas do 😂 Mais Fácil até o, 🤬 Mais Difícil \n contendo 25 perguntas divididas para os diferentes 5 temas, podendo ter a ajuda da; \n\n 👨  Plateia 3 vezes \n 🎓 Universitários 5 vezes \n\n  | ENTER | \n"))

        print (input(" 🎤 Cada pergunta vale 💵 40,000,00 \n  Mas se você errar, o jogo acaba na hora e você perde tudo!!! \n\n | ENTER | \n"))

        print (input("\n 🎤 Seu Único Objetivo é responder corretamente todas as 25 Perguntas, e tentar chegar ao 1 milhão \n\n  MAS ATENÇÃO!!! \n se chegar até o fim \n há uma Pergunta Bônus chamada \n\n 💀 ARRISCA TUDO 💀 \n\n  Pergunta na qual se você acertar leva seu 💵 Milhão 🤑  \n  Mas se Errar não levara o 💵 Valor Acumulado 💀 \n\n | ENTER | \n"))

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
                    Valor_Acumulado = 40000
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
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acumulado: R$ " + str(Valor_Acumulado) + "\n 👨   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

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
                        print (" 👨  É Alternativa (C)! \n 👨  Claro que é (E)! \n 👨  Obvio que é (C)! \n 👨  Nunca que seria (E)! \n\n")
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
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 40,000,00 \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_2_resposta == "B":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Informar um acontecimento), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 40,000,00 \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_2_resposta == "C":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Convencer o consumidor), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ✅ exata ✅ \n Você acaba de chegar há 💵 80,000,00!!! \n\n | ENTER | \n"))
                    Valor_Acumulado = 80000
                    break

                elif pergunta_2_resposta == "D":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Fazer uma denúncia), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 40,000,00 \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_2_resposta == "E":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Ensinar gramática), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 40,000,00 \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit()

        RESPOSTAS_PERGUNTA_2(pergunta_2_resposta = "")

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 2️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 3️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
        menu = menu.upper()

        if menu == "M":
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 👨   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

        # PERGUNTA NUMERO 3

        def RESPOSTAS_PERGUNTA_3 (pergunta_3_resposta):

            # VARIAVEIS GLOBAL PARA AS AJUDAS
            global Ajuda_plateia
            global Ajuda_Universitarios
            global Valor_Acumulado

            while True:
                pergunta_3_resposta = (input(" 🎤 PERGUNTA 3️: \n\n [ Ontem ocorreu uma forte chuva na cidade. ] \n\n A Esse trecho pertence mais provavelmente a:❔ \n\n 🎤 Alternativa (A) Notícia \n 🎤 Alternativa (B) Receita \n 🎤 Alternativa (C) Poema \n 🎤 Alternativa (D) Propaganda \n 🎤 Alternativa (E) Música \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 👨  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                
                pergunta_3_resposta = pergunta_3_resposta.upper()

                # ALTERNATIVA DE AJUDA: 👨PLATEIA👨(P)
                if pergunta_3_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 👨  É Alternativa (D)! \n 👨  Claro que é (E)! \n 👨  Obvio que é (A)! \n 👨  Nunca que seria (A)! \n 👨  Chuto que é (A)!\n\n")
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
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (A) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

                # ALTERNATIVA A (❌ ERRADA ❌)
                
                elif pergunta_3_resposta == "D":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Propaganda), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 80,000,00 \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit()

                # ALTERNATIVA B (❌ ERRADA ❌)

                elif pergunta_3_resposta == "B":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Receita), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 80,000,00 \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit()

                # ALTERNATIVA C (❌ ERRADA ❌)

                elif pergunta_3_resposta == "C":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Poema), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 80,000,00 \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit()

                # ALTERNATIVA D (✅ CORRETA ✅)

                elif pergunta_3_resposta == "A":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Notícia), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ✅ exata ✅ \n Você acaba de chegar há 💵  120,000,00!!! \n\n | ENTER | \n"))
                    Valor_Acumulado = 120000
                    break

                # ALTERNATIVA E (❌ ERRADA ❌)

                elif pergunta_3_resposta == "E":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Música), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 80,000,00 \n Fim de Jogo para você! 🫵  😂 \n\n | ENTER | \n"))
                    exit()

        RESPOSTAS_PERGUNTA_3(pergunta_3_resposta = "")

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 3️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 4️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
        menu = menu.upper()

        if menu == "M":
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 👨   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

        # PERGUNTA NUMERO 4

        def RESPOSTAS_PERGUNTA_4 (pergunta_4_resposta):

            # VARIAVEIS GLOBAL PARA AS AJUDAS

            global Ajuda_plateia
            global Ajuda_Universitarios
            global Valor_Acumulado

            while True:
                pergunta_4_resposta = (input(" 🎤 PERGUNTA 4️: \n\n [ Beba mais água e cuide da sua saúde. ] \n\n A finalidade é:❔ \n\n 🎤 Alternativa (A) Informar um acidente \n 🎤 Alternativa (B) Narrar um fato histórico \n 🎤 Alternativa (C) Divulgar um filme \n 🎤 Alternativa (D) Fazer humor \n 🎤 Alternativa (E) Dar orientação \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 👨  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                
                pergunta_4_resposta = pergunta_4_resposta.upper()

                # ALTERNATIVA DE AJUDA: 👨PLATEIA👨(P)
                if pergunta_4_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        
                        print (" 👨  Não pode ser (D)! \n 👨  Claro que é (E)! \n 👨  Obvio que é (E)! \n 👨  Nunca que seria (C)! \n 👨  Chuto que é (E) \n 👨  Claro que é (E)! \n 👨  Eu iria na (A)! \n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                # ALTERNATIVA DE AJUDA: 🎓UNIVERSITÁRIOS🎓 (U)
                elif pergunta_4_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (E) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

                # ALTERNATIVA A (❌ ERRADA ❌)
                elif pergunta_4_resposta == "A":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Informar um acidente), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 120,000,00  🫵  😂 \n\n | ENTER | \n"))
                    exit()

                # ALTERNATIVA B (❌ ERRADA ❌)
                elif pergunta_4_resposta == "B":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Narrar um fato histórico), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 120,000,00  🫵  😂 \n\n | ENTER | \n"))
                    exit()

                # ALTERNATIVA C (✅ CORRETA ✅)
                elif pergunta_4_resposta == "E":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Dar orientação), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ✅ exata ✅ \n Você acaba de chegar há 💵  160,000,00!!! \n\n | ENTER | \n"))
                    Valor_Acumulado = 160000
                    break

                # ALTERNATIVA D (❌ ERRADA ❌)
                elif pergunta_4_resposta == "D":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Fazer humor), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 120,000,00  🫵  😂 \n\n | ENTER | \n"))
                    exit()

                # ALTERNATIVA E (❌ ERRADA ❌)
                elif pergunta_4_resposta == "C":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Divulgar um filme), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 120,000,00  🫵  😂 \n\n | ENTER | \n"))
                    exit()

        RESPOSTAS_PERGUNTA_4(pergunta_4_resposta = "")

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 4️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 5️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
        menu = menu.upper()

        if menu == "M":
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 👨   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))


        # PERGUNTA NUMERO 5

        def RESPOSTAS_PERGUNTA_5 (pergunta_5_resposta):

            global Ajuda_plateia
            global Ajuda_Universitarios
            global Valor_Acumulado

            while True:
                pergunta_5_resposta = (input(" 🎤 PERGUNTA 5️: \n\n [ Vacinação contra gripe começa na próxima semana. ] \n\n O objetivo principal é:❔ \n\n 🎤 Alternativa (A) Contar uma aventura \n 🎤 Alternativa (B) Criticar uma ação pública \n 🎤 Alternativa (C) Convencer a comprar algo \n 🎤 Alternativa (D) Informar \n 🎤 Alternativa (E) Entreter \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 👨  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_5_resposta = pergunta_5_resposta.upper()

                if pergunta_5_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 👨  Não pode ser (A)! \n 👨  Claro que é (E)! \n 👨  Vamos na (D)! \n 👨  Nunca que seria (D)! \n 👨  Chuto que é (D) \n 👨  Claro que é (D)! \n 👨  Eu não iria na (D)! \n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))
                    
                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                elif pergunta_5_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (D) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))
                
                elif pergunta_5_resposta == "D":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Informar), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ✅ exata ✅ \n Você acaba de chegar há 💵  200,000,00!!! \n\n | ENTER | \n"))
                    Valor_Acumulado = 200000
                    break

                elif pergunta_5_resposta == "B":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Criticar uma ação pública), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 160,000,00  🫵  😂 \n\n | ENTER | \n"))
                    exit()

                elif pergunta_5_resposta == "C":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Convencer a comprar algo), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 160,000,00  🫵  😂 \n\n | ENTER | \n"))
                    exit()

                elif pergunta_5_resposta == "A":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Contar uma aventura), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 160,000,00  🫵  😂 \n\n | ENTER | \n"))
                    exit()

                elif pergunta_5_resposta == "E":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Entreter), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 160,000,00  🫵  😂 \n\n | ENTER | \n"))
                    exit()

        RESPOSTAS_PERGUNTA_5(pergunta_5_resposta = "")

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 5️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 6️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
        menu = menu.upper()

        if menu == "M":
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 👨   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))


        # AQUI È COMEÇANDO O TEMA 2

        # TEMA 2: (Barroco e Arcadismo) DIFICULDADE: (😊 Facil😊)

        print (input(" 🎤 Vamos dar inicio: \n Segundo Tema: Barroco e Arcadismo \n Dificuldade: 😊 Facil😊  \n\n | ENTER | \n"))

        def RESPOSTAS_PERGUNTA_6 (pergunta_6_resposta):

            global Ajuda_plateia
            global Ajuda_Universitarios
            global Valor_Acumulado

            while True:
                
                pergunta_6_resposta = (input(" 🎤 PERGUNTA 6️:\n\n [ A cidade inaugurou um novo hospital. ] \n [ O novo hospital é uma excelente conquista para a população. ] \n\n Qual a diferença de um para o outro:❔ \n\n 🎤 Alternativa (A) Ambos informam apenas fatos \n 🎤 Alternativa (B) O primeiro informa e o segundo opina \n 🎤 Alternativa (C) Ambos são propagandas \n 🎤 Alternativa (D) Ambos são poemas \n 🎤 Alternativa (E) O segundo é uma receita \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 👨  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_6_resposta = pergunta_6_resposta.upper()

                if pergunta_6_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 👨  É Alternativa (B)! \n 👨  Claro que é (C)! \n 👨  Obvio que é (A)! \n 👨  Obvio que é (E)! \n 👨  Obvio que é (B)\n 👨  É Alternativa (B)!\n\n")
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
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 200,000,00  🫵  😂  \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_6_resposta == "B":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (O primeiro informa e o segundo opina), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 240,000,00!!! \n\n | ENTER | \n"))
                    Valor_Acumulado = 240000
                    break

                elif pergunta_6_resposta == "C":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Ambos são propagandas), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 200,000,00  🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_6_resposta == "D":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Ambos são poemas), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 200,000,00  🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_6_resposta == "E":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (O segundo é uma receita), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 200,000,00  🫵  😂 \n\n | ENTER | \n"))
                    exit() 

        RESPOSTAS_PERGUNTA_6(pergunta_6_resposta = "")

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 6️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 7️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
        menu = menu.upper()

        if menu == "M":
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 👨   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

        # PERGUNTA NUMERO 7

        def RESPOSTAS_PERGUNTA_7 (pergunta_7_resposta):

            global Ajuda_plateia
            global Ajuda_Universitarios
            global Valor_Acumulado

            while True:
                pergunta_7_resposta = (input(" 🎤 PERGUNTA 7️: \n\n [ O trânsito aumentou 20% ] \n [ O aumento do trânsito mostra a falta de planejamento urbano. ] \n\n O textos 2 em relação ao texto 1 apresenta:❔ \n\n 🎤 Alternativa (A) Opinião \n 🎤 Alternativa (B) Receita \n 🎤 Alternativa (C) Propaganda \n 🎤 Alternativa (D) Entrevista \n 🎤 Alternativa (E) Fábula \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 👨  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_7_resposta = pergunta_7_resposta.upper()

                if pergunta_7_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 👨  É Alternativa (D)! \n 👨  Claro que é (A)! \n 👨  Obvio que é (D)! \n 👨  Nunca que seria (B)! \n 👨  Chuto que é (A)!\n 👨  Acho que é (A)!\n 👨  Com certeza é (A)!\n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                elif pergunta_7_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (A) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

                elif pergunta_7_resposta == "B":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Receita), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 240,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_7_resposta == "A":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Opinião), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 280,000,00!!! \n\n | ENTER | \n"))
                    Valor_Acumulado = 280000
                    break

                elif pergunta_7_resposta == "C":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Propaganda), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 240,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_7_resposta == "D":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Entrevista), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 240,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_7_resposta == "E":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Fábula), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 240,000,00 🫵 😂 \n\n | ENTER | \n"))
                    exit() 

        RESPOSTAS_PERGUNTA_7(pergunta_7_resposta = "")

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 7️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 8️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
        menu = menu.upper()

        if menu == "M":
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 👨   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

        # PERGUNTA NUMERO 8

        def RESPOSTAS_PERGUNTA_8 (pergunta_8_resposta):

            global Ajuda_plateia
            global Ajuda_Universitarios
            global Valor_Acumulado

            while True:
                pergunta_8_resposta = (input(" 🎤 PERGUNTA 8️: \n\n [ Nova praça é inaugurada no centro. ] \n [ A praça deve melhorar o lazer dos moradores. ] \n\n Qual deles expressa opinião:❔ \n\n 🎤 Alternativa (A) Texto 1 \n 🎤 Alternativa (B) Nenhum \n 🎤 Alternativa (C) Ambos \n 🎤 Alternativa (D) Texto 2 \n 🎤 Alternativa (E) Não é possível saber \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 👨  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_8_resposta = pergunta_8_resposta.upper()

                if pergunta_8_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 👨  É Alternativa (C)! \n 👨  Claro que é (D)! \n 👨  Obvio que NÂO é (D)! \n 👨  Nunca que seria (E)! \n 👨  Chuto que é (A)! \n 👨  Só poderia ser (D)!\n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                elif pergunta_8_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (D) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

                elif pergunta_8_resposta == "A":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Texto 1), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 240,000,00 🫵 😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_8_resposta == "D":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Texto 2), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 320,000,00!!! \n\n | ENTER | \n"))
                    Valor_Acumulado = 320000
                    break

                elif pergunta_8_resposta == "C":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Ambos), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 240,000,00 🫵 😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_8_resposta == "B":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Nenhum), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 240,000,00 🫵 😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_8_resposta == "E":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Não é possível saber), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 240,000,00 🫵 😂 \n\n | ENTER | \n"))
                    exit() 

        RESPOSTAS_PERGUNTA_8(pergunta_8_resposta = "")

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 8️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 9️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
        menu = menu.upper()

        if menu == "M":
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 👨   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

        # PERGUNTA NUMERO 9

        def RESPOSTAS_PERGUNTA_9 (pergunta_9_resposta):

            global Ajuda_plateia
            global Ajuda_Universitarios
            global Valor_Acumulado

            while True:
                pergunta_9_resposta = (input(" 🎤 PERGUNTA 9️: \n\n [ Escola recebe novos computadores. ] \n [ Os novos computadores representam um avanço importante. ] \n\n O Texto 2:❔ \n\n 🎤 Alternativa (A) É uma propaganda \n 🎤 Alternativa (B) Informar um fato apenas \n 🎤 Alternativa (C) Faz uma avaliação \n 🎤 Alternativa (D) É uma receita \n 🎤 Alternativa (E) É uma notícia policial \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 👨  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_9_resposta = pergunta_9_resposta.upper()

                if pergunta_9_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 👨  É Alternativa (E)! \n 👨  Claro que é (A)! \n 👨  Obvio que NÂO é (A)! \n 👨  Nunca que seria (D)! \n 👨  Chuto que é (C)! \n 👨  Só poderia ser (C)! \n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                elif pergunta_9_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (C) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

                elif pergunta_9_resposta == "C":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Faz uma avaliação), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 360,000,00!!! \n\n | ENTER | \n"))
                    Valor_Acumulado = 360000
                    break

                elif pergunta_9_resposta == "B":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Informar um fato apenas), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 320,000,00 🫵 😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_9_resposta == "A":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (É uma propaganda), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 320,000,00 🫵 😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_9_resposta == "D":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (É uma receita), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 320,000,00 🫵 😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_9_resposta == "E":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (É uma notícia policial), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 320,000,00 🫵 😂 \n\n | ENTER | \n"))
                    exit() 

        RESPOSTAS_PERGUNTA_9(pergunta_9_resposta = "")

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 9️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 1️0️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
        menu = menu.upper()

        if menu == "M":
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 👨   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

        # PERGUNTA NUMERO 10

        def RESPOSTAS_PERGUNTA_10 (pergunta_10_resposta):

            global Ajuda_plateia
            global Ajuda_Universitarios
            global Valor_Acumulado

            while True:
                pergunta_10_resposta = (input(" 🎤 PERGUNTA 1️0️: \n\n Qual habilidade está sendo usada ao comparar dois textos sobre o mesmo assunto: ❔ \n\n 🎤 Alternativa (A) Resolver contas \n 🎤 Alternativa (B) Traduzir idiomas \n 🎤 Alternativa (C) Decorar palavras \n 🎤 Alternativa (D) Fazer desenhos \n 🎤 Alternativa (E) Reconhecer diferentes tratamentos da informação \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 👨  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_10_resposta = pergunta_10_resposta.upper()

                if pergunta_10_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 👨  É Alternativa (E)! \n 👨  Claro que é (D)! \n 👨  Obvio que NÂO é (D)! \n 👨  Nunca que seria (D)! \n 👨  Chuto que é (E)! \n 👨  Só poderia ser (C)! \n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                elif pergunta_10_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (E) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

                elif pergunta_10_resposta == "A":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Resolver contas), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 360,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_10_resposta == "E":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Reconhecer diferentes tratamentos da informação), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 400,000,00!!! \n\n | ENTER | \n"))
                    Valor_Acumulado = 400000
                    break

                elif pergunta_10_resposta == "C":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Decorar palavras), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 360,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_10_resposta == "D":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Fazer desenhos), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 360,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_10_resposta == "B":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Traduzir idiomas), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 360,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_10_resposta == "B":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Traduzir idiomas), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 360,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

        RESPOSTAS_PERGUNTA_10(pergunta_10_resposta = "")

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 1️0️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 1️1️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
        menu = menu.upper()

        if menu == "M":
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 👨   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

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
                pergunta_11_resposta = (input(" 🎤 PERGUNTA 1️1️: \n\n Qual é o principal objetivo de um artigo de opinião:❔ \n\n 🎤 Alternativa (A) Defender um ponto de vista sobre um assunto \n 🎤 Alternativa (B) Contar uma história fictícia \n 🎤 Alternativa (C) Ensinar uma receita culinária \n 🎤 Alternativa (D) Anunciar um produto \n 🎤 Alternativa (E) Relatar apenas fatos sem comentários \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 👨  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_11_resposta = pergunta_11_resposta.upper()

                if pergunta_11_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 👨  É Alternativa (C)! \n 👨  Claro que é (A)! \n 👨  Obvio que NÂO é (A)! \n 👨  Nunca que seria (E)! \n 👨  Chuto que é (B)! \n 👨  Só poderia ser (E)! \n 👨  Certeza que é (A)! \n 👨  Com certeza é (C)!\n 👨  Acho que é (A)!\n\n")
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
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Defender um ponto de vista sobre um assunto), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 440,000,00!!! \n\n | ENTER | \n"))
                    Valor_Acumulado = 440000
                    break

                elif pergunta_11_resposta == "B":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Contar uma história fictícia), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 400,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_11_resposta == "C":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Ensinar uma receita culinária), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 400,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_11_resposta == "D":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Anunciar um produto), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 400,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_11_resposta == "E":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Relatar apenas fatos sem comentários), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 400,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

        RESPOSTAS_PERGUNTA_11(pergunta_11_resposta = "")

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 1️1️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 1️2️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
        menu = menu.upper()

        if menu == "M":
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 👨   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

            # PERGUNTA NUMERO 12

        def RESPOSTAS_PERGUNTA_12 (pergunta_12_resposta):

            global Ajuda_plateia
            global Ajuda_Universitarios
            global Valor_Acumulado

            while True:
                pergunta_12_resposta = (input(" 🎤 PERGUNTA 1️2️: \n\n Em um artigo de opinião, os argumentos servem para:❔ \n\n 🎤 Alternativa (A) Decorar o texto \n 🎤 Alternativa (B) Aumentar o número de páginas \n 🎤 Alternativa (C) Convencer o leitor da opinião do autor \n 🎤 Alternativa (D) Fazer propaganda \n 🎤 Alternativa (E) Contar a vida do autor \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 👨  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_12_resposta = pergunta_12_resposta.upper()

                if pergunta_12_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 👨  Claro que é (C)! \n 👨  Chuto que é (A)! \n 👨  Com certeza é (B)! 👨  Com certeza é (C)! \n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                elif pergunta_12_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (C) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

                elif pergunta_12_resposta == "C":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Convencer o leitor da opinião do autor), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 480,000,00!!! \n\n | ENTER | \n"))
                    Valor_Acumulado = 480000
                    break

                elif pergunta_12_resposta == "B":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Aumentar o número de páginas), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 440,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_12_resposta == "A":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Decorar o texto), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 440,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_12_resposta == "D":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Fazer propaganda), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 440,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_12_resposta == "E":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Contar a vida do autor), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 440,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

        RESPOSTAS_PERGUNTA_12(pergunta_12_resposta = "")

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 1️2️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 1️3️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
        menu = menu.upper()

        if menu == "M":
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 👨   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

        # PERGUNTA NUMERO 13

        def RESPOSTAS_PERGUNTA_13 (pergunta_13_resposta):

            global Ajuda_plateia
            global Ajuda_Universitarios
            global Valor_Acumulado

            while True:
                pergunta_13_resposta = (input(" 🎤 PERGUNTA 1️3️: \n\n Como é chamada a ideia principal defendida pelo autor:❔ \n\n 🎤 Alternativa (A) Moral \n 🎤 Alternativa (B) Cenário \n 🎤 Alternativa (C) Resumo \n 🎤 Alternativa (D) Personagem \n 🎤 Alternativa (E) Tese \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 👨  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_13_resposta = pergunta_13_resposta.upper()

                if pergunta_13_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 👨  É Alternativa (E)! \n 👨  Claro que é (A)! \n 👨  Obvio que NÂO é (C)! \n 👨  Nunca que seria (E)! \n 👨  Chuto que é (A)! \n 👨  Só poderia ser (E)! \n 👨  Certeza que é (A)! \n 👨  Com certeza é (D)!\n 👨  Acho que é não é (A)! \n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                elif pergunta_13_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (E) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

                elif pergunta_13_resposta == "A":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Moral), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 480,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_13_resposta == "E":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Tese), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 520,000,00!!! \n\n | ENTER | \n"))
                    Valor_Acumulado = 520000
                    break

                elif pergunta_13_resposta == "C":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Resumo), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 480,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_13_resposta == "D":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Personagem), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 480,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_13_resposta == "B":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Cenário), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 480,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

        RESPOSTAS_PERGUNTA_13(pergunta_13_resposta = "")

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 1️3️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 1️4️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
        menu = menu.upper()

        if menu == "M":
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 👨   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

        # PERGUNTA NUMERO 14

        def RESPOSTAS_PERGUNTA_14 (pergunta_14_resposta):

            global Ajuda_plateia
            global Ajuda_Universitarios
            global Valor_Acumulado

            while True:
                pergunta_14_resposta = (input(" 🎤 PERGUNTA 1️4️: \n\n Qual característica é comum em artigos de opinião:❔ \n\n 🎤 Alternativa (A) Uso obrigatório de personagens fictícios \n 🎤 Alternativa (B) Presença de argumentos e justificativas \n 🎤 Alternativa (C) Narração de aventuras imaginárias \n 🎤 Alternativa (D) Apenas descrição de lugares \n 🎤 Alternativa (E) Explicação de experiências científicas \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 👨  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_14_resposta = pergunta_14_resposta.upper()

                if pergunta_14_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 👨  Não é Alternativa (B)! \n 👨  Claro que não é (B)! \n 👨  Obvio que NÂO é (B)! \n 👨  Nunca que seria (B)! \n 👨  Chuto que é (D)! \n 👨  Só poderia ser (E)! \n 👨  Certeza que é (A)! \n 👨  Com certeza não é (B)!\n 👨  Acho que é (B)! \n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                elif pergunta_14_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (B) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

                elif pergunta_14_resposta == "B":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Presença de argumentos e justificativas), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 560,000,00!!! \n\n | ENTER | \n"))
                    Valor_Acumulado = 560000
                    break

                elif pergunta_14_resposta == "A":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Uso obrigatório de personagens fictícios), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 520,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_14_resposta == "C":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Narração de aventuras imaginárias), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 520,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_14_resposta == "D":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Apenas descrição de lugares), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 520,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_14_resposta == "E":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Explicação de experiências científicas), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 520,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

        RESPOSTAS_PERGUNTA_14(pergunta_14_resposta = "")

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 1️4️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 1️5️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
        menu = menu.upper()

        if menu == "M":
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 👨   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

        # PERGUNTA NUMERO 15

        def RESPOSTAS_PERGUNTA_15 (pergunta_15_resposta):

            global Ajuda_plateia
            global Ajuda_Universitarios
            global Valor_Acumulado

            while True:
                pergunta_15_resposta = (input(" 🎤 PERGUNTA 1️5️: \n\n Quando o autor apresenta dados e pesquisas, ele está:❔ \n\n 🎤 Alternativa (A) Inventando informações \n 🎤 Alternativa (B) Fazendo humor \n 🎤 Alternativa (C) Mudando de assunto \n 🎤 Alternativa (D) Fortalecendo seus argumentos \n 🎤 Alternativa (E) Escrevendo uma lenda \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 👨  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_15_resposta = pergunta_15_resposta.upper()

                if pergunta_15_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 👨  sei lá deve ser (E)! \n 👨  Acho que não seja (D)! \n 👨  Obvio que NÂO é (C)! \n 👨  Nunca que seria (E)! \n 👨  Chuto que é (B)! \n 👨  Só poderia ser (A)! \n 👨  Certeza que é (D)! \n 👨  Com certeza é (D)!\n 👨  Acho que é (E)! \n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                elif pergunta_15_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (D) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

                elif pergunta_15_resposta == "D":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Fortalecendo seus argumentos), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 600,000,00!!! \n\n | ENTER | \n"))
                    Valor_Acumulado = 600000
                    break

                elif pergunta_15_resposta == "B":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Fazendo humor), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 560,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_15_resposta == "C":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Mudando de assunto), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 560,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_15_resposta == "A":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Inventando informações), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 560,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_15_resposta == "E":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Escrevendo uma lenda), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 560,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

        RESPOSTAS_PERGUNTA_15(pergunta_15_resposta = "")

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 1️5️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 1️6️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
        menu = menu.upper()

        if menu == "M":
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 👨   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

        # AQUI È COMEÇANDO O TEMA 4

        # TEMA 4: (Textos Publicitários) DIFICULDADE: (😡 Dificil😡)

        print (input(" 🎤 Vamos dar inicio: \n Quarto Tema: Textos Publicitários \n Dificuldade: 😡 Dificil😡  \n\n | ENTER | \n"))

        # PERGUNTA NUMERO 16

        def RESPOSTAS_PERGUNTA_16 (pergunta_16_resposta):

            global Ajuda_plateia
            global Ajuda_Universitarios
            global Valor_Acumulado

            while True:
                pergunta_16_resposta = (input(" 🎤 PERGUNTA 1️6️: \n\n Qual é a principal finalidade de um texto publicitário:❔ \n\n 🎤 Alternativa (A) Relatar fatos de forma imparcial \n 🎤 Alternativa (B) Convencer o público a adquirir uma ideia, produto ou serviço \n 🎤 Alternativa (C) Narrar acontecimentos históricos \n 🎤 Alternativa (D) Registrar experimentos científicos \n 🎤 Alternativa (E) Contar uma história fictícia \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 👨  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_16_resposta = pergunta_16_resposta.upper()

                if pergunta_16_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 👨  Claro que é (B)! \n 👨  Chuto que é (A)! \n 👨  Com certeza é (E)! \n 👨  Chuto que é (D)! \n 👨  Não é (C)! \n\n")
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
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Relatar fatos de forma imparcial), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 600,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_16_resposta == "B":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Convencer o público a adquirir uma ideia, produto ou serviço), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 640,000,00!!! \n\n | ENTER | \n"))
                    Valor_Acumulado = 640000
                    break

                elif pergunta_16_resposta == "C":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Narrar acontecimentos históricos), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 600,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_16_resposta == "D":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Registrar experimentos científicos), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 600,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_16_resposta == "E":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Contar uma história fictícia), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 600,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

        RESPOSTAS_PERGUNTA_16(pergunta_16_resposta = "")

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 1️6️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 1️7️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
        menu = menu.upper()

        if menu == "M":
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 👨   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

        # PERGUNTA NUMERO 17

        def RESPOSTAS_PERGUNTA_17 (pergunta_17_resposta):

            global Ajuda_plateia
            global Ajuda_Universitarios
            global Valor_Acumulado

            while True:
                pergunta_17_resposta = (input(" 🎤 PERGUNTA 1️7️: \n\n O que é um slogan em uma campanha publicitária:❔ \n\n 🎤 Alternativa (A) Uma tabela de preços \n 🎤 Alternativa (B) Um texto científico sobre o produto \n 🎤 Alternativa (C) Uma reportagem sobre a empresa \n 🎤 Alternativa (D) Uma frase curta e marcante que facilita a lembrança da marca \n 🎤 Alternativa (E) Um regulamento de venda \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 👨  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_17_resposta = pergunta_17_resposta.upper()

                if pergunta_17_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 👨  Claro que é (D)! \n 👨  Chuto que é (D)! \n 👨  Com certeza é (N?)! \n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                elif pergunta_17_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (D) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

                elif pergunta_17_resposta == "A":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Receita), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 640,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_17_resposta == "D":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Uma frase curta e marcante que facilita a lembrança da marca), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 680,000,00!!! \n\n | ENTER | \n"))
                    Valor_Acumulado = 680000
                    break

                elif pergunta_17_resposta == "C":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Tabela), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 640,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_17_resposta == "B":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Um texto científico sobre o produto), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 640,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_17_resposta == "E":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Calendário), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 640,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

        RESPOSTAS_PERGUNTA_17(pergunta_17_resposta = "")

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 1️7️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 1️8️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
        menu = menu.upper()

        if menu == "M":
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 👨   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

        # PERGUNTA NUMERO 18

        def RESPOSTAS_PERGUNTA_18 (pergunta_18_resposta):

            global Ajuda_plateia
            global Ajuda_Universitarios
            global Valor_Acumulado

            while True:
                pergunta_18_resposta = (input(" 🎤 PERGUNTA 1️8️: \n\n Qual recurso é mais utilizado para atrair rapidamente a atenção do consumidor:❔ \n\n 🎤 Alternativa (A) Linguagem excessivamente técnica \n 🎤 Alternativa (B) Longos parágrafos explicativos \n 🎤 Alternativa (C) Ausência de elementos visuais \n 🎤 Alternativa (D) Citações de leis e normas \n 🎤 Alternativa (E) Uso de imagens, cores e palavras de destaque \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 👨  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_18_resposta = pergunta_18_resposta.upper()

                if pergunta_18_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 👨  É Alternativa (E)! \n 👨  Claro que é (A)! \n 👨  Obvio que NÂO é (C)! \n 👨  Nunca que seria (E)! \n 👨  Chuto que é (A)! \n 👨  Só poderia ser (E)! \n 👨  Certeza que é (A)! \n 👨  Com certeza é (D)!\n 👨  Acho que é não é (A)! \n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                elif pergunta_18_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (E) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

                elif pergunta_18_resposta == "A":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Linguagem excessivamente técnica), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 680,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_18_resposta == "E":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Uso de imagens, cores e palavras de destaque), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 720,000,00!!! \n\n | ENTER | \n"))
                    Valor_Acumulado = 720000
                    break

                elif pergunta_18_resposta == "C":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Ausência de elementos visuais), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 680,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_18_resposta == "D":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Citações de leis e normas), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 680,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_18_resposta == "B":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Longos parágrafos explicativos), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 680,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

        RESPOSTAS_PERGUNTA_18(pergunta_18_resposta = "")

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 1️8️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 1️9️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
        menu = menu.upper()

        if menu == "M":
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 👨   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

        # PERGUNTA NUMERO 19

        def RESPOSTAS_PERGUNTA_19 (pergunta_19_resposta):

            global Ajuda_plateia
            global Ajuda_Universitarios
            global Valor_Acumulado

            while True:
                pergunta_19_resposta = (input(" 🎤 PERGUNTA 1️9️: \n\n Ao usar expressões como [ Oferta por tempo limitado ] ou [ Últimas unidades ] \n A propaganda pretende:❔ \n\n 🎤 Alternativa (A) Criar um senso de urgência no consumidor \n 🎤 Alternativa (B) Contar a história da empresa \n 🎤 Alternativa (C) Explicar a fabricação do produto \n 🎤 Alternativa (D) Apresentar dados científicos \n 🎤 Alternativa (E) Informar um fato jornalístico \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 👨  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_19_resposta = pergunta_19_resposta.upper()

                if pergunta_19_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 👨  É Alternativa (C)! \n 👨  Claro que é (A)! \n 👨  Obvio que NÂO é (A)! \n 👨  Nunca que seria (E)! \n 👨  Chuto que é (B)! \n 👨  Só poderia ser (E)! \n 👨  Certeza que é (A)! \n 👨  Com certeza é (C)!\n 👨  Acho que é (A)! \n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                elif pergunta_19_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (A) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

                elif pergunta_19_resposta == "C":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Explicar a fabricação do produto), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 720,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_19_resposta == "B":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Contar a história da empresa), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 720,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_19_resposta == "A":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Criar um senso de urgência no consumidor), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 760,000,00!!! \n\n | ENTER | \n"))
                    Valor_Acumulado = 760000
                    break

                elif pergunta_19_resposta == "D":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Apresentar dados científicos), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 720,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_19_resposta == "E":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Informar um fato jornalístico), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 720,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

        RESPOSTAS_PERGUNTA_19(pergunta_19_resposta = "")

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 1️9️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 2️0️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
        menu = menu.upper()

        if menu == "M":
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 👨   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

        # PERGUNTA NUMERO 20

        def RESPOSTAS_PERGUNTA_20 (pergunta_20_resposta):

            global Ajuda_plateia
            global Ajuda_Universitarios
            global Valor_Acumulado

            while True:
                pergunta_20_resposta = (input(" 🎤 PERGUNTA 2️0️: \n\n Qual alternativa apresenta uma característica típica dos textos publicitários:❔ \n\n 🎤 Alternativa (A) Linguagem exclusivamente formal \n 🎤 Alternativa (B) Neutralidade absoluta sobre o assunto \n 🎤 Alternativa (C) Uso de recursos persuasivos para influenciar o público \n 🎤 Alternativa (D) Relato cronológico de acontecimentos \n 🎤 Alternativa (E) Explicação detalhada de teorias científicas \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 👨  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_20_resposta = pergunta_20_resposta.upper()

                if pergunta_20_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 👨  É Alternativa (C)! \n 👨  Claro que é (E)! \n 👨  Obvio que é (C)! \n 👨  Nunca que seria (E)! \n 👨  Chuto que seja (A)! \n 👨  Nunca que seria (D)! \n 👨  Só poderia ser a (C)! \n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                elif pergunta_20_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (C) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

                elif pergunta_20_resposta == "A":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Linguagem exclusivamente formal), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 760,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_20_resposta == "B":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Neutralidade absoluta sobre o assunto), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 760,000,00 \n\n | ENTER | \n"))
                    exit()

                elif pergunta_20_resposta == "C":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Uso de recursos persuasivos para influenciar o público), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 800,000,00!!! \n\n | ENTER | \n"))
                    Valor_Acumulado = 800000
                    break

                elif pergunta_20_resposta == "D":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Relato cronológico de acontecimentos), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 760,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_20_resposta == "E":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Explicação detalhada de teorias científica), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 760,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

        RESPOSTAS_PERGUNTA_20(pergunta_20_resposta = "")

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 2️0️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 2️1️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
        menu = menu.upper()

        if menu == "M":
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 👨   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

        # AQUI È COMEÇANDO O TEMA 5

        # TEMA 5: (Complementos Verbais) DIFICULDADE: (🤬 MUITO DIFICIL🤬)

        print (input(" 🎤 Vamos dar inicio: \n Quarto e ultimo Tema: Complementos Verbais \n Dificuldade: 🤬 MUITO DIFICIL🤬  \n\n | ENTER | \n"))

        def RESPOSTAS_PERGUNTA_21 (pergunta_21_resposta):

            global Ajuda_plateia
            global Ajuda_Universitarios
            global Valor_Acumulado

            while True:
                pergunta_21_resposta = (input(" 🎤 PERGUNTA 2️1️: \n\n Qual alternativa apresenta um verbo com objeto direto:❔ \n\n 🎤 Alternativa (A) Ela gosta de música \n 🎤 Alternativa (B) Nós precisamos de ajuda \n 🎤 Alternativa (C) O aluno assistiu ao filme \n 🎤 Alternativa (D) O escritor publicou um livro \n 🎤 Alternativa (E) Ele obedeceu ao regulamento \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 👨  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_21_resposta = pergunta_21_resposta.upper()

                if pergunta_21_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 👨  Estou em duvida entre (D e A)! \n 👨  Chuto que é (A)! \n 👨  Talvez seja (B ou D)! \n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                elif pergunta_21_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (D) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

                elif pergunta_21_resposta == "A":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Ela gosta de música), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ n Você não acertou então saira com 💵 800,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_21_resposta == "D":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (O escritor publicou um livro), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 840,000,00!!! \n\n | ENTER | \n"))
                    Valor_Acumulado = 840000
                    break

                elif pergunta_21_resposta == "C":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (O aluno assistiu ao filme), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 800,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_21_resposta == "B":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Nós precisamos de ajuda), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 800,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_21_resposta == "E":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Ele obedeceu ao regulamento), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 800,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

        RESPOSTAS_PERGUNTA_21(pergunta_21_resposta = "")

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 2️1️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 2️2️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
        menu = menu.upper()

        if menu == "M":
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 👨   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

        # PERGUNTA NUMERO 22

        def RESPOSTAS_PERGUNTA_22 (pergunta_22_resposta):

            global Ajuda_plateia
            global Ajuda_Universitarios
            global Valor_Acumulado

            while True:
                pergunta_22_resposta = (input(" 🎤 PERGUNTA 2️2️: \n\n Em qual alternativa o termo destacado exerce a função de objeto indireto:❔ \n\n 🎤 Alternativa (A) O atleta venceu a competição \n 🎤 Alternativa (B) A criança encontrou o brinquedo \n 🎤 Alternativa (C) O professor necessita de apoio \n 🎤 Alternativa (D) O turista visitou a cidade \n 🎤 Alternativa (E) A empresa lançou um produto \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 👨  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_22_resposta = pergunta_22_resposta.upper()

                if pergunta_22_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 👨  Só pode ser (C ou E)! \n  \n\n")
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
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (O atleta venceu a competição), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 840,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_22_resposta == "B":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (A criança encontrou o brinquedo), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 840,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_22_resposta == "C":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (O professor necessita de apoio), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 880,000,00!!! \n\n | ENTER | \n"))
                    Valor_Acumulado = 880000
                    break

                elif pergunta_22_resposta == "D":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (O turista visitou a cidade), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 840,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_22_resposta == "E":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (A empresa lançou um produto), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 840,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

        RESPOSTAS_PERGUNTA_22(pergunta_22_resposta = "")

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 2️2️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 2️3️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
        menu = menu.upper()

        if menu == "M":
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 👨   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

        # PERGUNTA NUMERO 23

        def RESPOSTAS_PERGUNTA_23 (pergunta_23_resposta):

            global Ajuda_plateia
            global Ajuda_Universitarios
            global Valor_Acumulado

            while True:
                pergunta_23_resposta = (input(" 🎤 PERGUNTA 2️3️: \n\n Qual frase apresenta um verbo bitransitivo ( que exige objeto direto e indireto ):❔ \n\n 🎤 Alternativa (A) O bebê dormiu \n 🎤 Alternativa (B) O aluno escreveu \n 🎤 Alternativa (C) A garota chegou cedo \n 🎤 Alternativa (D) O juiz decidiu o caso \n 🎤 Alternativa (E) A mãe entregou o presente ao filho \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 👨  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_23_resposta = pergunta_23_resposta.upper()

                if pergunta_23_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 👨  Chuto que seja (E ou A ou B) \n 👨  Eu com certeza iria na (A ou C ou E)! \n 👨  Com certeza é (B)! \n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                elif pergunta_23_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (E) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

                elif pergunta_23_resposta == "A":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (O bebê dormiu), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 880,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_23_resposta == "E":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (A mãe entregou o presente ao filho), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 920,000,00!!! \n\n | ENTER | \n"))
                    Valor_Acumulado = 920000
                    break

                elif pergunta_23_resposta == "C":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (A garota chegou cedo), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 880,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_23_resposta == "D":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (O juiz decidiu o caso), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 880,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_23_resposta == "B":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (O aluno escreveu), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 880,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

        RESPOSTAS_PERGUNTA_23(pergunta_23_resposta = "")

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 2️3️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 2️4️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
        menu = menu.upper()

        if menu == "M":
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 👨   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

        # PERGUNTA NUMERO 24

        def RESPOSTAS_PERGUNTA_24 (pergunta_24_resposta):

            global Ajuda_plateia
            global Ajuda_Universitarios
            global Valor_Acumulado

            while True:
                pergunta_24_resposta = (input(" 🎤 PERGUNTA 2️4️: \n\n Na frase [ Os estudantes confiaram nos professores. ] o complemento verbal é:❔ \n\n 🎤 Alternativa (A) Objeto indireto \n 🎤 Alternativa (B) Predicativo do sujeito \n 🎤 Alternativa (C) Adjunto adverbial \n 🎤 Alternativa (D) Objeto direto \n 🎤 Alternativa (E) Aposto \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 👨  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_24_resposta = pergunta_24_resposta.upper()

                if pergunta_24_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 👨  Claro que é (A ou B ou E)! \n 👨  Chuto que é (A)! \n 👨  Com certeza é (B ou E, mas tambem poderia ser a C né?)! \n\n")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | PARA VER NOVAMENTE AS RESPOSTAS | | ENTER | \n\n"))
                    
                    else:
                        print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

                elif pergunta_24_resposta == "U":
                    if Ajuda_Universitarios > 0:
                        Ajuda_Universitarios -= 1
                        print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                        print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (A) \n\n ")
                        print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                    else:
                        print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

                elif pergunta_24_resposta == "B":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Predicativo do sujeito), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 920,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_24_resposta == "A":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Objeto indireto), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 960,000,00!!! \n\n | ENTER | \n"))
                    Valor_Acumulado = 960000
                    break

                elif pergunta_24_resposta == "C":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Adjunto adverbial), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 920,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_24_resposta == "D":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Objeto direto), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 920,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_24_resposta == "E":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Aposto), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 920,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

        RESPOSTAS_PERGUNTA_24(pergunta_24_resposta = "")

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 2️4️ \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA 2️5️ \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
        menu = menu.upper()

        if menu == "M":
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 👨   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

        # PERGUNTA NUMERO 25

        def RESPOSTAS_PERGUNTA_25 (pergunta_25_resposta):

            global Ajuda_plateia
            global Ajuda_Universitarios
            global Valor_Acumulado

            while True:
                pergunta_25_resposta = (input(" 🎤 PERGUNTA 2️5️: \n\n Consegue assinalar qual alternativa esta \n com a classificação dos complementos verbais correta:❔ \n\n 🎤 Alternativa (A) [ Ela comprou flores ] = objeto indireto \n 🎤 Alternativa (B) [ Entreguei a carta ao diretor ] = objeto direto e objeto indireto \n 🎤 Alternativa (C) [ Necessitamos de recursos ] = objeto direto \n 🎤 Alternativa (D) [ Gosto de café ] = objeto direto \n 🎤 Alternativa (E) [ Assisti ao espetáculo ] = objeto direto \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 👨  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 "))

                pergunta_25_resposta = pergunta_25_resposta.upper()

                if pergunta_25_resposta == "P":
                    if Ajuda_plateia > 0:
                        Ajuda_plateia -= 1
                        
                        print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | ENTER | "))
                        print (" 👨  Claro que é (B)! \n 👨  Chuto que é (B)! \n 👨  Com certeza é (B)! \n\n")
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
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Ela comprou flores e etc...), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ \n Você não acertou então saira com 💵 960,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_25_resposta == "B":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Entreguei a carta ao diretor e etc...), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ✅ exata ✅ \n Você acaba de receber 💵 1,000,000,00!!! \n\n | ENTER | \n"))
                    Valor_Acumulado = 1000000
                    break

                elif pergunta_25_resposta == "C":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Necessitamos de recursos e etc...), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ Você não acertou então saira com 💵 960,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_25_resposta == "D":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Gosto de café e etc...), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ Você não acertou então saira com 💵 960,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

                elif pergunta_25_resposta == "E":
                    print (input("\n 🎤 " + nome_usuario + ", Você acha que a resposta é (Assisti ao espetáculo e etc...), sua resposta está eee... \n\n | ENTER | "))
                    print (input(" 🎤 ❌ errada ❌ Você não acertou então saira com 💵 960,000,00 🫵  😂 \n\n | ENTER | \n"))
                    exit() 

        RESPOSTAS_PERGUNTA_25(pergunta_25_resposta = "")

        menu = (input(" 🎤 " + nome_usuario + ", Após responder a sua PERGUNTA 25 \n Você pode ver em seu (👜 MENU) o quanto já acomulou do premio, e quantas ajudas tem ao seu dispor \n Ou você pode prosseguir para sua PERGUNTA BONUS \n Escolha!!! \n\n | PRESSIONE [M] PARA VER MENU | \n | PARA PROSEGUIR | \n\n | ENTER | \n "))
        menu = menu.upper()

        if menu == "M":
            menu = (input("\n 👜 MENU: \n\n 💵  Valor acomulado: " + str(Valor_Acumulado) + "\n 👨   Plateia: " + str(Ajuda_plateia) + "\n 🎓  Universitários: " + str(Ajuda_Universitarios) + "\n\n | ENTER | \n"))

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


















elif Máteria_selecionada == "3" :


    Ajuda_da_pessoas = 3
    Ajuda_dos_Universitarios = 5

    nome_usuario = input("Antes de Iniciarmos Gostaria de Saber, qual seria seu nome? \n\n 👤 | DIGITE O SEU NOME E TECLE ENTER PARA CONTINUAR | \n ")


    print (input("🎤 Bem Vindo ao nosso programa Cyber Mind!!! \n\n 🎤Você selecionou a materia de História \n\n 🎤Vamos dar inicio ao primeiro Tema: Princípios da Revolução Francesa ao caráter burguês   \n\n  | TECLE ENTER PARA CONTINUAR | \n"))




    def RESPOSTAS_PERGUNTA_1 ():
        
        # VARIAVEIS GLOBAL PARA AS AJUDAS
        global Ajuda_da_pessoas
        global Ajuda_dos_Universitarios

        while True:

            pergunta_1_resposta = (input(" 🎤 PERGUNTA 1: Qual grupo social teve grande influência na Revolução Francesa?: \n\n  Alternativa (A) Nobres \n  Alternativa (B) Camponeses \n  Alternativa (C) Burguesia \n  Alternativa (D) Clero  \n\n | PARA RESPONDER DIGITE [A/B/C/D] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | DIGITE A ALTERNATIVA MAIS ENTER PARA CONTINUAR | \n\n 👤 "))
            # AJUDA DA PLATEIA
            if pergunta_1_resposta == "P" or pergunta_1_resposta == "p":
                if Ajuda_da_pessoas > 0:
                    Ajuda_da_pessoas -= 1

                    print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🥸  É Alternativa (C)! \n 🥸  Claro que é (C)! \n 🥸  Obvio que é (B)! \n\n")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))
                

                else:
                    print("\n❌ Você não possui mais ajuda da plateia!\n")
            # AJUDA DOS UNIVERSITARIOS
            elif pergunta_1_resposta == "U" or pergunta_1_resposta == "u":
                if Ajuda_dos_Universitarios > 0:
                    Ajuda_dos_Universitarios -= 1

                    print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n |TECLE ENTER PARA CONTINUAR | "))
                    print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (C) \n\n ")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                else:
                    print("\n❌ Você não possui mais ajuda dos universitários!\n")
            # RESPOSTA CERTA
            elif pergunta_1_resposta == "C" or pergunta_1_resposta == "c":
                print("\n✅ CORRETA!")
                print("💵 Você ganhou 1,000 reais!\n")
                break
            # RESPOSTAS ERRADAS
            elif pergunta_1_resposta in ["A", "B", "D"]:
                print("\n❌ ERRADA!")
                print("💀 Você perdeu tudo!\n")
                exit()
            else:
                print("\n❌ Resposta inválida!\n")
                exit ()
            
                
    RESPOSTAS_PERGUNTA_1()

    print (input("\n 🎤 Parabéns " + nome_usuario + ", você acertou a primeira pergunta e já tem 💵 1,000 reais acumulados! \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    print (input(" 🎤 Agora vamos para a segunda pergunta. \n\n | TECLE ENTER PARA CONTINUAR | \n"))


    def RESPOSTAS_PERGUNTA_2():

        global Ajuda_da_pessoas
        global Ajuda_dos_Universitarios

        while True:

            pergunta_2_resposta = input("🎤 PERGUNTA 2: Qual era um dos principais ideais da Revolução Francesa? \n\n Alternativa (A) Escravidão \n Alternativa (B) Monarquia absoluta \n Alternativa (C) Privilégios da nobreza \n Alternativa (D) Liberdade \n\n | DIGITE [A/B/C/D] | \n | PLATEIA [P] | \n | UNIVERSITARIOS [U] | \n\n | DIGITE A ALTERNATIVA MAIS ENTER PARA CONTINUAR | \n\n 👤 ")
                
            # AJUDA DA PLATEIA
            if pergunta_2_resposta == "P" or pergunta_2_resposta == "p":
                if Ajuda_da_pessoas > 0:
                    Ajuda_da_pessoas -= 1

                    print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🥸  É Alternativa (D)! \n 🥸  Claro que é (D)! \n 🥸  Obvio que é (A)! \n\n")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))
                

                else:
                    print("\n❌ Você não possui mais ajuda da plateia!\n")

            # AJUDA DOS UNIVERSITARIOS
            elif pergunta_2_resposta == "U" or pergunta_2_resposta == "u":

                if Ajuda_dos_Universitarios > 0:
                    Ajuda_dos_Universitarios -= 1

                    print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (D) \n\n ")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                else:
                    print("\n❌ Você não possui mais ajuda dos universitários!\n")

            # RESPOSTA CERTA
            elif pergunta_2_resposta == "D" or pergunta_2_resposta == "d":

                print("\n✅ CORRETA!")
                print("💵 Você ganhou mais 1,000 reais!\n")
                break

            # RESPOSTAS ERRADAS
            elif pergunta_2_resposta in ["A", "B", "C"]:

                print("\n❌ ERRADA!")
                print("💀 Você perdeu tudo!\n")
                exit()

            else:
                print("\n❌ Resposta inválida!\n")
                exit()
    RESPOSTAS_PERGUNTA_2()

    print (input("\n 🎤 Parabéns " + nome_usuario + ", você acertou a segunda pergunta e já tem 💵 2,000 reais acumulados! \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    print (input(" 🎤 Agora vamos para a terceira pergunta. \n\n | TECLE ENTER PARA CONTINUAR | \n"))

    def RESPOSTAS_PERGUNTA_3():
        global Ajuda_da_pessoas
        global Ajuda_dos_Universitarios

        while True:
            pergunta_3_resposta = input("🎤 PERGUNTA 3: O que a burguesia queria conquistar?:\n\n Alternativa (A)Mais privilégios para os nobres \n Alternativa (B) Maior participação política e econômica \n Alternativa (C) Menos comércio \n Alternativa (D) Mais impostos  \n\n | DIGITE [A/B/C/D] | \n | PLATEIA [P] | \n | UNIVERSITARIOS [U] | \n\n | DIGITE A ALTERNATIVA MAIS ENTER PARA CONTINUAR | \n\n 👤 ")
            # AJUDA DA PLATEIA
            if pergunta_3_resposta == "P" or pergunta_3_resposta == "p":

                if Ajuda_da_pessoas > 0:
                    Ajuda_da_pessoas -= 1

                    print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🥸  É Alternativa (B)! \n 🥸  Claro que é (B)! \n 🥸  Obvio que nao é (A)! \n\n")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                else:
                    print("\n❌ Você não possui mais ajuda da plateia!\n")
            # AJUDA DOS UNIVERSITARIOS
            elif pergunta_3_resposta == "U" or pergunta_3_resposta == "u":
                if Ajuda_dos_Universitarios > 0:
                    Ajuda_dos_Universitarios -= 1

                    print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (B) \n\n ")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                else:
                    print("\n❌ Você não possui mais ajuda dos universitários!\n")
            # RESPOSTA CERTA
            elif pergunta_3_resposta == "B" or pergunta_3_resposta == "b":

                print("\n✅ CORRETA!")
                print("💵 Você ganhou mais 1,000 reais!\n")
                break
            # RESPOSTAS ERRADAS
            elif pergunta_3_resposta in ["A", "C", "D"]:

                print("\n❌ ERRADA!")
                print("💀 Você perdeu tudo!\n")
                exit()

            else:
                print("\n❌ Resposta inválida!\n")
                exit()

    RESPOSTAS_PERGUNTA_3()
    print (input("\n 🎤 Parabéns " + nome_usuario + ", você acertou a terceira pergunta e já tem 💵 3,000 reais acumulados! \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    print (input(" 🎤 Agora vamos para a quarta pergunta. \n\n | TECLE ENTER PARA CONTINUAR | \n"))

    def RESPOSTAS_PERGUNTA_4():
        global Ajuda_da_pessoas
        global Ajuda_dos_Universitarios

        while True:
            pergunta_4_resposta = input("🎤 PERGUNTA 4: Qual lema ficou famoso durante a Revolução Francesa?:\n\n Alternativa (A) Guerra e Poder \n Alternativa (B) Rei e Reino \n Alternativa (C) Terra e Trabalho \n Alternativa (D) Liberdade, Igualdade e Fraternidade  \n\n | DIGITE [A/B/C/D] | \n | PLATEIA [P] | \n | UNIVERSITARIOS [U] | \n\n | DIGITE A ALTERNATIVA MAIS ENTER PARA CONTINUAR | \n\n 👤 ")
        #   AJUDA DA PLATEIA
            if pergunta_4_resposta == "P" or pergunta_4_resposta == "p":
                if Ajuda_da_pessoas > 0:
                    Ajuda_da_pessoas -= 1

                    print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🥸  É Alternativa (D)! \n 🥸  Claro que é (D)! \n 🥸  Obvio que nao é (A)! \n\n")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                else:
                    print("\n❌ Você não possui mais ajuda da plateia!\n")
            # AJUDA DOS UNIVERSITARIOS
            elif pergunta_4_resposta == "U" or pergunta_4_resposta == "u":
                if Ajuda_dos_Universitarios > 0:
                    Ajuda_dos_Universitarios -= 1

                    print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (D) \n\n ")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                else:
                    print("\n❌ Você não possui mais ajuda dos universitários!\n")
            # RESPOSTA CERTA
            elif pergunta_4_resposta == "D" or pergunta_4_resposta == "d":

                print("\n✅ CORRETA!")
                print("💵 Você ganhou mais 1,000 reais!\n")
                break
            # RESPOSTAS ERRADAS
            elif pergunta_4_resposta in ["A", "B", "C"]:
                print("\n❌ ERRADA!")
                print("💀 Você perdeu tudo!\n")
                exit()
            else:
                print("\n❌ Resposta inválida!\n")
                exit()

    RESPOSTAS_PERGUNTA_4()
    print (input("\n 🎤 Parabéns " + nome_usuario + ", você acertou a quarta pergunta e já tem 💵 4,000 reais acumulados! \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    print (input(" 🎤 Agora vamos para a quinta e ultima do primeiro bloco! \n\n | TECLE ENTER PARA CONTINUAR | \n"))

    def RESPOSTAS_PERGUNTA_5():
        global Ajuda_da_pessoas
        global Ajuda_dos_Universitarios

        while True:
            pergunta_5_resposta = input ("🎤 PERGUNTA 5:Por que a Revolução Francesa é considerada burguesa?:\n\n Alternativa (A) Porque foi feita apenas por reis \n Alternativa (B) Porque defendia somente os nobres \n Alternativa (C) Porque favoreceu os interesses da burguesia \n Alternativa (D) Porque acabou com o comércio \n\n | DIGITE [A/B/C/D] | \n | PLATEIA [P] | \n | UNIVERSITARIOS [U] | \n\n | DIGITE A ALTERNATIVA MAIS ENTER PARA CONTINUAR | \n\n")
            # AJUDA DA PLATEIA
            if pergunta_5_resposta == "P" or pergunta_5_resposta == "p":
                if Ajuda_da_pessoas > 0:
                    Ajuda_da_pessoas -= 1

                    print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🥸  É Alternativa (C)! \n 🥸  Claro que é (C)! \n 🥸  Obvio que nao é (D)! \n\n")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                else:
                    print("\n❌ Você não possui mais ajuda da plateia!\n")
            # AJUDA DOS UNIVERSITARIOS
            elif pergunta_5_resposta == "U" or pergunta_5_resposta == "u":
                if Ajuda_dos_Universitarios > 0:
                    Ajuda_dos_Universitarios -= 1

                    print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (C) \n\n ")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                else:
                    print("\n❌ Você não possui mais ajuda dos universitários!\n")
            # RESPOSTA CERTA
            elif pergunta_5_resposta == "C" or pergunta_5_resposta == "c":

                print("\n✅ CORRETA!")
                print("💵 Você ganhou mais 1,000 reais!\n")
                break

            # RESPOSTAS ERRADAS
            elif pergunta_5_resposta in ["A", "B", "D"]:
                print("\n❌ ERRADA!")
                print("💀 Você perdeu tudo!\n")
                exit()

            else:
                print("\n❌ Resposta inválida!\n")
                exit()

    RESPOSTAS_PERGUNTA_5()
    print (input("\n 🎤 Parabéns " + nome_usuario + ", você acertou a quinta pergunta e já tem 💵 5,000 reais acumulados! \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    print (input(" 🎤Agora vamos para o proximo bloco Agora as perguntas vão ser um pouco mais complicadas, NIVEL FACIL INTERMEDIARIO. \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    print (input(" 🎤 No proximo Bloco voce podera ganhar muito mais dinheiro! QUER CONTINUAR? OU PARAR? \n\n | TECLE ENTER PARA CONTINUAR | \n"))

    if input("🎤 DIGITE [P] PARA PARAR OU [C] PARA CONTINUAR \n\n 👤 ") in ["P", "p"]:
        print(input("\n Quero Parar e ficar com o dinheiro que acumulei."))
        exit()
    else:    print(input("\n 🎤 Você escolheu continuar, vamos para o para o segundo bloco. \n\n | TECLE ENTER PARA CONTINUAR | \n")) 
    print (input(" 🎤  O valor das perguntas vai aumentar para 10,000 reais cada pergunta \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    print (input(" 🎤 Segundo Tema: Identificar interesses políticos, sociais e econômicos nas independências da América. \n\n | TECLE ENTER PARA CONTINUAR | \n"))

    def RESPOSTAS_PERGUNTA_6_bloco_2():
        global Ajuda_da_pessoas
        global Ajuda_dos_Universitarios

        while True:
            pergunta_6_resposta = input("🎤 PERGUNTA 6: Quem queria mais liberdade nas colônias americanas?:\n\n Alternativa (A) Os colonos \n Alternativa (B) Os reis europeus \n Alternativa (C) Os soldados estrangeiros \n Alternativa (D) Os piratas \n\n | DIGITE [A/B/C/D] | \n | PLATEIA [P] | \n | UNIVERSITARIOS [U] | \n\n | DIGITE A ALTERNATIVA MAIS ENTER PARA CONTINUAR | \n\n 👤 ")
            # AJUDA DA PLATEIA
            if pergunta_6_resposta == "P" or pergunta_6_resposta == "p":
                if Ajuda_da_pessoas > 0:
                    Ajuda_da_pessoas -= 1

                    print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🥸  É Alternativa (A)! \n 🥸  Claro que é (A)! \n 🥸  Obvio que nao é (B)! \n\n")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                else:
                    print("\n❌ Você não possui mais ajuda da plateia!\n")
            # AJUDA DOS UNIVERSITARIOS
            elif pergunta_6_resposta == "U" or pergunta_6_resposta == "u":
                if Ajuda_dos_Universitarios > 0:
                    Ajuda_dos_Universitarios -= 1

                    print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (A) \n\n ")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                else:
                    print("\n❌ Você não possui mais ajuda dos universitários!\n")
            # RESPOSTA CERTA
            elif pergunta_6_resposta == "A" or pergunta_6_resposta == "a":

                print("\n✅ CORRETA!")
                print("💵 Você ganhou 10,000 reais!\n")
                break
            # RESPOSTAS ERRADAS
            elif pergunta_6_resposta in ["B", "C", "D"]:

                print("\n❌ ERRADA!")
                print("💀 Você perdeu tudo!\n")
                exit()
            else:
                print("\n❌ Resposta inválida!\n")
                exit()

    RESPOSTAS_PERGUNTA_6_bloco_2()
    print (input("\n 🎤 Parabéns " + nome_usuario + ", você acertou a sexta pergunta e já tem 💵 15,000 reais acumulados! \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    print (input(" 🎤 Agora vamos para a sétima pergunta. \n\n | TECLE ENTER PARA CONTINUAR | \n"))

    def RESPOSTAS_PERGUNTA_7_bloco_2():
        global Ajuda_da_pessoas
        global Ajuda_dos_Universitarios

        while True:
            pergunta_7_resposta = input("🎤 PERGUNTA 7: Qual era um interesse econômico das independências?:\n\n Alternativa (A) Produzir menos alimentos \n Alternativa (B) Ter mais controle sobre o comércio \n Alternativa (C) Fechar todas as cidades \n Alternativa (D) Acabar com o dinheiro \n\n | DIGITE [A/B/C/D] | \n | PLATEIA [P] | \n | UNIVERSITARIOS [U] | \n\n | DIGITE A ALTERNATIVA MAIS ENTER PARA CONTINUAR | \n\n 👤 ")
            # AJUDA DA PLATEIA
            if pergunta_7_resposta == "P" or pergunta_7_resposta == "p":
                if Ajuda_da_pessoas > 0:
                    Ajuda_da_pessoas -= 1

                    print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🥸  É Alternativa (B)! \n 🥸  Claro que é (B)! \n 🥸  Obvio que nao é (A)! \n\n")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                else:
                    print("\n❌ Você não possui mais ajuda da plateia!\n")
            # AJUDA DOS UNIVERSITARIOS
            elif pergunta_7_resposta == "U" or pergunta_7_resposta == "u":
                if Ajuda_dos_Universitarios > 0:
                    Ajuda_dos_Universitarios -= 1

                    print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (B) \n\n ")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))
                    
                else:
                    print("\n❌ Você não possui mais ajuda dos universitários!\n")
            # RESPOSTA CERTA
            elif pergunta_7_resposta == "B" or pergunta_7_resposta == "b":

                print("\n✅ CORRETA!")
                print("💵 Você ganhou mais 10,000 reais!\n")
                break
            # RESPOSTAS ERRADAS
            elif pergunta_7_resposta in ["A", "C", "D"]:
                print("\n❌ ERRADA!")
                print("💀 Você perdeu tudo!\n")
                exit()
            else:
                print("\n❌ Resposta inválida!\n")
                exit()

    RESPOSTAS_PERGUNTA_7_bloco_2()
    print (input("\n 🎤 Parabéns " + nome_usuario + ", você acertou a sétima pergunta e já tem 💵 25,000 reais acumulados! \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    print (input(" 🎤 Agora vamos para a oitava pergunta. \n\n | TECLE ENTER PARA CONTINUAR | \n"))

    def RESPOSTAS_PERGUNTA_8_bloco_2():
        global Ajuda_da_pessoas
        global Ajuda_dos_Universitarios

        while True:
            pergunta_8_resposta = input("🎤 PERGUNTA 8: O que muitas colônias queriam fazer?:\n\n Alternativa (A) Continuar obedecendo as metropoles \n Alternativa (B) Mudar de continente \n Alternativa (C) Tornar-se independentes \n Alternativa (D) Fechar as escolas \n\n | DIGITE [A/B/C/D] | \n | PLATEIA [P] | \n | UNIVERSITARIOS [U] | \n\n | DIGITE A ALTERNATIVA MAIS ENTER PARA CONTINUAR | \n\n 👤 ")
            # AJUDA DA PLATEIA
            if pergunta_8_resposta == "P" or pergunta_8_resposta == "p":
                if Ajuda_da_pessoas > 0:
                    Ajuda_da_pessoas -= 1

                    print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🥸  É Alternativa (A)! \n 🥸  Claro que é (A)! \n 🥸  Obvio que nao é (B)! \n\n")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                else:
                    print("\n❌ Você não possui mais ajuda da plateia!\n")
            # AJUDA DOS UNIVERSITARIOS
            elif pergunta_8_resposta == "U" or pergunta_8_resposta == "u":
                if Ajuda_dos_Universitarios > 0:
                    Ajuda_dos_Universitarios -= 1

                    print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (A) \n\n ")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))
                    
                else:
                    print("\n❌ Você não possui mais ajuda dos universitários!\n")
            # RESPOSTA CERTA
            elif pergunta_8_resposta == "C" or pergunta_8_resposta == "c":

                print("\n✅ CORRETA!")
                print("💵 Você ganhou mais 10,000 reais!\n")
                break
            # RESPOSTAS ERRADAS
            elif pergunta_8_resposta in ["A", "B", "D"]:
                print("\n❌ ERRADA!")
                print("💀 Você perdeu tudo!\n")
                exit()

            else:
                print("\n❌ Resposta inválida!\n")
                exit()
    RESPOSTAS_PERGUNTA_8_bloco_2()
    print (input("\n 🎤 Parabéns " + nome_usuario + ", você acertou a oitava pergunta e já tem 💵 35,000 reais acumulados! \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    print (input(" 🎤 Agora vamos para a nona pergunta. \n\n | TECLE ENTER PARA CONTINUAR | \n"))

    def RESPOSTAS_PERGUNTA_9_bloco_2():
        global Ajuda_da_pessoas
        global Ajuda_dos_Universitarios

        while True:
            pergunta_9_resposta = input("🎤 PERGUNTA 9: Qual era um interesse político dos líderes das independências?:\n\n Alternativa (A) Governar seus próprios países \n Alternativa (B) Acabar com as cidades \n Alternativa (C) Proibir a agricultura \n Alternativa (D) Fechar os portos \n\n | DIGITE [A/B/C/D] | \n | PLATEIA [P] | \n | UNIVERSITARIOS [U] | \n\n | DIGITE A ALTERNATIVA MAIS ENTER PARA CONTINUAR | \n\n 👤 ")
            # AJUDA DA PLATEIA
            if pergunta_9_resposta == "P" or pergunta_9_resposta == "p":
                if Ajuda_da_pessoas > 0:
                    Ajuda_da_pessoas -= 1

                    print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🥸  É Alternativa (A)! \n 🥸  Claro que é (A)! \n 🥸  Obvio que nao é (B)! \n\n")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                else:
                    print("\n❌ Você não possui mais ajuda da plateia!\n")
            # AJUDA DOS UNIVERSITARIOS
            elif pergunta_9_resposta == "U" or pergunta_9_resposta == "u":
                if Ajuda_dos_Universitarios > 0:
                    Ajuda_dos_Universitarios -= 1

                    print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (A) \n\n ")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))
                    
                else:
                    print("\n❌ Você não possui mais ajuda dos universitários!\n")
            # RESPOSTA CERTA
            elif pergunta_9_resposta == "A" or pergunta_9_resposta == "a":

                print("\n✅ CORRETA!")
                print("💵 Você ganhou mais 10,000 reais!\n")
                break
            # RESPOSTAS ERRADAS
            elif pergunta_9_resposta in ["B", "C", "D"]:
                print("\n❌ ERRADA!")
                print("💀 Você perdeu tudo!\n")
                exit()

            else:
                print("\n❌ Resposta inválida!\n")
                exit()

    RESPOSTAS_PERGUNTA_9_bloco_2()
    print (input("\n 🎤 Parabéns " + nome_usuario + ", você acertou a nona pergunta e já tem 💵 45,000 reais acumulados! \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    print (input(" 🎤 Agora vamos para a décima pergunta. \n\n | TECLE ENTER PARA CONTINUAR | \n"))

    def RESPOSTAS_PERGUNTA_10_bloco_2():
        global Ajuda_da_pessoas
        global Ajuda_dos_Universitarios

        while True:
            pergunta_10_resposta = input("🎤 PERGUNTA 10: O que a independência trouxe para muitos países da América?:\n\n Alternativa (A) Mais autonomia para decidir seus assuntos \n Alternativa (B) Menos população \n Alternativa (C) Menos território \n Alternativa (D) Fim do comércio \n\n | DIGITE [A/B/C/D] | \n | PLATEIA [P] | \n | UNIVERSITARIOS [U] | \n\n | DIGITE A ALTERNATIVA MAIS ENTER PARA CONTINUAR | \n\n 👤 ")
            # AJUDA DA PLATEIA
            if pergunta_10_resposta == "P" or pergunta_10_resposta == "p":
                if Ajuda_da_pessoas > 0:
                    Ajuda_da_pessoas -= 1

                    print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🥸  É Alternativa (A)! \n 🥸  Claro que é (A)! \n 🥸  Obvio que nao é (C)! \n\n")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                else:
                    print("\n❌ Você não possui mais ajuda da plateia!\n")
            # AJUDA DOS UNIVERSITARIOS
            elif pergunta_10_resposta == "U" or pergunta_10_resposta == "u":
                if Ajuda_dos_Universitarios > 0:
                    Ajuda_dos_Universitarios -= 1

                    print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (A) \n\n ")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                    
                else:
                    print("\n❌ Você não possui mais ajuda dos universitários!\n")
            # RESPOSTA CERTA
            elif pergunta_10_resposta == "A" or pergunta_10_resposta == "a":

                print("\n✅ CORRETA!")
                print("💵 Você ganhou mais 10,000 reais!\n")
                break
            # RESPOSTAS ERRADAS
            elif pergunta_10_resposta in ["B", "C", "D"]:
                print("\n❌ ERRADA!")
                print("💀 Você perdeu tudo!\n")
                exit()

            else:
                print("\n❌ Resposta inválida!\n")
                exit()

    RESPOSTAS_PERGUNTA_10_bloco_2()
    print (input("\n 🎤 Parabéns " + nome_usuario + ", você acertou a décima pergunta e já tem 💵 55,000 reais acumulados! \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    print (input(" 🎤 Agora vamos para o proximo bloco Agora as perguntas vão ser um pouco mais complicadas, NIVEL INTERMEDIARIO. \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    print (input(" 🎤 No proximo Bloco voce podera ganhar muito mais dinheiro! QUER CONTINUAR? OU PARAR? \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    if input("🎤 DIGITE [P] PARA PARAR OU [C] PARA CONTINUAR \n\n 👤 ") in ["P", "p"]:
        print(input("\n Quero Parar e ficar com o dinheiro que acumulei."))
        exit()
    else:    print(input("\n 🎤 Você escolheu continuar, vamos para o para o terceiro bloco. \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    print (input(" 🎤  O valor das perguntas vai aumentar para 20,000 reais cada pergunta \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    print (input(" 🎤 Terceiro Tema:Cangaço. \n\n | TECLE ENTER PARA CONTINUAR | \n"))

    def RESPOSTAS_PERGUNTA_11_bloco_3():
        global Ajuda_da_pessoas
        global Ajuda_dos_Universitarios

        while True:
            pergunta_11_resposta = input("🎤 PERGUNTA 11: O que foi o cangaço no Brasil? :\n\n Alternativa (A) Um movimento artístico do século XX \n Alternativa (B) Um grupo de imigrantes europeus \n Alternativa (C) Um fenômeno social de grupos armados que atuavam no sertão nordestino \n Alternativa (D) Uma revolta indígena na Amazônia \n\n | DIGITE [A/B/C/D] | \n | PLATEIA [P] | \n | UNIVERSITARIOS [U] | \n\n | DIGITE A ALTERNATIVA MAIS ENTER PARA CONTINUAR | \n\n 👤 ")
            # AJUDA DA PLATEIA
            if pergunta_11_resposta == "P" or pergunta_11_resposta == "p":
                if Ajuda_da_pessoas > 0:
                    Ajuda_da_pessoas -= 1

                    print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🥸  É Alternativa (C)! \n 🥸  Claro que é (C)! \n 🥸  Obvio que nao é (A)! \n\n")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                else:
                    print("\n❌ Você não possui mais ajuda da plateia!\n")
            # AJUDA DOS UNIVERSITARIOS
            elif pergunta_11_resposta == "U" or pergunta_11_resposta == "u":
                if Ajuda_dos_Universitarios > 0:
                    Ajuda_dos_Universitarios -= 1

                    print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (C) \n\n ")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))
                    
                else:
                    print("\n❌ Você não possui mais ajuda dos universitários!\n")
            # RESPOSTA CERTA
            elif pergunta_11_resposta == "C" or pergunta_11_resposta == "c":

                print("\n✅ CORRETA!")
                print("💵 Você ganhou 20,000 reais!\n")
                break
            # RESPOSTAS ERRADAS
            elif pergunta_11_resposta in ["A", "B", "D"]:
                print("\n❌ ERRADA!")
                print("💀 Você perdeu tudo!\n")
                exit()
            else:
                print("\n❌ Resposta inválida!\n")
                exit()

    RESPOSTAS_PERGUNTA_11_bloco_3()
    print (input("\n 🎤 Parabéns " + nome_usuario + ", você acertou a décima primeira pergunta e já tem 💵 75,000 reais acumulados! \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    print (input(" 🎤 Agora vamos para a décima segunda pergunta. \n\n | TECLE ENTER PARA CONTINUAR | \n"))

    def RESPOSTAS_PERGUNTA_12_bloco_3():
        global Ajuda_da_pessoas
        global Ajuda_dos_Universitarios

        while True:
            pergunta_12_resposta = input("🎤 PERGUNTA 12: Qual foi o cangaceiro mais famoso da história do Brasil?:\n\n Alternativa (A) Lampião \n Alternativa (B) Antônio Conselheiro \n Alternativa (C) Zumbi dos Palmares \n Alternativa (D) Tiradentes \n\n | DIGITE [A/B/C/D] | \n | PLATEIA [P] | \n | UNIVERSITARIOS [U] | \n\n | DIGITE A ALTERNATIVA MAIS ENTER PARA CONTINUAR | \n\n 👤 ")
            # AJUDA DA PLATEIA
            if pergunta_12_resposta == "P" or pergunta_12_resposta == "p":
                if Ajuda_da_pessoas > 0:
                    Ajuda_da_pessoas -= 1

                    print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🥸  É Alternativa (A)! \n 🥸  Claro que é (A)! \n 🥸  Obvio que nao é (C)! \n\n")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                else:
                    print("\n❌ Você não possui mais ajuda da plateia!\n")
            # AJUDA DOS UNIVERSITARIOS
            elif pergunta_12_resposta == "U" or pergunta_12_resposta == "u":
                if Ajuda_dos_Universitarios > 0:
                    Ajuda_dos_Universitarios -= 1

                    print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (A) \n\n ")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))
                    
                else:
                    print("\n❌ Você não possui mais ajuda dos universitários!\n")
            # RESPOSTA CERTA
            elif pergunta_12_resposta == "A" or pergunta_12_resposta == "a":

                print("\n✅ CORRETA!")
                print("💵 Você ganhou mais 20,000 reais!\n")
                break
            # RESPOSTAS ERRADAS
            elif pergunta_12_resposta in ["B", "C", "D"]:
                print("\n❌ ERRADA!")
                print("💀 Você perdeu tudo!\n")
                exit()
            else:
                print("\n❌ Resposta inválida!\n")
                exit()

    RESPOSTAS_PERGUNTA_12_bloco_3()
    print (input("\n 🎤 Parabéns " + nome_usuario + ", você acertou a décima segunda pergunta e já tem 💵 95,000 reais acumulados! \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    print (input(" 🎤 Agora vamos para a décima terceira pergunta. \n\n | TECLE ENTER PARA CONTINUAR | \n"))

    def RESPOSTAS_PERGUNTA_13_bloco_3():
        global Ajuda_da_pessoas
        global Ajuda_dos_Universitarios

        while True:
            pergunta_13_resposta = input("🎤 PERGUNTA 13: Um dos fatores que contribuíram para o surgimento do cangaço foi? :\n\n Alternativa (A) A industrialização do Sudeste \n Alternativa (B) As dificuldades sociais e econômicas do sertão nordestino \n Alternativa (C) O crescimento das universidades \n Alternativa (D) A chegada da internet \n\n | DIGITE [A/B/C/D] | \n | PLATEIA [P] | \n | UNIVERSITARIOS [U] | \n\n | DIGITE A ALTERNATIVA MAIS ENTER PARA CONTINUAR | \n\n 👤 ")
            # AJUDA DA PLATEIA
            if pergunta_13_resposta == "P" or pergunta_13_resposta == "p":
                if Ajuda_da_pessoas > 0:
                    Ajuda_da_pessoas -= 1

                    print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🥸  É Alternativa (B)! \n 🥸  Claro que é (B)! \n 🥸  Obvio que nao é (A)! \n\n")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                else:
                    print("\n❌ Você não possui mais ajuda da plateia!\n")
            # AJUDA DOS UNIVERSITARIOS
            elif pergunta_13_resposta == "U" or pergunta_13_resposta == "u":
                if Ajuda_dos_Universitarios > 0:
                    Ajuda_dos_Universitarios -= 1

                    print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (B) \n\n ")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))
                    
                else:
                    print("\n❌ Você não possui mais ajuda dos universitários!\n")
            # RESPOSTA CERTA
            elif pergunta_13_resposta == "B" or pergunta_13_resposta == "b":

                print("\n✅ CORRETA!")
                print("💵 Você ganhou mais 20,000 reais!\n")
                break
            # RESPOSTAS ERRADAS
            elif pergunta_13_resposta in ["A", "C", "D"]:
                print("\n❌ ERRADA!")
                print("💀 Você perdeu tudo!\n")
                exit()
            else:
                print("\n❌ Resposta inválida!\n")
                exit()

    RESPOSTAS_PERGUNTA_13_bloco_3()
    print (input("\n 🎤 Parabéns " + nome_usuario + ", você acertou a décima terceira pergunta e já tem 💵 115,000 reais acumulados! \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    print (input(" 🎤 Agora vamos para a décima quarta pergunta. \n\n | TECLE ENTER PARA CONTINUAR | \n"))

    def RESPOSTAS_PERGUNTA_14_bloco_3():
        global Ajuda_da_pessoas
        global Ajuda_dos_Universitarios

        while True:
            pergunta_14_resposta = input("🎤 PERGUNTA 14: Como era chamada a companheira de Lampião que também participou do cangaço?: \n\n Alternativa (A) Anita Garibaldi \n Alternativa (B) Princesa Isabel \n Alternativa (C) Chiquinha Gonzaga \n Alternativa (D) Maria Bonita \n\n | DIGITE [A/B/C/D] | \n | PLATEIA [P] | \n | UNIVERSITARIOS [U] | \n\n | DIGITE A ALTERNATIVA MAIS ENTER PARA CONTINUAR | \n\n 👤 ")
            # AJUDA DA PLATEIA
            if pergunta_14_resposta == "P" or pergunta_14_resposta == "p":
                if Ajuda_da_pessoas > 0:
                    Ajuda_da_pessoas -= 1

                    print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🥸  É Alternativa (D)! \n 🥸  Claro que é (D)! \n 🥸  Obvio que nao é (A)! \n\n")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                else:
                    print("\n❌ Você não possui mais ajuda da plateia!\n")
            # AJUDA DOS UNIVERSITARIOS
            elif pergunta_14_resposta == "U" or pergunta_14_resposta == "u":
                if Ajuda_dos_Universitarios > 0:
                    Ajuda_dos_Universitarios -= 1

                    print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (D) \n\n ")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                else:
                    print("\n❌ Você não possui mais ajuda dos universitários!\n")
            # RESPOSTA CERTA
            elif pergunta_14_resposta == "D" or pergunta_14_resposta == "d":

                print("\n✅ CORRETA!")
                print("💵 Você ganhou mais 20,000 reais!\n")
                break
            # RESPOSTAS ERRADAS
            elif pergunta_14_resposta in ["A", "B", "C"]:
                print("\n❌ ERRADA!")
                print("💀 Você perdeu tudo!\n")
                exit()
            else:
                print("\n❌ Resposta inválida!\n")
                exit()

    RESPOSTAS_PERGUNTA_14_bloco_3()
    print (input("\n 🎤 Parabéns " + nome_usuario + ", você acertou a décima quarta pergunta e já tem 💵 135,000 reais acumulados! \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    print (input(" 🎤 Agora vamos para a décima quinta pergunta. \n\n | TECLE ENTER PARA CONTINUAR | \n"))

    def RESPOSTAS_PERGUNTA_15_bloco_3():
        global Ajuda_da_pessoas
        global Ajuda_dos_Universitarios

        while True:
            pergunta_15_resposta = input("🎤 PERGUNTA 15: Qual era uma característica dos grupos de cangaceiros?: \n\n Alternativa (A) Atuavam principalmente em grandes cidades \n Alternativa (B) Eram grupos armados que se deslocavam pelo sertão \n Alternativa (C) Trabalhavam apenas na agricultura \n Alternativa (D) Faziam parte do Exército Brasileiro \n\n | DIGITE [A/B/C/D] | \n | PLATEIA [P] | \n | UNIVERSITARIOS [U] | \n\n | DIGITE A ALTERNATIVA MAIS ENTER PARA CONTINUAR | \n\n 👤 ")
            # AJUDA DA PLATEIA
            if pergunta_15_resposta == "P" or pergunta_15_resposta == "p":
                if Ajuda_da_pessoas > 0:
                    Ajuda_da_pessoas -= 1

                    print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🥸  É Alternativa (B)! \n 🥸  Claro que é (B)! \n 🥸  Obvio que nao é (A)! \n\n")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                else:
                    print("\n❌ Você não possui mais ajuda da plateia!\n")
            # AJUDA DOS UNIVERSITARIOS
            elif pergunta_15_resposta == "U" or pergunta_15_resposta == "u":
                if Ajuda_dos_Universitarios > 0:
                    Ajuda_dos_Universitarios -= 1

                    print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (B) \n\n ")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))
                    
                else:
                    print("\n❌ Você não possui mais ajuda dos universitários!\n")
            # RESPOSTA CERTA
            elif pergunta_15_resposta == "B" or pergunta_15_resposta == "b":

                print("\n✅ CORRETA!")
                print("💵 Você ganhou mais 20,000 reais!\n")
                break
            # RESPOSTAS ERRADAS
            elif pergunta_15_resposta in ["A", "C", "D"]:
                print("\n❌ ERRADA!")
                print("💀 Você perdeu tudo!\n")
                exit()
            else:
                print("\n❌ Resposta inválida!\n")
                exit()

    RESPOSTAS_PERGUNTA_15_bloco_3()
    print (input("\n 🎤 Parabéns " + nome_usuario + ", você acertou a décima quinta pergunta e já tem 💵 155,000 reais acumulados! \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    print (input(" 🎤 Agora vamos para o proximo bloco. \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    print (input(" 🎤 No proximo bloco voce podera ganhar muito mais dinheiro! QUER CONTINUAR? OU PARAR? \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    if input("🎤 DIGITE [P] PARA PARAR OU [C] PARA CONTINUAR \n\n 👤 ") in ["P", "p"]:
        print(input("\n Quero Parar e ficar com o dinheiro que acumulei."))
        exit()
    else:    print(input("\n 🎤 Você escolheu continuar, vamos para o para o quarto bloco. \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    print (input(" 🎤  O valor das perguntas vai aumentar para 30,000 reais cada pergunta \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    print (input(" 🎤 Quarto Tema: Contestado. \n\n | TECLE ENTER PARA CONTINUAR | \n"))

    def RESPOSTAS_PERGUNTA_16_bloco_4():
        global Ajuda_da_pessoas
        global Ajuda_dos_Universitarios

        while True:
            pergunta_16_resposta = input("🎤 PERGUNTA 16: Em quais estados brasileiros ocorreu a Guerra do Contestado? : \n\n Alternativa (A) Bahia e Sergipe \n Alternativa (B) Paraná e Santa Catarina \n Alternativa (C) São Paulo e Rio de Janeiro \n Alternativa (D) Minas Gerais e Goiás \n\n | DIGITE [A/B/C/D] | \n | PLATEIA [P] | \n | UNIVERSITARIOS [U] | \n\n | DIGITE A ALTERNATIVA MAIS ENTER PARA CONTINUAR | \n\n 👤 ")
            # AJUDA DA PLATEIA
            if pergunta_16_resposta == "P" or pergunta_16_resposta == "p":
                if Ajuda_da_pessoas > 0:
                    Ajuda_da_pessoas -= 1

                    print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🥸  É Alternativa (B)! \n 🥸  Claro que é (B)! \n 🥸  Obvio que nao é (A)! \n\n")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                else:
                    print("\n❌ Você não possui mais ajuda da plateia!\n")
            # AJUDA DOS UNIVERSITARIOS
            elif pergunta_16_resposta == "U" or pergunta_16_resposta == "u":
                if Ajuda_dos_Universitarios > 0:
                    Ajuda_dos_Universitarios -= 1

                    print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (B) \n\n ")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))
                    
                else:
                    print("\n❌ Você não possui mais ajuda dos universitários!\n")
            # RESPOSTA CERTA
            elif pergunta_16_resposta == "B" or pergunta_16_resposta == "b":

                print("\n✅ CORRETA!")
                print("💵 Você ganhou 30,000 reais!\n")
                break
            # RESPOSTAS ERRADAS
            elif pergunta_16_resposta in ["A", "C", "D"]:
                print("\n❌ ERRADA!")
                print("💀 Você perdeu tudo!\n")
                exit()
            else:
                print("\n❌ Resposta inválida!\n")
                exit()

    RESPOSTAS_PERGUNTA_16_bloco_4()
    print (input("\n 🎤 Parabéns " + nome_usuario + ", você acertou a décima sexta pergunta e já tem 💵 185,000 reais acumulados! \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    print (input(" 🎤 Agora vamos para a décima sétima pergunta. \n\n | TECLE ENTER PARA CONTINUAR | \n"))

    def RESPOSTAS_PERGUNTA_17_bloco_4():
        global Ajuda_da_pessoas
        global Ajuda_dos_Universitarios

        while True:
            pergunta_17_resposta = input("🎤 PERGUNTA 17: Qual foi uma das principais causas da Guerra do Contestado? : \n\n Alternativa (A) A disputa por terras e a expulsão de moradores da região \n Alternativa (B) A luta pela independência do Brasil \n Alternativa (C) A abolição da escravidão \n Alternativa (D) A construção de Brasília \n\n | DIGITE [A/B/C/D] | \n | PLATEIA [P] | \n | UNIVERSITARIOS [U] | \n\n | DIGITE A ALTERNATIVA MAIS ENTER PARA CONTINUAR | \n\n 👤 ")
            # AJUDA DA PLATEIA
            if pergunta_17_resposta == "P" or pergunta_17_resposta == "p":
                if Ajuda_da_pessoas > 0:
                    Ajuda_da_pessoas -= 1

                    print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🥸  É Alternativa (A)! \n 🥸  Claro que é (A)! \n 🥸  Obvio que nao é (B)! \n\n")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                else:
                    print("\n❌ Você não possui mais ajuda da plateia!\n")
            # AJUDA DOS UNIVERSITARIOS
            elif pergunta_17_resposta == "U" or pergunta_17_resposta == "u":
                if Ajuda_dos_Universitarios > 0:
                    Ajuda_dos_Universitarios -= 1

                    print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (A) \n\n ")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))
                    
                else:
                    print("\n❌ Você não possui mais ajuda dos universitários!\n")
            # RESPOSTA CERTA
            elif pergunta_17_resposta == "A" or pergunta_17_resposta == "a":

                print("\n✅ CORRETA!")
                print("💵 Você ganhou mais 30,000 reais!\n")
                break
            # RESPOSTAS ERRADAS
            elif pergunta_17_resposta in ["B", "C", "D"]:
                print("\n❌ ERRADA!")
                print("💀 Você perdeu tudo!\n")
                exit()
            else:
                print("\n❌ Resposta inválida!\n")
                exit()

    RESPOSTAS_PERGUNTA_17_bloco_4()
    print (input("\n 🎤 Parabéns " + nome_usuario + ", você acertou a décima sétima pergunta e já tem 💵 215,000 reais acumulados! \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    print (input(" 🎤 Agora vamos para a décima oitava pergunta. \n\n | TECLE ENTER PARA CONTINUAR | \n"))

    def RESPOSTAS_PERGUNTA_18_bloco_4():
        global Ajuda_da_pessoas
        global Ajuda_dos_Universitarios

        while True:
            pergunta_18_resposta = input("🎤 PERGUNTA 18: A Guerra do Contestado aconteceu durante qual período? : \n\n Alternativa (A) Império do Brasil \n Alternativa (B) Brasil Colonial \n Alternativa (C) Ditadura Militar \n Alternativa (D) República Velha \n\n | DIGITE [A/B/C/D] | \n | PLATEIA [P] | \n | UNIVERSITARIOS [U] | \n\n | DIGITE A ALTERNATIVA MAIS ENTER PARA CONTINUAR | \n\n 👤 ")
            # AJUDA DA PLATEIA
            if pergunta_18_resposta == "P" or pergunta_18_resposta == "p":
                if Ajuda_da_pessoas > 0:
                    Ajuda_da_pessoas -= 1

                    print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🥸  É Alternativa (D)! \n 🥸  Claro que é (D)! \n 🥸  Obvio que nao é (A)! \n\n")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                else:
                    print("\n❌ Você não possui mais ajuda da plateia!\n")
            # AJUDA DOS UNIVERSITARIOS
            elif pergunta_18_resposta == "U" or pergunta_18_resposta == "u":
                if Ajuda_dos_Universitarios > 0:
                    Ajuda_dos_Universitarios -= 1

                    print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (D) \n\n ")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))
                    
                else:
                    print("\n❌ Você não possui mais ajuda dos universitários!\n")
            # RESPOSTA CERTA
            elif pergunta_18_resposta == "D" or pergunta_18_resposta == "d":

                print("\n✅ CORRETA!")
                print("💵 Você ganhou mais 30,000 reais!\n")
                break
            # RESPOSTAS ERRADAS
            elif pergunta_18_resposta in ["A", "B", "C"]:
                print("\n❌ ERRADA!")
                print("💀 Você perdeu tudo!\n")
                exit()
            else:
                print("\n❌ Resposta inválida!\n")
                exit()

    RESPOSTAS_PERGUNTA_18_bloco_4()
    print (input("\n 🎤 Parabéns " + nome_usuario + ", você acertou a décima oitava pergunta e já tem 💵 245,000 reais acumulados! \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    print (input(" 🎤 Agora vamos para a décima nona pergunta. \n\n | TECLE ENTER PARA CONTINUAR | \n"))

    def RESPOSTAS_PERGUNTA_19_bloco_4():
        global Ajuda_da_pessoas
        global Ajuda_dos_Universitarios

        while True:
            pergunta_19_resposta = input("🎤 PERGUNTA 19: Além da questão das terras, o movimento do Contestado teve forte influência? : \n\n Alternativa (A) Religiosa e messiânica \n Alternativa (B) Industrial e tecnológica \n Alternativa (C) Marítima e comercial \n Alternativa (D) Esportiva e cultural \n\n | DIGITE [A/B/C/D] | \n | PLATEIA [P] | \n | UNIVERSITARIOS [U] | \n\n | DIGITE A ALTERNATIVA MAIS ENTER PARA CONTINUAR | \n\n 👤 ")
            # AJUDA DA PLATEIA
            if pergunta_19_resposta == "P" or pergunta_19_resposta == "p":
                if Ajuda_da_pessoas > 0:
                    Ajuda_da_pessoas -= 1

                    print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🥸  É Alternativa (A)! \n 🥸  Claro que é (A)! \n 🥸  Obvio que nao é (B)! \n\n")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                else:
                    print("\n❌ Você não possui mais ajuda da plateia!\n")
            # AJUDA DOS UNIVERSITARIOS
            elif pergunta_19_resposta == "U" or pergunta_19_resposta == "u":
                if Ajuda_dos_Universitarios > 0:
                    Ajuda_dos_Universitarios -= 1

                    print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (A) \n\n ")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))
                    
                else:
                    print("\n❌ Você não possui mais ajuda dos universitários!\n")
            # RESPOSTA CERTA
            elif pergunta_19_resposta == "A" or pergunta_19_resposta == "a":

                print("\n✅ CORRETA!")
                print("💵 Você ganhou mais 30,000 reais!\n")
                break
            # RESPOSTAS ERRADAS
            elif pergunta_19_resposta in ["B", "C", "D"]:
                print("\n❌ ERRADA!")
                print("💀 Você perdeu tudo!\n")
                exit()
            else:
                print("\n❌ Resposta inválida!\n")
                exit()

    RESPOSTAS_PERGUNTA_19_bloco_4()
    print (input("\n 🎤 Parabéns " + nome_usuario + ", você acertou a décima nona pergunta e já tem 💵 275,000 reais acumulados! \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    print (input(" 🎤 Agora vamos para a vigésima pergunta. \n\n | TECLE ENTER PARA CONTINUAR | \n"))

    def RESPOSTAS_PERGUNTA_20_bloco_4():
        global Ajuda_da_pessoas
        global Ajuda_dos_Universitarios

        while True:
            pergunta_20_resposta = input("🎤 PERGUNTA 20: Qual foi o resultado da Guerra do Contestado? : \n\n Alternativa (A) Criação de um novo país no Sul do Brasil \n Alternativa (B) Vitória dos rebeldes e independência da região \n Alternativa (C) Derrota dos sertanejos pelas forças do governo \n Alternativa (D) Fim da República Velha \n\n | DIGITE [A/B/C/D] | \n | PLATEIA [P] | \n | UNIVERSITARIOS [U] | \n\n | DIGITE A ALTERNATIVA MAIS ENTER PARA CONTINUAR | \n\n 👤 ")
            # AJUDA DA PLATEIA
            if pergunta_20_resposta == "P" or pergunta_20_resposta == "p":
                if Ajuda_da_pessoas > 0:
                    Ajuda_da_pessoas -= 1

                    print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🥸  É Alternativa (C)! \n 🥸  Claro que é (c)! \n 🥸  Obvio que nao é (A)! \n\n")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                else:
                    print("\n❌ Você não possui mais ajuda da plateia!\n")
            # AJUDA DOS UNIVERSITARIOS
            elif pergunta_20_resposta == "U" or pergunta_20_resposta == "u":
                if Ajuda_dos_Universitarios > 0:
                    Ajuda_dos_Universitarios -= 1

                    print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (C) \n\n ")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))
                    
                else:
                    print("\n❌ Você não possui mais ajuda dos universitários!\n")
            # RESPOSTA CERTA
            elif pergunta_20_resposta == "C" or pergunta_20_resposta == "c":

                print("\n✅ CORRETA!")
                print("💵 Você ganhou mais 30,000 reais!\n")
                break
            # RESPOSTAS ERRADAS
            elif pergunta_20_resposta in ["A", "B", "D"]:
                print("\n❌ ERRADA!")
                print("💀 Você perdeu tudo!\n")
                exit()
            else:
                print("\n❌ Resposta inválida!\n")
                exit()

    RESPOSTAS_PERGUNTA_20_bloco_4()
    print (input("\n 🎤 Parabéns " + nome_usuario + ", você acertou a vigésima pergunta e já tem 💵 305,000 reais acumulados! \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    print (input(" 🎤 Agora vamos para o proximo bloco, NIVEL DIFÍCIL 💀 \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    print (input(" 🎤 No proximo bloco voce podera ganhar muito mais dinheiro! QUER CONTINUAR? OU PARAR? \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    if input("🎤 DIGITE [P] PARA PARAR OU [C] PARA CONTINUAR \n\n 👤 ") in ["P", "p"]:
        print(input("\n Quero Parar e ficar com o dinheiro que acumulei."))
        exit()
    else:    print(input("\n 🎤 Você escolheu continuar, vamos para o para o quinto bloco. \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    print (input(" 🎤  O valor das perguntas vai aumentar para 40,000 reais cada pergunta \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    print (input(" 🎤 Quinto Tema: Escravidão . \n\n | TECLE ENTER PARA CONTINUAR | \n"))

    def RESPOSTAS_PERGUNTA_21_bloco_5():
        global Ajuda_da_pessoas
        global Ajuda_dos_Universitarios

        while True:
            pergunta_21_resposta = input("🎤 PERGUNTA 21: Em que ano foi assinada a Lei Áurea, que aboliu a escravidão no Brasil? : \n\n Alternativa (A) 1888 \n Alternativa (B) 1822 \n Alternativa (C) 1910 \n Alternativa (D) 1850 \n\n | DIGITE [A/B/C/D] | \n | PLATEIA [P] | \n | UNIVERSITARIOS [U] | \n\n | DIGITE A ALTERNATIVA MAIS ENTER PARA CONTINUAR | \n\n 👤 ")
            # AJUDA DA PLATEIA
            if pergunta_21_resposta == "P" or pergunta_21_resposta == "p":
                if Ajuda_da_pessoas > 0:
                    Ajuda_da_pessoas -= 1

                    print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🥸  É Alternativa (A)! \n 🥸  Claro que é (A)! \n 🥸  Obvio que nao é (B)! \n\n")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                else:
                    print("\n❌ Você não possui mais ajuda da plateia!\n")
            # AJUDA DOS UNIVERSITARIOS
            elif pergunta_21_resposta == "U" or pergunta_21_resposta == "u":
                if Ajuda_dos_Universitarios > 0:
                    Ajuda_dos_Universitarios -= 1

                    print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (A) \n\n ")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))
                    
                else:
                    print("\n❌ Você não possui mais ajuda dos universitários!\n")
            # RESPOSTA CERTA
            elif pergunta_21_resposta == "A" or pergunta_21_resposta == "a":

                print("\n✅ CORRETA!")
                print("💵 Você ganhou 40,000 reais!\n")
                break
            # RESPOSTAS ERRADAS
            elif pergunta_21_resposta in ["B", "C", "D"]:
                print("\n❌ ERRADA!")
                print("💀 Você perdeu tudo!\n")
                exit()
            else:
                print("\n❌ Resposta inválida!\n")
                exit()

    RESPOSTAS_PERGUNTA_21_bloco_5()
    print (input("\n 🎤 Parabéns " + nome_usuario + ", você acertou a vigésima primeira pergunta e já tem 💵 345,000 reais acumulados! \n\n | TECLE ENTER PARA CONTINUAR | \n"))

    print (input(" 🎤 Agora vamos para a vigésima segunda pergunta. \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    def RESPOSTAS_PERGUNTA_22_bloco_5():
        global Ajuda_da_pessoas
        global Ajuda_dos_Universitarios

        while True:
            pergunta_22_resposta = input("🎤 PERGUNTA 22: Qual era a principal atividade econômica que utilizava mão de obra escrava no Brasil? : \n\n Alternativa (A) Agricultura, especialmente a produção de açúcar e café \n Alternativa (B) Indústria têxtil \n Alternativa (C) Mineração de ouro \n Alternativa (D) Comércio marítimo \n\n | DIGITE [A/B/C/D] | \n | PLATEIA [P] | \n | UNIVERSITARIOS [U] | \n\n | DIGITE A ALTERNATIVA MAIS ENTER PARA CONTINUAR | \n\n 👤 ")
            # AJUDA DA PLATEIA
            if pergunta_22_resposta == "P" or pergunta_22_resposta == "p":
                if Ajuda_da_pessoas > 0:
                    Ajuda_da_pessoas -= 1

                    print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🥸  É Alternativa (A)! \n 🥸  Claro que é (A)! \n 🥸  Obvio que nao é (B)! \n\n")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                else:
                    print("\n❌ Você não possui mais ajuda da plateia!\n")
            # AJUDA DOS UNIVERSITARIOS
            elif pergunta_22_resposta == "U" or pergunta_22_resposta == "u":
                if Ajuda_dos_Universitarios > 0:
                    Ajuda_dos_Universitarios -= 1

                    print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (A) \n\n ")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))
                    
                else:
                    print("\n❌ Você não possui mais ajuda dos universitários!\n")
            # RESPOSTA CERTA
            elif pergunta_22_resposta == "A" or pergunta_22_resposta == "a":

                print("\n✅ CORRETA!")
                print("💵 Você ganhou 40,000 reais!\n")
                break
            # RESPOSTAS ERRADAS
            elif pergunta_22_resposta in ["B", "C", "D"]:
                print("\n❌ ERRADA!")
                print("💀 Você perdeu tudo!\n")
                exit()
            else:
                print("\n❌ Resposta inválida!\n")
                exit()

    RESPOSTAS_PERGUNTA_22_bloco_5()
    print (input("\n 🎤 Parabéns " + nome_usuario + ", você acertou a vigésima segunda pergunta e já tem 💵 385,000 reais acumulados! \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    print (input(" 🎤 Agora vamos para a vigésima terceira pergunta. \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    def RESPOSTAS_PERGUNTA_23_bloco_5():
        global Ajuda_da_pessoas
        global Ajuda_dos_Universitarios

        while True:
            pergunta_23_resposta = input("🎤 PERGUNTA 23: Qual foi o nome do movimento de resistência liderado por escravos no Quilombo dos Palmares? : \n\n Alternativa (A) Revolta dos Malês \n Alternativa (B) Guerra dos Emboabas \n Alternativa (C) Insurgência Comunista \n Alternativa (D) Rebelião dos Povos Indígenas \n\n | DIGITE [A/B/C/D] | \n | PLATEIA [P] | \n | UNIVERSITARIOS [U] | \n\n | DIGITE A ALTERNATIVA MAIS ENTER PARA CONTINUAR | \n\n 👤 ")
            # AJUDA DA PLATEIA
            if pergunta_23_resposta == "P" or pergunta_23_resposta == "p":
                if Ajuda_da_pessoas > 0:
                    Ajuda_da_pessoas -= 1

                    print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🥸  É Alternativa (A)! \n 🥸  Claro que é (A)! \n 🥸  Obvio que nao é (B)! \n\n")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                else:
                    print("\n❌ Você não possui mais ajuda da plateia!\n")
            # AJUDA DOS UNIVERSITARIOS
            elif pergunta_23_resposta == "U" or pergunta_23_resposta == "u":
                if Ajuda_dos_Universitarios > 0:
                    Ajuda_dos_Universitarios -= 1

                    print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (A) \n\n ")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))
                    
                else:
                    print("\n❌ Você não possui mais ajuda dos universitários!\n")
            # RESPOSTA CERTA
            elif pergunta_23_resposta == "A" or pergunta_23_resposta == "a":

                print("\n✅ CORRETA!")
                print("💵 Você ganhou 40,000 reais!\n")
                break
            # RESPOSTAS ERRADAS
            elif pergunta_23_resposta in ["B", "C", "D"]:
                print("\n❌ ERRADA!")
                print("💀 Você perdeu tudo!\n")
                exit()
            else:
                print("\n❌ Resposta inválida!\n")
                exit()

    RESPOSTAS_PERGUNTA_23_bloco_5()
    print (input("\n 🎤 Parabéns " + nome_usuario + ", você acertou a vigésima terceira pergunta e já tem 💵 425,000 reais acumulados! \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    print (input(" 🎤 Agora vamos para a vigésima quarta pergunta. \n\n | TECLE ENTER PARA CONTINUAR | \n"))

    def RESPOSTAS_PERGUNTA_24_bloco_5():
        global Ajuda_da_pessoas
        global Ajuda_dos_Universitarios

        while True:
            pergunta_24_resposta = input("🎤 PERGUNTA 24: Qual foi o nome do líder do Quilombo dos Palmares, um dos maiores quilombos do Brasil? : \n\n Alternativa (A) Zumbi dos Palmares \n Alternativa (B) Tiradentes \n Alternativa (C) Lampião \n Alternativa (D) Dom Pedro II \n\n | DIGITE [A/B/C/D] | \n | PLATEIA [P] | \n | UNIVERSITARIOS [U] | \n\n | DIGITE A ALTERNATIVA MAIS ENTER PARA CONTINUAR | \n\n 👤 ")
            # AJUDA DA PLATEIA
            if pergunta_24_resposta == "P" or pergunta_24_resposta == "p":
                if Ajuda_da_pessoas > 0:
                    Ajuda_da_pessoas -= 1

                    print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🥸  É Alternativa (A)! \n 🥸  Claro que é (A)! \n 🥸  Obvio que nao é (B)! \n\n")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                else:
                    print("\n❌ Você não possui mais ajuda da plateia!\n")
            # AJUDA DOS UNIVERSITARIOS
            elif pergunta_24_resposta == "U" or pergunta_24_resposta == "u":
                if Ajuda_dos_Universitarios > 0:
                    Ajuda_dos_Universitarios -= 1

                    print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (A) \n\n ")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                else:
                    print("\n❌ Você não possui mais ajuda dos universitários!\n")
            # RESPOSTA CERTA
            elif pergunta_24_resposta == "A" or pergunta_24_resposta == "a":

                print("\n✅ CORRETA!")
                print("💵 Você ganhou 40,000 reais!\n")
                break
            # RESPOSTAS ERRADAS
            elif pergunta_24_resposta in ["B", "C", "D"]:
                print("\n❌ ERRADA!")
                print("💀 Você perdeu tudo!\n")
                exit()
            else:
                print("\n❌ Resposta inválida!\n")
                exit()

    RESPOSTAS_PERGUNTA_24_bloco_5()
    print (input("\n 🎤 Parabéns " + nome_usuario + ", você acertou a vigésima quarta pergunta e já tem 💵 465,000 reais acumulados! \n\n | TECLE ENTER PARA CONTINUAR | \n"))

    print (input(" 🎤 Agora vamos para a vigésima quinta pergunta. \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    def RESPOSTAS_PERGUNTA_25_bloco_5():
        global Ajuda_da_pessoas
        global Ajuda_dos_Universitarios

        while True:
            pergunta_25_resposta = input("🎤 PERGUNTA 25: Qual foi o nome da lei que proibiu o tráfico de escravos para o Brasil? : \n\n Alternativa (A) Lei Eusébio de Queirós \n Alternativa (B) Lei do Ventre Livre \n Alternativa (C) Lei dos Sexagenários \n Alternativa (D) Lei da Liberdade \n\n | DIGITE [A/B/C/D] | \n | PLATEIA [P] | \n | UNIVERSITARIOS [U] | \n\n | DIGITE A ALTERNATIVA MAIS ENTER PARA CONTINUAR | \n\n 👤 ")
            # AJUDA DA PLATEIA
            if pergunta_25_resposta == "P" or pergunta_25_resposta == "p":
                if Ajuda_da_pessoas > 0:
                    Ajuda_da_pessoas -= 1

                    print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🥸  É Alternativa (A)! \n 🥸  Claro que é (A)! \n 🥸  Obvio que nao é (B)! \n\n")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                else:
                    print("\n❌ Você não possui mais ajuda da plateia!\n")
            # AJUDA DOS UNIVERSITARIOS
            elif pergunta_25_resposta == "U" or pergunta_25_resposta == "u":
                if Ajuda_dos_Universitarios > 0:
                    Ajuda_dos_Universitarios -= 1

                    print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (A) \n\n ")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                else:
                    print("\n❌ Você não possui mais ajuda dos universitários!\n")
            # RESPOSTA CERTA
            elif pergunta_25_resposta == "A" or pergunta_25_resposta == "a":

                print("\n✅ CORRETA!")
                print("💵 Você ganhou 40,000 reais!\n")
                break
            # RESPOSTAS ERRADAS
            elif pergunta_25_resposta in ["B", "C", "D"]:
                print("\n❌ ERRADA!")
                print("💀 Você perdeu tudo!\n")
                exit()
            else:
                print("\n❌ Resposta inválida!\n")
                exit()

    RESPOSTAS_PERGUNTA_25_bloco_5()
    print (input("\n 🎤 Parabéns " + nome_usuario + ", você acertou a vigésima quinta pergunta e já tem 💵 505,000 reais acumulados! \n\n | TECLE ENTER PARA CONTINUAR | \n"))

    print (input(" 🎤 Agora vamos para a Temida e Grande Ultima Pergunta Do Milhão 💀💀💀 . \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    print (input(" 🎤 Se acertar essa pergunta, você ganhará 1 milhão de reais, mas se errar, perderá tudo! \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    print (input(" 🎤 Está preparado para a última pergunta? Voce pode para ou continuar ou desistir. QUER CONTINUAR? OU PARAR? \n\n |  | \n\n 👤 "))
    if input("🎤 DIGITE [P] PARA PARAR OU [C] PARA CONTINUAR \n\n 👤 ") in ["P", "p"]:
        print(input("\n Quero Parar e ficar com o dinheiro que acumulei."))
        exit()
    else:    print(input("\n 🎤 Você escolheu continuar, vamos para a última pergunta. \n\n | TECLE ENTER PARA CONTINUAR | \n"))


    def RESPOSTAS_PERGUNTA_26_bloco_5():
        global Ajuda_da_pessoas
        global Ajuda_dos_Universitarios

        while True:
            pergunta_26_resposta = input("🎤 PERGUNTA FINAL: Qual foi o líder religioso mais importante da Guerra do Contestado, considerado uma inspiração para muitos sertanejos? : \n\n Alternativa (A) Padre Cícero \n Alternativa (B) Antônio Conselheiro \n Alternativa (C) José Maria \n Alternativa (D) Frei Caneca \n\n | DIGITE [A/B/C/D] | \n | PLATEIA [P] | \n | UNIVERSITARIOS [U] | \n\n | DIGITE A ALTERNATIVA MAIS ENTER PARA CONTINUAR | \n\n 👤 ")
            # AJUDA DA PLATEIA
            if pergunta_26_resposta == "P" or pergunta_26_resposta == "p":
                if Ajuda_da_pessoas > 0:
                    Ajuda_da_pessoas -= 1

                    print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🥸  É Alternativa (B)! \n 🥸  Claro que é (B)! \n 🥸  Obvio que nao é (A)! \n\n")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                else:
                    print("\n❌ Você não possui mais ajuda da plateia!\n")
            # AJUDA DOS UNIVERSITARIOS
            elif pergunta_26_resposta == "U" or pergunta_26_resposta == "u":
                if Ajuda_dos_Universitarios > 0:
                    Ajuda_dos_Universitarios -= 1

                    print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | TECLE ENTER PARA CONTINUAR | "))
                    print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (B) \n\n ")
                    print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

                else:
                    print("\n❌ Você não possui mais ajuda dos universitários!\n")
            # RESPOSTA CERTA
            elif pergunta_26_resposta == "B" or pergunta_26_resposta == "b":
                print("\n✅ CORRETA!")
                print("💵 Você ganhou 1,000,000 reais!\n")
                break
            # RESPOSTAS ERRADAS
            elif pergunta_26_resposta in ["A", "C", "D"]:
                print("\n❌ ERRADA!")
                print("💀 Você perdeu tudo!\n")
                exit()
            else:
                print("\n❌ Resposta inválida!\n")
                exit()

    RESPOSTAS_PERGUNTA_26_bloco_5()
    print (input("\n 🎤 Parabéns " + nome_usuario + ", você acertou a última pergunta e ganhou 💵 1,000,000 de reais! \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    print (input(" 🎤 Você é um verdadeiro especialista em história do Brasil! \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    print (input(" 🎤 Obrigado por jogar o nosso Show do Milhão! \n\n | TECLE ENTER PARA CONTINUAR | \n"))
    print (input(" 🎤 Até a próxima! \n\n | TECLE ENTER PARA CONTINUAR | \n"))



# === ABERTURA DO JOGO ===
elif Máteria_selecionada == "5":

    Ajuda_d_plateia = 5
    Ajuda_dos_Uni = 3
    print("=== Bem-vindo ao SHOW DO MILHÃO ===")
    print("PREPARE-SE PARA TESTAR SEUS CONHECIMENTOS E CONCORRER AO PRÊMIO DE UM MILHÃO DE REAIS!\n")

    def obter_nome():
        nome = input("PARA DAR INÍCIO, DIGITE SEU NOME E APERTE ENTER PARA CONTINUAR: ")
        return nome

    # Chamamos a função e guardamos o nome do jogador na variável global
    nome_usuario = obter_nome()

    print(f"\n🎤 Seja bem-vindo, {nome_usuario}! Vamos às regras.")
    input("Pressione | ENTER | para ler as instruções...")

    # === REGRAS DO JOGO ===
    print("\n🎤 As Instruções do Jogo são as seguintes:")
    print("O Show será baseado na matéria de BIOLOGIA e dividido em 5 temas, do 😂 Mais Fácil até o 🤬 Mais Difícil.")
    print(f"Contém 25 perguntas divididas para os 5 temas, e você poderá pedir ajuda da:")
    print(f"🥸  Plateia ({Ajuda_d_plateia} vezes)")
    print(f"🎓 Universitários ({Ajuda_dos_Uni} vezes)")
    input("\nTODA VEZ QUE APARECER ESSE BOTÃO| ENTER |TERÁ QUE APERTAR ELE NO TECLADO,DEPOIS DE ESCREVER A ALTERNATIVA APERTA O ENTER")

    print("\n🎤 Cada pergunta certa gera uma recompensa!")
    print("A cada acerto o valor acumulado aumenta progressivamente rumo ao milhão.")
    print("Mas cuidado: se você errar, você perde o valor acumulado ou sai com uma fração dele!")
    input("\n| ENTER |")

    print("\n🎤 Seu Único Objetivo é responder todas as 25 Perguntas e tentar chegar ao 1 milhão.")
    print("\nMAS ATENÇÃO!!!")
    print("Se até o final da pergunta Número 25 você tiver acumulado o valor necessário, você terá direito a uma Pergunta Bônus chamada:")
    print("💀 ARRISCA TUDO 💀")
    print("Pergunta na qual se você acertar, leva seu 💵 Valor Acumulado ao Dobro 🤑")
    print("Mas se Errar, perde todo o 💵 Valor Acumulado 💀")
    input("\n| ENTER |")

    # Início da primeira rodada
    print(f"\n🎤 Agora que você já conhece as regras do jogo, vamos começar o SHOW DO MILHÃO, {nome_usuario}!")
    print("Vamos dar início ao primeiro Tema: Reconhecementoprocessos de divisão celular (Biologia) 🌿")
    input("\n| ENTER | para a primeira pergunta...\n")


    import sys

    def RESPOSTAS_f():
        global Ajuda_d_plateia
        global Ajuda_dos_Uni
        global nome_usuario

        while True:
            print("\nNÍVEL 1 - FÁCIL (QUESTÃO 1)")
            print("tema:DIVISÃO CELULAR") 
            print("1. O que a célula faz na divisão celular?")
            print("A) Dorme")
            print("B) Se divide")
            print("C) Corre")
            print("D) Nada")
            print("E) Canta")

            facil_1 = input("Qual das alternativas está correta? | PARA RESPONDER DIGITE [A/B/C/D/E] |\n"
                            "| PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] |\n"
                            "| PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] |\n\n"
                            "👤 ").strip().upper()

            if facil_1 == "P":
                if Ajuda_d_plateia > 0:
                    Ajuda_d_plateia -= 1
                    input("\n🎤 Você pediu a ajuda da Plateia: \nEles não têm certeza de qual seja a certa, então boa sorte! \n\n| ENTER | ")
                    print("🥸  É Alternativa (B)!")
                    print("🥸  Claro que é (D)!")
                    print("🥸  Óbvio que é (B)!\n")
                    input(f"🎤 {nome_usuario}, após receber a ajuda da Plateia: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n")
                    continue 
                else:
                    input("\n⚠️ Você não tem mais ajudas da Plateia disponíveis! \n\n| ENTER | ")
                    continue

            elif facil_1 == "U":
                if Ajuda_dos_Uni > 0:
                    Ajuda_dos_Uni -= 1
                    input("\n🎤 Você pediu a ajuda dos Universitários: \nVeja o que eles dirão \n\n| ENTER | ")
                    print("🎓  Temos certeza de que todas estão erradas \n🎓  Menos a alternativa (B)\n")
                    input(f"🎤 {nome_usuario}, após receber a ajuda dos Universitários: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n")
                    continue 
                else:
                    input("\n⚠️ Você não tem mais ajudas dos Universitários disponíveis! \n\n| ENTER | ")
                    continue
            
            elif facil_1 == "B":
                print("🎤 Você acha que é 'Se divide'... SUA RESPOSTA ESTÁ EEEEEEE....| ENTER ")
                print("✅ EXATA, Parabéns você acaba de ganhar 💵 1000,00")
                return True

            else:
                print("Sua resposta está eeeeee....❌ERRADA❌ | ENTER ")
                print("Você ganhou o total de 💵 0,00")
                sys.exit()


    def RESPOSTAS_F2():
        global Ajuda_d_plateia
        global Ajuda_dos_Uni
        global nome_usuario

        while True:
            print("\nNÍVEL 1 - FÁCIL (QUESTÃO 2)")
            print("tema:DIVISÃO CELULAR") 
            print("2. A mitose forma quantas células?")
            print("A) 1")
            print("B) 2")
            print("C) 3")
            print("D) 4")
            print("E) 5")

            facil_2 = input("Qual das alternativas está correta? | PARA RESPONDER DIGITE [A/B/C/D/E] |\n"
                            "| PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] |\n"
                            "| PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] |\n\n"
                            "👤 ").strip().upper()

            if facil_2 == "P":
                if Ajuda_d_plateia > 0:
                    Ajuda_d_plateia -= 1
                    input("\n🎤 Você pediu a ajuda da Plateia: \nEles não têm certeza de qual seja a certa, então boa sorte! \n\n| ENTER | ")
                    print("🥸  É Alternativa (B)!")
                    print("🥸  Claro que é (D)!")
                    print("🥸  Óbvio que é (B)!\n")
                    input(f"🎤 {nome_usuario}, após receber a ajuda da Plateia: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n")
                    continue 
                else:
                    input("\n⚠️ Você não tem mais ajudas da Plateia disponíveis! \n\n| ENTER | ")
                    continue

            elif facil_2 == "U":
                if Ajuda_dos_Uni > 0:
                    Ajuda_dos_Uni -= 1
                    input("\n🎤 Você pediu a ajuda dos Universitários: \nVeja o que eles dirão \n\n| ENTER | ")
                    print("🎓  Temos certeza de que todas estão erradas \n🎓  Menos a alternativa (B)\n")
                    input(f"🎤 {nome_usuario}, após receber a ajuda dos Universitários: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n")
                    continue 
                else:
                    input("\n⚠️ Você não tem mais ajudas dos Universitários disponíveis! \n\n| ENTER | ")
                    continue
            
            elif facil_2 == "B":
                print("🎤 Você acha que é '2'... SUA RESPOSTA ESTÁ EEEEEEE....| ENTER ")
                print("✅ EXATA, Parabéns você acaba de ganhar 💵 2000,00")
                return True

            else:
                print("Sua resposta está eeeeee....❌ERRADA❌ | ENTER ")
                print("Você ganhou o total de 💵 0,00")
                sys.exit()


    def RESPOSTAS_F3():
        global Ajuda_d_plateia
        global Ajuda_dos_Uni
        global nome_usuario

        while True:
            print("\nNÍVEL 1 - FÁCIL (QUESTÃO 3)")
            print("tema:DIVISÃO CELULAR") 
            print("3. A divisão celular ajuda o corpo a:")
            print("A) Crescer")
            print("B) Voar")
            print("C) Nadar")
            print("D) Falar")
            print("E) Ouvir")

            facil_3 = input("Qual das alternativas está correta? | PARA RESPONDER DIGITE [A/B/C/D/E] |\n"
                            "| PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] |\n"
                            "| PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] |\n\n"
                            "👤 ").strip().upper()
            
            if facil_3 == "P":
                if Ajuda_d_plateia > 0:
                    Ajuda_d_plateia -= 1
                    input("\n🎤 Você pediu a ajuda da Plateia: \nEles não têm certeza de qual seja a certa, então boa sorte! \n\n| ENTER | ")
                    print("🥸  É Alternativa (A)!")
                    print("🥸  Claro que é (C)!")
                    print("🥸  Óbvio que é (A)!\n")
                    input(f"🎤 {nome_usuario}, após receber a ajuda da Plateia: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n")
                    continue 
                else:
                    input("\n⚠️ Você não tem mais ajudas da Plateia disponíveis! \n\n| ENTER | ")
                    continue

            elif facil_3 == "U":
                if Ajuda_dos_Uni > 0:
                    Ajuda_dos_Uni -= 1
                    input("\n🎤 Você pediu a ajuda dos Universitários: \nVeja o que eles dirão \n\n| ENTER | ")
                    print("🎓  Temos certeza de que todas estão erradas \n🎓  Menos a alternativa (A)\n")
                    input(f"🎤 {nome_usuario}, após receber a ajuda dos Universitários: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n")
                    continue 
                else:
                    input("\n⚠️ Você não tem mais ajudas dos Universitários disponíveis! \n\n| ENTER | ")
                    continue
            
            elif facil_3 == "A":
                print("🎤 Você acha que é 'Crescer'... sua resposta está eeeeeeee....| ENTER ")
                print("✅ EXATA ✔, Parabéns você acaba de ganhar 💵 3.000,00 ")
                return True

            else:
                print("Sua resposta está eeee.....| ENTER ")
                print("❌ ERRADA ❌, VOCÊ PERDEU TODO O DINHEIRO 00,00")
                sys.exit()


    def RESPOSTAS_F4():
        global Ajuda_d_plateia
        global Ajuda_dos_Uni
        global nome_usuario

        while True:
            print("\nNÍVEL 1 - FÁCIL (QUESTÃO 4)")
            print("tema:DIVISÃO CELULAR") 
            print("4. Onde fica o DNA da célula?")
            print("A) Pé")
            print("B) Braço")
            print("C) Núcleo")
            print("D) Boca")
            print("E) Olho")

            facil_4 = input("Qual das alternativas está correta? | PARA RESPONDER DIGITE [A/B/C/D/E] |\n"
                            "| PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] |\n"
                            "| PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] |\n\n"
                            "👤 ").strip().upper()
            
            if facil_4 == "P":
                if Ajuda_d_plateia > 0:
                    Ajuda_d_plateia -= 1
                    input("\n🎤 Você pediu a ajuda da Plateia: \nEles não têm certeza de qual seja a certa, então boa sorte! \n\n| ENTER | ")
                    print("🥸  É Alternativa (C)!")
                    print("🥸  Claro que é (A)!")
                    print("🥸  Óbvio que é (C)!\n")
                    input(f"🎤 {nome_usuario}, após receber a ajuda da Plateia: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n")
                    continue 
                else:
                    input("\n⚠️ Você não tem mais ajudas da Plateia disponíveis! \n\n| ENTER | ")
                    continue

            elif facil_4 == "U":
                if Ajuda_dos_Uni > 0:
                    Ajuda_dos_Uni -= 1
                    input("\n🎤 Você pediu a ajuda dos Universitários: \nVeja o que eles dirão \n\n| ENTER | ")
                    print("🎓  Temos certeza de que todas estão erradas \n🎓  Menos a alternativa (C)\n")
                    input(f"🎤 {nome_usuario}, após receber a ajuda dos Universitários: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n")
                    continue 
                else:
                    input("\n⚠️ Você não tem mais ajudas dos Universitários disponíveis! \n\n| ENTER | ")
                    continue
            
            elif facil_4 == "C":
                print("🎤 Você acha que é 'Núcleo'... sua resposta está eeeeeeee....| ENTER ")
                print("✅ EXATA ✔, Parabéns você acaba de ganhar 💵 4.000,00 ")
                return True

            else:
                print("Sua resposta está eeee.....| ENTER ")
                print("❌ ERRADA ❌, VOCÊ PERDEU TODO O DINHEIRO 00,00")
                sys.exit()


    def RESPOSTAS_F5():
        global Ajuda_d_plateia
        global Ajuda_dos_Uni
        global nome_usuario

        while True:
            print("\nNÍVEL 1 - FÁCIL (QUESTÃO 5)")
            print("tema:DIVISÃO CELULAR") 
            print("5. Mitose é um tipo de:")
            print("A) Divisão celular")
            print("B) Esporte")
            print("C) Alimento")
            print("D) Planeta")
            print("E) Brinquedo")

            facil_5 = input("Qual das alternativas está correta? | PARA RESPONDER DIGITE [A/B/C/D/E] |\n"
                            "| PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] |\n"
                            "| PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] |\n\n"
                            "👤 ").strip().upper()
            
            if facil_5 == "P":
                if Ajuda_d_plateia > 0:
                    Ajuda_d_plateia -= 1
                    input("\n🎤 Você pediu a ajuda da Plateia: \nEles não têm certeza de qual seja a certa, então boa sorte! \n\n| ENTER | ")
                    print("🥸  É Alternativa (C)!")
                    print("🥸  Claro que é (A)!")
                    print("🥸  Óbvio que é (C)!\n")
                    input(f"🎤 {nome_usuario}, após receber a ajuda da Plateia: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n")
                    continue 
                else:
                    input("\n⚠️ Você não tem mais ajudas da Plateia disponíveis! \n\n| ENTER | ")
                    continue

            elif facil_5 == "U":
                if Ajuda_dos_Uni > 0:
                    Ajuda_dos_Uni -= 1
                    input("\n🎤 Você pediu a ajuda dos Universitários: \nVeja o que eles dirão \n\n| ENTER | ")
                    print("🎓  Temos certeza de que todas estão erradas \n🎓  Menos a alternativa (C)\n")
                    input(f"🎤 {nome_usuario}, após receber a ajuda dos Universitários: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n")
                    continue 
                else:
                    input("\n⚠️ Você não tem mais ajudas dos Universitários disponíveis! \n\n| ENTER | ")
                    continue
            
            elif facil_5 == "A":
                input("🎤 Você acha que é 'Divisão celular'... sua resposta está eeeeeeee....| ENTER ")
                print("✅ EXATA ✔, Parabéns você acaba de ganhar 💵 5.000,00 ")
                return True

            else:
                input("Sua resposta está eeee.....| ENTER ")
                print("❌ ERRADA ❌, VOCÊ PERDEU TODO O DINHEIRO 00,00")
                sys.exit()



    RESPOSTAS_f()
    RESPOSTAS_F2()
    RESPOSTAS_F3()
    RESPOSTAS_F4()
    RESPOSTAS_F5()

    def RESPOSTAS_M(): 
        global Ajuda_d_plateia 
        global Ajuda_dos_Uni 
        global nome_usuario 
        
        while True: 
            print("\nNÍVEL 2-MÉDIO") 
            print("tema:UNIDADES DE CONSERVAÇÃO") 
            print("O que são Unidades de Conservação?") 
            print("A) Áreas destinadas apenas à agricultura.") 
            print("B) Áreas protegidas para conservar a natureza.") 
            print("C) Áreas usadas somente para mineração.") 
            print("D) Áreas destinadas à construção de cidades.") 
            print("E) Áreas exclusivas para atividades industriais.") 
            
            medio_1 = input("Qual das alternativas está correta? | PARA RESPONDER DIGITE [A/B/C/D/E] |\n" 
                            "| PARA CHAMAR A 🥸 PLATEIA PRESSIONE [P] |\n" 
                            "| PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] |\n\n" 
                            "👤 ").strip().upper() 
            
            
            if medio_1 == "P": 
                if Ajuda_d_plateia > 0: 
                    Ajuda_d_plateia -= 1 
                    input("\n🎤 Você pediu a ajuda da Plateia: \nEles não têm certeza de qual seja a certa, então boa sorte! \n\n| ENTER | ") 
                    print("🥸 É Alternativa (B)!") 
                    print("🥸 Claro que é (A)!") 
                    print("🥸 Óbvio que é (B)!\n") 
                    input(f"🎤 {nome_usuario}, após receber a ajuda da Plateia: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n") 
                    continue 
                else: 
                    input("\n⚠️ Você não tem mais ajudas da Plateia disponíveis! \n\n| ENTER | ") 
                    continue 
                    
            elif medio_1 == "U": 
                if Ajuda_dos_Uni > 0: 
                    Ajuda_dos_Uni -= 1 
                    input("\n🎤 Você pediu a ajuda dos Universitários: \nVeja o que eles dirão \n\n| ENTER | ") 
                    print("🎓 Temos certeza de que todas estão erradas \n🎓 Menos a alternativa (B)\n") 
                    input(f"🎤 {nome_usuario}, após receber a ajuda dos Universitários: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n") 
                    continue 
                else: 
                    input("\n⚠️ Você não tem mais ajudas dos Universitários disponíveis! \n\n| ENTER | ") 
                    continue 
                    
            elif medio_1 == "B": 
                print("🎤Você acha que é Áreas protegidas para conservar a natureza, sua resposta eeeeeee...| ENTER") 
                print("✅ EXATA, Parabéns ganhou 10.000 reais") 
                break 
            else: 
                print("🎤 Sua resposta está eeeee...") 
                print("❌ ERRADA ❌, VOCÊ PERDEU TODO O DINHEIRO 00,00")
                sys.exit()

        
        

    def RESPOSTAS_M2 ():        

        while True:
            print("NÍVEL 2- MÉDIO")
            print("2. Qual é o principal objetivo das Unidades de Conservação?")
            print("A) Aumentar a produção industrial.")
            print("B) Proteger a biodiversidade e os recursos naturais.")
            print("C) Expandir as áreas urbanas.")
            print("D)Construir rodovias.")
            print("E) Incentivar o desmatamento.")

            medio_2 = input("Qual das alternativas está correta? | PARA RESPONDER DIGITE [A/B/C/D/E] |\n" 
                            "| PARA CHAMAR A 🥸 PLATEIA PRESSIONE [P] |\n" 
                            "| PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] |\n\n" 
                            "👤 ").strip().upper() 
            
            
            if medio_2 == "P": 
                if Ajuda_d_plateia > 0: 
                    Ajuda_d_plateia -= 1 
                    input("\n🎤 Você pediu a ajuda da Plateia: \nEles não têm certeza de qual seja a certa, então boa sorte! \n\n| ENTER | ") 
                    print("🥸 É Alternativa (B)!") 
                    print("🥸 Claro que é (A)!") 
                    print("🥸 Óbvio que é (B)!\n") 
                    input(f"🎤 {nome_usuario}, após receber a ajuda da Plateia: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n") 
                    continue 
                else: 
                    input("\n⚠️ Você não tem mais ajudas da Plateia disponíveis! \n\n| ENTER | ") 
                    continue 
                    
            elif medio_2 == "U": 
                if Ajuda_dos_Uni > 0: 
                    Ajuda_dos_Uni -= 1 
                    input("\n🎤 Você pediu a ajuda dos Universitários: \nVeja o que eles dirão \n\n| ENTER | ") 
                    print("🎓 Temos certeza de que todas estão erradas \n🎓 Menos a alternativa (B)\n") 
                    input(f"🎤 {nome_usuario}, após receber a ajuda dos Universitários: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n") 
                    continue 
                else: 
                    input("\n⚠️ Você não tem mais ajudas dos Universitários disponíveis! \n\n| ENTER | ") 
                    continue 
                    
            elif medio_2 == "B": 
                print("🎤Você acha que é Proteger a biodiversidade e os recursos naturais, sua resposta eeeeeee...| ENTER") 
                print("✅ EXATA, Parabéns ganhou 10.000 reais") 
                break 
            else: 
                print("🎤 Sua resposta está eeeee...") 
                print("❌ ERRADA ❌, VOCÊ PERDEU TODO O DINHEIRO 00,00")
                sys.exit()


    def RESPOSTAS_M3():
        global Ajuda_d_plateia
        global Ajuda_dos_Uni
        global nome_usuario

        while True:
            print("NÍVEL 2- MÉDIO")
            print("tema:UNIDADES DE CONSERVAÇÃO")
            print("A)Aeroporto")
            print("B)Parque Nacional")
            print("C)Shopping center")
            print("D)Fábrica")
            print("E)Estádio de futebol")

            medio_2 = input("Qual das alternativas está correta? | PARA RESPONDER DIGITE [A/B/C/D/E] |\n" 
                            "| PARA CHAMAR A 🥸 PLATEIA PRESSIONE [P] |\n" 
                            "| PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] |\n\n" 
                            "👤 ").strip().upper() 
            
            
            if medio_2 == "P": 
                if Ajuda_d_plateia > 0: 
                    Ajuda_d_plateia -= 1 
                    input("\n🎤 Você pediu a ajuda da Plateia: \nEles não têm certeza de qual seja a certa, então boa sorte! \n\n| ENTER | ") 
                    print("🥸 É Alternativa (B)!") 
                    print("🥸 Claro que é (A)!") 
                    print("🥸 Óbvio que é (B)!\n") 
                    input(f"🎤 {nome_usuario}, após receber a ajuda da Plateia: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n") 
                    continue 
                else: 
                    input("\n⚠️ Você não tem mais ajudas da Plateia disponíveis! \n\n| ENTER | ") 
                    continue 
                    
            elif medio_2 == "U": 
                if Ajuda_dos_Uni > 0: 
                    Ajuda_dos_Uni -= 1 
                    input("\n🎤 Você pediu a ajuda dos Universitários: \nVeja o que eles dirão \n\n| ENTER | ") 
                    print("🎓 Temos certeza de que todas estão erradas \n🎓 Menos a alternativa (B)\n") 
                    input(f"🎤 {nome_usuario}, após receber a ajuda dos Universitários: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n") 
                    continue 
                else: 
                    input("\n⚠️ Você não tem mais ajudas dos Universitários disponíveis! \n\n| ENTER | ") 
                    continue 
                    
            elif medio_2 == "B": 
                print("🎤Você acha que é Parque Nacional, sua resposta eeeeeee...| ENTER") 
                print("✅ EXATA, Parabéns ganhou 20.000 reais") 
                break 
            else: 
                print("🎤 Sua resposta está eeeee...") 
                print("❌ ERRADA ❌, VOCÊ PERDEU TODO O DINHEIRO 00,00")
                sys.exit()



    def RESPOSTAS_M4(): 
        global Ajuda_d_plateia 
        global Ajuda_dos_Uni 
        global nome_usuario 
        
        while True: 
            print("\nNÍVEL-MÉDIO - QUESTÃO 4") 
            print("tema:UNIDADES DE CONSERVAÇÃO") 
            print("As Unidades de Conservação ajudam a:") 
            print("A) Preservar animais e plantas.") 
            print("B) Aumentar a poluição.") 
            print("C) Destruir habitats naturais.") 
            print("D) Reduzir a quantidade de florestas.") 
            print("E) Incentivar a caça ilegal.") 
            
            medio_4 = input("Qual das alternativas está correta? | PARA RESPONDER DIGITE [A/B/C/D/E] |\n" 
                            "| PARA CHAMAR A 🥸 PLATEIA PRESSIONE [P] |\n" 
                            "| PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] |\n\n" 
                            "👤 ").strip().upper() 
            
            if medio_4 == "P": 
                if Ajuda_d_plateia > 0: 
                    Ajuda_d_plateia -= 1 
                    input("\n🎤 Você pediu a ajuda da Plateia: \nEles não têm certeza de qual seja a certa, então boa sorte! \n\n| ENTER | ") 
                    print("🥸 É Alternativa (A)!") 
                    print("🥸 Claro que é (C)!") 
                    print("🥸 Óbvio que é (A)!\n") 
                    input(f"🎤 {nome_usuario}, após receber a ajuda da Plateia: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n") 
                    continue 
                else: 
                    input("\n⚠️ Você não tem mais ajudas da Plateia disponíveis! \n\n| ENTER | ") 
                    continue 
                    
            elif medio_4 == "U": 
                if Ajuda_dos_Uni > 0: 
                    Ajuda_dos_Uni -= 1 
                    input("\n🎤 Você pediu a ajuda dos Universitários: \nVeja o que eles dirão \n\n| ENTER | ") 
                    print("🎓 Temos certeza de que todas estão erradas \n🎓 Menos a alternativa (A)\n") 
                    input(f"🎤 {nome_usuario}, após receber a ajuda dos Universitários: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n") 
                    continue 
                else: 
                    input("\n⚠️ Você não tem mais ajudas dos Universitários disponíveis! \n\n| ENTER | ") 
                    continue 
                    
            elif medio_4 == "A": 
                print("🎤Você acha que é Preservar animais e plantas sua resposta eeeeeee...| ENTER") 
                print("✅ EXATA, Parabéns ganhou 40.000 reais") 
                break 
                
            else: 
                print("🎤 Sua resposta está eeeee...") 
                print("❌ ERRADA ❌, VOCÊ PERDEU TODO O DINHEIRO 00,00")
                sys.exit()



    def RESPOSTAS_M5(): 
        global Ajuda_d_plateia 
        global Ajuda_dos_Uni 
        global nome_usuario 
        
        while True: 
            print("\nNÍVEL-MÉDIO - QUESTÃO 5") 
            print("tema:UNIDADES DE CONSERVAÇÃO") 
            print("Quem pode criar Unidades de Conservação no Brasil?") 
            print("A) Apenas empresas privadas.") 
            print("B) Apenas fazendeiros.") 
            print("C) Apenas turistas.") 
            print("D) O poder público (governo).") 
            print("E) Apenas escolas.") 
            
            medio_5 = input("Qual das alternativas está correta? | PARA RESPONDER DIGITE [A/B/C/D/E] |\n" 
                            "| PARA CHAMAR A 🥸 PLATEIA PRESSIONE [P] |\n" 
                            "| PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] |\n\n" 
                            "👤 ").strip().upper() 
            
            if medio_5 == "P": 
                if Ajuda_d_plateia > 0: 
                    Ajuda_d_plateia -= 1 
                    input("\n🎤 Você pediu a ajuda da Plateia: \nEles não têm certeza de qual seja a certa, então boa sorte! \n\n| ENTER | ") 
                    print("🥸 É Alternativa (D)!") 
                    print("🥸 Claro que é (A)!") 
                    print("🥸 Óbvio que é (D)!\n") 
                    input(f"🎤 {nome_usuario}, após receber a ajuda da Plateia: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n") 
                    continue 
                else: 
                    input("\n⚠️ Você não tem mais ajudas da Plateia disponíveis! \n\n| ENTER | ") 
                    continue 
                    
            elif medio_5 == "U": 
                if Ajuda_dos_Uni > 0: 
                    Ajuda_dos_Uni -= 1 
                    input("\n🎤 Você pediu a ajuda dos Universitários: \nVeja o que eles dirão \n\n| ENTER | ") 
                    print("🎓 Temos certeza de que todas estão erradas \n🎓 Menos a alternativa (D)\n") 
                    input(f"🎤 {nome_usuario}, após receber a ajuda dos Universitários: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n") 
                    continue 
                else: 
                    input("\n⚠️ Você não tem mais ajudas dos Universitários disponíveis! \n\n| ENTER | ") 
                    continue 
                    
            elif medio_5 == "D": 
                print("🎤Você acha que é O poder público (governo) sua resposta eeeeeee...| ENTER") 
                print("✅ EXATA, Parabéns ganhou 10.000 reais") 
                break 
                
            else: 
                print("🎤 Sua resposta está eeeee...") 
                print("❌ ERRADA ❌, VOCÊ PERDEU TODO O DINHEIRO 00,00")
                sys.exit()




    RESPOSTAS_M()
    RESPOSTAS_M2()
    RESPOSTAS_M3()
    RESPOSTAS_M4()
    RESPOSTAS_M5()

    # === DEFINIÇÃO DA FUNÇÃO DA PERGUNTA 1 ===
    def RESPOSTAS_PERGUNTA_1():
        global Ajuda_d_plateia
        global Ajuda_dos_Uni
        global nome_usuario

        while True:
            print("tema:RADIAÇÃO")
            print("PERGUNTA 1 - intermediário")
            print("Na área da medicina, a radiação é amplamente utilizada para dois fins principais. Quais são eles?\n"
                "A) Estética e musculação.\n"
                "B) Diagnóstico e tratamento de doenças.\n"
                "C) Higienização de ambientes e produção de remédios.\n"
                "D) Apenas para exames de rotina em atletas.\n")
            print("E)Apenas exames em idosos")

            pergunt_1 = input("Qual das alternativas está correta? | PARA RESPONDER DIGITE [A/B/C/D] |\n"
                            "| PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] |\n"
                            "| PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] |\n\n"
                            "👤 ").strip().upper()

            # ALTERNATIVA DE AJUDA: 🥸 PLATEIA 🥸
            if pergunt_1 == "P":
                if Ajuda_d_plateia > 0:
                    Ajuda_d_plateia -= 1
                    input("\n🎤 Você pediu a ajuda da Plateia: \nEles não têm certeza de qual seja a certa, então boa sorte! \n\n| ENTER | ")
                    print("🥸  É Alternativa (B)!")
                    print("🥸  Claro que é (A)!")
                    print("🥸  Óbvio que é (B)!\n")
                    input(f"🎤 {nome_usuario}, após receber a ajuda da Plateia: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n")
                    continue 
                else:
                    input("\n⚠️ Você não tem mais ajudas da Plateia disponíveis! \n\n| ENTER | ")
                    continue

            # ALTERNATIVA DE AJUDA: 🎓 UNIVERSITÁRIOS 🎓
            elif pergunt_1 == "U":
                if Ajuda_dos_Uni > 0:
                    Ajuda_dos_Uni -= 1
                    input("\n🎤 Você pediu a ajuda dos Universitários: \nVeja o que eles dirão \n\n| ENTER | ")
                    print("🎓  Temos certeza de que todas estão erradas \n🎓  Menos a alternativa (B)\n")
                    input(f"🎤 {nome_usuario}, após receber a ajuda dos Universitários: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n")
                    continue 
                else:
                    input("\n⚠️ Você não tem mais ajudas dos Universitários disponíveis! \n\n| ENTER | ")
                    continue

            # ALTERNATIVA A (❌ ERRADA ❌)
            elif pergunt_1 == "A":
                input(f"\n🎤 {nome_usuario}, você acha que a resposta é Estética e musculação, sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ❌ errada ❌ \nVocê não ganhou nada  💵 0,00!!! 🫵  😂 \n\n| ENTER | \n")
                sys.exit()

            # ALTERNATIVA B (✅ CORRETA ✅)
            elif pergunt_1 == "B":
                input(f"\n🎤 {nome_usuario}, você acha que a resposta é Diagnóstico e tratamento de doenças, sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ✅ exata ✅ \nVocê acaba de receber 💵 70.000,00!!! \n\n| ENTER | \n")
                return True 

            # ALTERNATIVA C (❌ ERRADA ❌)
            elif pergunt_1 == "C":
                input(f"\n🎤 {nome_usuario}, você acha que a resposta é Higienização e remédios, sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ❌ errada ❌ \nVocê não ganhou nada  💵 0,00!!! 🫵  😂 \n\n| ENTER | \n")
                sys.exit()

            # ALTERNATIVA D (❌ ERRADA ❌)
            elif pergunt_1 == "D":
                input(f"\n🎤 {nome_usuario}, você acha que a resposta é apenas exames em atletas, sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ❌ errada ❌ \nVocê não ganhou nada  💵 0,00!!! 🫵  😂 \n\n| ENTER | \n")
                sys.exit()


            elif pergunt_1 == "E":
                input(f"\n🎤 {nome_usuario}, você acha que a resposta é apenas exames em idosos, sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ❌ errada ❌ \nVocê não ganhou nada  💵 0,00!!! 🫵  😂 \n\n| ENTER | \n")
                sys.exit()
                    
            else:
                input("\n⚠️ Opção inválida! Digite A, B, C, D, P ou U. \n\n| ENTER | ")



    def RESPOSTAS_PERGUNTA_2():
        global Ajuda_d_plateia
        global Ajuda_dos_Uni
        global nome_usuario 

        while True:
            print("PERGUNTA 2- intermediário")
            print("\nQual dos itens abaixo é um exemplo de exame de diagnóstico por imagem que utiliza radiação?" \
            "\nA) Radioterapia." \
            "\nB) Fisioterapia." \
            "\nC) Mamografia." \
            "\nD) Hemograma.")
            print("E)Radio laser")
            pergunt_2 = input("Qual das alternativas está correta? | PARA RESPONDER DIGITE [A/B/C/D] |\n"
                            "| PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] |\n"
                            "| PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] |\n\n"
                            "👤 ").strip().upper()
            # ALTERNATIVA DE AJUDA: 🥸 PLATEIA 🥸
            if pergunt_2 == "P":
                if Ajuda_d_plateia > 0:
                    Ajuda_d_plateia -= 1
                    input("\n🎤 Você pediu a ajuda da Plateia: \nEles não têm certeza de qual seja a certa, então boa sorte! \n\n| ENTER | ")
                    print("🥸  É Alternativa (C)!")
                    print("🥸  Claro que é (D)!")
                    print("🥸  Óbvio que é (C)!\n")
                    input(f"🎤 {nome_usuario}, após receber a ajuda da Plateia: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n")
                    continue 
                else:
                    input("\n⚠️ Você não tem mais ajudas da Plateia disponíveis! \n\n| ENTER | ")
                    continue

            # ALTERNATIVA DE AJUDA: 🎓 UNIVERSITÁRIOS 🎓
            elif pergunt_2 == "U":
                if Ajuda_dos_Uni > 0:
                    Ajuda_dos_Uni -= 1
                    input("\n🎤 Você pediu a ajuda dos Universitários: \nVeja o que eles dirão \n\n| ENTER | ")
                    print("🎓  Temos certeza de que todas estão erradas \n🎓  Menos a alternativa (C)\n")
                    input(f"🎤 {nome_usuario}, após receber a ajuda dos Universitários: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n")
                    continue 
                else:
                    input("\n⚠️ Você não tem mais ajudas dos Universitários disponíveis! \n\n| ENTER | ")
                    continue
            
            # ALTERNATIVA A (❌ ERRADA ❌)
            elif pergunt_2 == "A":
                input(f"\n🎤 {nome_usuario},Você acha que é Radioterapia ... sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ❌ errada ❌ \nVocê não ganhou nada  💵 0,00!!! 🫵  😂 \n\n| ENTER | \n")
                sys.exit() 

            # ALTERNATIVA B (❌ ERRADA ❌)
            elif pergunt_2 == "B":
                input(f"\n🎤 {nome_usuario},Você acha que é Fisioterapia... sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ❌ errada ❌ \nVocê não ganhou nada  💵 0,00!!! 🫵  😂 \n\n| ENTER | \n")
                sys.exit()

            # ALTERNATIVA C (✅ CORRETA ✅)
            elif pergunt_2== "C":
                input(f"\n🎤 {nome_usuario},Você acha que é Mamografia... sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ✅ exata ✅ \nVocê acaba de receber 💵 90.000,00!!! \n\n| ENTER | \n")
                return True 

            # ALTERNATIVA D (❌ ERRADA ❌)
            elif pergunt_2 == "D":
                input(f"\n🎤 {nome_usuario},Você acha que é Hemograma... sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ❌ errada ❌ \nVocê não ganhou nada  💵 0,00!!! 🫵  😂 \n\n| ENTER | \n")
                sys.exit()

            elif pergunt_2 == "E":
                input(f"\n🎤 {nome_usuario},Você acha que é radio laser... sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ❌ errada ❌ \nVocê não ganhou nada  💵 0,00!!! 🫵  😂 \n\n| ENTER | \n")
                sys.exit()    
                
            else:
                input("\n⚠️ Opção inválida! Digite A, B, C, D, P ou U. \n\n| ENTER | ")



    # === DEFINIÇÃO DA FUNÇÃO DA PERGUNTA 3 ===
    def RESPOSTAS_PERGUNTA_3 ():
        global Ajuda_d_plateia
        global Ajuda_dos_Uni
        global nome_usuario

        while True:
            print("PERGUNTA 3 - INTERMEDIÁRIO")
            print("\nOs efeitos da radiação ionizante no organismo humano não são iguais para todos. Quais fatores esses efeitos dependem?" \
            "\nA) Apenas da idade do paciente e do horário do exame." \
            "\nB) Da dose absorvida, do tempo, da frequência de exposição e da área irradiada." \
            "\nC) Somente da marca do equipamento utilizado no hospital." \
            "\nD) Do tipo sanguíneo e do peso do indivíduo.")
            print("E)Do tipo sanguíneo")

            pergunt_3 = input("Qual das alternativas está correta? | PARA RESPONDER DIGITE [A/B/C/D] |\n"
                            "| PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] |\n"
                            "| PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] |\n\n"
                            "👤 ").strip().upper()
            if pergunt_3 == "P":
                if Ajuda_d_plateia > 0:
                    Ajuda_d_plateia -= 1
                    input("\n🎤 Você pediu a ajuda da Plateia: \nEles não têm certeza de qual seja a certa, então boa sorte! \n\n| ENTER | ")
                    print("🥸  É Alternativa (B)!")
                    print("🥸  Claro que é (C)!")
                    print("🥸  Óbvio que é (D)!\n")
                    input(f"🎤 {nome_usuario}, após receber a ajuda da Plateia: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n")
                    continue 
                else:
                    input("\n⚠️ Você não tem mais ajudas da Plateia disponíveis! \n\n| ENTER | ")
                    continue

            # ALTERNATIVA DE AJUDA: 🎓 UNIVERSITÁRIOS 🎓
            elif pergunt_3 == "U":
                if Ajuda_dos_Uni > 0:
                    Ajuda_dos_Uni -= 1
                    input("\n🎤 Você pediu a ajuda dos Universitários: \nVeja o que eles dirão \n\n| ENTER | ")
                    print("🎓  Temos certeza de que todas estão erradas \n🎓  Menos a alternativa (B)\n")
                    input(f"🎤 {nome_usuario}, após receber a ajuda dos Universitários: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n")
                    continue 
                else:
                    input("\n⚠️ Você não tem mais ajudas dos Universitários disponíveis! \n\n| ENTER | ")
                    continue
        # ALTERNATIVA A (❌ ERRADA ❌)    
            elif pergunt_3 == "A":
                input(f"\n🎤 {nome_usuario},você acha que é apenas da idade do paciente e do horário do exame ... sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ❌ errada ❌ \nVocê não ganhou nada  💵 0,00!!! 🫵  😂 \n\n| ENTER | \n")
                sys.exit() 

        # ALTERNATIVA B (✅ CORRETA ✅)
            elif pergunt_3 == "B":
                input(f"\n🎤 {nome_usuario}, você acha que é da dose absorvida, do tempo, da frequência de exposição e da área irradiada ... sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ✅ exata ✅ \nVocê acaba de receber 💵110.000,00!!! \n\n| ENTER | \n")
                return True 

        # ALTERNATIVA C (❌ ERRADA ❌)    
            elif pergunt_3 == "C":
                input(f"\n🎤 {nome_usuario},você acha que é somente da marca do equipamento utilizado no hospital  ... sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ❌ errada ❌ \nVocê não ganhou nada  💵 0,00!!! 🫵  😂 \n\n| ENTER | \n")
                sys.exit() 
        
        # ALTERNATIVA D (❌ ERRADA ❌)    
            elif pergunt_3 == "D":
                input(f"\n🎤 {nome_usuario},você acha que é do tipo sanguíneo e do peso do indivíduo ... sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ❌ errada ❌ \nVocê não ganhou nada  💵 0,00!!! 🫵  😂 \n\n| ENTER | \n")
                sys.exit() 
            

            elif pergunt_3 == "E":
                input(f"\n🎤 {nome_usuario},você acha que é do tipo sanguíneo  ... sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ❌ errada ❌ \nVocê não ganhou nada  💵 0,00!!! 🫵  😂 \n\n| ENTER | \n")
                sys.exit() 
            
            else:
                input("\n⚠️ Opção inválida! Digite A, B, C, D, P ou U. \n\n| ENTER | ")


    # === DEFINIÇÃO DA FUNÇÃO DA PERGUNTA 4 ===
    def RESPOSTAS_PERGUNTAS_4():
        global Ajuda_d_plateia
        global Ajuda_dos_Uni
        global nome_usuario

        while True:
            print("PERGUNTA 4- intermediário")
            print("\nPara garantir a segurança em ambientes médicos e industriais onde existe radiação, são adotadas medidas preventivas. Quais são as principais precauções para reduzir os riscos de exposição?" \
            "\nA) Uso de equipamentos de proteção (EPIs), sinalização/monitoramento dos locais e realização de exames apenas quando necessário." \
            "\nB) Extinção total do uso de radiação em áreas urbanas e uso de roupas comuns." \
            "\nC) Realização de exames semanais para todos os profissionais, sem necessidade de proteção." \
            "\nD) Apenas o isolamento do paciente por 48 horas após qualquer tipo de raio-X.")
            print("Apenas o isolamento do paciente por 24 horas após qualquer tipo de raio-X")

            pergunt_4 = input("Qual das alternativas está correta? | PARA RESPONDER DIGITE [A/B/C/D] |\n"
                            "| PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] |\n"
                            "| PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] |\n\n"
                            "👤 ").strip().upper()
            if pergunt_4 == "P":
                if Ajuda_d_plateia > 0:
                    Ajuda_d_plateia -= 1
                    input("\n🎤 Você pediu a ajuda da Plateia: \nEles não têm certeza de qual seja a certa, então boa sorte! \n\n| ENTER | ")
                    print("🥸  É Alternativa (A)!")
                    print("🥸  Claro que é (C)!")
                    print("🥸  Óbvio que é (A)!\n")
                    input(f"🎤 {nome_usuario}, após receber a ajuda da Plateia: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n")
                    continue 
                else:
                    input("\n⚠️ Você não tem mais ajudas da Plateia disponíveis! \n\n| ENTER | ")
                    continue

            # ALTERNATIVA DE AJUDA: 🎓 UNIVERSITÁRIOS 🎓
            elif pergunt_4 == "U":
                if Ajuda_dos_Uni > 0:
                    Ajuda_dos_Uni -= 1
                    input("\n🎤 Você pediu a ajuda dos Universitários: \nVeja o que eles dirão \n\n| ENTER | ")
                    print("🎓  Temos certeza de que todas estão erradas \n🎓  Menos a alternativa (A)\n")
                    input(f"🎤 {nome_usuario}, após receber a ajuda dos Universitários: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n")
                    continue 
                else:
                    input("\n⚠️ Você não tem mais ajudas dos Universitários disponíveis! \n\n| ENTER | ")
                    continue 

        # ALTERNATIVA A (✅ CORRETA ✅)
            elif pergunt_4 == "A":
                input(f"\n🎤 {nome_usuario}, você acha que é do Uso de equipamentos de proteção (EPIs), sinalização/monitoramento dos locais e realização de exames apenas quando necessário ... sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ✅ exata ✅ \nVocê acaba de receber 💵 130.000,00!!! \n\n| ENTER | \n")
                return True 
            
        # ALTERNATIVA B (❌ ERRADA ❌)    
            elif pergunt_4 == "B":
                input(f"\n🎤 {nome_usuario},você acha que é Extinção total do uso de radiação em áreas urbanas e uso de roupas comuns ... sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ❌ errada ❌ \nVocê não ganhou nada  💵 0,00!!! 🫵  😂 \n\n| ENTER | \n")
                sys.exit() 

        # ALTERNATIVA C (❌ ERRADA ❌)    
            elif pergunt_4 == "C":
                input(f"\n🎤 {nome_usuario},você acha que é Realização de exames semanais para todos os profissionais, sem necessidade de proteção  ... sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ❌ errada ❌ \nVocê não ganhou nada  💵 0,00!!! 🫵  😂 \n\n| ENTER | \n")
                sys.exit() 
        
        # ALTERNATIVA D (❌ ERRADA ❌)    
            elif pergunt_4 == "D":
                input(f"\n🎤 {nome_usuario},você acha que é Apenas o isolamento do paciente por 48 horas após qualquer tipo de raio-X ... sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ❌ errada ❌ \nVocê não ganhou nada  💵 0,00!!! 🫵  😂 \n\n| ENTER | \n")
                sys.exit() 

            elif pergunt_4 == "E":
                input(f"\n🎤 {nome_usuario},você acha que é Apenas o isolamento do paciente por 24 horas após qualquer tipo de raio-X ... sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ❌ errada ❌ \nVocê não ganhou nada  💵 0,00!!! 🫵  😂 \n\n| ENTER | \n")
                sys.exit()    
            
            else:
                input("\n⚠️ Opção inválida! Digite A, B, C, D, P ou U. \n\n| ENTER | ")

        

    # === DEFINIÇÃO DA FUNÇÃO DA PERGUNTA 5 ===
    def RESPOSTAS_PERGUNTA_5():
        global Ajuda_d_plateia
        global Ajuda_dos_Uni
        global nome_usuario
        
        while True:
            print("PERGUNTA 5 - intermediário")
            print("\nSobre a dualidade entre os benefícios e os riscos da radiação assinale a alternativa que melhor define a gestão segura dessa tecnologia:\n"
                "A) O risco é nonexistent desde que a área irradiada seja apenas uma parte específica do corpo.\n"
                "B) A radiação deve ser evitada em qualquer circunstância, pois os danos biológicos são imediatos e irreversíveis, independentemente da dose.\n"
                "C) O uso seguro da radiação baseia-se em protocolos rigorosos, regulamentação constante e na minimização da exposição de profissionais e pacientes.\n"
                "D) A eficácia da radioterapia no tratamento do câncer elimina a necessidade de monitoramento de radiação em clínicas oncológicas.\n") 
            print("E)eficácia elimina a necessidade de maconha")

            pergunt_5 = input("Qual das alternativas está correta? | PARA RESPONDER DIGITE [A/B/C/D] |\n"
                            "| PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] |\n"
                            "| PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] |\n\n"
                            "👤 ").strip().upper()
            

            # ALTERNATIVA DE AJUDA: 🥸 PLATEIA 🥸
            if pergunt_5 == "P":
                if Ajuda_d_plateia > 0:
                    Ajuda_d_plateia -= 1
                    input("\n🎤 Você pediu a ajuda da Plateia: \nEles não têm certeza de qual seja a certa, então boa sorte! \n\n| ENTER | ")
                    print("🥸  É Alternativa (C)!")
                    print("🥸  Claro que é (B)!")
                    print("🥸  Óbvio que é (D)!\n")
                    input(f"🎤 {nome_usuario}, após receber a ajuda da Plateia: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n")
                    continue 
                else:
                    input("\n⚠️ Você não tem mais ajudas da Plateia disponíveis! \n\n| ENTER | ")
                    continue

            # ALTERNATIVA DE AJUDA: 🎓 UNIVERSITÁRIOS 🎓
            elif pergunt_5 == "U":
                if Ajuda_dos_Uni > 0:
                    Ajuda_dos_Uni -= 1
                    input("\n🎤 Você pediu a ajuda dos Universitários: \nVeja o que eles dirão \n\n| ENTER | ")
                    print("🎓  Temos certeza de que todas estão erradas \n🎓  Menos a alternativa (C)\n")
                    input(f"🎤 {nome_usuario}, após receber a ajuda dos Universitários: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n")
                    continue 
                else:
                    input("\n⚠️ Você não tem mais ajudas dos Universitários disponíveis! \n\n| ENTER | ")
                    continue

            # ALTERNATIVA A (❌ ERRADA ❌)
            elif pergunt_5 == "A":
                input(f"\n🎤 {nome_usuario}, você acha que o risco é inexistente dependendo da área do corpo... sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ❌ errada ❌ \nVocê não ganhou nada  💵 0,00!!! 🫵  😂 \n\n| ENTER | \n")
                sys.exit() 

            # ALTERNATIVA B (❌ ERRADA ❌)
            elif pergunt_5 == "B":
                input(f"\n🎤 {nome_usuario}, você acha que a radiação deve ser evitada em qualquer circunstância... sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ❌ errada ❌ \nVocê não ganhou nada  💵 0,00!!! 🫵  😂 \n\n| ENTER | \n")
                sys.exit()

            # ALTERNATIVA C (✅ CORRETA ✅)
            elif pergunt_5 == "C":
                input(f"\n🎤 {nome_usuario}, você acha que o uso seguro baseia-se em protocolos e minimização da exposição... sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ✅ exata ✅ \nVocê acaba de receber 💵 150.000,00!!! \n\n| ENTER | \n")
                return True 

            # ALTERNATIVA D (❌ ERRADA ❌)
            elif pergunt_5 == "D":
                input(f"\n🎤 {nome_usuario}, você acha que a eficácia elimina a necessidade de monitoramento... sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ❌ errada ❌ \nVocê não ganhou nada  💵 0,00!!! 🫵  😂 \n\n| ENTER | \n")
                sys.exit()
                

            elif pergunt_5 == "E":
                input(f"\n🎤 {nome_usuario}, você acha que a eficácia elimina a necessidade de maconha... sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ❌ errada ❌ \nVocê não ganhou nada  💵 0,00!!! 🫵  😂 \n\n| ENTER | \n")
                sys.exit()
                    
            else:
                input("\n⚠️ Opção inválida! Digite A, B, C, D, P ou U. \n\n| ENTER | ")


    # === EXECUÇÃO DO FLUXO DO JOGO ===
    # 1. Roda o bloco 1
    RESPOSTAS_PERGUNTA_1()
    RESPOSTAS_PERGUNTA_2()
    RESPOSTAS_PERGUNTA_3()
    RESPOSTAS_PERGUNTAS_4()
    RESPOSTAS_PERGUNTA_5()


    import os
    os.system('cls')

    def RESPOSTAS_d_1():
        global Ajuda_d_plateia
        global Ajuda_dos_Uni
        global nome_usuario

    while True:
        print("NÍVEL 4 - DIFÍCIL")
        print("\nQual é a principal diferença entre conservação e preservação ambiental?")
        print("\nA) Conservação permite o uso sustentável dos recursos naturais, enquanto preservação busca proteger áreas sem interferência humana significativa.")
        print("\nB) Conservação proíbe qualquer atividade humana, enquanto preservação permite exploração econômica.")
        print("\nC) Conservação e preservação possuem exatamente o mesmo significado.")
        print("\nD) Conservação é aplicada apenas a animais, enquanto preservação é aplicada apenas a plantas.")
        print("\nE) Conservação protege somente florestas, enquanto preservação protege rios.")
        
        dificil_1 = input("Qual das alternativas está correta? | PARA RESPONDER DIGITE [A/B/C/D/E] |\n"
                            "| PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] |\n"
                            "| PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] |\n\n"
                            "👤 ").strip().upper()

            # ALTERNATIVA DE AJUDA: 🥸 PLATEIA 🥸
        if dificil_1 == "P":
                if Ajuda_d_plateia > 0:
                    Ajuda_d_plateia -= 1
                    input("\n🎤 Você pediu a ajuda da Plateia: \nEles não têm certeza de qual seja a certa, então boa sorte! \n\n| ENTER | ")
                    print("🥸  É Alternativa (A)!")
                    print("🥸  Claro que é (B)!")
                    print("🥸  Óbvio que é (A)!\n")
                    input(f"🎤 {nome_usuario}, após receber a ajuda da Plateia: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n")
                    continue 
                else:
                    input("\n⚠️ Você não tem mais ajudas da Plateia disponíveis! \n\n| ENTER | ")
                    continue

            # ALTERNATIVA DE AJUDA: 🎓 UNIVERSITÁRIOS 🎓
        elif dificil_1 == "U":
                if Ajuda_dos_Uni > 0:
                    Ajuda_dos_Uni -= 1
                    input("\n🎤 Você pediu a ajuda dos Universitários: \nVeja o que eles dirão \n\n| ENTER | ")
                    print("🎓  Temos certeza de que todas estão erradas \n🎓  Menos a alternativa (A)\n")
                    input(f"🎤 {nome_usuario}, após receber a ajuda dos Universitários: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n")
                    continue 
                else:
                    input("\n⚠️ Você não tem mais ajudas dos Universitários disponíveis! \n\n| ENTER | ")
                    continue

            
                # ALTERNATIVA A (✅ CORRETA ✅)
        elif dificil_1 == "A":
            input(f"\n🎤 {nome_usuario}, você acha que a resposta é Diagnóstico e tratamento de doenças, sua resposta está eee...\n\n| ENTER | ")
            input("🎤 ✅ exata ✅ \nVocê acaba de receber 💵 180.000,00!!! \n\n| ENTER | \n")
            break
        
                # ALTERNATIVA B (❌ ERRADA ❌)
        elif dificil_1 == "B":  
            input(f"\n🎤 {nome_usuario}, você acha que a resposta é Conservação proíbe qualquer atividade humana, enquanto preservação permite exploração econômica, sua resposta está eee... \n\n| ENTER | ")
            input("🎤 ❌ Errada ❌ \nInfelizmente, essa não é a resposta correta. \n\n| ENTER | \n")
            sys.exit()
        
                # ALTERNATIVA C (❌ ERRADA ❌)
        elif dificil_1 == "C":                  
            input(f"\n🎤 {nome_usuario}, você acha que a resposta é Conservação e preservação possuem exatamente o mesmo significado, sua resposta está eee... \n\n| ENTER | ")
            input("🎤 ❌ Errada ❌ \nInfelizmente, essa não é a resposta correta. \n\n| ENTER | \n")
            sys.exit()
        
                # ALTERNATIVA D (❌ ERRADA ❌)          
        elif dificil_1 == "D":
            input(f"\n🎤 {nome_usuario}, você acha que a resposta é Conservação é aplicada apenas a animais, enquanto preservação é aplicada apenas a plantas, sua resposta está eee... \n\n| ENTER | ")
            input("🎤 ❌ Errada ❌ \nInfelizmente, essa não é a resposta correta. \n\n| ENTER | \n")
            sys.exit()
        
                # ALTERNATIVA E (❌ ERRADA ❌)
        elif dificil_1 == "E":
            input(f"\n🎤 {nome_usuario}, você acha que a resposta é Conservação protege somente florestas, enquanto preservação protege rios, sua resposta está eee... \n\n| ENTER | ")
            input("🎤 ❌ Errada ❌ \nInfelizmente, essa não é a resposta correta. \n\n| ENTER | \n")
            sys.exit()

        else:
            input("\n⚠️ Opção inválida! Por favor, escolha uma alternativa válida. \n\n| ENTER | \n")
            break



    def RESPOSTAS_d_2():
        global Ajuda_d_plateia
        global Ajuda_dos_Uni
        global nome_usuario


    while True:
        print("PERGUNTA 2-NÍVEL DIFÍCIL")
        print("2. A criação de corredores ecológicos tem como principal objetivo:"
    "\nA) Facilitar a expansão de áreas urbanas."
    "\nB) Aumentar a exploração de recursos naturais."
    "\nC) Conectar habitats fragmentados, permitindo o deslocamento de espécies."
    "\nD) Substituir unidades de conservação."
    "\nE) Impedir completamente a circulação de animais.")
        
        dificil_2 = input("Qual das alternativas está correta? | PARA RESPONDER DIGITE [A/B/C/D/E] |\n"
                            "| PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] |\n"
                            "| PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] |\n\n"
                            "👤 ").strip().upper()

            # ALTERNATIVA DE AJUDA: 🥸 PLATEIA 🥸
        if dificil_2 == "P":
                if Ajuda_d_plateia > 0:
                    Ajuda_d_plateia -= 1
                    input("\n🎤 Você pediu a ajuda da Plateia: \nEles não têm certeza de qual seja a certa, então boa sorte! \n\n| ENTER | ")
                    print("🥸  É Alternativa (C)!")
                    print("🥸  Claro que é (A)!")
                    print("🥸  Óbvio que é (C)!\n")
                    input(f"🎤 {nome_usuario}, após receber a ajuda da Plateia: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n")
                    continue 
                else:
                    input("\n⚠️ Você não tem mais ajudas da Plateia disponíveis! \n\n| ENTER | ")
                    continue

            # ALTERNATIVA DE AJUDA: 🎓 UNIVERSITÁRIOS 🎓
        elif dificil_2 == "U":
                if Ajuda_dos_Uni > 0:
                    Ajuda_dos_Uni -= 1
                    input("\n🎤 Você pediu a ajuda dos Universitários: \nVeja o que eles dirão \n\n| ENTER | ")
                    print("🎓  Temos certeza de que todas estão erradas \n🎓  Menos a alternativa (C)\n")
                    input(f"🎤 {nome_usuario}, após receber a ajuda dos Universitários: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n")
                    continue 
                else:
                    input("\n⚠️ Você não tem mais ajudas dos Universitários disponíveis! \n\n| ENTER | ")
                    continue

            
        # ALTERNATIVA A (❌ ERRADA ❌)
        elif dificil_2 == "A":                  
            input(f"\n🎤 {nome_usuario},Facilitar a expansão de áreas urbanas, sua resposta está eee... \n\n| ENTER | ")
            input("🎤 ❌ Errada ❌ \nInfelizmente, essa não é a resposta correta. \n\n| ENTER | \n")
            sys.exit()
        
                # ALTERNATIVA B (❌ ERRADA ❌)
        elif dificil_2 == "B":  
            input(f"\n🎤 {nome_usuario},  Aumentar a exploração de recursos naturais, enquanto preservação permite exploração econômica, sua resposta está eee... \n\n| ENTER | ")
            input("🎤 ❌ Errada ❌ \nInfelizmente, essa não é a resposta correta. \n\n| ENTER | \n")
            sys.exit()

            # ALTERNATIVA C (✅ CORRETA ✅)
        elif dificil_2 == "C":
            input(f"\n🎤 {nome_usuario},Conectar habitats fragmentados, permitindo o deslocamento de espécies , sua resposta está eee...\n\n| ENTER | ")
            input("🎤 ✅ exata ✅ \nVocê acaba de receber 💵 210.000,00!!! \n\n| ENTER | \n")
            break    
        
                # ALTERNATIVA D (❌ ERRADA ❌)          
        elif dificil_2 == "D":
            input(f"\n🎤 {nome_usuario}, Substituir unidades de conservação, enquanto preservação é aplicada apenas a plantas, sua resposta está eee... \n\n| ENTER | ")
            input("🎤 ❌ Errada ❌ \nInfelizmente, essa não é a resposta correta. \n\n| ENTER | \n")
            sys.exit()
        
                # ALTERNATIVA E (❌ ERRADA ❌)
        elif dificil_2 == "E":
            input(f"\n🎤 {nome_usuario},Impedir completamente a circulação de animais, enquanto preservação protege rios, sua resposta está eee... \n\n| ENTER | ")
            input("🎤 ❌ Errada ❌ \nInfelizmente, essa não é a resposta correta. \n\n| ENTER | \n")
            sys.exit()

        else:
            input("\n⚠️ Opção inválida! Por favor, escolha uma alternativa válida. \n\n| ENTER | \n")
            break


    def RESPOSTAS_d_3():
        global Ajuda_d_plateia
        global Ajuda_dos_Uni
        global nome_usuario

    while True:
        print("PERGUNTA 3-NÍVEL DIFÍCIL")
        print("tema:PREVENÇÃO E CONSERVAÇÃO")
        print("3. Qual das ações abaixo contribui diretamente para a conservação da biodiversidade?"
    "\nA) Introdução de espécies exóticas em ecossistemas naturais."
    "\nB) Desmatamento para expansão agrícola sem planejamento."
    "\nC) Uso sustentável dos recursos naturais e proteção dos habitats."
    "\nD) Caça indiscriminada de espécies silvestres."
    "\nE) Ocupação irregular de áreas protegidas")

        dificil_3 = input("Qual das alternativas está correta? | PARA RESPONDER DIGITE [A/B/C/D/E] |\n"
                            "| PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] |\n"
                            "| PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] |\n\n"
                            "👤 ").strip().upper()

            # ALTERNATIVA DE AJUDA: 🥸 PLATEIA 🥸
        if dificil_3 == "P":
                if Ajuda_d_plateia > 0:
                    Ajuda_d_plateia -= 1
                    input("\n🎤 Você pediu a ajuda da Plateia: \nEles não têm certeza de qual seja a certa, então boa sorte! \n\n| ENTER | ")
                    print("🥸  É Alternativa (C)!")
                    print("🥸  Claro que é (A)!")
                    print("🥸  Óbvio que é (C)!\n")
                    input(f"🎤 {nome_usuario}, após receber a ajuda da Plateia: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n")
                    continue 
                else:
                    input("\n⚠️ Você não tem mais ajudas da Plateia disponíveis! \n\n| ENTER | ")
                    continue

            # ALTERNATIVA DE AJUDA: 🎓 UNIVERSITÁRIOS 🎓
        elif dificil_3 == "U":
                if Ajuda_dos_Uni > 0:
                    Ajuda_dos_Uni -= 1
                    input("\n🎤 Você pediu a ajuda dos Universitários: \nVeja o que eles dirão \n\n| ENTER | ")
                    print("🎓  Temos certeza de que todas estão erradas \n🎓  Menos a alternativa (C)\n")
                    input(f"🎤 {nome_usuario}, após receber a ajuda dos Universitários: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n")
                    continue 
                else:
                    input("\n⚠️ Você não tem mais ajudas dos Universitários disponíveis! \n\n| ENTER | ")
                    continue

            
        # ALTERNATIVA A (❌ ERRADA ❌)
        elif dificil_3 == "A":                  
            input(f"\n🎤 {nome_usuario},Introdução de espécies exóticas em ecossistemas naturais, sua resposta está eee... \n\n| ENTER | ")
            input("🎤 ❌ Errada ❌ \nInfelizmente, essa não é a resposta correta. \n\n| ENTER | \n")
            sys.exit()
        
                # ALTERNATIVA B (❌ ERRADA ❌)
        elif dificil_3 == "B":  
            input(f"\n🎤 {nome_usuario},  Desmatamento para expansão agrícola sem planejamento, sua resposta está eee... \n\n| ENTER | ")
            input("🎤 ❌ Errada ❌ \nInfelizmente, essa não é a resposta correta. \n\n| ENTER | \n")
            sys.exit()

            # ALTERNATIVA C (✅ CORRETA ✅)
        elif dificil_3 == "C":
            input(f"\n🎤 {nome_usuario},Uso sustentável dos recursos naturais e proteção dos habitats, sua resposta está eee...\n\n| ENTER | ")
            input("🎤 ✅ exata ✅ \nVocê acaba de receber 💵 240.000,00!!! \n\n| ENTER | \n")
            break    
        
                # ALTERNATIVA D (❌ ERRADA ❌)          
        elif dificil_3 == "D":
            input(f"\n🎤 {nome_usuario},Caça indiscriminada de espécies silvestres, sua resposta está eee... \n\n| ENTER | ")
            input("🎤 ❌ Errada ❌ \nInfelizmente, essa não é a resposta correta. \n\n| ENTER | \n")
            sys.exit()
        
                # ALTERNATIVA E (❌ ERRADA ❌)
        elif dificil_3 == "E":
            input(f"\n🎤 {nome_usuario}, Ocupação irregular de áreas protegidas, sua resposta está eee... \n\n| ENTER | ")
            input("🎤 ❌ Errada ❌ \nInfelizmente, essa não é a resposta correta. \n\n| ENTER | \n")
            sys.exit()

        else:
            input("\n⚠️ Opção inválida! Por favor, escolha uma alternativa válida. \n\n| ENTER | \n")
            break


    def RESPOSTAS_d_4():
        global Ajuda_d_plateia
        global Ajuda_dos_Uni
        global nome_usuario

        while True:
            print("\n=== PERGUNTA 4 - NÍVEL DIFÍCIL ===")
            print(
                "4. As Unidades de Conservação são importantes porque:\n"
                "A) Eliminam a necessidade de educação ambiental.\n"
                "B) Garantem a proteção de ecossistemas e espécies, contribuindo para a manutenção da biodiversidade.\n"
                "C) Permitem a exploração ilimitada dos recursos naturais.\n"
                "D) Têm como único objetivo promover o turismo.\n"
                "E) Substituem todas as leis ambientais existentes."
            )

            dificil_4 = (
                input(
                    "\nQual das alternativas está correta? | PARA RESPONDER DIGITE [A/B/C/D/E] |\n"
                    "| PARA CHAMAR A 🥸 PLATEIA PRESSIONE [P] |\n"
                    "| PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] |\n\n"
                    "👤 "
                )
                .strip()
                .upper()
            )

            # ALTERNATIVA DE AJUDA: 🥸 PLATEIA
            if dificil_4 == "P":
                if Ajuda_d_plateia > 0:
                    Ajuda_d_plateia -= 1
                    input(
                        "\n🎤 Você pediu a ajuda da Plateia: \n"
                        "Eles não têm certeza de qual seja a certa, então boa sorte! \n\n"
                        "| ENTER | "
                    )
                    print("🥸 É Alternativa (B)!")
                    print("🥸 Claro que é (A)!")
                    print("🥸 Óbvio que é (B)!\n")
                    input(
                        f"🎤 {nome_usuario}, após receber a ajuda da Plateia: \n"
                        "| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n"
                    )
                    continue
                else:
                    input(
                        "\n⚠️ Você não tem mais ajudas da Plateia disponíveis! \n\n"
                        "| ENTER | "
                    )
                    continue

            # ALTERNATIVA DE AJUDA: 🎓 UNIVERSITÁRIOS
            elif dificil_4 == "U":
                if Ajuda_dos_Uni > 0:
                    Ajuda_dos_Uni -= 1
                    input(
                        "\n🎤 Você pediu a ajuda dos Universitários: \n"
                        "Veja o que eles dirão \n\n"
                        "| ENTER | "
                    )
                    print("🎓 Temos certeza de que todas estão erradas")
                    print("🎓 Menos a alternativa (B)\n")
                    input(
                        f"🎤 {nome_usuario}, após receber a ajuda dos Universitários: \n"
                        "| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n"
                    )
                    continue
                else:
                    input(
                        "\n⚠️ Você não tem mais ajudas dos Universitários disponíveis! \n\n"
                        "| ENTER | "
                    )
                    continue

            # ALTERNATIVA A (❌ ERRADA)
            elif dificil_4 == "A":
                input(
                    f"\n🎤 {nome_usuario}, 'Eliminam a necessidade de educação ambiental', sua resposta está eee... \n\n"
                    "| ENTER | "
                )
                input(
                    "🎤 ❌ Errada ❌ \n"
                    "Infelizmente, essa não é a resposta correta. \n\n"
                    "| ENTER | \n"
                )
                sys.exit()

            # ALTERNATIVA B (✅ CORRETA)
            elif dificil_4 == "B":
                input(
                    f"\n🎤 {nome_usuario}, 'Garantem a proteção de ecossistemas e espécies...', sua resposta está eee...\n\n"
                    "| ENTER | "
                )
                input(
                    "🎤 ✅ exata ✅ \n"
                    "Você acaba de receber 💵 270.000,00!!! \n\n"
                    "| ENTER | \n"
                )
                break  # Sai do loop e avança no jogo

            # ALTERNATIVA C (❌ ERRADA)
            elif dificil_4 == "C":
                input(
                    f"\n🎤 {nome_usuario}, 'Permitem a exploração ilimitada...', sua resposta está eee... \n\n"
                    "| ENTER | "
                )
                input(
                    "🎤 ❌ Errada ❌ \n"
                    "Infelizmente, essa não é a resposta correta. \n\n"
                    "| ENTER | \n"
                )
                sys.exit()

            # ALTERNATIVA D (❌ ERRADA)
            elif dificil_4 == "D":
                input(
                    f"\n🎤 {nome_usuario}, 'Têm como único objetivo promover o turismo', sua resposta está eee... \n\n"
                    "| ENTER | "
                )
                input(
                    "🎤 ❌ Errada ❌ \n"
                    "Infelizmente, essa não é a resposta correta. \n\n"
                    "| ENTER | \n"
                )
                sys.exit()

            # ALTERNATIVA E (❌ ERRADA)
            elif dificil_4 == "E":
                input(
                    f"\n🎤 {nome_usuario}, 'Substituem todas as leis ambientais existentes', sua resposta está eee... \n\n"
                    "| ENTER | "
                )
                input(
                    "🎤 ❌ Errada ❌ \n"
                    "Infelizmente, essa não é a resposta correta. \n\n"
                    "| ENTER | \n"
                )
                sys.exit()

        
            else:
                input(
                    "\n⚠️ Opção inválida! Por favor, escolha uma alternativa válida. \n\n"
                    "| ENTER | \n"
                )
                continue


    def RESPOSTAS_d_5():
        global Ajuda_d_plateia
        global Ajuda_dos_Uni
        global nome_usuario

        while True:
            print("\n=== PERGUNTA 5 - NÍVEL DIFÍCIL ===")
            print(
                "5. A preservação de nascentes e matas ciliares é importante porque:\n"
                "A) Reduz a disponibilidade de água para a população.\n"
                "B) Aumenta a erosão do solo e o assoreamento dos rios.\n"
                "C) Favorece apenas a reprodução de peixes.\n"
                "D) Contribui para a qualidade da água, proteção do solo e equilíbrio dos ecossistemas aquáticos.\n"
                "E) Impede totalmente a ocorrência de enchentes."
            )

            dificil_5 = (
                input(
                    "\nQual das alternativas está correta? | PARA RESPONDER DIGITE [A/B/C/D/E] |\n"
                    "| PARA CHAMAR A 🥸 PLATEIA PRESSIONE [P] |\n"
                    "| PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] |\n\n"
                    "👤 "
                )
                .strip()
                .upper()
            )

            # ALTERNATIVA DE AJUDA: 🥸 PLATEIA
            if dificil_5 == "P":
                if Ajuda_d_plateia > 0:
                    Ajuda_d_plateia -= 1
                    input(
                        "\n🎤 Você pediu a ajuda da Plateia: \n"
                        "Eles não têm certeza de qual seja a certa, então boa sorte! \n\n"
                        "| ENTER | "
                    )
                    print("🥸 É Alternativa (D)!")
                    print("🥸 Claro que é (B)!")
                    print("🥸 Óbvio que é (D)!\n")
                    input(
                        f"🎤 {nome_usuario}, após receber a ajuda da Plateia: \n"
                        "| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n"
                    )
                    continue
                else:
                    input(
                        "\n⚠️ Você não tem mais ajudas da Plateia disponíveis! \n\n"
                        "| ENTER | "
                    )
                    continue

            # ALTERNATIVA DE AJUDA: 🎓 UNIVERSITÁRIOS
            elif dificil_5 == "U":
                if Ajuda_dos_Uni > 0:
                    Ajuda_dos_Uni -= 1
                    input(
                        "\n🎤 Você pediu a ajuda dos Universitários: \n"
                        "Veja o que eles dirão \n\n"
                        "| ENTER | "
                    )
                    print("🎓 Temos certeza de que todas estão erradas")
                    print("🎓 Menos a alternativa (D)\n")
                    input(
                        f"🎤 {nome_usuario}, após receber a ajuda dos Universitários: \n"
                        "| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n"
                    )
                    continue
                else:
                    input(
                        "\n⚠️ Você não tem mais ajudas dos Universitários disponíveis! \n\n"
                        "| ENTER | "
                    )
                    continue

            # ALTERNATIVA A (❌ ERRADA)
            elif dificil_5 == "A":
                input(
                    f"\n🎤 {nome_usuario}, 'Reduz a disponibilidade de água para a população', sua resposta está eee... \n\n"
                    "| ENTER | "
                )
                input(
                    "🎤 ❌ Errada ❌ \n"
                    "Infelizmente, essa não é a resposta correta. \n\n"
                    "| ENTER | \n"
                )
                sys.exit()

            # ALTERNATIVA B (❌ ERRADA)
            elif dificil_5 == "B":
                input(
                    f"\n🎤 {nome_usuario}, 'Aumenta a erosão do solo e o assoreamento dos rios', sua resposta está eee... \n\n"
                    "| ENTER | "
                )
                input(
                    "🎤 ❌ Errada ❌ \n"
                    "Infelizmente, essa não é a resposta correta. \n\n"
                    "| ENTER | \n"
                )
                sys.exit()

            # ALTERNATIVA C (❌ ERRADA)
            elif dificil_5 == "C":
                input(
                    f"\n🎤 {nome_usuario}, 'Favorece apenas a reprodução de peixes', sua resposta está eee... \n\n"
                    "| ENTER | "
                )
                input(
                    "🎤 ❌ Errada ❌ \n"
                    "Infelizmente, essa não é a resposta correta. \n\n"
                    "| ENTER | \n"
                )
                sys.exit()

            # ALTERNATIVA D (✅ CORRETA)
            elif dificil_5 == "D":
                input(
                    f"\n🎤 {nome_usuario}, 'Contribui para a qualidade da água, proteção do solo e equilíbrio...', sua resposta está eee...\n\n"
                    "| ENTER | "
                )
                input(
                    "🎤 ✅ exata ✅ \n"
                    "Você acaba de receber 💵 300.000!!! \n\n"
                    "| ENTER | \n"
                )
                break  # Passa para a próxima fase/pergunta do jogo

            # ALTERNATIVA E (❌ ERRADA)
            elif dificil_5 == "E":
                input(
                    f"\n🎤 {nome_usuario}, 'Impede totalmente a ocorrência de enchentes', sua resposta está eee... \n\n"
                    "| ENTER | "
                )
                input(
                    "🎤 ❌ Errada ❌ \n"
                    "Infelizmente, essa não é a resposta correta. \n\n"
                    "| ENTER | \n"
                )
                sys.exit()

            # Retorno de segurança para entradas incorretas
            else:
                input(
                    "\n⚠️ Opção inválida! Por favor, escolha uma alternativa válida. \n\n"
                    "| ENTER | \n"
                )
                continue


        
    RESPOSTAS_d_1()
    RESPOSTAS_d_2()
    RESPOSTAS_d_3()
    RESPOSTAS_d_4()
    RESPOSTAS_d_5()



    def RESPOSTAS_ULT_1():
        global Ajuda_d_plateia
        global Ajuda_dos_Uni
        global nome_usuario


    while True:
        print("======NÍVEL 5- ULTRA DÍFICIL======")
        print("tema: RADIAÇÃO SOLAR")
        print("A exposição excessiva à radiação UV-B está associada ao aumento do risco de câncer de pele porque essa radiação: \n"
    "A) Provoca desnaturação imediata da melanina presente na epiderme.\n"
    "B) Estimula exclusivamente a apoptose de queratinócitos sem afetar o DNA.\n"
    "C) Induz a formação de dímeros de pirimidina no DNA, podendo gerar mutações durante a replicação celular.\n"
    "D) Destrói diretamente os ribossomos das células da derme.\n"
    "E) Impede a síntese de proteínas envolvidas na resposta inflamatória.\n")

        
        ult_1 = input("Qual das alternativas está correta? | PARA RESPONDER DIGITE [A/B/C/D/E] |\n"
                            "| PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] |\n"
                            "| PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] |\n\n"
                            "👤 ").strip().upper()

            # ALTERNATIVA DE AJUDA: 🥸 PLATEIA 🥸
        if ult_1 == "P":
                if Ajuda_d_plateia > 0:
                    Ajuda_d_plateia -= 1
                    input("\n🎤 Você pediu a ajuda da Plateia: \nEles não têm certeza de qual seja a certa, então boa sorte! \n\n| ENTER | ")
                    print("🥸  É Alternativa (C)!")
                    print("🥸  Claro que é (A)!")
                    print("🥸  Óbvio que é (C)!\n")
                    input(f"🎤 {nome_usuario}, após receber a ajuda da Plateia: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n")
                    continue 
                else:
                    input("\n⚠️ Você não tem mais ajudas da Plateia disponíveis! \n\n| ENTER | ")
                    continue

            # ALTERNATIVA DE AJUDA: 🎓 UNIVERSITÁRIOS 🎓
        elif ult_1 == "U":
                if Ajuda_dos_Uni > 0:
                    Ajuda_dos_Uni -= 1
                    input("\n🎤 Você pediu a ajuda dos Universitários: \nVeja o que eles dirão \n\n| ENTER | ")
                    print("🎓  Temos certeza de que todas estão erradas \n🎓  Menos a alternativa (C)\n")
                    input(f"🎤 {nome_usuario}, após receber a ajuda dos Universitários: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n")
                    continue 
                else:
                    input("\n⚠️ Você não tem mais ajudas dos Universitários disponíveis! \n\n| ENTER | ")
                    continue

            
        # ALTERNATIVA A (❌ ERRADA ❌)
        elif ult_1 == "A":                  
            input(f"\n🎤 {nome_usuario}, Provoca desnaturação imediata da melanina presente na epiderme, sua resposta está eee... \n\n| ENTER | ")
            input("🎤 ❌ Errada ❌ \nInfelizmente, essa não é a resposta correta. \n\n| ENTER | \n")
            sys.exit()
        
                # ALTERNATIVA B (❌ ERRADA ❌)
        elif ult_1 == "B":  
            input(f"\n🎤 {nome_usuario}, Estimula exclusivamente a apoptose de queratinócitos sem afetar o DNA, sua resposta está eee... \n\n| ENTER | ")
            input("🎤 ❌ Errada ❌ \nInfelizmente, essa não é a resposta correta. \n\n| ENTER | \n")
            sys.exit()

            # ALTERNATIVA C (✅ CORRETA ✅)
        elif ult_1 == "C":
            input(f"\n🎤 {nome_usuario}, Induz a formação de dímeros de pirimidina no DNA, podendo gerar mutações durante a replicação celular, sua resposta está eee...\n\n| ENTER | ")
            input("🎤 ✅ exata ✅ \nVocê acaba de receber MAIS 💵340.000,00!!! \n\n| ENTER | \n")
            break    
        
                # ALTERNATIVA D (❌ ERRADA ❌)          
        elif ult_1 == "D":
            input(f"\n🎤 {nome_usuario},Destrói diretamente os ribossomos das células da derme, sua resposta está eee... \n\n| ENTER | ")
            input("🎤 ❌ Errada ❌ \nInfelizmente, essa não é a resposta correta. \n\n| ENTER | \n")
            sys.exit()
        
                # ALTERNATIVA E (❌ ERRADA ❌)
        elif ult_1 == "E":
            input(f"\n🎤 {nome_usuario},Impede a síntese de proteínas envolvidas na resposta inflamatória, sua resposta está eee... \n\n| ENTER | ")
            input("🎤 ❌ Errada ❌ \nInfelizmente, essa não é a resposta correta. \n\n| ENTER | \n")
            sys.exit()

        else:
            input("\n⚠️ Opção inválida! Por favor, escolha uma alternativa válida. \n\n| ENTER | \n")
            break



    def RESPOSTAS_ULT_2():
        global Ajuda_d_plateia
        global Ajuda_dos_Uni
        global nome_usuario

        while True:
            print("======NÍVEL 5- ULTRA DIFÍCIL======")
            print("tema: RADIAÇÃO SOLAR")
            print("A exposição excessiva à radiação UV-B está associada ao aumento do risco de câncer de pele porque essa radiação:\n"
    "A) Provoca desnaturação imediata da melanina presente na epiderme.\n"
    "B) Estimula exclusivamente a apoptose de queratinócitos sem afetar o DNA.\n"
    "C) Induz a formação de dímeros de pirimidina no DNA, podendo gerar mutações durante a replicação celular.\n"
    "D) Destrói diretamente os ribossomos das células da derme.\n"
    "E) Impede a síntese de proteínas envolvidas na resposta inflamatória.\n")
            
            ult_2 = input("Qual das alternativas está correta? | PARA RESPONDER DIGITE [A/B/C/D/E] |\n"
                            "| PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] |\n"
                            "| PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] |\n\n"
                            "👤 ").strip().upper()

            if ult_2 == "P":
                if Ajuda_d_plateia > 0:
                    Ajuda_d_plateia -= 1
                    input("\n🎤 Você pediu a ajuda da Plateia: \nEles não têm certeza de qual seja a certa, então boa sorte! \n\n| ENTER | ")
                    print("🥸  É Alternativa (C)!")
                    print("🥸  Claro que é (A)!")
                    print("🥸  Óbvio que é (C)!\n")
                    input(f"🎤 {nome_usuario}, após receber a ajuda da Plateia: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n")
                    continue 
                else:
                    input("\n⚠️ Você não tem mais ajudas da Plateia disponíveis! \n\n| ENTER | ")
                    continue

            elif ult_2 == "U":
                if Ajuda_dos_Uni > 0:
                    Ajuda_dos_Uni -= 1
                    input("\n🎤 Você pediu a ajuda dos Universitários: \nVeja o que eles dirão \n\n| ENTER | ")
                    print("🎓  Temos certeza de que todas estão erradas \n🎓  Menos a alternativa (C)\n")
                    input(f"🎤 {nome_usuario}, após receber a ajuda dos Universitários: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n")
                    continue 
                else:
                    input("\n⚠️ Você não tem mais ajudas dos Universitários disponíveis! \n\n| ENTER | ")
                    continue

            elif ult_2 == "A":                  
                input(f"\n🎤 {nome_usuario}, Provoca desnaturação imediata da melanina presente na epiderme, sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ❌ Errada ❌ \nInfelizmente, essa não é a resposta correta. \n\n| ENTER | \n")
                sys.exit()
        
            elif ult_2 == "B":  
                input(f"\n🎤 {nome_usuario}, Estimula exclusivamente a apoptose de queratinócitos sem afetar o DNA, sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ❌ Errada ❌ \nInfelizmente, essa não é a resposta correta. \n\n| ENTER | \n")
                sys.exit()

            elif ult_2 == "C":
                input(f"\n🎤 {nome_usuario}, Induz a formação de dímeros de pirimidina no DNA, podendo gerar mutações durante a replicação celular, sua resposta está eee...\n\n| ENTER | ")
                input("🎤 ✅ exata ✅ \nVocê acaba de receber 💵 R$ 380.000,00!!! \n\n| ENTER | \n")
                break    
                
            elif ult_2 == "D":
                input(f"\n🎤 {nome_usuario},Destrói diretamente os ribossomos das células da derme, sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ❌ Errada ❌ \nInfelizmente, essa não é a resposta correta. \n\n| ENTER | \n")
                sys.exit()
        
            elif ult_2 == "E":
                input(f"\n🎤 {nome_usuario},Impede a síntese de proteínas envolvidas na resposta inflamatória, sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ❌ Errada ❌ \nInfelizmente, essa não é a resposta correta. \n\n| ENTER | \n")
                sys.exit()

            else:
                input("\n⚠️ Opção inválida! Por favor, escolha uma alternativa válida. \n\n| ENTER | \n")
                break



    def RESPOSTAS_ULT_23():
        global Ajuda_d_plateia
        global Ajuda_dos_Uni
        global nome_usuario

        while True:
            print("======NÍVEL 5- ULTRA DIFÍCIL======")
            print("tema: RADIAÇÃO SOLAR")
            print("A exposição excessiva à radiação UV-B está associada ao aumento do risco de câncer de pele porque essa radiação: \n"
    "A) Provoca desnaturação imediata da melanina presente na epiderme.\n"
    "B) Estimula exclusivamente a apoptose de queratinócitos sem afetar o DNA.\n"
    "C) Induz a formação de dímeros de pirimidina no DNA, podendo gerar mutações durante a replicação celular.\n"
    "D) Destrói diretamente os ribossomos das células da derme.\n"
    "E) Impede a síntese de proteínas envolvidas na resposta inflamatória.\n")

            
            ult_23 = input("Qual das alternativas está correta? | PARA RESPONDER DIGITE [A/B/C/D/E] |\n"
                            "| PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] |\n"
                            "| PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] |\n\n"
                            "👤 ").strip().upper()

            if ult_23 == "P":
                if Ajuda_d_plateia > 0:
                    Ajuda_d_plateia -= 1
                    input("\n🎤 Você pediu a ajuda da Plateia: \nEles não têm certeza de qual seja a certa, então boa sorte! \n\n| ENTER | ")
                    print("🥸  É Alternativa (C)!")
                    print("🥸  Claro que é (A)!")
                    print("🥸  Óbvio que é (C)!\n")
                    input(f"🎤 {nome_usuario}, após receber a ajuda da Plateia: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n")
                    continue 
                else:
                    input("\n⚠️ Você não tem mais ajudas da Plateia disponíveis! \n\n| ENTER | ")
                    continue

            elif ult_23 == "U":
                if Ajuda_dos_Uni > 0:
                    Ajuda_dos_Uni -= 1
                    input("\n🎤 Você pediu a ajuda dos Universitários: \nVeja o que eles dirão \n\n| ENTER | ")
                    print("🎓  Temos certeza de que todas estão erradas \n🎓  Menos a alternativa (C)\n")
                    input(f"🎤 {nome_usuario}, após receber a ajuda dos Universitários: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n")
                    continue 
                else:
                    input("\n⚠️ Você não tem mais ajudas dos Universitários disponíveis! \n\n| ENTER | ")
                    continue

            elif ult_23 == "A":                  
                input(f"\n🎤 {nome_usuario}, Provoca desnaturação imediata da melanina presente na epiderme, sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ❌ Errada ❌ \nInfelizmente, essa não é a resposta correta. \n\n| ENTER | \n")
                sys.exit()
        
            elif ult_23 == "B":  
                input(f"\n🎤 {nome_usuario}, Estimula exclusivamente a apoptose de queratinócitos sem afetar o DNA, sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ❌ Errada ❌ \nInfelizmente, essa não é a resposta correta. \n\n| ENTER | \n")
                sys.exit()

            elif ult_23 == "C":
                input(f"\n🎤 {nome_usuario}, Induz a formação de dímeros de pirimidina no DNA, podendo gerar mutações durante a replicação celular, sua resposta está eee...\n\n| ENTER | ")
                input("🎤 ✅ exata ✅ \nVocê acaba de receber 💵 R$ 420.000,00!!! \n\n| ENTER | \n")
                break    
                
            elif ult_23 == "D":
                input(f"\n🎤 {nome_usuario},Destrói diretamente os ribossomos das células da derme, sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ❌ Errada ❌ \nInfelizmente, essa não é a resposta correta. \n\n| ENTER | \n")
                sys.exit()
        
            elif ult_23 == "E":
                input(f"\n🎤 {nome_usuario},Impede a síntese de proteínas envolvidas na resposta inflamatória, sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ❌ Errada ❌ \nInfelizmente, essa não é a resposta correta. \n\n| ENTER | \n")
                sys.exit()

            else:
                input("\n⚠️ Opção inválida! Por favor, escolha uma alternativa válida. \n\n| ENTER | \n")
                break



    def RESPOSTAS_ULT_24():
        global Ajuda_d_plateia
        global Ajuda_dos_Uni
        global nome_usuario

        while True:
            print("======NÍVEL 5- ULTRA DIFÍCIL======")
            print("tema: RADIAÇÃO SOLAR")
            print("A exposição excessiva à radiação UV-B está associada ao aumento do risco de câncer de pele porque essa radiação:\n"
    "A) Provoca desnaturação imediata da melanina presente na epiderme.\n"
    "B) Estimula exclusivamente a apoptose de queratinócitos sem afetar o DNA.\n"
    "C) Induz a formação de dímeros de pirimidina no DNA, podendo gerar mutações durante a replicação celular.\n"
    "D) Destrói diretamente os ribossomos das células da derme.\n"
    "E) Impede a síntese de proteínas envolvidas na resposta inflamatória.\n")

            
            ult_24 = input("Qual das alternativas está correta? | PARA RESPONDER DIGITE [A/B/C/D/E] |\n"
                            "| PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] |\n"
                            "| PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] |\n\n"
                            "👤 ").strip().upper()

            if ult_24 == "P":
                if Ajuda_d_plateia > 0:
                    Ajuda_d_plateia -= 1
                    input("\n🎤 Você pediu a ajuda da Plateia: \nEles não têm certeza de qual seja a certa, então boa sorte! \n\n| ENTER | ")
                    print("🥸  É Alternativa (C)!")
                    print("🥸  Claro que é (A)!")
                    print("🥸  Óbvio que é (C)!\n")
                    input(f"🎤 {nome_usuario}, após receber a ajuda da Plateia: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n")
                    continue 
                else:
                    input("\n⚠️ Você não tem mais ajudas da Plateia disponíveis! \n\n| ENTER | ")
                    continue

            elif ult_24 == "U":
                if Ajuda_dos_Uni > 0:
                    Ajuda_dos_Uni -= 1
                    input("\n🎤 Você pediu a ajuda dos Universitários: \nVeja o que eles dirão \n\n| ENTER | ")
                    print("🎓  Temos certeza de que todas estão erradas \n🎓  Menos a alternativa (C)\n")
                    input(f"🎤 {nome_usuario}, após receber a ajuda dos Universitários: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n")
                    continue 
                else:
                    input("\n⚠️ Você não tem mais ajudas dos Universitários disponíveis! \n\n| ENTER | ")
                    continue

            elif ult_24 == "A":                  
                input(f"\n🎤 {nome_usuario}, Provoca desnaturação imediata da melanina presente na epiderme, sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ❌ Errada ❌ \nInfelizmente, essa não é a resposta correta. \n\n| ENTER | \n")
                sys.exit()
        
            elif ult_24 == "B":  
                input(f"\n🎤 {nome_usuario}, Estimula exclusivamente a apoptose de queratinócitos sem afetar o DNA, sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ❌ Errada ❌ \nInfelizmente, essa não é a resposta correta. \n\n| ENTER | \n")
                sys.exit()

            elif ult_24 == "C":
                input(f"\n🎤 {nome_usuario}, Induz a formação de dímeros de pirimidina no DNA, podendo gerar mutações durante a replication celular, sua resposta está eee...\n\n| ENTER | ")
                input("🎤 ✅ exata ✅ \nVocê acaba de receber 💵 R$ 460.000,00!!! \n\n| ENTER | \n")
                break    
                
            elif ult_24 == "D":
                input(f"\n🎤 {nome_usuario},Destrói diretamente os ribossomos das células da derme, sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ❌ Errada ❌ \nInfelizmente, essa não é a resposta correta. \n\n| ENTER | \n")
                sys.exit()
        
            elif ult_24 == "E":
                input(f"\n🎤 {nome_usuario},Impede a síntese de proteínas envolvidas na resposta inflamatória, sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ❌ Errada ❌ \nInfelizmente, essa não é a resposta correta. \n\n| ENTER | \n")
                sys.exit()

            else:
                input("\n⚠️ Opção inválida! Por favor, escolha uma alternativa válida. \n\n| ENTER | \n")
                break



    def RESPOSTAS_ULT_25():
        global Ajuda_d_plateia
        global Ajuda_dos_Uni
        global nome_usuario

        while True:
            print("======NÍVEL 5- ULTRA DIFÍCIL======")
            print("tema: RADIAÇÃO SOLAR")
            print("A exposição excessiva à radiação UV-B está associada ao aumento do risco de câncer de pele porque essa radiação:\n"
    "A) Provoca desnaturação imediata da melanina presente na epiderme\n"
    "B) Estimula exclusivamente a apoptose de queratinócitos sem afetar o DNA.\n"
    "C) Induz a formação de dímeros de pirimidina no DNA, podendo gerar mutações durante a replicação celular.\n"
    "D) Destrói diretamente os ribossomos das células da derme.\n"
    "E) Impede a síntese de proteínas envolvidas na resposta inflamatória.\n")

            
            ult_25 = input("Qual das alternativas está correta? | PARA RESPONDER DIGITE [A/B/C/D/E] |\n"
                            "| PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] |\n"
                            "| PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] |\n\n"
                            "👤 ").strip().upper()

            if ult_25 == "P":
                if Ajuda_d_plateia > 0:
                    Ajuda_d_plateia -= 1
                    input("\n🎤 Você pediu a ajuda da Plateia: \nEles não têm certeza de qual seja a certa, então boa sorte! \n\n| ENTER | ")
                    print("🥸  É Alternativa (C)!")
                    print("🥸  Claro que é (A)!")
                    print("🥸  Óbvio que é (C)!\n")
                    input(f"🎤 {nome_usuario}, após receber a ajuda da Plateia: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n")
                    continue 
                else:
                    input("\n⚠️ Você não tem mais ajudas da Plateia disponíveis! \n\n| ENTER | ")
                    continue

            elif ult_25 == "U":
                if Ajuda_dos_Uni > 0:
                    Ajuda_dos_Uni -= 1
                    input("\n🎤 Você pediu a ajuda dos Universitários: \nVeja o que eles dirão \n\n| ENTER | ")
                    print("🎓  Temos certeza de que todas estão erradas \n🎓  Menos a alternativa (C)\n")
                    input(f"🎤 {nome_usuario}, após receber a ajuda dos Universitários: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n")
                    continue 
                else:
                    input("\n⚠️ Você não tem mais ajudas dos Universitários disponíveis! \n\n| ENTER | ")
                    continue

            elif ult_25 == "A":                  
                input(f"\n🎤 {nome_usuario}, Provoca desnaturação imediata da melanina presente na epiderme, sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ❌ Errada ❌ \nInfelizmente, essa não é a resposta correta e você perdeu tudo! \n\n| ENTER | \n")
                sys.exit()
        
            elif ult_25 == "B":  
                input(f"\n🎤 {nome_usuario}, Estimula exclusivamente a apoptose de queratinócitos sem afetar o DNA, sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ❌ Errada ❌ \nInfelizmente, essa não é a resposta correta e você perdeu tudo! \n\n| ENTER | \n")
                sys.exit()

            elif ult_25 == "C":
                input(f"\n🎤 {nome_usuario}, Induz a formação de dímeros de pirimidina no DNA, podendo gerar mutações durante a replicação celular, sua resposta está eee...\n\n| ENTER | ")
                print("🎤 ✅ EXATA! PARABÉNS! ✅ \nVocê acabou de garantir 💵 R$ 500.000,00!!! MEIO MILHÃO DE REAIS É SEU! \n")
                
                # --- DECISÃO DO MILHÃO ---
                print("="*60)
                print("🚨 ATENÇÃO! MOMENTO MÁXIMO NO SHOW DA BIOLOGIA! 🚨")
                print(f"🎤 {nome_usuario}, você está a apenas UMA PERGUNTA do prêmio supremo!")
                print("Mas preste muita atenção nas regras:")
                print("-> Se você escolher PARAR, leva para casa seus R$ 500.000,00 garantidos.")
                print("-> Se você escolher ARRISCAR e ACERTAR o Desafio Máximo, você ganha R$ 1.000.000,00!")
                print("-> Se você escolher ARRISCAR e ERRAR... você perde TUDO o que ganhou e sai com R$ 0,00!")
                print("="*60)
                
                decisao = input("E aí? Você quer PARAR [P] ou ARRISCAR TUDO [A]? \n👤 ").strip().upper()
                
                if decisao == "A":
                    input("\n🎤 QUE CORAGEM INCRÍVEL! Vamos para a PERGUNTA DO MILHÃO! \n\n| ENTER PARA O TUDO OU NADA | \n")
                    RESPOSTAS_ULT_26()
                    break
                else:
                    print(f"\n🎤 Decisão inteligentíssima! Você preferiu segurar sua fortuna.")
                    print(f"🏆 Fim de jogo! Parabéns {nome_usuario}, você sai vitorioso com 💵 R$ 500.000,00 no bolso! 🏆\n")
                    sys.exit()
        
            elif ult_25 == "D":
                input(f"\n🎤 {nome_usuario}, Destrói diretamente os ribossomos das células da derme, sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ❌ Errada ❌ \nInfelizmente, essa não é a resposta correta e você perdeu tudo! \n\n| ENTER | \n")
                sys.exit()
        
            elif ult_25 == "E":
                input(f"\n🎤 {nome_usuario}, Impede a síntese de proteínas envolvidas na resposta inflamatória, sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ❌ Errada ❌ \nInfelizmente, essa não é a resposta correta e você perdeu tudo! \n\n| ENTER | \n")
                sys.exit()

            else:
                input("\n⚠️ Opção inválida! Por favor, escolha uma alternativa válida. \n\n| ENTER | \n")
                break




    def RESPOSTAS_ULT_26():
        global Ajuda_d_plateia
        global Ajuda_dos_Uni
        global nome_usuario

        # --- TELA DE CONFIRMAÇÃO DRAMÁTICA ---
        print("\n🚨 SEJA BEM-VINDO À PERGUNTA FINAL DO SHOW DO MILHÃO! 🚨")
        print(f"🎤 {nome_usuario}, as luzes do estúdio se apagam agora.")
        print("Você está de frente com a pergunta de UM MILHÃO DE REAIS.")
        print("\nEsta é a sua ÚLTIMA CHANCE de mudar de ideia:")
        print("-> Se digitar [P] para PARAR AGORA: Você desiste e leva R$ 500.000,00 para casa.")
        print("-> Se digitar [A] para ARRISCAR: Eu vou liberar a pergunta na tela.")
        print("   Lembre-se: se você errar a resposta, perderá tudo e sairá com R$ 0,00!")
        
        confirmacao = input("E aí? Você quer PARAR e levar meio milhão [P] ou quer ARRISCAR TUDO [A]? \n👤 ").strip().upper()
        
        if confirmacao != "A":
            print(f"\n🎤 Uma escolha muito prudente! Você preferiu não colocar sua fortuna em risco.")
            print(f"🏆 PARABÉNS {nome_usuario.upper()}! Você encerra o jogo com 💵 R$ 500.000,00 garantidos! 🏆\n")
            sys.exit()

        # Se o jogador digitou 'A', o jogo continua e mostra a pergunta do milhão:
        input("\n🎤 O PARTICIPANTE DECIDIU ARRISCAR! TENSÃO TOTAL NO ESTÚDIO! \n\n| ENTER PARA REVELAR A PERGUNTA DO MILHÃO | \n")

        while True:
            print("======👑 PERGUNTA FINAL - DESAFIO MÁXIMO 👑======")
            print("tema: RADIAÇÃO SOLAR")
            print("A proteína p53 desempenha papel fundamental na proteção contra o câncer de pele induzido pela radiação solar. Sua principal função é:\n"
                "A) Estimular a produção de melanina pelos queratinócitos.\n"
                "B) Promover a síntese de colágeno na derme.\n"
                "C) Detectar danos ao DNA e interromper o ciclo celular ou induzir apoptose quando necessário.\n"
                "D) Aumentar a absorção de radiação ultravioleta pela epiderme.\n"
                "E) Produzir vitamina D em resposta à exposição solar.")

            ult_26 = input("\nQual das alternativas está correta? | PARA RESPONDER DIGITE [A/B/C/D/E] |\n"
                        "| PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] |\n"
                        "| PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] |\n\n"
                        "👤 ").strip().upper()

            if ult_26 == "P":
                if Ajuda_d_plateia > 0:
                    Ajuda_d_plateia -= 1
                    input("\n🎤 Você pediu a ajuda da Plateia: \nEles não têm certeza de qual seja a certa, então boa sorte! \n\n| ENTER | ")
                    print("🥸  É Alternativa (C)!")
                    print("🥸  Claro que é (A)!")
                    print("🥸  Óbvio que é (C)!\n")
                    input(f"🎤 {nome_usuario}, após receber a ajuda da Plateia: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n")
                    continue 
                else:
                    input("\n⚠️ Você não tem mais ajudas da Plateia disponíveis! \n\n| ENTER | ")
                    continue

            elif ult_26 == "U":
                if Ajuda_dos_Uni > 0:
                    Ajuda_dos_Uni -= 1
                    input("\n🎤 Você pediu a ajuda dos Universitários: \nVeja o que eles dirão \n\n| ENTER | ")
                    print("🎓  Temos certeza de que todas estão erradas \n🎓  Menos a alternativa (C)\n")
                    input(f"🎤 {nome_usuario}, após receber a ajuda dos Universitários: \n| ENTER PARA VER NOVAMENTE AS RESPOSTAS E RESPONDER | \n")
                    continue 
                else:
                    input("\n⚠️ Você não tem mais ajudas dos Universitários disponíveis! \n\n| ENTER | ")
                    continue

            elif ult_26 == "A":                  
                input(f"\n🎤 {nome_usuario}, Estimular a produção de melanina pelos queratinócitos, sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ❌ ERRADA! ❌ \nQue pena! Você arriscou tudo e perdeu tudo na última pergunta! Você sai com R$ 0,00. \n\n| ENTER | \n")
                sys.exit()
            
            elif ult_26 == "B":  
                input(f"\n🎤 {nome_usuario}, Promover a síntese de colágeno na derme, sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ❌ ERRADA! ❌ \nQue pena! Você arriscou tudo e perdeu tudo na última pergunta! Você sai com R$ 0,00. \n\n| ENTER | \n")
                sys.exit()

            # ALTERNATIVA C (✅ RESPOSTA DO MILHÃO ✅)
            elif ult_26 == "C":
                input(f"\n🎤 {nome_usuario}, Detectar danos ao DNA e interromper o ciclo celular ou induzir apoptose quando necessário, sua resposta está eee...\n\n| ENTER | ")
                print("🎉🎉 EXTRAORDINÁRIO!!! HISTÓRIA FOI FEITA!!! 🎉🎉")
                print(f"🏆 VOCÊ ACABA DE ACERTAR A PERGUNTA 26 E GANHOU 💵 R$ 1.000.000,00 !!! 🏆")
                input("\n| ENTER PARA FINALIZAR O JOGO COMO UM NOVO MILIONÁRIO | \n")
                break    
            
            elif ult_26 == "D":
                input(f"\n🎤 {nome_usuario}, Aumentar a absorção de radiação ultravioleta pela epiderme, sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ❌ ERRADA! ❌ \nQue pena! Você arriscou tudo e perdeu tudo na última pergunta! Você sai com R$ 0,00. \n\n| ENTER | \n")
                sys.exit()
            
            elif ult_26 == "E":
                input(f"\n🎤 {nome_usuario}, Produzir vitamina D em resposta à exposição solar, sua resposta está eee... \n\n| ENTER | ")
                input("🎤 ❌ ERRADA! ❌ \nQue pena! Você arriscou tudo e perdeu tudo na última pergunta! Você sai com R$ 0,00. \n\n| ENTER | \n")
                sys.exit()

            else:
                input("\n⚠️ Opção inválida! Por favor, escolha uma alternativa válida. \n\n| ENTER | \n")
                break



    RESPOSTAS_ULT_1()
    RESPOSTAS_ULT_2()
    RESPOSTAS_ULT_23()
    RESPOSTAS_ULT_24()
    RESPOSTAS_ULT_25()

        

        
























elif Máteria_selecionada == "6":

    # =========================================
    # SHOW DO MILHÃO - SOCIOLOGIA
    # =========================================

    while True:

        # =========================================
        # VARIÁVEIS DO JOGO
        # =========================================

        pontuacao = 0
        ajuda_plateia = 3
        ajuda_universitarios = 2
        jogo_ativo = True

        valores = [
            100,
            200,
            300,
            500,
            1_000,
            2_000,
            4_000,
            8_000,
            16_000,
            32_000,
            64_000,
            80_000,
            100_000,
            120_000,
            140_000,
            160_000,
            180_000,
            200_000,
            250_000,
            300_000,
            350_000,
            400_000,
            450_000,
            480_000,
            500_000,
            1_000_000
        ]

        indice_pergunta = 0

        # =========================================
        # MENU INICIAL
        # =========================================

        print("==========================================")
        print("🎤 BEM-VINDO A CYBER MIND 🎤")
        print("==========================================\n")

        print("📚 Tema do jogo: SOCIOLOGIA\n")

        print("O jogo possui:")
        print("✅ 5 perguntas fáceis")
        print("✅ 5 perguntas fáceis/intermediárias")
        print("✅ 5 perguntas intermediárias")
        print("✅ 5 perguntas difíceis")
        print("✅ 5 perguntas avançadas")
        print("💀 1 pergunta do milhão\n")

        print("AJUDAS:")
        print("🥸 Plateia = 3 usos")
        print("🎓 Universitários = 2 usos\n")

        nome_usuario = input("👤 Digite seu nome: ")
        serie_usuario = input("🏫 Digite sua série: ")

        print(f"\nOlá, {nome_usuario}!")
        print(f"Este jogo foi pensado para sua turma {serie_usuario}!\n")

        input("\n| ENTER PARA CONTINUAR |\n")

        # =========================================
        # FUNÇÃO DAS PERGUNTAS
        # =========================================

        def fazer_pergunta(
            pergunta,
            alternativa_a,
            alternativa_b,
            alternativa_c,
            alternativa_d,
            correta,
            justificativa
        ):

            global pontuacao
            global ajuda_plateia
            global ajuda_universitarios
            global indice_pergunta

            while True:

                valor_atual = valores[indice_pergunta]

                print("\n====================================")
                print(
                    f"💰 VALENDO: "
                    f"R$ {valor_atual:,}".replace(",", ".")
                )
                print("====================================\n")

                print(pergunta)
                print()

                print(f"A) {alternativa_a}")
                print(f"B) {alternativa_b}")
                print(f"C) {alternativa_c}")
                print(f"D) {alternativa_d}")

                resposta = input(
                    "\nDigite [A/B/C/D]\n"
                    "🥸 Plateia [P]\n"
                    "🎓 Universitários [U]\n\n"
                    "👤 "
                ).upper()

                # =========================================
                # AJUDA DA PLATEIA
                # =========================================

                if resposta == "P":

                    if ajuda_plateia > 0:

                        ajuda_plateia -= 1

                        print("\n====================================")
                        print("🥸 RESPOSTA DA PLATEIA")
                        print("====================================\n")

                        print(
                            f"🥸 A maioria da plateia escolheu: "
                            f"{correta}"
                        )

                        print(
                            f"\n🥸 Restam "
                            f"{ajuda_plateia} ajudas da plateia."
                        )

                    else:

                        print(
                            "\n❌ Você não possui mais ajuda da plateia!"
                        )

                # =========================================
                # AJUDA UNIVERSITÁRIOS
                # =========================================

                elif resposta == "U":

                    if ajuda_universitarios > 0:

                        ajuda_universitarios -= 1

                        print("\n====================================")
                        print("🎓 RESPOSTA DOS UNIVERSITÁRIOS")
                        print("====================================\n")

                        print(
                            f"🎓 Os universitários acreditam "
                            f"que a resposta correta é: {correta}"
                        )

                        print(
                            f"\n🎓 Restam "
                            f"{ajuda_universitarios} ajudas universitárias."
                        )

                    else:

                        print(
                            "\n❌ Você não possui mais ajuda universitária!"
                        )

                # =========================================
                # RESPOSTA CORRETA
                # =========================================

                elif resposta == correta:

                    # CORREÇÃO:
                    # NÃO SOMA MAIS.
                    # AGORA A PONTUAÇÃO VIRA O VALOR DA PERGUNTA.

                    pontuacao = valor_atual

                    print("\n✅ RESPOSTA CORRETA!")

                    print(
                        f"\n💵 Você ganhou "
                        f"R$ {valor_atual:,}".replace(",", ".")
                    )

                    print("\n📚 Justificativa:")
                    print(justificativa)

                    print(
                        f"\n💰 Valor acumulado: "
                        f"R$ {pontuacao:,}".replace(",", ".")
                    )

                    indice_pergunta += 1

                    input("\n| ENTER PARA CONTINUAR |\n")

                    return True

                # =========================================
                # RESPOSTA ERRADA
                # =========================================

                elif resposta in ["A", "B", "C", "D"]:

                    print("\n❌ RESPOSTA ERRADA!")

                    print(f"\n✅ Resposta correta: {correta}")

                    print("\n📚 Justificativa:")
                    print(justificativa)

                    print("\n💀 GAME OVER!")

                    print(
                        f"\n💰 Você saiu com: "
                        f"R$ {pontuacao:,}".replace(",", ".")
                    )

                    return False

                else:

                    print("\n❌ Opção inválida!")

        # =========================================
        # BLOCO 1
        # =========================================

        if jogo_ativo:

            print("\n🎤 BLOCO 1 - PERGUNTAS FÁCEIS\n")

            jogo_ativo = fazer_pergunta(
                "1) Qual é o principal objeto de estudo da Sociologia enquanto ciência?",
                "O comportamento individual e os processos biológicos do cérebro.",
                "As relações sociais, as estruturas e as instituições que formam a sociedade.",
                "A evolução física das espécies e os ecossistemas naturais.",
                "O funcionamento do mercado financeiro e a economia de ações.",
                "B",
                "A Sociologia foca na estrutura social e nas relações coletivas."
            )

        if jogo_ativo:

            jogo_ativo = fazer_pergunta(
                "2) Qual filósofo francês é considerado o pai do Positivismo e criador do termo Sociologia?",
                "Auguste Comte",
                "Karl Marx",
                "Max Weber",
                "Émile Durkheim",
                "A",
                "Auguste Comte criou o termo Sociologia."
            )

        if jogo_ativo:

            jogo_ativo = fazer_pergunta(
                "3) A Sociologia se diferencia do senso comum porque utiliza:",
                "Opiniões pessoais.",
                "Crenças religiosas.",
                "Método científico e pesquisa empírica.",
                "Intuição individual.",
                "C",
                "A Sociologia utiliza métodos científicos."
            )

        if jogo_ativo:

            jogo_ativo = fazer_pergunta(
                "4) O processo de integração do indivíduo à sociedade chama-se:",
                "Globalização",
                "Alienação",
                "Socialização",
                "Urbanização",
                "C",
                "Socialização é o aprendizado social."
            )

        if jogo_ativo:

            jogo_ativo = fazer_pergunta(
                "5) Regras e costumes que orientam o comportamento social são:",
                "Normas sociais",
                "Interações monetárias",
                "Instintos biológicos",
                "Fatos isolados",
                "A",
                "As normas sociais regulam a sociedade."
            )

        # =========================================
        # BLOCO 2
        # =========================================

        if jogo_ativo:

            print("\n🎤 BLOCO 2 - SOCIOLOGIA E SOCIEDADE\n")

            jogo_ativo = fazer_pergunta(
                "6) Como a Sociologia contribui para políticas públicas?",
                "Determinando leis autoritárias.",
                "Oferecendo diagnósticos baseados em dados.",
                "Mudando apenas a psicologia dos governantes.",
                "Eliminando debates políticos.",
                "B",
                "A Sociologia fornece dados para políticas públicas."
            )

        if jogo_ativo:

            jogo_ativo = fazer_pergunta(
                "7) O conceito de imaginação sociológica permite:",
                "Isolar problemas pessoais.",
                "Relacionar indivíduo e sociedade.",
                "Ignorar problemas econômicos.",
                "Aceitar desigualdades como naturais.",
                "B",
                "Relaciona biografia e sociedade."
            )

        if jogo_ativo:

            jogo_ativo = fazer_pergunta(
                "8) O estudo das relações de gênero e raça promove:",
                "Preconceitos históricos.",
                "Fim da organização jurídica.",
                "Debate crítico sobre igualdade.",
                "Isolamento social.",
                "C",
                "A Sociologia promove igualdade."
            )

        if jogo_ativo:

            jogo_ativo = fazer_pergunta(
                "9) O estranhamento da realidade serve para:",
                "Desnaturalizar comportamentos sociais.",
                "Evitar contato humano.",
                "Aumentar preconceitos.",
                "Negar conflitos sociais.",
                "A",
                "Ajuda a perceber forças sociais."
            )

        if jogo_ativo:

            jogo_ativo = fazer_pergunta(
                "10) A Sociologia da Educação demonstra que a escola:",
                "É totalmente neutra.",
                "Garante sucesso igual para todos.",
                "Pode reproduzir ou transformar desigualdades.",
                "Depende apenas da genética.",
                "C",
                "A escola pode reproduzir desigualdades."
            )

        # =========================================
        # BLOCO 3
        # =========================================

        if jogo_ativo:

            print("\n🎤 BLOCO 3 - ÉMILE DURKHEIM\n")

            jogo_ativo = fazer_pergunta(
                "11) Para Durkheim, os fatos sociais devem ser tratados como:",
                "Fenômenos psicológicos.",
                "Coisas externas e coercitivas.",
                "Eventos individuais.",
                "Ideias abstratas.",
                "B",
                "Os fatos sociais são coercitivos."
            )

        if jogo_ativo:

            jogo_ativo = fazer_pergunta(
                "12) Características do fato social:",
                "Generalidade, exterioridade e coercitividade.",
                "Subjetividade e individualidade.",
                "Afetividade e racionalidade.",
                "Espiritualidade e lucratividade.",
                "A",
                "São características do fato social."
            )

        if jogo_ativo:

            jogo_ativo = fazer_pergunta(
                "13) Punições sociais demonstram:",
                "Exterioridade",
                "Coercitividade",
                "Generalidade",
                "Abstração",
                "B",
                "A punição demonstra coerção."
            )

        if jogo_ativo:

            jogo_ativo = fazer_pergunta(
                "14) Idiomas e leis demonstram:",
                "Generalidade econômica.",
                "Livre-arbítrio.",
                "Subjetividade moral.",
                "Exterioridade do fato social.",
                "D",
                "Existem antes do indivíduo."
            )

        if jogo_ativo:

            jogo_ativo = fazer_pergunta(
                "15) Anomia social significa:",
                "Equilíbrio social.",
                "Enfraquecimento das normas sociais.",
                "Fim dos crimes.",
                "Controle familiar absoluto.",
                "B",
                "Anomia é ausência de normas."
            )

        # =========================================
        # BLOCO 4
        # =========================================

        if jogo_ativo:

            print("\n🎤 BLOCO 4 - MAX WEBER\n")

            jogo_ativo = fazer_pergunta(
                "16) Para Weber, a Sociologia estuda:",
                "Estrutura econômica.",
                "Ação social.",
                "Evolução biológica.",
                "Fatos coercitivos.",
                "B",
                "Weber analisa ações sociais."
            )

        if jogo_ativo:

            jogo_ativo = fazer_pergunta(
                "17) Buscar diploma para conseguir emprego é:",
                "Ação racional com valores.",
                "Ação afetiva.",
                "Ação racional com relação a fins.",
                "Ação tradicional.",
                "C",
                "Existe cálculo racional dos meios."
            )

        if jogo_ativo:

            jogo_ativo = fazer_pergunta(
                "18) Participar de manifestação por princípios morais é:",
                "Ação racional com valores.",
                "Ação tradicional.",
                "Ação afetiva.",
                "Ação racional com fins.",
                "A",
                "É guiada por valores morais."
            )

        if jogo_ativo:

            jogo_ativo = fazer_pergunta(
                "19) Comemorar o Natal por costume representa:",
                "Ação racional.",
                "Ação tradicional.",
                "Ação afetiva.",
                "Ação burocrática.",
                "B",
                "Baseada em costumes."
            )

        if jogo_ativo:

            jogo_ativo = fazer_pergunta(
                "20) Modelo teórico criado por Weber:",
                "Fato social ideal.",
                "Materialismo histórico.",
                "Tipo ideal.",
                "Consciência coletiva.",
                "C",
                "Ferramenta metodológica de Weber."
            )

        # =========================================
        # BLOCO 5
        # =========================================

        if jogo_ativo:

            print("\n🎤 BLOCO 5 - KARL MARX\n")

            jogo_ativo = fazer_pergunta(
                "21) A alienação do trabalho ocorre porque:",
                "O trabalhador não entende as máquinas.",
                "O trabalhador é separado dos meios de produção.",
                "Os impostos são muito altos.",
                "Os salários são iguais.",
                "B",
                "O trabalhador perde controle da produção."
            )

        if jogo_ativo:

            jogo_ativo = fazer_pergunta(
                "22) O produto do trabalho alienado aparece como:",
                "Bem comunitário.",
                "Extensão natural da criatividade.",
                "Força estranha que domina o trabalhador.",
                "Patrimônio pessoal.",
                "C",
                "O produto se torna algo estranho."
            )

        if jogo_ativo:

            jogo_ativo = fazer_pergunta(
                "23) O trabalho alienado passa a ser:",
                "Sacrifício para sobreviver.",
                "Ascensão social rápida.",
                "Atividade prazerosa.",
                "Vocação religiosa.",
                "A",
                "O trabalhador trabalha para sobreviver."
            )

        if jogo_ativo:

            jogo_ativo = fazer_pergunta(
                "24) A alienação entre trabalhadores gera:",
                "Mais solidariedade.",
                "Fim da concorrência.",
                "Concorrência e fragmentação.",
                "Fim dos conflitos.",
                "C",
                "A competição enfraquece os trabalhadores."
            )

        if jogo_ativo:

            jogo_ativo = fazer_pergunta(
                "25) Conceito que esconde relações de exploração:",
                "Fetiche da mercadoria.",
                "Tipo ideal.",
                "Solidariedade mecânica.",
                "Racionalismo mercantil.",
                "A",
                "O fetiche oculta relações sociais."
            )

        # =========================================
        # ESCOLHA FINAL
        # =========================================

        if jogo_ativo:

            print("\n====================================")
            print("💰 VOCÊ CHEGOU A R$ 500.000!")
            print("====================================")

            escolha = input(
                "\nVocê deseja:\n"
                "[P] PARAR COM R$ 500.000\n"
                "[C] CONTINUAR PARA A PERGUNTA DO MILHÃO\n\n"
                "👤 "
            ).upper()

            if escolha == "P":

                print("\n🏆 PARABÉNS!")
                print("💰 Você saiu com R$ 500.000")

                jogo_ativo = False

            elif escolha == "C":

                print("\n🔥 VOCÊ DECIDIU SE ARRISCAR!")
                print("💀 VALENDO R$ 1.000.000!")

            else:

                print("\n❌ Opção inválida!")
                jogo_ativo = False

        # =========================================
        # PERGUNTA DO MILHÃO
        # =========================================

        if jogo_ativo:

            jogo_ativo = fazer_pergunta(
                "26) Sobre a uberização do trabalho, qual alternativa relaciona corretamente Marx e Weber?",
                "Durkheim via a uberização como solidariedade mecânica.",
                "Marx relaciona alienação e Weber racionalização do algoritmo.",
                "Weber via aplicativos como ação afetiva.",
                "Marx acreditava no fim da alienação pela posse do celular.",
                "B",
                "Marx analisa alienação e Weber racionalização técnica."
            )

        # =========================================
        # FINAL DO JOGO
        # =========================================

        print("\n==========================================")
        print("🎤 FIM DO JOGO")
        print("==========================================\n")

        print(f"👤 Jogador: {nome_usuario}")

        print(
            f"💰 Pontuação final: "
            f"R$ {pontuacao:,}".replace(",", ".")
        )

        if pontuacao == 1_000_000:

            print("\n🏆 VOCÊ VIROU UM MILIONÁRIO!")

        elif pontuacao >= 500_000:

            print("\n🎉 Excelente desempenho!")

        else:

            print("\n📚 Continue estudando Sociologia!")

        print("\n🎤 Obrigado por jogar!")

        jogar_novamente = input(
            "\n🎮 Você quer jogar novamente? [SIM/NÃO]: "
        ).upper()

        if jogar_novamente == "NÃO" or jogar_novamente == "NAO":

            print("\n👋 Até a próxima!")
            break
