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
            break
            
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
RESPOSTAS_PERGUNTA_26_bloco_5()
print (input("\n 🎤 Parabéns " + nome_usuario + ", você acertou a última pergunta e ganhou 💵 1,000,000 de reais! \n\n | TECLE ENTER PARA CONTINUAR | \n"))
print (input(" 🎤 Você é um verdadeiro especialista em história do Brasil! \n\n | TECLE ENTER PARA CONTINUAR | \n"))
print (input(" 🎤 Obrigado por jogar o nosso Show do Milhão! \n\n | TECLE ENTER PARA CONTINUAR | \n"))
print (input(" 🎤 Até a próxima! \n\n | TECLE ENTER PARA CONTINUAR | \n"))
