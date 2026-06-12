Ajuda_da_pessoas = 3
Ajuda_dos_Universitarios = 5
nome_usuario = input("Antes de Iniciarmos Gostaria de Saber, qual seria seu nome? \n\n 👤 | DIGITE O SEU NOME E TECLE ENTER PARA CONTINUAR | \n ")


print (input("🎤Você selecionou a materia Física \n\n 🎤Vamos dar inicio ao primeiro Tema: Propagação de Calor   \n\n  | TECLE ENTER PARA CONTINUAR | \n"))




def RESPOSTAS_PERGUNTA_1 ():
    
    # VARIAVEIS GLOBAL PARA AS AJUDAS
    global Ajuda_da_pessoas
    global Ajuda_dos_Universitarios

    while True:
        print (input("=== NIVEL 1 - FACIL ==="))
        pergunta_1_resposta = (input(" 🎤 PERGUNTA 1: \n Tema: Propagação de calor \n\n O calor do Sol chega na Terra por?: \n\n  Alternativa (A) Chuva \n  Alternativa (B) Vento \n  Alternativa (C) Radiação \n  Alternativa (D) Gelo \n\n | PARA RESPONDER DIGITE [A/B/C/D] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | DIGITE A ALTERNATIVA MAIS ENTER PARA CONTINUAR | \n\n 👤 "))
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
        elif pergunta_1_resposta in ["A", "B", "D"] or ["a" , "b" , "d"]:
            print("\n❌ ERRADA!")
            print("💀 Você perdeu tudo!\n")
            exit()
        else:
            print("\n❌ Resposta inválida!\n")
            exit () 
            
      

RESPOSTAS_PERGUNTA_1()

print (input("\n 🎤 Parabéns " + nome_usuario + ", você acertou a primeira pergunta e já tem 💵 1,000 reais acumulados! \n\n | TECLE ENTER PARA CONTINUAR | \n"))



def RESPOSTAS_PERGUNTA_2():

    global Ajuda_da_pessoas
    global Ajuda_dos_Universitarios

    while True:

        pergunta_2_resposta = input("🎤 PERGUNTA 2: A colher esquenta na panela por?\n\n Alternativa (A) Condução\n Alternativa (B) Futebol\n Alternativa (C) Planta\n Alternativa (D) Neve \n\n | DIGITE [A/B/C/D] | \n | PLATEIA [P] | \n | UNIVERSITARIOS [U] | \n\n | DIGITE A ALTERNATIVA MAIS ENTER PARA CONTINUAR | \n\n 👤 ")
            
        # AJUDA DA PLATEIA
        if pergunta_2_resposta == "P" or pergunta_2_resposta == "p":
            if Ajuda_da_pessoas > 0:
                Ajuda_da_pessoas -= 1

                print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | TECLE ENTER PARA CONTINUAR | "))
                print (" 🥸  É Alternativa (A)! \n 🥸  Claro que é (A)! \n 🥸  Obvio que é (B)! \n\n")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))
            

            else:
                print("\n❌ Você não possui mais ajuda da plateia!\n")

        # AJUDA DOS UNIVERSITARIOS
        elif pergunta_2_resposta == "U" or pergunta_2_resposta == "u":

            if Ajuda_dos_Universitarios > 0:
                Ajuda_dos_Universitarios -= 1

                print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | TECLE ENTER PARA CONTINUAR | "))
                print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (A) \n\n ")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

            else:
                print("\n❌ Você não possui mais ajuda dos universitários!\n")

        # RESPOSTA CERTA
        elif pergunta_2_resposta == "A" or pergunta_2_resposta == "a":

            print("\n✅ CORRETA!")
            print("💵 Você ganhou mais 1,000 reais!\n")
            break

        # RESPOSTAS ERRADAS
        elif pergunta_2_resposta in ["B", "C", "D"] or ["b" , "c" , "d"]:

            print("\n❌ ERRADA!")
            print("💀 Você perdeu tudo!\n")
            exit()

        else:
            print("\n❌ Resposta inválida!\n")
            exit()
RESPOSTAS_PERGUNTA_2()

print (input("\n 🎤 Parabéns " + nome_usuario + ", você acertou a segunda pergunta e já tem 💵 2,000 reais acumulados! \n\n | TECLE ENTER PARA CONTINUAR | \n"))


def RESPOSTAS_PERGUNTA_3():
    global Ajuda_da_pessoas
    global Ajuda_dos_Universitarios

    while True:
        pergunta_3_resposta = input("🎤 PERGUNTA 3: A convecção acontece em?:\n\n Alternativa (A)Líquidos e gases \n Alternativa (B) Papel \n Alternativa (C) Pedra \n Alternativa (D) Vidro \n\n | DIGITE [A/B/C/D] | \n | PLATEIA [P] | \n | UNIVERSITARIOS [U] | \n\n | DIGITE A ALTERNATIVA MAIS ENTER PARA CONTINUAR | \n\n 👤 ")
        # AJUDA DA PLATEIA
        if pergunta_3_resposta == "P" or pergunta_3_resposta == "p":

            if Ajuda_da_pessoas > 0:
                Ajuda_da_pessoas -= 1

                print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | TECLE ENTER PARA CONTINUAR | "))
                print (" 🥸  É Alternativa (A)! \n 🥸  Claro que é (A)! \n 🥸  Obvio que nao é (B)! \n\n")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

            else:
                print("\n❌ Você não possui mais ajuda da plateia!\n")
        # AJUDA DOS UNIVERSITARIOS
        elif pergunta_3_resposta == "U" or pergunta_3_resposta == "u":
            if Ajuda_dos_Universitarios > 0:
                Ajuda_dos_Universitarios -= 1

                print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | TECLE ENTER PARA CONTINUAR | "))
                print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (A) \n\n ")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

            else:
                print("\n❌ Você não possui mais ajuda dos universitários!\n")
        # RESPOSTA CERTA
        elif pergunta_3_resposta == "A" or pergunta_3_resposta == "a":

            print("\n✅ CORRETA!")
            print("💵 Você ganhou mais 1,000 reais!\n")
            break
        # RESPOSTAS ERRADAS
        elif pergunta_3_resposta in ["B", "C", "D"] or ["b" , "c" , "d"]:

            print("\n❌ ERRADA!")
            print("💀 Você perdeu tudo!\n")
            exit()

        else:
            print("\n❌ Resposta inválida!\n")
            exit()
RESPOSTAS_PERGUNTA_3()
print (input("\n 🎤 Parabéns " + nome_usuario + ", você acertou a terceira pergunta e já tem 💵 3,000 reais acumulados! \n\n | TECLE ENTER PARA CONTINUAR | \n"))


def RESPOSTAS_PERGUNTA_4():
    global Ajuda_da_pessoas
    global Ajuda_dos_Universitarios

    while True:
        pergunta_4_resposta = input("🎤 PERGUNTA 4: Qual é um modo de propagação de calor?:\n\n Alternativa (A) Corrida \n Alternativa (B) Condução \n Alternativa (C) Música \n Alternativa (D) Pintura \n Alternativa (E) Dança \n\n | DIGITE [A/B/C/D/E] | \n | PLATEIA [P] | \n | UNIVERSITARIOS [U] | \n\n | DIGITE A ALTERNATIVA MAIS ENTER PARA CONTINUAR | \n\n 👤 ")
     #   AJUDA DA PLATEIA
        if pergunta_4_resposta == "P" or pergunta_4_resposta == "p":
            if Ajuda_da_pessoas > 0:
                Ajuda_da_pessoas -= 1

                print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | TECLE ENTER PARA CONTINUAR | "))
                print (" 🥸  É Alternativa (B)! \n 🥸  Claro que é (B)! \n 🥸  Obvio que nao é (C)! \n\n")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

            else:
                print("\n❌ Você não possui mais ajuda da plateia!\n")
        # AJUDA DOS UNIVERSITARIOS
        elif pergunta_4_resposta == "U" or pergunta_4_resposta == "u":
            if Ajuda_dos_Universitarios > 0:
                Ajuda_dos_Universitarios -= 1

                print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | TECLE ENTER PARA CONTINUAR | "))
                print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (B) \n\n ")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

            else:
                print("\n❌ Você não possui mais ajuda dos universitários!\n")
        # RESPOSTA CERTA
        elif pergunta_4_resposta == "B" or pergunta_4_resposta == "b":

            print("\n✅ CORRETA!")
            print("💵 Você ganhou mais 1,000 reais!\n")
            break
        # RESPOSTAS ERRADAS
        elif pergunta_4_resposta in ["A", "C", "D"] or ["a" , "c" , "d"]:
            print("\n❌ ERRADA!")
            print("💀 Você perdeu tudo!\n")
            exit()
        else:
            print("\n❌ Resposta inválida!\n")
            exit()
RESPOSTAS_PERGUNTA_4()
print (input("\n 🎤 Parabéns " + nome_usuario + ", você acertou a quarta pergunta e já tem 💵 4,000 reais acumulados! \n\n | TECLE ENTER PARA CONTINUAR | \n"))


def RESPOSTAS_PERGUNTA_5():
    global Ajuda_da_pessoas
    global Ajuda_dos_Universitarios

    while True:
        pergunta_5_resposta = input ("🎤 PERGUNTA 5:O calor sempre vai do?:\n\n Alternativa (A) Frio para o quente \n Alternativa (B) Quente para o frio \n Alternativa (C) Azul para o verde \n Alternativa (D) Pequeno para o grande  \n\n | DIGITE [A/B/C/D] | \n | PLATEIA [P] | \n | UNIVERSITARIOS [U] | \n\n | DIGITE A ALTERNATIVA MAIS ENTER PARA CONTINUAR | \n\n")
        # AJUDA DA PLATEIA
        if pergunta_5_resposta == "P" or pergunta_5_resposta == "p":
            if Ajuda_da_pessoas > 0:
                Ajuda_da_pessoas -= 1

                print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | TECLE ENTER PARA CONTINUAR | "))
                print (" 🥸  É Alternativa (B)! \n 🥸  Claro que é (B)! \n 🥸  Obvio que nao é (C)! \n\n")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

            else:
                print("\n❌ Você não possui mais ajuda da plateia!\n")
        # AJUDA DOS UNIVERSITARIOS
        elif pergunta_5_resposta == "U" or pergunta_5_resposta == "u":
            if Ajuda_dos_Universitarios > 0:
                Ajuda_dos_Universitarios -= 1

                print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | TECLE ENTER PARA CONTINUAR | "))
                print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (B) \n\n ")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

            else:
                print("\n❌ Você não possui mais ajuda dos universitários!\n")
        # RESPOSTA CERTA
        elif pergunta_5_resposta == "B" or pergunta_5_resposta == "b":

            print("\n✅ CORRETA!")
            print("💵 Você ganhou mais 1,000 reais!\n")
            break

        # RESPOSTAS ERRADAS
        elif pergunta_5_resposta in ["A", "C", "D"] or ["a" , "c" , "D"]:
            print("\n❌ ERRADA!")
            print("💀 Você perdeu tudo!\n")
            exit()

        else:
            print("\n❌ Resposta inválida!\n")
            exit()
RESPOSTAS_PERGUNTA_5()
print (input("\n 🎤 Parabéns " + nome_usuario + ", você acertou a quinta pergunta e já tem 💵 5,000 reais acumulados! \n\n | TECLE ENTER PARA CONTINUAR | \n"))
print (input(" 🎤Agora vamos para o proximo bloco Agora as perguntas vão ser um pouco mais dificeis \n\n | TECLE ENTER PARA CONTINUAR | \n"))










import sys

# Variáveis globais do jogo
Ajuda_d_plateia = 5
Ajuda_dos_Uni = 5


def pergunta_facil_1():
    global Ajuda_d_plateia
    global Ajuda_dos_Uni
    while True: 
        print("\n=== NÍVEL 2 - MEDIANO ===") 
        print("Tema: Calor Sensível e Calor Latente")
        print("1. O que acontece com a temperatura de um corpo quando ele recebe calor sensível?") 
        print("a) A temperatura muda.") 
        print("b) A temperatura fica igual.") 
        print("c) A temperatura zera.") 
        print("d) O corpo desaparece.") 
        print("e) O corpo vira gás imediatamente.") 
        
        facil_1 = input("\nQual das alternativas está correta?\n| DIGITE [A/B/C/D/E] | [P] PLATEIA | [U] UNIVERSITÁRIOS |\n\n👤 ").strip().upper() 
        
        if facil_1 == 'P': 
            if Ajuda_d_plateia > 0: 
                Ajuda_d_plateia -= 1 
                input("\n🎤 Você pediu a ajuda da Plateia: \n| ENTER |") 
                print("🥸 Calor sensível serve justamente para mudar o termômetro! É a (A)!") 
                print("🥸 Com certeza a temperatura muda, alternativa (A)!\n") 
                continue 
            else: 
                input("\n⚠️ Você não tem mais ajudas da Plateia! | ENTER |") 
                continue 
        elif facil_1 == 'U': 
            if Ajuda_dos_Uni > 0: 
                Ajuda_dos_Uni -= 1 
                input("\n🎤 Você pediu a ajuda dos Universitários: \n| ENTER |") 
                print("🎓 O calor sensível provoca variação térmica no sistema sem alterar seu estado. Resposta (A).\n") 
                continue 
            else: 
                input("\n⚠️ Você não tem mais ajudas dos Universitários! | ENTER |") 
                continue 
        elif facil_1 == 'A': 
            print("\n✅ CORRETA! Parabéns, você ganhou 💵 2.000,00\n") 
            return True 
        else: 
            print("\n❌ ERRADA! Você perdeu tudo e saiu com 💵 0,00") 
            sys.exit()

def pergunta_facil_2():
    global Ajuda_d_plateia
    global Ajuda_dos_Uni
    while True: 
        print("\n=== NÍVEL 2 - MEDIANO ===") 
        print("Tema: Calor Sensível e Calor Latente")
        print("2. O calor latente é aquele que faz o corpo mudar de:") 
        print("a) Cor") 
        print("b) Estado físico (como o gelo derreter)") 
        print("c) Tamanho da sombra") 
        print("d) Nome") 
        print("e) Peso na Lua") 
        
        facil_2 = input("\nQual das alternativas está correta?\n| DIGITE [A/B/C/D/E] | [P] PLATEIA | [U] UNIVERSITÁRIOS |\n\n👤 ").strip().upper() 
        
        if facil_2 == 'P': 
            if Ajuda_d_plateia > 0: 
                Ajuda_d_plateia -= 1 
                input("\n🎤 Você pediu a ajuda da Plateia: \n| ENTER |") 
                print("🥸 Latente lembra derretimento ou fervura! É a (B)!") 
                print("🥸 Sem dúvida é o estado físico, alternativa (B)!\n") 
                continue 
            else: 
                input("\n⚠️ Você não tem mais ajudas da Plateia! | ENTER |") 
                continue 
        elif facil_2 == 'U': 
            if Ajuda_dos_Uni > 0: 
                Ajuda_dos_Uni -= 1 
                input("\n🎤 Você pediu a ajuda dos Universitários: \n| ENTER |") 
                print("🎓 Calor latente quebra as ligações intermoleculares, gerando mudança de fase. Resposta (B).\n") 
                continue 
            else: 
                input("\n⚠️ Você não tem mais ajudas dos Universitários! | ENTER |") 
                continue 
        elif facil_2 == 'B': 
            print("\n✅ CORRETA! Parabéns, você acumulou 💵 4.000,00\n") 
            return True 
        else: 
            print("\n❌ ERRADA! Você perdeu tudo e saiu com 💵 0,00") 
            sys.exit()

def pergunta_facil_3():
    global Ajuda_d_plateia
    global Ajuda_dos_Uni
    while True: 
        print("\n=== NÍVEL 2 - MEDIANO ===") 
        print("Tema: Calor Sensível e Calor Latente")
        print("3. Quando colocamos água no fogo e a temperatura dela começa a subir,\n"
              "ela está recebendo que tipo de calor?") 
        print("a) Calor Sensível") 
        print("b) Calor Latente") 
        print("c) Calor Frio") 
        print("d) Calor Invisível") 
        print("e) Calor Congelante") 
        
        facil_3 = input("\nQual das alternativas está correta?\n| DIGITE [A/B/C/D/E] | [P] PLATEIA | [U] UNIVERSITÁRIOS |\n\n👤 ").strip().upper() 
        
        if facil_3 == 'P': 
            if Ajuda_d_plateia > 0: 
                Ajuda_d_plateia -= 1 
                input("\n🎤 Você pediu a ajuda da Plateia: \n| ENTER |") 
                print("🥸 Se a temperatura está subindo e mudando, é a letra (A)!") 
                print("Vai na (A) de Calor Sensível que está certo!\n") 
                continue 
            else: 
                input("\n⚠️ Você não tem mais ajudas da Plateia! | ENTER |") 
                continue 
        elif facil_3 == 'U': 
            if Ajuda_dos_Uni > 0: 
                Ajuda_dos_Uni -= 1 
                input("\n🎤 Você pediu a ajuda dos Universitários: \n| ENTER |") 
                print("🎓 Se a água continua líquida mas fica mais quente, o calor absorvido é o sensível. Letra (A).\n") 
                continue 
            else: 
                input("\n⚠️ Você não tem mais ajudas dos Universitários! | ENTER |") 
                continue 
        elif facil_3 == 'A': 
            print("\n✅ CORRETA! Parabéns, você acumulou 💵 6.000,00\n") 
            return True 
        else: 
            print("\n❌ ERRADA! Você perdeu tudo e saiu com 💵 0,00") 
            sys.exit()

def pergunta_facil_4():
    global Ajuda_d_plateia
    global Ajuda_dos_Uni
    while True: 
        print("\n=== NÍVEL 2 - MEDIANO ===") 
        print("Tema: Calor Sensível e Calor Latente")
        print("4. Qual é o nome do processo em que o gelo vira água líquida ao receber calor latente?") 
        print("a) Vaporização") 
        print("b) Solidificação") 
        print("c) Fusão") 
        print("d) Congelamento") 
        print("e) Sublimação direta") 
        
        facil_4 = input("\nQual das alternativas está correta?\n| DIGITE [A/B/C/D/E] | [P] PLATEIA | [U] UNIVERSITÁRIOS |\n\n👤 ").strip().upper() 
        
        if facil_4 == 'P': 
            if Ajuda_d_plateia > 0: 
                Ajuda_d_plateia -= 1 
                input("\n🎤 Você pediu a ajuda da Plateia: \n| ENTER |") 
                print("🥸 Derreter o gelo cientificamente se chama fusão! Alternativa (C)!") 
                print("🥸 Com certeza é a (C), o processo de Fusão!\n") 
                continue 
            else: 
                input("\n⚠️ Você não tem mais ajudas da Plateia! | ENTER |") 
                continue 
        elif facil_4 == 'U': 
            if Ajuda_dos_Uni > 0: 
                Ajuda_dos_Uni -= 1 
                input("\n🎤 Você pediu a ajuda dos Universitários: \n| ENTER |") 
                print("🎓 A transição da fase sólida para a fase líquida é denominada fusão. Resposta (C).\n") 
                continue 
            else: 
                input("\n⚠️ Você não tem mais ajudas dos Universitários! | ENTER |") 
                continue 
        elif facil_4 == 'C': 
            print("\n✅ CORRETA! Parabéns, você acumulou 💵 8.000,00\n") 
            return True 
        else: 
            print("\n❌ ERRADA! Você perdeu tudo e saiu com 💵 0,00") 
            sys.exit()

def pergunta_facil_5():
    global Ajuda_d_plateia
    global Ajuda_dos_Uni
    while True: 
        print("\n=== NÍVEL 2 - MEDIANO ===") 
        print("Tema: Calor Sensível e Calor Latente")
        print("5. Se um corpo ganha calor e a sua temperatura aumenta, o que acontece se ele perder calor?") 
        print("a) A temperatura aumenta mais.") 
        print("b) A temperatura diminui.") 
        print("c) A temperatura fica congelada.") 
        print("d) Nada acontece.") 
        print("e) Ele explode espontaneamente.") 
        
        facil_5 = input("\nQual das alternativas está correta?\n| DIGITE [A/B/C/D/E] | [P] PLATEIA | [U] UNIVERSITÁRIOS |\n\n👤 ").strip().upper() 
        
        if facil_5 == 'P': 
            if Ajuda_d_plateia > 0: 
                Ajuda_d_plateia -= 1 
                input("\n🎤 Você pediu a ajuda da Plateia: \n| ENTER |") 
                print("🥸 Perder calor significa que o corpo está esfriando. Letra (B)!") 
                print("🥸 Vai na alternativa (B) que a temperatura diminui!\n") 
                continue 
            else: 
                input("\n⚠️ Você não tem mais ajudas da Plateia! | ENTER |") 
                continue 
        elif facil_5 == 'U': 
            if Ajuda_dos_Uni > 0: 
                Ajuda_dos_Uni -= 1 
                input("\n🎤 Você pediu a ajuda dos Universitários: \n| ENTER |") 
                print("🎓 A perda de energia térmica (calor) reduz a energia cinética das moléculas, diminuindo a temperatura. Letra (B).\n") 
                continue 
            else: 
                input("\n⚠️ Você não tem mais ajudas dos Universitários! | ENTER |") 
                continue 
        elif facil_5 == 'B': 
            print("\n✅ CORRETA! Parabéns, você venceu o jogo e faturou o prêmio máximo! 💵 10.000,00\n") 
            return True 
        else: 
            print("\n❌ ERRADA! Você perdeu tudo e saiu com 💵 0,00") 
            sys.exit()

# Início do programa principal executando as funções em ordem

pergunta_facil_1()
pergunta_facil_2()
pergunta_facil_3()
pergunta_facil_4()
pergunta_facil_5()

def RESPOSTAS_PERGUNTA_1 ():
    
    # VARIAVEIS GLOBAL PARA AS AJUDAS
    global Ajuda_da_pessoas
    global Ajuda_dos_Universitarios

    while True:
        print (input("=== NIVEL 3 - INTERMEDIARIO ==="))
        print (input("Tema: Transformações dos Gases"))
        pergunta_1_resposta = (input(" 🎤 PERGUNTA 1: Na transformação isotérmica, a temperatura do gás?: \n\n  Alternativa (A) Aumenta \n  Alternativa (B) Diminui \n  Alternativa (C) Fica constante \n  Alternativa (D) Some \n\n | PARA RESPONDER DIGITE [A/B/C/D] | \n | PARA CHAMAR A 🥸  PLATEIA PRESSIONE [P] | \n | PARA CHAMAR OS 🎓 UNIVERSITARIOS PRESSIONE [U] | \n\n | DIGITE A ALTERNATIVA MAIS ENTER PARA CONTINUAR | \n\n 👤 "))
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
            print("💵 Você ganhou 20,000 reais!\n")
            break
        # RESPOSTAS ERRADAS
        elif pergunta_1_resposta in ["A", "B", "D"] or ["a" , "b" , "d"]:
            print("\n❌ ERRADA!")
            print("💀 Você perdeu tudo!\n")
            exit()
        else:
            print("\n❌ Resposta inválida!\n")
            exit () 
            
      

RESPOSTAS_PERGUNTA_1()

print (input("\n 🎤 Parabéns " + nome_usuario + ", você acertou a primeira pergunta e já tem 💵 75,000 reais acumulados! \n\n | TECLE ENTER PARA CONTINUAR | \n"))



def RESPOSTAS_PERGUNTA_2():

    global Ajuda_da_pessoas
    global Ajuda_dos_Universitarios

    while True:

        pergunta_2_resposta = input("🎤 PERGUNTA 2: Se um gás é apertado (comprimido), o seu volume:?\n\n Alternativa (A) A) Aumenta \n Alternativa (B) Diminui \n Alternativa (C) Não muda \n Alternativa (D) Explode \n\n | DIGITE [A/B/C/D] | \n | PLATEIA [P] | \n | UNIVERSITARIOS [U] | \n\n | DIGITE A ALTERNATIVA MAIS ENTER PARA CONTINUAR | \n\n 👤 ")
            
        # AJUDA DA PLATEIA
        if pergunta_2_resposta == "P" or pergunta_2_resposta == "p":
            if Ajuda_da_pessoas > 0:
                Ajuda_da_pessoas -= 1

                print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | TECLE ENTER PARA CONTINUAR | "))
                print (" 🥸  É Alternativa (B)! \n 🥸  Claro que é (B)! \n 🥸  Obvio que é (D)! \n\n")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))
            

            else:
                print("\n❌ Você não possui mais ajuda da plateia!\n")

        # AJUDA DOS UNIVERSITARIOS
        elif pergunta_2_resposta == "U" or pergunta_2_resposta == "u":

            if Ajuda_dos_Universitarios > 0:
                Ajuda_dos_Universitarios -= 1

                print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | TECLE ENTER PARA CONTINUAR | "))
                print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (B) \n\n ")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

            else:
                print("\n❌ Você não possui mais ajuda dos universitários!\n")

        # RESPOSTA CERTA
        elif pergunta_2_resposta == "B" or pergunta_2_resposta == "b":

            print("\n✅ CORRETA!")
            print("💵 Você ganhou mais 20,000 reais!\n")
            break

        # RESPOSTAS ERRADAS
        elif pergunta_2_resposta in ["A", "C", "D"] or ["a" , "c" , "d"]:

            print("\n❌ ERRADA!")
            print("💀 Você perdeu tudo!\n")
            exit()

        else:
            print("\n❌ Resposta inválida!\n")
            exit()
RESPOSTAS_PERGUNTA_2()

print (input("\n 🎤 Parabéns " + nome_usuario + ", você acertou a segunda pergunta e já tem 💵 95,000 reais acumulados! \n\n | TECLE ENTER PARA CONTINUAR | \n"))


def RESPOSTAS_PERGUNTA_3():
    global Ajuda_da_pessoas
    global Ajuda_dos_Universitarios

    while True:
        pergunta_3_resposta = input("🎤 PERGUNTA 3: Na transformação isobárica, o que não muda?:\n\n Alternativa (A) Volume \n Alternativa (B) Temperatura \n Alternativa (C) Pressão \n Alternativa (D) Massa \n\n | DIGITE [A/B/C/D] | \n | PLATEIA [P] | \n | UNIVERSITARIOS [U] | \n\n | DIGITE A ALTERNATIVA MAIS ENTER PARA CONTINUAR | \n\n 👤 ")
        # AJUDA DA PLATEIA
        if pergunta_3_resposta == "P" or pergunta_3_resposta == "p":

            if Ajuda_da_pessoas > 0:
                Ajuda_da_pessoas -= 1

                print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | TECLE ENTER PARA CONTINUAR | "))
                print (" 🥸  É Alternativa (C)! \n 🥸  Claro que é (C)! \n 🥸  Obvio que nao é (A)! \n\n")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

            else:
                print("\n❌ Você não possui mais ajuda da plateia!\n")
        # AJUDA DOS UNIVERSITARIOS
        elif pergunta_3_resposta == "U" or pergunta_3_resposta == "u":
            if Ajuda_dos_Universitarios > 0:
                Ajuda_dos_Universitarios -= 1

                print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | TECLE ENTER PARA CONTINUAR | "))
                print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (C) \n\n ")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

            else:
                print("\n❌ Você não possui mais ajuda dos universitários!\n")
        # RESPOSTA CERTA
        elif pergunta_3_resposta == "C" or pergunta_3_resposta == "c":

            print("\n✅ CORRETA!")
            print("💵 Você ganhou mais 20,000 reais!\n")
            break
        # RESPOSTAS ERRADAS
        elif pergunta_3_resposta in ["B", "A", "D"] or ["b" , "a" , "d"]:

            print("\n❌ ERRADA!")
            print("💀 Você perdeu tudo!\n")
            exit()

        else:
            print("\n❌ Resposta inválida!\n")
            exit()
RESPOSTAS_PERGUNTA_3()
print (input("\n 🎤 Parabéns " + nome_usuario + ", você acertou a terceira pergunta e já tem 💵 115,000 reais acumulados! \n\n | TECLE ENTER PARA CONTINUAR | \n"))


def RESPOSTAS_PERGUNTA_4():
    global Ajuda_da_pessoas
    global Ajuda_dos_Universitarios

    while True:
        pergunta_4_resposta = input("🎤 PERGUNTA 4: Se um gás esquenta e o volume não muda, a pressão?:\n\n Alternativa (A) Aumenta \n Alternativa (B) Diminui \n Alternativa (C) Não muda \n Alternativa (D) Desaparece  \n\n | DIGITE [A/B/C/D] | \n | PLATEIA [P] | \n | UNIVERSITARIOS [U] | \n\n | DIGITE A ALTERNATIVA MAIS ENTER PARA CONTINUAR | \n\n 👤 ")
     #   AJUDA DA PLATEIA
        if pergunta_4_resposta == "P" or pergunta_4_resposta == "p":
            if Ajuda_da_pessoas > 0:
                Ajuda_da_pessoas -= 1

                print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | TECLE ENTER PARA CONTINUAR | "))
                print (" 🥸  É Alternativa (A)! \n 🥸  Claro que é (A)! \n 🥸  Obvio que nao é (C)! \n\n")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

            else:
                print("\n❌ Você não possui mais ajuda da plateia!\n")
        # AJUDA DOS UNIVERSITARIOS
        elif pergunta_4_resposta == "U" or pergunta_4_resposta == "u":
            if Ajuda_dos_Universitarios > 0:
                Ajuda_dos_Universitarios -= 1

                print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | TECLE ENTER PARA CONTINUAR | "))
                print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (A) \n\n ")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

            else:
                print("\n❌ Você não possui mais ajuda dos universitários!\n")
        # RESPOSTA CERTA
        elif pergunta_4_resposta == "A" or pergunta_4_resposta == "a":

            print("\n✅ CORRETA!")
            print("💵 Você ganhou mais 20,000 reais!\n")
            break
        # RESPOSTAS ERRADAS
        elif pergunta_4_resposta in ["B", "C", "D"] or ["b" , "c" , "d"]:
            print("\n❌ ERRADA!")
            print("💀 Você perdeu tudo!\n")
            exit()
        else:
            print("\n❌ Resposta inválida!\n")
            exit()
RESPOSTAS_PERGUNTA_4()
print (input("\n 🎤 Parabéns " + nome_usuario + ", você acertou a quarta pergunta e já tem 💵 135,000 reais acumulados! \n\n | TECLE ENTER PARA CONTINUAR | \n"))


def RESPOSTAS_PERGUNTA_5():
    global Ajuda_da_pessoas
    global Ajuda_dos_Universitarios

    while True:
        pergunta_5_resposta = input ("🎤 PERGUNTA 5:Na transformação isovolumétrica, o volume do gás?:\n\n Alternativa (A) Aumenta \n Alternativa (B) Diminui \n Alternativa (C) Vira líquido \n Alternativa (D) Fica igual  \n\n | DIGITE [A/B/C/D] | \n | PLATEIA [P] | \n | UNIVERSITARIOS [U] | \n\n | DIGITE A ALTERNATIVA MAIS ENTER PARA CONTINUAR | \n\n")
        # AJUDA DA PLATEIA
        if pergunta_5_resposta == "P" or pergunta_5_resposta == "p":
            if Ajuda_da_pessoas > 0:
                Ajuda_da_pessoas -= 1

                print (input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não tem certeza de qual seja a certa então boa sorte! \n\n | TECLE ENTER PARA CONTINUAR | "))
                print (" 🥸  É Alternativa (D)! \n 🥸  Claro que é (D)! \n 🥸  Obvio que nao é (B)! \n\n")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

            else:
                print("\n❌ Você não possui mais ajuda da plateia!\n")
        # AJUDA DOS UNIVERSITARIOS
        elif pergunta_5_resposta == "U" or pergunta_5_resposta == "u":
            if Ajuda_dos_Universitarios > 0:
                Ajuda_dos_Universitarios -= 1

                print (input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que eles dirão \n\n | TECLE ENTER PARA CONTINUAR | "))
                print (" 🎓  Temos certeza de que todas estão erradas \n Menos a alternativa (D) \n\n ")
                print (input(" 🎤 " + nome_usuario + ", Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | ENTER PARA VER NOVAMENTE AS RESPOSTAS | \n"))

            else:
                print("\n❌ Você não possui mais ajuda dos universitários!\n")
        # RESPOSTA CERTA
        elif pergunta_5_resposta == "D" or pergunta_5_resposta == "d":

            print("\n✅ CORRETA!")
            print("💵 Você ganhou mais 20,000 reais!\n")
            break

        # RESPOSTAS ERRADAS
        elif pergunta_5_resposta in ["A", "C", "B"] or ["a" , "c" , "b"]:
            print("\n❌ ERRADA!")
            print("💀 Você perdeu tudo!\n")
            exit()

        else:
            print("\n❌ Resposta inválida!\n")
            exit()
RESPOSTAS_PERGUNTA_5()
print (input("\n 🎤 Parabéns " + nome_usuario + ", você acertou a quinta pergunta e já tem 💵 155,000 reais acumulados! \n\n | TECLE ENTER PARA CONTINUAR | \n"))
print (input(" 🎤Agora vamos para o proximo bloco Agora as perguntas vão ser um pouco mais dificeis \n\n | TECLE ENTER PARA CONTINUAR | \n"))




