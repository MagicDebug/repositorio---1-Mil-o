Ajuda_plateia = 3
Ajuda_Universitarios = 5
Valor_Acumulado = 0.0

# AQUI É A INTRODUÇÃO DO JOGO COM O TÍTULO
print (input("\n\n 💰!!! O CYBER MIND SHOW !!!💰  | ENTER |"))

# AQUI É ONDE O APRESENTADOR/MÁQUINA QUE SE IDENTIFICA PELO MICROFONE (🎤) DÁ AS BOAS-VINDAS AO USUÁRIO E PEDE PARA ELE SE APRESENTAR, USUÁRIO SENDO (👤)
print ("\n 🎤 Seja Bem-Vindo ao Cyber Mind Show! ")
nome_usuario = (input(" Vamos dar início ao Grande Show. Por Favor, Se Apresente nos dizendo seu nome | DIGITE SEU NOME | \n\n | ENTER | \n\n 👤 "))

# AQUI ESTÃO AS EXPLICAÇÕES DE COMO SÃO AS REGRAS DO JOGO, SOBRE O VALOR DAS PERGUNTAS, AS AJUDAS E O OBJETIVO DO JOGO QUE É CHEGAR AO 1 MILHÃO

print (input("\n 🎤 " + nome_usuario + ", as Instruções do Jogo são as seguintes: \n  O Show será dividido em 5 temas do 😂 Mais Fácil até o, 🤬 Mais Difícil \n contendo 25 perguntas divididas para os diferentes 5 temas, podendo ter a ajuda da; \n\n 🥸  Plateia 3 vezes \n 🎓 Universitários 5 vezes \n\n  | ENTER | \n"))
print (input(" 🎤 Cada pergunta vale 💵 200,00 \n  A cada acerto o valor da próxima pergunta dobra, aumentando o resultado acumulado \n  Mas se você errar, o jogo acaba na hora! \n\n | ENTER | \n"))
print (input("\n 🎤 Seu Único Objetivo é responder todas as 25 Perguntas e tentar chegar ao 1 milhão \n\n  MAS ATENÇÃO!!! \n no fim das 25 perguntas você acertar tudo irá \n há uma Pergunta Bônus chamada \n\n 💀 ARRISCA TUDO 💀 \n\n  Pergunta na qual se você acertar leva seu 💵 Valor Acumulado ao Dobro🤑  \n  Mas se Errar perde todo 💵 Valor Acumulado 💀 \n\n | ENTER | \n"))

import os

def RESPOSTAS_PERGUNTA_1 (pergunta_1_resposta_m):
    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_1_resposta_m = input("Para aquecer vamos começar o nível fácil resolvendo algumas equações do primeiro grau!!! \n\n 🎤 Resolva a equação: \n\n 2x + 6 = 16 \n\n 🎤 Alternativa (A) x = 3 \n 🎤 Alternativa (B) x = 4 \n 🎤 Alternativa (C) x = 5 \n 🎤 Alternativa (D) x = 6 \n 🎤 Alternativa (E) x = 7 \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITÁRIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 ")
        
        # .upper() serve para aceitar letras minúsculas digitadas pelo usuário
        pergunta_1_resposta_m = pergunta_1_resposta_m.upper()

        if pergunta_1_resposta_m == "P":
            if Ajuda_plateia > 0:
                Ajuda_plateia -= 1
                print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não têm certeza de qual seja a certa, então boa sorte! \n\n | ENTER | "))
                print (" 🥸  É Alternativa (C)! \n 🥸  Claro que é (A)! \n 🥸  Óbvio que é (C)! \n\n")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))
            else:
                print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))



        if pergunta_1_resposta_m == "U":
            if Ajuda_Universitarios > 0:
                Ajuda_Universitarios -= 1
                print (input("\n 🎤 Você pediu a ajuda do Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (C) \n\n ")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

            else:
                print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

        if pergunta_1_resposta_m == "C":
            print("\n🎤 Resposta correta!")
            print("✅ Você ganhou R$ 100,00! \n\n Vamos prosseguir para a pergunta 2\n\n")
            input(" | ENTER | \n")

            Valor_Acumulado = 100.0
            break
        
        if pergunta_1_resposta_m in ["A", "B", "D", "E"]:
            print("\n🎤 Resposta incorreta! O jogo acabou! \n\n O valor acumulado foi de R$ " + str(Valor_Acumulado) + " \n\n Obrigado por jogar o Show do Milhão, " + nome_usuario + "! \n\n | ENTER | \n")
            exit()


RESPOSTAS_PERGUNTA_1( pergunta_1_resposta_m = "")

import os
os.system("cls")

def RESPOSTAS_PERGUNTA_2 (pergunta_2_resposta_m):
    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_2_resposta_m = input(" 🎤 PERGUNTA 2:\n\n Resolva a equação: "" \n\n 3x - 9 = 12 \n\n 🎤 Alternativa (A) x = 5 \n 🎤 Alternativa (B) x = 6 \n 🎤 Alternativa (C) x = 7 \n 🎤 Alternativa (D) x = 8 \n 🎤 Alternativa (E) x = 9 \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITÁRIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 ")
        
        # .upper() serve para aceitar letras minúsculas digitadas pelo usuário
        pergunta_2_resposta_m = pergunta_2_resposta_m.upper()

        if pergunta_2_resposta_m == "P":
            if Ajuda_plateia > 0:
                Ajuda_plateia -= 1
                print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não têm certeza de qual seja a certa, então boa sorte! \n\n | ENTER | "))
                print (" 🥸  É Alternativa (A)! \n 🥸  Claro que é (C)! \n 🥸  Óbvio que é (C)! \n\n")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))
            else:
                print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))



        if pergunta_2_resposta_m == "U":
            if Ajuda_Universitarios > 0:
                Ajuda_Universitarios -= 1
                print (input("\n 🎤 Você pediu a ajuda do Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (C) \n\n ")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

            else:
                print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

        if pergunta_2_resposta_m == "C":
         print("\n🎤 Resposta correta!")
         print("✅ Você ganhou R$ 100,00! \n\n Vamos prosseguir para a pergunta 3")
        input(" | ENTER | \n")
        Valor_Acumulado = 200.0
        break
    
    if pergunta_2_resposta_m in ["A", "B", "D", "E"]:
        print("\n🎤 Resposta incorreta! O jogo acabou! \n\n O valor acumulado foi de R$ " + str(Valor_Acumulado) + " \n\n Obrigado por jogar o Show do Milhão, " + nome_usuario + "! \n\n | ENTER | \n")
        exit()


RESPOSTAS_PERGUNTA_2(pergunta_2_resposta_m ="")

import os
os.system("cls")

def RESPOSTAS_PERGUNTA_3 (pergunta_3_resposta_m):
    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_3_resposta_m = input(" 🎤 PERGUNTA 3:\n\n Resolva a equação: ""\n\n 4x + 8 = 24 \n\n 🎤 Alternativa (A) x = 2 \n 🎤 Alternativa (B) x = 3 \n 🎤 Alternativa (C) x = 4 \n 🎤 Alternativa (D) x = 5 \n 🎤 Alternativa (E) x = 6 \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITÁRIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 ")
        
        # .upper() serve para aceitar letras minúsculas digitadas pelo usuário
        pergunta_3_resposta_m = pergunta_3_resposta_m.upper()

        if pergunta_3_resposta_m == "P":
            if Ajuda_plateia > 0:
                Ajuda_plateia -= 1
                print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não têm certeza de qual seja a certa, então boa sorte! \n\n | ENTER | "))
                print (" 🥸  É Alternativa (C)! \n 🥸  Claro que é (C)! \n 🥸  Óbvio que é (D)! \n\n")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))
            else:
                print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))



        if pergunta_3_resposta_m == "U":
            if Ajuda_Universitarios > 0:
                Ajuda_Universitarios -= 1
                print (input("\n 🎤 Você pediu a ajuda do Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (C) \n\n ")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

            else:
                print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

        if pergunta_3_resposta_m == "C":
         print("\n🎤 Resposta correta!")
         print("✅ Você ganhou R$ 200,00! \n\n Vamos prosseguir para a pergunta 4")
         input(" | ENTER | \n")
         Valor_Acumulado = 400.0
         break

    if pergunta_3_resposta_m in ["A", "B", "D", "E"]:     
        print("\n🎤 Resposta incorreta! O jogo acabou! \n\n O valor acumulado foi de R$ " + str(Valor_Acumulado) + " \n\n Obrigado por jogar o Show do Milhão, " + nome_usuario + "! \n\n | ENTER | \n")
        exit()


RESPOSTAS_PERGUNTA_3(pergunta_3_resposta_m = "")

import os
os.system("cls")

def RESPOSTAS_PERGUNTA_4 (pergunta_4_resposta_m):
    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_4_resposta_m = input(" 🎤 PERGUNTA 4:\n\n Resolva a equação:   " + str(Valor_Acumulado) + " \n\n 5x - 15 = 20 \n\n 🎤 Alternativa (A) x = 5 \n 🎤 Alternativa (B) x = 6 \n 🎤 Alternativa (C) x = 7 \n 🎤 Alternativa (D) x = 8 \n 🎤 Alternativa (E) x = 9 \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITÁRIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 ")
        
        # .upper() serve para aceitar letras minúsculas digitadas pelo usuário
        pergunta_4_resposta_m = pergunta_4_resposta_m.upper()

        if pergunta_4_resposta_m == "P":
            if Ajuda_plateia > 0:
                Ajuda_plateia -= 1
                print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não têm certeza de qual seja a certa, então boa sorte! \n\n | ENTER | "))
                print (" 🥸  É Alternativa (C)! \n 🥸  Claro que é (C)! \n 🥸  Óbvio que é (C)! \n\n")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))
            else:
                print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))



        if pergunta_4_resposta_m == "U":
            if Ajuda_Universitarios > 0:
                Ajuda_Universitarios -= 1
                print (input("\n 🎤 Você pediu a ajuda do Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (C) \n\n ")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

            else:
                print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

        if pergunta_4_resposta_m == "C":
         print("\n🎤 Resposta correta!")
         print("✅ Você ganhou R$ 400,00! \n Vamos prosseguir para a pergunta 5")
         input(" | ENTER | \n")
        Valor_Acumulado = 800.0
        break

    if pergunta_4_resposta_m in ["A", "B", "D", "E"]:
        print("\n🎤 Resposta incorreta! O jogo acabou! \n\n O valor acumulado foi de R$ " + str(Valor_Acumulado) + " \n\n Obrigado por jogar o Show do Milhão, " + nome_usuario + "! \n\n | ENTER | \n")
        exit()

RESPOSTAS_PERGUNTA_4("")

import os
os.system("cls")

def RESPOSTAS_PERGUNTA_5 (pergunta_5_resposta_m):
    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_5_resposta_m = input(" 🎤 PERGUNTA 5:\n\n Resolva a equação: "" \n\n 2x - 4 = 10 \n\n 🎤 Alternativa (A) x = 5 \n 🎤 Alternativa (B) x = 6 \n 🎤 Alternativa (C) x = 7 \n 🎤 Alternativa (D) x = 8 \n 🎤 Alternativa (E) x = 9 \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITÁRIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 ")
        
        # .upper() serve para aceitar letras minúsculas digitadas pelo usuário
        pergunta_5_resposta_m = pergunta_5_resposta_m.upper()

        if pergunta_5_resposta_m == "P":
            if Ajuda_plateia > 0:
                Ajuda_plateia -= 1
                print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não têm certeza de qual seja a certa, então boa sorte! \n\n | ENTER | "))
                print (" 🥸  É Alternativa (c)! \n 🥸  Claro que é (c)! \n 🥸  Óbvio que é (c)! \n\n")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))
            else:
                print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))



        if pergunta_5_resposta_m == "U":
            if Ajuda_Universitarios > 0:
                Ajuda_Universitarios -= 1
                print (input("\n 🎤 Você pediu a ajuda do Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                print (" 🎓  O desenvolvedor endoidou? \n Está me parecendo a (C) de novo...\n\n ")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

            else:
                print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

        if pergunta_5_resposta_m == "C":
         print("\n🎤 Resposta correta!")
         print("✅ Você ganhou R$ 800,00!")
         input(" | ENTER | \n")
         Valor_Acumulado = 1600.0
         break

    if pergunta_5_resposta_m in ["A", "B", "D", "E"]:
        print("\n🎤 Resposta incorreta! O jogo acabou! \n\n O valor acumulado foi de R$ " + str(Valor_Acumulado) + " \n\n Obrigado por jogar o Show do Milhão, " + nome_usuario + "! \n\n | ENTER | \n")
        exit()

RESPOSTAS_PERGUNTA_5(pergunta_5_resposta_m = "")

import os
os.system("cls")



import os
os.system("cls")


def RESPOSTAS_PERGUNTA_6 (pergunta_6_resposta_m):
    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_6_resposta_m = input("Vamos começar com as perguntas de nível médio!!! \n O tema agora será Grandezas e Medidas \n\n 🎤 PERGUNTA 6:\n\n Qual é a unidade principal de comprimento no Sistema Internacional de Unidades (SI)?"" \n\n 🎤 Alternativa A) Litro \n 🎤 Alternativa B) Metro \n 🎤 Alternativa C) Quilograma \n 🎤 Alternativa D) Segundo \n 🎤 Alternativa E) Grau Celsius \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITÁRIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 ")
        
        # .upper() serve para aceitar letras minúsculas digitadas pelo usuário
        pergunta_6_resposta_m = pergunta_6_resposta_m.upper()

        if pergunta_6_resposta_m == "P":
            if Ajuda_plateia > 0:
                Ajuda_plateia -= 1
                print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não têm certeza de qual seja a certa, então boa sorte! \n\n | ENTER | "))
                print (" 🥸  É Alternativa (B)! \n 🥸  Claro que é (B)! \n 🥸  Óbvio que é (B)! \n\n")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))
            else:
                print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))



        if pergunta_6_resposta_m == "U":
            if Ajuda_Universitarios > 0:
                Ajuda_Universitarios -= 1
                print (input("\n 🎤 Você pediu a ajuda do Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (C) \n\n ")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

            else:
                print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

        if pergunta_6_resposta_m == "B":
         print("\n🎤 Resposta correta!")
         print("✅ Você ganhou R$ 1400,00!")
         input(" | ENTER | \n")
         Valor_Acumulado = 3000.0
         break

    if pergunta_6_resposta_m in ["A", "C", "D", "E"]:
        print("\n🎤 Resposta incorreta! O jogo acabou! \n\n O valor acumulado foi de R$ " + str(Valor_Acumulado) + " \n\n Obrigado por jogar o Show do Milhão, " + nome_usuario + "! \n\n | ENTER | \n")
        exit()

RESPOSTAS_PERGUNTA_6(pergunta_6_resposta_m = "")

import os
os.system("cls")



def RESPOSTAS_PERGUNTA_7 (pergunta_7_resposta_m):
    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_7_resposta_m = input("🎤 PERGUNTA 7:\n\n Quantos gramas existem em 3 quilogramas?"" \n\n 🎤 Alternativa A) 30 \n 🎤 Alternativa B) 300 \n 🎤 Alternativa C) 3000 \n 🎤 Alternativa D) 30000 \n 🎤 Alternativa E) 300000 \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITÁRIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 ")
        
        # .upper() serve para aceitar letras minúsculas digitadas pelo usuário
        pergunta_7_resposta_m = pergunta_7_resposta_m.upper()

        if pergunta_7_resposta_m == "P":
            if Ajuda_plateia > 0:
                Ajuda_plateia -= 1
                print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não têm certeza de qual seja a certa, então boa sorte! \n\n | ENTER | "))
                print (" 🥸  É Alternativa (C)! \n 🥸  Claro que é (C)! \n 🥸  Óbvio que é (C)! \n\n")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))
            else:
                print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))



        if pergunta_7_resposta_m == "U":
            if Ajuda_Universitarios > 0:
                Ajuda_Universitarios -= 1
                print (input("\n 🎤 Você pediu a ajuda do Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (C) \n\n ")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

            else:
                print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

        if pergunta_7_resposta_m == "C":
         print("\n🎤 Resposta correta!")
         print("✅ Você ganhou R$ 2000,00!")
         input(" | ENTER | \n")
         Valor_Acumulado = 5000.0
         break

    if pergunta_7_resposta_m in ["A", "B", "D", "E"]:
        print("\n🎤 Resposta incorreta! O jogo acabou! \n\n O valor acumulado foi de R$ " + str(Valor_Acumulado) + " \n\n Obrigado por jogar o Show do Milhão, " + nome_usuario + "! \n\n | ENTER | \n")
        exit()

RESPOSTAS_PERGUNTA_7(pergunta_5_resposta_m = "")

def RESPOSTAS_PERGUNTA_8 (pergunta_8_resposta_m):
    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_8_resposta_m = input("🎤 PERGUNTA 8:\n\n Uma garrafa contém 2 litros de refrigerante. Quantos mililitros ela possui?"" \n\n 🎤 Alternativa A) 200 \n 🎤 Alternativa B) 2000 \n 🎤 Alternativa C) 20000 \n 🎤 Alternativa D) 200000 \n 🎤 Alternativa E) 2000000 \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITÁRIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 ")
        
        # .upper() serve para aceitar letras minúsculas digitadas pelo usuário
        pergunta_8_resposta_m = pergunta_8_resposta_m.upper()

        if pergunta_8_resposta_m == "P":
            if Ajuda_plateia > 0:
                Ajuda_plateia -= 1
                print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não têm certeza de qual seja a certa, então boa sorte! \n\n | ENTER | "))
                print (" 🥸  É Alternativa (B)! \n 🥸  Claro que é (B)! \n 🥸  Óbvio que é (B)! \n\n")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))
            else:
                print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))



        if pergunta_8_resposta_m == "U":
            if Ajuda_Universitarios > 0:
                Ajuda_Universitarios -= 1
                print (input("\n 🎤 Você pediu a ajuda do Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (B) \n\n ")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

            else:
                print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

        if pergunta_8_resposta_m == "B":
         print("\n🎤 Resposta correta!")
         print("✅ Você ganhou R$ 2500,00!")
         input(" | ENTER | \n")
         Valor_Acumulado = 7500.0
         break

    if pergunta_8_resposta_m in ["A", "C", "D", "E"]:
        print("\n🎤 Resposta incorreta! O jogo acabou! \n\n O valor acumulado foi de R$ " + str(Valor_Acumulado) + " \n\n Obrigado por jogar o Show do Milhão, " + nome_usuario + "! \n\n | ENTER | \n")
        exit()

RESPOSTAS_PERGUNTA_8(pergunta_8_resposta_m = "")

import os
os.system("cls")


def RESPOSTAS_PERGUNTA_9 (pergunta_9_resposta_m):
    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_9_resposta_m = input("🎤 PERGUNTA 9:\n\n Uma aula dura 1 hora e 30 minutos. Quantos minutos ela dura ao todo?"" \n\n 🎤 Alternativa A) 60 minutos \n 🎤 Alternativa B) 75 minutos \n 🎤 Alternativa C) 80 minutos \n 🎤 Alternativa D) 90 minutos \n 🎤 Alternativa E) 120 minutos \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITÁRIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 ")
        
        # .upper() serve para aceitar letras minúsculas digitadas pelo usuário
        pergunta_9_resposta_m = pergunta_9_resposta_m.upper()

        if pergunta_9_resposta_m == "P":
            if Ajuda_plateia > 0:
                Ajuda_plateia -= 1
                print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não têm certeza de qual seja a certa, então boa sorte! \n\n | ENTER | "))
                print (" 🥸  É Alternativa (E)! \n 🥸  Claro que é (C)! \n 🥸  Óbvio que é (D)! \n\n")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))
            else:
                print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))



        if pergunta_9_resposta_m == "U":
            if Ajuda_Universitarios > 0:
                Ajuda_Universitarios -= 1
                print (input("\n 🎤 Você pediu a ajuda do Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (D) \n\n ")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

            else:
                print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

        if pergunta_9_resposta_m == "D":
         print("\n🎤 Resposta correta!")
         print("✅ Você ganhou R$ 2500,00!")
         input(" | ENTER | \n")
         Valor_Acumulado = 10000.0
         break

    if pergunta_9_resposta_m in ["A", "C", "B", "E"]:
        print("\n🎤 Resposta incorreta! O jogo acabou! \n\n O valor acumulado foi de R$ " + str(Valor_Acumulado) + " \n\n Obrigado por jogar o Show do Milhão, " + nome_usuario + "! \n\n | ENTER | \n")
        exit()

RESPOSTAS_PERGUNTA_9(pergunta_9_resposta_m = "")

def RESPOSTAS_PERGUNTA_10 (pergunta_10_resposta_m):
    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_10_resposta_m = input("🎤 PERGUNTA 10:\n\n Um terreno retangular mede 8 metros de comprimento e 5 metros de largura. Qual é sua área?"" \n\n 🎤 Alternativa A) 13 m² \n 🎤 Alternativa B) 26 m² \n 🎤 Alternativa C) 35 m² \n 🎤 Alternativa D) 40 m² \n 🎤 Alternativa E) 45 m² \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITÁRIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 ")
        
        # .upper() serve para aceitar letras minúsculas digitadas pelo usuário
        pergunta_10_resposta_m = pergunta_10_resposta_m.upper()

        if pergunta_10_resposta_m == "P":
            if Ajuda_plateia > 0:
                Ajuda_plateia -= 1
                print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não têm certeza de qual seja a certa, então boa sorte! \n\n | ENTER | "))
                print (" 🥸  É Alternativa (D)! \n 🥸  Claro que é (A)! \n 🥸  Óbvio que é (D)! \n\n")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))
            else:
                print (input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))



        if pergunta_10_resposta_m == "U":
            if Ajuda_Universitarios > 0:
                Ajuda_Universitarios -= 1
                print (input("\n 🎤 Você pediu a ajuda do Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
                print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (D) \n\n ")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))

            else:
                print (input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

        if pergunta_10_resposta_m == "D":
         print("\n🎤 Resposta correta!")
         print("✅ Você ganhou R$ 5000,00!")
         input(" | ENTER | \n")
         Valor_Acumulado = 15000.0
         break

    if pergunta_10_resposta_m in ["A", "C", "B", "E"]:
        print("\n🎤 Resposta incorreta! O jogo acabou! \n\n O valor acumulado foi de R$ " + str(Valor_Acumulado) + " \n\n Obrigado por jogar o Show do Milhão, " + nome_usuario + "! \n\n | ENTER | \n")
        exit()

RESPOSTAS_PERGUNTA_10(pergunta_10_resposta_m = "")

input("Impressionante, " + nome_usuario + "! Você concluiu a Pergunta 10, demais!!! \n\n O valor atual acumulado é de R$ " + str(Valor_Acumulado) + " \n\n Muito cuidado para não perde-lo! \n\n Vamos continuar para a Pergunta 11, onde iniciamos o nível intermediário!!! \n\n | ENTER | \n")


def RESPOSTAS_PERGUNTA_11 (pergunta_11_resposta_m):
    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_11_resposta_m = input("🎤 PERGUNTA 11:\n\n Uma caixa tem 5 m de comprimento, 3 m de largura e 2 m de altura. Qual é o seu volume?\n\n 🎤 Alternativa A) 10 m³ \n 🎤 Alternativa B) 20 m³ \n 🎤 Alternativa C) 30 m³ \n 🎤 Alternativa D) 40 m³ \n 🎤 Alternativa E) 50 m³ \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸 PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITÁRIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 ")
        pergunta_11_resposta_m = pergunta_11_resposta_m.upper()

        if pergunta_11_resposta_m == "P":
         if Ajuda_plateia > 0:
          Ajuda_plateia -= 1
          print(input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não têm certeza de qual seja a certa, então boa sorte! \n\n | ENTER | "))
          print(" 🥸 É Alternativa (B)! \n 🥸 Claro que é (C)! \n 🥸 Óbvio que é (D)! \n\n")
          print(input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))
        else:
            print(input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

        if pergunta_11_resposta_m == "U":
         if Ajuda_Universitarios > 0:
          Ajuda_Universitarios -= 1
          print(input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
          print(" 🎓 Temos certeza de que todas estão erradas \n Menos a alternativa (C) \n\n ")
          print(input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))
        else:
           print(input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

        if pergunta_11_resposta_m == "C":
         print("\n🎤 Resposta correta!")
         print("✅ Você ganhou R$ 5000,00!")
         input(" | ENTER | \n")
         Valor_Acumulado = 15000.0
         break

        if pergunta_11_resposta_m in ["A", "B", "D", "E"]:
          print("\n🎤 Resposta incorreta! O jogo acabou!")
          print("\nO valor acumulado foi de R$ " + str(Valor_Acumulado))
          print("\nObrigado por jogar o Show do Milhão, " + nome_usuario + "!")
          input("\n| ENTER |")
          exit()


RESPOSTAS_PERGUNTA_11(pergunta_11_resposta_m = "") 

def RESPOSTAS_PERGUNTA_12 (pergunta_12_resposta_m):
    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_12_resposta_m = input("🎤 PERGUNTA 12:\n\n Um aquário possui dimensões de 80 cm × 50 cm × 40 cm. Qual é o seu volume?\n\n 🎤 Alternativa A) A) 120.000 cm³ \n 🎤 Alternativa B) 140.000 cm³ \n 🎤 Alternativa C) 160.000 cm³ \n 🎤 Alternativa D) 180.000 cm³ \n 🎤 Alternativa E) 200.000 cm³ \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸 PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITÁRIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 ")
        pergunta_12_resposta_m = pergunta_12_resposta_m.upper()

        if pergunta_12_resposta_m == "P":
         if Ajuda_plateia > 0:
          Ajuda_plateia -= 1
          print(input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não têm certeza de qual seja a certa, então boa sorte! \n\n | ENTER | "))
          print(" 🥸 É Alternativa (B)! \n 🥸 Claro que é (C)! \n 🥸 Óbvio que é (D)! \n\n")
          print(input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))
        else:
            print(input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n"))

        if pergunta_12_resposta_m == "U":
         if Ajuda_Universitarios > 0:
          Ajuda_Universitarios -= 1
          print(input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | "))
          print(" 🎓 Temos certeza de que todas estão erradas \n Menos a alternativa (C) \n\n ")
          print(input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS RESPOSTAS | \n"))
        else:
           print(input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n"))

        if pergunta_12_resposta_m == "C":
         print("\n🎤 Resposta correta!")
         print("✅ Você ganhou R$ 5000,00!")
         input(" | ENTER | \n")
         Valor_Acumulado = 15000.0
         break

        if pergunta_12_resposta_m in ["A", "B", "D", "E"]:
          print("\n🎤 Resposta incorreta! O jogo acabou!")
          print("\nO valor acumulado foi de R$ " + str(Valor_Acumulado))
          print("\nObrigado por jogar o Show do Milhão, " + nome_usuario + "!")
          input("\n| ENTER |")
          exit()

RESPOSTAS_PERGUNTA_12(pergunta_12_resposta_m = "")

#===================================================
#PARTE DO LEO
#===================================================

input("\n Impressionante, " + nome_usuario + "! Você concluiu a Pergunta 20, demais!!! \n\n O valor atual acumulado é de R$ " + str(Valor_Acumulado) + " \n\n Muito cuidado para não perde-lo! \n\n Vamos continuar para a Pergunta 16, onde iniciamos o nível Dificil!!! \n Tema: Equação do 2º grau (análise do Δ) \n\n | ENTER | \n")

def RESPOSTAS_PERGUNTA_16 (pergunta_16_resposta_m):

    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_16_resposta_m = input("🎤 PERGUNTA 16:\n\n Para quais valores de 𝓶  a equação abaixo possui raízes reais e distintas? \n\n  (𝓶  - 1) x² + 2x + 1 = 0  \n\n 🎤 Alternativa A) 𝓶  < 2 e 𝓶  ≠ 1 \n 🎤 Alternativa B) 𝓶  ≥ 2 \n 🎤 Alternativa C) 𝓶  < 1 \n 🎤 Alternativa D) 𝓶  ≠ 2 \n 🎤 Alternativa E) 𝓶  > 1 \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITÁRIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 ").upper()

        if pergunta_16_resposta_m == "P":
            if Ajuda_plateia > 0:
                Ajuda_plateia -= 1
                input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não têm certeza de qual seja a certa, então boa sorte! \n\n | ENTER | ")
                print(" 🥸  É Alternativa (A)! \n 🥸  Claro que é (E)! \n 🥸  Óbvio que é (A)!\n")
                input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n pressione ENTER para voltar e responder \n")
            else:
                input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n")
            continue

        # AJUDA DOS UNIVERSITÁRIOS
        elif pergunta_16_resposta_m == "U":
            if Ajuda_Universitarios > 0:
                Ajuda_Universitarios -= 1
                input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | ")
                print(" 🎓 Temos certeza de que todas estão erradas \n Menos a alternativa (A) \n\n ")
                input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n pressione ENTER para voltar e responder \n")
            else:
                input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n")
            continue

        elif pergunta_16_resposta_m == "A":
            print("\n🎤 Resposta correta!")
            print("✅ Você ganhou R$ 5000,00!")
            Valor_Acumulado = 0.0
            input(" | ENTER | \n")
            break

        elif pergunta_16_resposta_m in ["C", "B", "D", "E"]:
            print("\n🎤 Resposta incorreta! O jogo acabou!")
            print("\nO valor acumulado foi de R$ " + str(Valor_Acumulado))
            print("\nObrigado por jogar o Show do Milhão, " + nome_usuario + "!")
            input("\n| ENTER |")
            exit()

RESPOSTAS_PERGUNTA_16 (pergunta_16_resposta_m = "")

def RESPOSTAS_PERGUNTA_17 (pergunta_17_resposta_m):

    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_17_resposta_m = input("🎤 PERGUNTA 17:\n\n Determine os valores de 𝓶  para que a equação tenha raízes reais: \n\n x² + (𝓶  - 4) x + 𝓶  = 0 \n\n 🎤 Alternativa A) 𝓶  ≤ 6 - 2√5 ou 𝓶  ≥ 6 + 2√5 \n 🎤 Alternativa B) 0 < 𝓶  < 16 \n 🎤 Alternativa C) 𝓶  < 1 \n 🎤 Alternativa D) 𝓶  ≠ 2 \n 🎤 Alternativa E) 𝓶  > 1 \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITÁRIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 ").upper()

        if pergunta_17_resposta_m == "P":
            if Ajuda_plateia > 0:
                Ajuda_plateia -= 1
                input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não têm certeza de qual seja a certa, então boa sorte! \n\n | ENTER | ")
                print(" 🥸  É Alternativa (A)! \n 🥸  Claro que é (D)! \n 🥸  Óbvio que é (A)!\n")
                input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n pressione ENTER para voltar e responder \n")
            else:
                input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n")
            continue

        # AJUDA DOS UNIVERSITÁRIOS
        elif pergunta_17_resposta_m == "U":
            if Ajuda_Universitarios > 0:
                Ajuda_Universitarios -= 1
                input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | ")
                print(" 🎓 Temos certeza de que todas estão erradas \n Menos a alternativa (A) \n\n ")
                input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n pressione ENTER para voltar e responder \n")
            else:
                input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n")
            continue

        elif pergunta_17_resposta_m == "A":
            print("\n🎤 Resposta correta!")
            print("✅ Você ganhou R$ 5000,00!")
            Valor_Acumulado = 0.0
            input(" | ENTER | \n")
            break

        elif pergunta_17_resposta_m in ["C", "B", "D", "E"]:
            print("\n🎤 Resposta incorreta! O jogo acabou!")
            print("\nO valor acumulado foi de R$ " + str(Valor_Acumulado))
            print("\nObrigado por jogar o Show do Milhão, " + nome_usuario + "!")
            input("\n| ENTER |")
            exit()

RESPOSTAS_PERGUNTA_17 (pergunta_17_resposta_m = "")

def RESPOSTAS_PERGUNTA_18 (pergunta_18_resposta_m):

    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_18_resposta_m = input("🎤 PERGUNTA 18:\n\n Para quais valores de 𝓶  a equação é do 2º grau e possui pelo menos uma raiz real? \n\n 𝓶 x² + 2x + (𝓶  + 1) = 0 \n\n 🎤 Alternativa A) 𝓶  ≠ 0 \n 🎤 Alternativa B) (- 1 - √5) / 2 ≤ 𝓶  ≤ (- 1 + √5) / 2 e 𝓶  ≠ 0 \n 🎤 Alternativa C) - 100 ≤ 𝓶  ≤ 100 \n 🎤 Alternativa D) 𝓶  ≤ 50 \n 🎤 Alternativa E) 𝓶  < 0 \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITÁRIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 ").upper()

        if pergunta_18_resposta_m == "P":
            if Ajuda_plateia > 0:
                Ajuda_plateia -= 1
                input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não têm certeza de qual seja a certa, então boa sorte! \n\n | ENTER | ")
                print(" 🥸  É Alternativa (C)! \n 🥸  Claro que é (B)! \n 🥸  Óbvio que é (B)!\n")
                input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n pressione ENTER para voltar e responder \n")
            else:
                input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n")
            continue

        # AJUDA DOS UNIVERSITÁRIOS
        elif pergunta_18_resposta_m == "U":
            if Ajuda_Universitarios > 0:
                Ajuda_Universitarios -= 1
                input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | ")
                print(" 🎓 Temos certeza de que todas estão erradas \n Menos a alternativa (B) \n\n ")
                input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n pressione ENTER para voltar e responder \n")
            else:
                input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n")
            continue

        elif pergunta_18_resposta_m == "B":
            print("\n🎤 Resposta correta!")
            print("✅ Você ganhou R$ 5000,00!")
            Valor_Acumulado = 0.0
            input(" | ENTER | \n")
            break

        elif pergunta_18_resposta_m in ["C", "A", "D", "E"]:
            print("\n🎤 Resposta incorreta! O jogo acabou!")
            print("\nO valor acumulado foi de R$ " + str(Valor_Acumulado))
            print("\nObrigado por jogar o Show do Milhão, " + nome_usuario + "!")
            input("\n| ENTER |")
            exit()

RESPOSTAS_PERGUNTA_18 (pergunta_18_resposta_m = "")

def RESPOSTAS_PERGUNTA_19 (pergunta_19_resposta_m = ""):

    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_19_resposta_m = input("🎤 PERGUNTA 19:\n\n Determine os valores de m para que a equação possua raízes reais iguais: \n\n x² + 2𝓶 x + (𝓶 ² - 4) = 0 \n\n 🎤 Alternativa A) 𝓶  = 0 \n 🎤 Alternativa B) 𝓶  ≠ 0 \n 🎤 Alternativa C) 𝓶  = 2 ou 𝓶  = - 2 \n 🎤 Alternativa D) 𝓶  ≥ 0 \n 🎤 Alternativa E) 𝓶  < 0 \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITÁRIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 ").upper()

        if pergunta_19_resposta_m == "P":
            if Ajuda_plateia > 0:
                Ajuda_plateia -= 1
                input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não têm certeza de qual seja a certa, então boa sorte! \n\n | ENTER | ")
                print(" 🥸  É Alternativa (A)! \n 🥸  Claro que é (C)! \n 🥸  Óbvio que é (C)!\n")
                input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n pressione ENTER para voltar e responder \n")
            else:
                input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n")
            continue

        # AJUDA DOS UNIVERSITÁRIOS
        elif pergunta_19_resposta_m == "U":
            if Ajuda_Universitarios > 0:
                Ajuda_Universitarios -= 1
                input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | ")
                print(" 🎓 Temos certeza de que todas estão erradas \n Menos a alternativa (C) \n\n ")
                input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n pressione ENTER para voltar e responder \n")
            else:
                input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n")
            continue

        elif pergunta_19_resposta_m == "C":
            print("\n🎤 Resposta correta!")
            print("✅ Você ganhou R$ 5000,00!")
            Valor_Acumulado = 0.0
            input(" | ENTER | \n")
            break

        elif pergunta_19_resposta_m in ["B", "A", "D", "E"]:
            print("\n🎤 Resposta incorreta! O jogo acabou!")
            print("\nO valor acumulado foi de R$ " + str(Valor_Acumulado))
            print("\nObrigado por jogar o Show do Milhão, " + nome_usuario + "!")
            input("\n| ENTER |")
            exit()

RESPOSTAS_PERGUNTA_19 (pergunta_19_resposta_m = "")

def RESPOSTAS_PERGUNTA_20 (pergunta_20_resposta_m = ""):

    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_20_resposta_m = input("🎤 PERGUNTA 20:\n\n Para quais valores de 𝓶  a equação a baixo possui sempre raízes reais, independentemente de x? \n\n (𝓶 ² - 4) x² + 4x + 1 = 0 \n\n 🎤 Alternativa A) 𝓶  = 0 \n 🎤 Alternativa B) 𝓶  ≠ ± 2 \n 🎤 Alternativa C) - 2√2 ≤ 𝓶  ≤ 2√2 \n 🎤 Alternativa D) 𝓶  = ± 2 \n 🎤 Alternativa E) 𝓶  < - 2 \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITÁRIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 ").upper()

        if pergunta_20_resposta_m == "P":
            if Ajuda_plateia > 0:
                Ajuda_plateia -= 1
                input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não têm certeza de qual seja a certa, então boa sorte! \n\n | ENTER | ")
                print(" 🥸  É Alternativa (D)! \n 🥸  Claro que é (D)! \n 🥸  Óbvio que é (C)!\n")
                input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n pressione ENTER para voltar e responder \n")
            else:
                input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n")
            continue

        # AJUDA DOS UNIVERSITÁRIOS
        elif pergunta_20_resposta_m == "U":
            if Ajuda_Universitarios > 0:
                Ajuda_Universitarios -= 1
                input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | ")
                print(" 🎓 Temos certeza de que todas estão erradas \n Menos a alternativa (D) \n\n ")
                input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n pressione ENTER para voltar e responder \n")
            else:
                input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n")
            continue

        elif pergunta_20_resposta_m == "D":
            print("\n🎤 Resposta correta!")
            print("✅ Você ganhou R$ 5000,00!")
            Valor_Acumulado = 0.0
            input(" | ENTER | \n")
            break

        elif pergunta_20_resposta_m in ["B", "A", "C", "E"]:
            print("\n🎤 Resposta incorreta! O jogo acabou!")
            print("\nO valor acumulado foi de R$ " + str(Valor_Acumulado))
            print("\nObrigado por jogar o Show do Milhão, " + nome_usuario + "!")
            input("\n| ENTER |")
            exit()

RESPOSTAS_PERGUNTA_20 (pergunta_20_resposta_m = "")

# PARTE DO LUIZZ


def RESPOSTAS_PERGUNTA_21 (pergunta_21_resposta_m = ""):

    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_21_resposta_m = input("🎤 PERGUNTA 21:\n\n Para que uma equação do 2º grau possua duas raízes reais e diferentes (distintas), qual deve ser a condição do discriminante (Delta)? \n\n 🎤 Alternativa A) Delta = 0 \n 🎤 Alternativa B) Delta < 0 \n 🎤 Alternativa C) Delta > 0 \n 🎤 Alternativa D) Delta ≤ 0 \n 🎤 Alternativa E) Delta não interfere nas raízes \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITÁRIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 ").upper()

        if pergunta_21_resposta_m == "P":
            if Ajuda_plateia > 0:
                Ajuda_plateia -= 1
                input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles se lembram  das aulas de álgebra! \n\n | ENTER | ")
                print(" 🥸  Acho que é a (C)! \n 🥸  Com certeza é a (C)! \n 🥸  Fiquei em dúvida com a (A)!\n")
                input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n pressione ENTER para voltar e responder \n")
            else:
                input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n")
            continue

        elif pergunta_21_resposta_m == "U":
            if Ajuda_Universitarios > 0:
                Ajuda_Universitarios -= 1
                input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | ENTER | ")
                print(" 🎓 Se o Delta for positivo, a raiz quadrada dele existe e gera dois valores diferentes na fórmula de Bhaskara. A certa é a (C). \n\n ")
                input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n pressione ENTER para voltar e responder \n")
            else:
                input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n")
            continue

        elif pergunta_21_resposta_m == "C":
            print("\n🎤 Resposta correta!")
            print("✅ Você ganhou R$ 10.000,00!")
            Valor_Acumulado = 10000.0
            input(" | ENTER | \n")
            break

        elif pergunta_21_resposta_m in ["A", "B", "D", "E"]:
            print("\n🎤 Resposta incorreta! O jogo acabou!")
            print("\nO valor acumulado foi de R$ " + str(Valor_Acumulado))
            print("\nObrigado por jogar o Show do Milhão, " + nome_usuario + "!")
            input("\n| ENTER |")
            exit()

RESPOSTAS_PERGUNTA_21 (pergunta_21_resposta_m = "")


def RESPOSTAS_PERGUNTA_22 (pergunta_22_resposta_m = ""):

    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_22_resposta_m = input("🎤 PERGUNTA 22:\n\n Analisando a equação x² - 6x + 9 = 0, o que podemos afirmar sobre a existência de suas soluções no conjunto dos números reais? \n\n 🎤 Alternativa A) Não possui nenhuma raiz real. \n 🎤 Alternativa B) Possui duas raízes reais e iguais. \n 🎤 Alternativa C) Possui duas raízes reais e diferentes. \n 🎤 Alternativa D) Possui infinitas soluções reais. \n 🎤 Alternativa E) A única solução real é x = 0. \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITÁRIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 ").upper()

        if pergunta_22_resposta_m == "P":
            if Ajuda_plateia > 0:
                Ajuda_plateia -= 1
                input("\n 🎤 Você pediu a ajuda da Plateia: \n\n | ENTER | ")
                print(" 🥸  O Delta dá zero, então é a (B)! \n 🥸  Acho que é (B) também! \n 🥸  Eu acho que é a (C).\n")
                input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n pressione ENTER para voltar e responder \n")
            else:
                input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n")
            continue

        elif pergunta_22_resposta_m == "U":
            if Ajuda_Universitarios > 0:
                Ajuda_Universitarios -= 1
                input("\n 🎤 Você pediu a ajuda dos Universitários: \n\n | ENTER | ")
                print(" 🎓 Calculando o Delta: (-6)² - 4*1*9 = 36 - 36 = 0. Quando Delta é igual a zero, a equação tem duas raízes reais e iguais. Alternativa (B). \n\n ")
                input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n pressione ENTER para voltar e responder \n")
            else:
                input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n")
            continue

        elif pergunta_22_resposta_m == "B":
            print("\n🎤 Resposta correta!")
            print("✅ Você ganhou R$ 50.000,00!")
            Valor_Acumulado = 50000.0
            input(" | ENTER | \n")
            break

        elif pergunta_22_resposta_m in ["A", "C", "D", "E"]:
            print("\n🎤 Resposta incorreta! O jogo acabou!")
            print("\nO valor acumulado foi de R$ " + str(Valor_Acumulado))
            print("\nObrigado por jogar o Show do Milhão, " + nome_usuario + "!")
            input("\n| ENTER |")
            exit()

RESPOSTAS_PERGUNTA_22 (pergunta_22_resposta_m = "")


def RESPOSTAS_PERGUNTA_23 (pergunta_23_resposta_m = ""):

    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_23_resposta_m = input("🎤 PERGUNTA 23:\n\n Qual das seguintes equações do 2º grau NÃO possui nenhuma raiz ou solução real? \n\n 🎤 Alternativa A) x² - 25 = 0 \n 🎤 Alternativa B) x² - 4x = 0 \n 🎤 Alternativa C) x² + 2x + 5 = 0 \n 🎤 Alternativa D) x² - 5x + 6 = 0 \n 🎤 Alternativa E) x² - x - 1 = 0 \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITÁRIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 ").upper()

        if pergunta_23_resposta_m == "P":
            if Ajuda_plateia > 0:
                Ajuda_plateia -= 1
                input("\n 🎤 Você pediu a ajuda da Plateia: \n\n | ENTER | ")
                print(" 🥸  Chuta (C)! \n 🥸  Acho que a (A) tem raiz que é 5, então não é ela... vai de (C)! \n 🥸  É a (C), confia!\n")
                input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n pressione ENTER para voltar e responder \n")
            else:
                input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n")
            continue

        elif pergunta_23_resposta_m == "U":
            if Ajuda_Universitarios > 0:
                Ajuda_Universitarios -= 1
                input("\n 🎤 Você pediu a ajuda dos Universitários: \n\n | ENTER | ")
                print(" 🎓 Na alternativa (C), se calcularmos o Delta, temos: 2² - 4*1*5 = 4 - 20 = -16. Como o Delta é negativo, não existem raízes reais. Alternativa (C). \n\n ")
                input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n pressione ENTER para voltar e responder \n")
            else:
                input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n")
            continue

        elif pergunta_23_resposta_m == "C":
            print("\n🎤 Resposta correta!")
            print("✅ Você ganhou R$ 100.000,00!")
            Valor_Acumulado = 100000.0
            input(" | ENTER | \n")
            break

        elif pergunta_23_resposta_m in ["A", "B", "D", "E"]:
            print("\n🎤 Resposta incorreta! O jogo acabou!")
            print("\nO valor acumulado foi de R$ " + str(Valor_Acumulado))
            print("\nObrigado por jogar o Show do Milhão, " + nome_usuario + "!")
            input("\n| ENTER |")
            exit()

RESPOSTAS_PERGUNTA_23 (pergunta_23_resposta_m = "")


def RESPOSTAS_PERGUNTA_24 (pergunta_24_resposta_m = ""):

    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_24_resposta_m = input("🎤 PERGUNTA 24:\n\n Entrando no tema de equações exponenciais: determine o valor da incógnita x que satisfaz a equação: 3^x = 81 \n\n 🎤 Alternativa A) x = 3 \n 🎤 Alternativa B) x = 4 \n 🎤 Alternativa C) x = 9 \n 🎤 Alternativa D) x = 27 \n 🎤 Alternativa E) x = 5 \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITÁRIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 ").upper()

        if pergunta_24_resposta_m == "P":
            if Ajuda_plateia > 0:
                Ajuda_plateia -= 1
                input("\n 🎤 Você pediu a ajuda da Plateia: \n\n | ENTER | ")
                print(" 🥸  Essa é fácil, \n 🥸  é a (B), dá 4! \n 🥸  Voto na (B)!\n")
                input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n pressione ENTER para voltar e responder \n")
            else:
                input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n")
            continue

        elif pergunta_24_resposta_m == "U":
            if Ajuda_Universitarios > 0:
                Ajuda_Universitarios -= 1
                input("\n 🎤 Você pediu a ajuda dos Universitários: \n\n | ENTER | ")
                print(" 🎓 Fatorando o número 81 na base 3, encontramos 3⁴. Portanto, se 3^x = 3⁴, então x = 4. Alternativa (B). \n\n ")
                input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n pressione ENTER para voltar e responder \n")
            else:
                input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n")
            continue

        elif pergunta_24_resposta_m == "B":
            print("\n🎤 Resposta correta!")
            print("✅ Você ganhou R$ 300.000,00!")
            Valor_Acumulado = 300000.0
            input(" | ENTER | \n")
            break

        elif pergunta_24_resposta_m in ["A", "C", "D", "E"]:
            print("\n🎤 Resposta incorreta! O jogo acabou!")
            print("\nO valor acumulado foi de R$ " + str(Valor_Acumulado))
            print("\nObrigado por jogar o Show do Milhão, " + nome_usuario + "!")
            input("\n| ENTER |")
            exit()

RESPOSTAS_PERGUNTA_24 (pergunta_24_resposta_m = "")


def RESPOSTAS_PERGUNTA_25 (pergunta_25_resposta_m = ""):

    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_25_resposta_m = input("🎤 PERGUNTA 25:\n\n Resolva a seguinte equação exponencial que envolve frações: 2^x = 1/32. Qual é o valor real de x? \n\n 🎤 Alternativa A) x = 5 \n 🎤 Alternativa B) x = -5 \n 🎤 Alternativa C) x = -4 \n 🎤 Alternativa D) x = 16 \n 🎤 Alternativa E) x = -16 \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITÁRIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 ").upper()

        if pergunta_25_resposta_m == "P":
            if Ajuda_plateia > 0:
                Ajuda_plateia -= 1
                input("\n 🎤 Você pediu a ajuda da Plateia: \n\n | ENTER | ")
                print(" 🥸  Como inverteu a fração, o expoente tem que ser negativo! \n 🥸  Acho que é a (B)! \n 🥸  Eu vou na (B) também!\n")
                input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n pressione ENTER para voltar e responder \n")
            else:
                input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n")
            continue

        elif pergunta_25_resposta_m == "U":
            if Ajuda_Universitarios > 0:
                Ajuda_Universitarios -= 1
                input("\n 🎤 Você pediu a ajuda dos Universitários: \n\n | ENTER | ")
                print(" 🎓 Sabemos que 32 é igual a 2⁵. Como ele está no denominador (1/32), aplicamos a propriedade do expoente negativo, transformando em 2⁻⁵. Logo, x = -5. Alternativa (B). \n\n ")
                input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n pressione ENTER para voltar e responder \n")
            else:
                input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n")
            continue

        elif pergunta_25_resposta_m == "B":
            print("\n🎤 Resposta correta!")
            print("✅ Você ganhou R$ 500.000,00!")
            Valor_Acumulado = 500000.0
            input(" | ENTER | \n")
            break

        elif pergunta_25_resposta_m in ["A", "C", "D", "E"]:
            print("\n🎤 Resposta incorreta! O jogo acabou!")
            print("\nO valor acumulado foi de R$ " + str(Valor_Acumulado))
            print("\nObrigado por jogar o Show do Milhão, " + nome_usuario + "!")
            input("\n| ENTER |")
            exit()

RESPOSTAS_PERGUNTA_25 (pergunta_25_resposta_m = "")


def RESPOSTAS_PERGUNTA_26 (pergunta_26_resposta_m = ""):

    global Ajuda_plateia
    global Ajuda_Universitarios
    global Valor_Acumulado

    while True:
        pergunta_26_resposta_m = input("🎤 PERGUNTA 26 - A PERGUNTA DO MILHÃO! 🏆:\n\n (Questão do Milhão) Resolva a equação exponencial que exige a redução de bases diferentes para uma mesma base comum: 9^(x + 1) = 27^(x - 1). Qual é o valor de x? \n\n 🎤 Alternativa A) x = 2 \n 🎤 Alternativa B) x = 3 \n 🎤 Alternativa C) x = 4 \n 🎤 Alternativa D) x = 5 \n 🎤 Alternativa E) x = 1 \n\n | PARA RESPONDER DIGITE [A/B/C/D/E] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITÁRIOS PRESSIONE [U] | \n\n | ENTER | \n\n 👤 ").upper()

        if pergunta_26_resposta_m == "P":
            if Ajuda_plateia > 0:
                Ajuda_plateia -= 1
                input("\n 🎤 Você pediu a ajuda da Plateia: \n  Ninguém sabe resolver de cabeça! \n\n | ENTER | ")
                print(" 🥸  Eita, chuta a (D). \n 🥸  Acho que é a (B). \n Instável... melhor pedir universitários!\n")
                input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n pressione ENTER para voltar e responder \n")
            else:
                input("\n 🎤 Você não tem mais ajudas da Plateia disponíveis! \n\n | ENTER | \n")
            continue

        elif pergunta_26_resposta_m == "U":
            if Ajuda_Universitarios > 0:
                Ajuda_Universitarios -= 1
                input("\n 🎤 Você pediu a ajuda dos Universitários: \n\n | ENTER | ")
                print(" 🎓 Vamos lá: igualando as bases para 3, temos (3²)^(x+1) = (3³)^(x-1). Isso vira 2(x + 1) = 3(x - 1), que resulta em 2x + 2 = 3x - 3. Isolando o x, descobrimos que x = 5. A alternativa correta é a (D). \n\n ")
                input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n pressione ENTER para voltar e responder \n")
            else:
                input("\n 🎤 Você não tem mais ajudas dos Universitários disponíveis! \n\n | ENTER | \n")
            continue

        elif pergunta_26_resposta_m == "D":
            
            print("🎤 INCRÍVEL! RESPOSTA ABSOLUTAMENTE CORRETA!!!")
            print("🏆 PARABÉNS! VOCÊ ACABA DE GANHAR R$ 1.000.000,00! 🏆")
            Valor_Acumulado = 1000000.0
            input(" | ENTER | \n")
            break

        elif pergunta_26_resposta_m in ["A", "B", "C", "E"]:
            print("\n🎤 Resposta incorreta! Que pena, você perdeu tudo na última pergunta!")
            print("\nO valor acumulado voltou para R$ 0.0")
            print("\nObrigado por jogar o Show do Milhão, " + nome_usuario + "!")
            input("\n| ENTER |")
            exit()

RESPOSTAS_PERGUNTA_26 (pergunta_26_resposta_m = "")



