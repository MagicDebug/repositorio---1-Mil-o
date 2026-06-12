
import sys

# --- VARIÁVEIS GLOBAIS DE CONTROLE ---
# Alterado para os valores que você definiu nas regras
Ajuda_d_plateia = 5
Ajuda_dos_Uni = 3

# === ABERTURA DO JOGO ===
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

    

    



