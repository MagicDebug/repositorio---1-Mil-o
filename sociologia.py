import sys  # 🔌 Importa o sistema nativo para conseguir fechar o jogo imediatamente se o jogador errar!

# =====================================================================
# 👥 SELEÇÃO DA MATÉRIA: (6) SOCIOLOGIA
# =====================================================================
if Máteria_selecionada == "6":

    # 🎬 [NARRAÇÃO DO DIRETOR]: O show vai começar! Aqui nós preparamos os motores do game,
    # configurando o estoque de ajudas e zerando o cofre de dinheiro do participante.
    Ajuda_d_plateia = 5        # 🥸 Quantidade de cartadas que o jogador tem com o público
    Ajuda_dos_Uni = 3          # 🎓 Quantidade de vezes que ele pode acionar os crânios da faculdade
    Valor_Acumulado = 0.0      # 💰 Cofre zerado, o participante começa sem nenhum tostão!
    jogando = True             # 🟢 Chave de ignição: enquanto for True, o show não para.

    # 🎭 MENU INICIAL & BOAS-VINDAS RECHEADO DE EMOJIS 🎉
    print("=====================================================================")
    print("🎤 🔥 👑 🤖 BEM-VINDO AO COLISEU DO CONHECIMENTO: CYBER MIND 🤖 👑 🔥 🎤")
    print("=====================================================================\n")

    # 🎬 [NARRAÇÃO DO DIRETOR]: Hora de abrir o microfone para o jogador se identificar.
    # Criamos uma mini-função isolada só para capturar esse momento solene.
    def obter_nome():
        nome = input("🚀 PARA DAR INÍCIO À SUA JORNADA, DIGITE SEU NOME E APERTE [ENTER]: ")
        return nome

    # 📥 Chamamos a função e carimbamos o nome do jogador na tela!
    nome_usuario = obter_nome()

    # 📜 EXIBIÇÃO DAS REGRAS DO JOGO
    print("\n=====================================================================")
    print(f"📜 👑 📑 REGRAS DO JOGO CYBER MIND - {nome_usuario.upper()} 👑 📑 📜")
    print("=====================================================================")
    print("1. 🛑 O jogo é composto por 5 blocos de dificuldades crescentes mais a Pergunta Final.")
    print("2. 🔠 Responda usando apenas as letras maiúsculas ou minúsculas [A, B, C, D].")
    print("3. 💀 Errar qualquer pergunta limpa o seu saldo e resulta em GAME OVER imediato.")
    print(f"4. 🥸  Você tem direito a {Ajuda_d_plateia} Ajudas da Plateia [P] para quando bater a dúvida.")
    print(f"5. 🎓 Você tem direito a {Ajuda_dos_Uni} Ajudas dos Universitários [U] para respostas cirúrgicas.")
    print("6. 💸 Ao responder a Pergunta 25, você poderá escolher PARAR ou CONTINUAR para o Milhão.")
    print("=====================================================================\n")

    print(input("🎤 Vamos dar início ao primeiro Tema: Objeto de estudo e o nascimento da Sociologia 🚀 \n\n  | 🆙 TECLE ENTER PARA CONTINUAR E IR AO PALCO | \n"))

    # =====================================================================
    # 🛠️ FUNÇÃO MASTER DE PROCESSAMENTO DE RESPOSTAS E AJUDAS
    # =====================================================================
    # 🎬 [NARRAÇÃO DO DIRETOR]: Esta é a "Função Master"! É o coração mecânico do jogo.
    # Toda pergunta que você criar no futuro vai passar por aqui dentro deste super 'while True'.
    # Ela controla o input do teclado, valida se a resposta tá certa, gasta as ajudas e dá Game Over!
    def RESPOSTAS_f(numero, enunciado, alternativas, alternativa_correta, valor):
        global Ajuda_d_plateia
        global Ajuda_dos_Uni
        global nome_usuario
        global Valor_Acumulado

        while True:
            # ✨ Imprime o painel de valores atualizado dinamicamente para o público chorar de emoção
            print("\n=====================================================================")
            print(f"💰 🔥 VALENDO AGORA NO CYBER MIND: 💵 R$ {valor:,.2f} Reais! 💵")
            print("=====================================================================")
            print(f"\n 📝 PERGUNTA {numero} 📝")
            print(f"\n 🎤 {enunciado}\n")

            # ✨ Mostra o leque de opções de A até D na tela
            for letra, texto in alternativas.items():
                print(f"  🍀 Alternativa ({letra}) {texto}")

            # ✨ Captura a jogada da pessoa e joga tudo para MAIÚSCULO para evitar bugs de digitação
            resposta = input(
                f"\n 📑 | RESPONDA [A/B/C/D] |"
                f"\n 🥸  | PLATEIA [P] (Restam: {Ajuda_d_plateia}) |"
                f"\n 🎓  | UNIVERSITÁRIOS [U] (Restam: {Ajuda_dos_Uni}) |"
                f"\n\n 👤 SUA DECISÃO: "
            ).upper()

            # 🎬 [NARRAÇÃO DO DIRETOR]: O jogador amarelou e pediu socorro para a plateia! 
            # O sistema verifica o estoque e, se tiver saldo, cospe três palpites na tela (com duas certezas).
            if resposta == "P":
                if Ajuda_d_plateia > 0:
                    print(input("\n 🎤 Você pediu a ajuda da Plateia: \n Eles não têm certeza de qual seja a certa então boa sorte! ✨ \n\n | 🆙 TECLE ENTER PARA OUVIR O COCHICHO DO POVO | "))
                    print(f" 🥸  Antônio cochicha: Ei, eu acho que é Alternativa ({alternativa_correta})! \n 🥸  Maria grita: Claro que é ({alternativa_correta})! \n 🥸  João chuta: Com certeza absoluta que é ({alternativa_correta})!\n\n")
                    print(input(f" 🎤 {nome_usuario}, Após receber a ajuda da Plateia: \n diga qual é a alternativa correta \n\n | [ENTER] PARA VER NOVAMENTE AS ALTERNATIVAS NA TELA | \n"))
                    Ajuda_d_plateia -= 1 # 📉 Consome 1 ponto de ajuda do estoque
                else:
                    print("\n ❌ Ih, caramba! Você não possui mais ajudas da plateia nesta noite!")

            # 🎬 [NARRAÇÃO DO DIRETOR]: O jogador acionou os Universitários.
            # Os crânios acadêmicos entram em cena e dão a resposta 100% mastigada na bandeja.
            elif resposta == "U":
                if Ajuda_dos_Uni > 0:
                    print(input("\n 🎤 Você pediu a ajuda dos Universitários: \n Veja o que os nossos crânios dirão 🧠 \n\n | 🆙 TECLE ENTER PARA ENTRAR NA LINHA COM A FACULDADE | "))
                    print(f" 🎓  Analisamos os dados sociológicos e temos certeza de que a resposta certa é a alternativa ({alternativa_correta}) !! \n\n ")
                    print(input(f" 🎤 {nome_usuario}, Após receber a ajuda dos Universitários: \n diga qual é a alternativa correta \n\n | [ENTER] PARA REVER O PAINEL DE RESPOSTAS | \n"))
                    Ajuda_dos_Uni -= 1 # 📉 Consome 1 ponto de ajuda do estoque
                else:
                    print("\n ❌ O tempo de consulta acabou! Você não possui mais ajudas dos universitários!")

            # 🎬 [NARRAÇÃO DO DIRETOR]: Momento de extrema tensão! O participante digitou uma letra de resposta.
            # O motor avalia se bate com a 'alternativa_correta' enviada pela produção.
            elif resposta in ["A", "B", "C", "D"]:
                if resposta == alternativa_correta:
                    print("\n ✅ EXATA! PARABÉNS!!! O COLISEU VEM ABAIXO!!! ✅")
                    Valor_Acumulado = valor  # 💰 Atualiza o prêmio corrente na carteira do jogador
                    print(f"💵 🎉 Saldo Atual trancado no cofre: R$ {Valor_Acumulado:,.2f} reais!\n")
                    break # 🔓 Rompe o loop 'while' e autoriza o script a ir para a próxima pergunta!
                else:
                    # 💀 Tragédia no palco! Resposta errada limpa o dinheiro todo e mata a execução do código na hora.
                    print("\n ❌ !!!ERRADA DE FORMA ESTRONDOSA!!! ❌")
                    print(" 💀 GAME OVER! O SEU SALDO FOI ZERADO E VOCÊ SAI DE MÃOS VAZIAS!")
                    Valor_Acumulado = 0.0
                    sys.exit() # 🛑 Desliga o programa imediatamente!
            else:
                # ⚠️ Tratamento de erro básico caso o usuário aperte qualquer tecla inválida do teclado.
                print("\n ⚠️ Comando inválido! Digite apenas A, B, C, D, P ou U.")
        return True

    # =====================================================================
    # 🟢 BLOCO 1 - PERGUNTAS FÁCEIS
    # =====================================================================
    # 🎬 [NARRAÇÃO DO DIRETOR]: Começa o aquecimento! Perguntas nível introdução para dar confiança.
    if jogando: jogando = RESPOSTAS_f(1, "Qual é o principal objeto de estudo da Sociologia enquanto ciência? 🏢",
        {"A": "O comportamento individual e os processos biológicos do cérebro.",
         "B": "As relações sociais, as estruturas e as instituições que formam a sociedade.",
         "C": "A evolução física das espécies e os ecossistemas naturais.",
         "D": "O funcionamento do mercado financeiro e a economia de ações."}, "B", 100)
    
    if jogando: jogando = RESPOSTAS_f(2, "Qual filósofo francês é historicamente considerado o pai do Positivismo e o responsável por cunhar o termo Sociologia? 🧔",
        {"A": "Auguste Comte", "B": "Karl Marx", "C": "Max Weber", "D": "Émile Durkheim"}, "A", 200)
        
    if jogando: jogando = RESPOSTAS_f(3, "A Sociologia se diferencia do senso comum porque utiliza: 🧪",
        {"A": "Opiniões pessoais e boatos de WhatsApp.", "B": "Crenças religiosas e misticismo.", "C": "Método científico e pesquisa empírica.", "D": "Intuição individual e palpites."}, "C", 300)
        
    if jogando: jogando = RESPOSTAS_f(4, "Como se chama o processo pelo qual o indivíduo aprende e interioriza as normas e valores sociais? 🤝",
        {"A": "Globalização comercial", "B": "Alienação industrial", "C": "Socialização", "D": "Urbanização desenfreada"}, "C", 500)
        
    if jogando: jogando = RESPOSTAS_f(5, "As regras e costumes invisíveis ou explícitos que orientam o comportamento social são chamados de: 📑",
        {"A": "Normas sociais", "B": "Interações monetárias", "C": "Instintos biológicos puros", "D": "Fatos isolados"}, "A", 1000)

    # =====================================================================
    # 🟡 BLOCO 2 - PERGUNTAS FÁCEIS/INTERMEDIÁRIAS
    # =====================================================================
    # 🎬 [NARRAÇÃO DO DIRETOR]: O nível sobe um degrau! A plateia começa a ficar mais atenta.
    if jogando:
        print("\n=====================================================================")
        print("🟡 📈 INICIANDO: Bloco 2 - Perguntas fáceis/intermediárias 📈 🟡")
        print("=====================================================================\n")
        jogando = RESPOSTAS_f(6, "Como a Sociologia pode contribuir de forma prática para o desenvolvimento de políticas públicas? 📈",
            {"A": "Determinando leis autoritárias sem consultar a população.",
             "B": "Oferecendo diagnósticos reais baseados em dados estatísticos e sociais.",
             "C": "Mudando apenas a mente e a psicologia individual dos governantes.",
             "D": "Eliminando de vez todos os debates políticos do país."}, "B", 2000)
             
    if jogando: jogando = RESPOSTAS_f(7, "O famoso conceito de 'imaginação sociológica' permite ao estudante e cientista: 🗺️",
        {"A": "Isolar completamente os seus problemas pessoais do resto do mundo.",
         "B": "Relacionar a biografia do indivíduo com a história da estrutura social.",
         "C": "Ignorar solenemente problemas econômicos e focar no imaginário.",
         "D": "Aceitar todas as desigualdades como regras naturais da vida."}, "B", 4000)
         
    if jogando: jogando = RESPOSTAS_f(8, "Nas ciências sociais, o estudo detalhado das relações de gênero e raça promove: ✊ 🕊️",
        {"A": "O aumento de preconceitos históricos antigos.",
         "B": "O fim absoluto da organização jurídica estatal.",
         "C": "Um debate crítico e necessário sobre igualdade e direitos.",
         "D": "O isolamento social total de minorias."}, "C", 8000)
         
    if jogando: jogando = RESPOSTAS_f(9, "O método do 'estranhamento da realidade' dentro da Sociologia serve para: 🤨 👁️",
        {"A": "Desnaturalizar comportamentos sociais cotidianos e questioná-los.",
         "B": "Evitar o contato humano e promover o isolamento.",
         "C": "Aumentar o preconceito contra culturas diferentes.",
         "D": "Negar completamente a existência de conflitos sociais."}, "A", 16000)
         
    if jogando: jogando = RESPOSTAS_f(10, "A vertente teórica da Sociologia da Educação demonstra claramente que a escola: 🏫 📚",
        {"A": "É uma instituição totalmente neutra no mundo.",
         "B": "Garante o sucesso e mérito exatamente igual para todos, sem exceção.",
         "C": "Pode funcionar reproduzindo ou transformando as desigualdades sociais.",
         "D": "Depende exclusivamente do DNA e genética de cada aluno."}, "C", 32000)

    # =====================================================================
    # 🟠 BLOCO 3 - PERGUNTAS INTERMEDIÁRIAS
    # =====================================================================
    # 🎬 [NARRAÇÃO DO DIRETOR]: Atenção! Entramos no miolo do jogo. Aqui entram os clássicos da Sociologia!
    # Durkheim assume os holofotes e o bicho começa a pegar!
    if jogando:
        print("\n=====================================================================")
        print("🟠 🧩 INICIANDO: Bloco 3 - Perguntas intermediárias (Os Clássicos) 🧩 🟠")
        print("=====================================================================\n")
        jogando = RESPOSTAS_f(11, "Para o sociólogo Émile Durkheim, os fatos sociais devem ser rigorosamente tratados como: 📦",
            {"A": "Fenômenos puramente psicológicos e individuais.",
             "B": "Coisas externas ao indivíduo e dotadas de poder coercitivo.",
             "C": "Eventos aleatórios e passageiros.",
             "D": "Ideias vagas e totalmente abstratas."}, "B", 64000)
             
    if jogando: jogando = RESPOSTAS_f(12, "Quais são as três características fundamentais do Fato Social segundo Durkheim? 📐",
        {"A": "Generalidade, exterioridade e coercitividade.",
         "B": "Subjetividade, individualidade e volatilidade.",
         "C": "Afetividade, rationality e espiritualidade.",
         "D": "Espiritualidade, lucratividade e opacidade."}, "A", 80000)
         
    if jogando: jogando = RESPOSTAS_f(13, "A aplicação de punições jurídicas ou o olhar de reprovação da sociedade demonstram qual characteristic do fato social? ⚖️ 👁️",
        {"A": "Exterioridade total", "B": "Coercitividade", "C": "Generalidade estatística", "D": "Abstração filosófica"}, "B", 100000)
        
    if jogando: jogando = RESPOSTAS_f(14, "O fato de falarmos um idioma que já existia e seguirmos leis criadas antes de nascermos demonstra a: 🗣️ 📜",
        {"A": "Generalidade econômica do mercado.", "B": "Capacidade plena de livre-arbítrio absoluto.", "C": "Subjetividade moral moderna.", "D": "Exterioridade do fato social."}, "D", 120000)
        
    if jogando: jogando = RESPOSTAS_f(15, "Dentro da sociologia durkheimiana, o termo 'Anomia Social' significa: 📉 💥",
        {"A": "O perfeito equilíbrio harmônico das funções do Estado.",
         "B": "Uma situação de crise com o enfraquecimento das normas e da coesão social.",
         "C": "O fim definitivo e utópico de todos os crimes.",
         "D": "O controle familiar absoluto sobre a vida urbana."}, "B", 140000)

    # =====================================================================
    # 🔴 BLOCO 4 - PERGUNTAS DIFÍCEIS
    # =====================================================================
    # 🎬 [NARRAÇÃO DO DIRETOR]: Max Weber entra na arena! As perguntas agora exigem interpretação de texto pesada
    # e conhecimento profundo de conceitos abstratos como Ação Social.
    if jogando:
        print("\n=====================================================================")
        print("🔴 🧠 INICIANDO: Bloco 4 - Perguntas difíceis (Aprofundamento) 🧠 🔴")
        print("=====================================================================\n")
        jogando = RESPOSTAS_f(16, "Diferente de Durkheim, Max Weber estipula que o papel central da Sociologia é compreender a: 👤 🔀",
            {"A": "Estrutura econômica mecânica global.",
             "B": "Ação social, analisando o sentido subjetivo dado pelos indivíduos.",
             "C": "Evolução puramente biológica das tribos antigas.",
             "D": "Força coercitiva e imutável dos fatos fixos."}, "B", 160000)
             
    if jogando: jogando = RESPOSTAS_f(17, "Estudar exaustivamente e buscar um diploma superior apenas com a meta direta de conseguir um emprego bem remunerado é classificado por Weber como: 🎓 💼",
        {"A": "Ação racional com relação a valores humanos.",
         "B": "Ação afetiva gerada pelo calor do momento.",
         "C": "Ação racional com relação a fins.",
         "D": "Ação tradicional motivada por hábitos geracionais."}, "C", 180000)
         
    if jogando: jogando = RESPOSTAS_f(18, "Se um indivíduo participa ativamente de uma passeata estritamente por fidelidade aos seus princípios morais ou convicções políticas, sem ligar para os riscos econômicos, ele executa uma: 🪧 ✊",
        {"A": "Ação racional com relação a valores.",
         "B": "Ação tradicional mecânica.",
         "C": "Ação afetiva e apaixonada.",
         "D": "Ação racional com relação a fins lucrativos."}, "A", 200000)
         
    if jogando: jogando = RESPOSTAS_f(19, "O ato cultural de reunir toda a família para comemorar o Natal todos os anos, unicamente por ser um costume de gerações, representa para a sociologia weberiana uma: 🎄 🕯️",
        {"A": "Ação racional milimétrica.", "B": "Ação tradicional.", "C": "Ação afetiva cega.", "D": "Ação burocrática estatal."}, "B", 250000)
        
    if jogando: jogando = RESPOSTAS_f(20, "Qual é o famoso modelo de recurso abstrato e metodológico formulado por Max Weber para analisar e comparar a realidade social? 🛠️ 📐",
        {"A": "O Fato Social Ideal regulador.", "B": "O Materialismo Histórico dialético.", "C": "O Tipo Ideal.", "D": "A Consciência Coletiva mecânica."}, "C", 300000)

    # =====================================================================
    # 🟣 BLOCO 5 - PERGUNTAS AVANÇADAS
    # =====================================================================
    # 🎬 [NARRAÇÃO DO DIRETOR]: O clímax do jogo normal! Karl Marx chega quebrando tudo com a teoria da alienação.
    # Se passar daqui, o jogador bate no teto de meio milhão de reais!
    if jogando:
        print("\n=====================================================================")
        print("🟣 ⛓️ INICIANDO: Bloco 5 - Perguntas avançadas (Reta Final) ⛓️ 🟣")
        print("=====================================================================\n")
        jogando = RESPOSTAS_f(21, "Na teoria crítica de Karl Marx, a famosa 'alienação do trabalho' dentro do capitalismo ocorre prioritariamente porque: 🏭 ⛓️",
            {"A": "O trabalhador fabril não sabe ler os manuais das máquinas inglesas.",
             "B": "O trabalhador é separado, expropriado e privado da posse dos meios de produção.",
             "C": "As taxas de juros bancárias cobradas pelo Estado são muito abusivas.",
             "D": "Os salários de toda a gerência de operários são padronizados igualmente."}, "B", 350000)
             
    if jogando: jogando = RESPOSTAS_f(22, "O produto gerado pelo trabalho alienado acaba se apresentando diante do operário produtor como: 📦 ⛓️",
        {"A": "Um valioso patrimônio comunitário a ser dividido entre a vizinhança.",
         "B": "Uma mera extensão natural, leve e orgânica da sua veia artística.",
         "C": "Uma força estranha, alheia e independente que passa a dominar o próprio trabalhador.",
         "D": "Um patrimônio financeiro individual dele garantido na justiça."}, "C", 400000)
         
    if jogando: jogando = RESPOSTAS_f(23, "Devido à alienação consolidada pelo sistema de produção, o ato de trabalhar deixa de ser uma atividade humana de auto-realização e vira: 😩 🧱",
        {"A": "Um mero sacrifício penoso voltado exclusivamente para a subsistência básica.",
         "B": "Uma escada garantida e rápida de ascensão social e enriquecimento na firma.",
         "C": "Uma jornada mágica, estimulante e puramente prazerosa.",
         "D": "Um chamado de vocação religiosa pura voltada para a purificação da alma."}, "A", 450000)
         
    if jogando: jogando = RESPOSTAS_f(24, "A alienação profunda desenvolvida dentro da lógica industrial capitalista acaba provocando entre a própria classe trabalhadora: 💥 🔀",
        {"A": "Uma onda imensa de solidariedade orgânica afetiva automática.",
         "B": "A quebra e o desaparecimento total de qualquer concorrência econômica.",
         "C": "Concorrência hostil entre indivíduos, isolamento e fragmentação da classe operária.",
         "D": "A pacificação definitiva e harmoniosa de todos os conflitos."}, "C", 480000)
         
    if jogando: jogando = RESPOSTAS_f(25, "Qual conceito marxista essencial mapeia a ilusão em que as mercadorias parecem ganhar vida própria com valores mágicos, ocultando a exploração e o trabalho humano embutido nelas? 🛍️ 🔮",
        {"A": "Fetiche da mercadoria.", "B": "Tipo ideal racionalizado.", "C": "Solidariedade mecânica estrutural.", "D": "Racionalismo mercantil burocrático."}, "A", 500000)

    # =====================================================================
    # 💀 PORTAL DA PERGUNTA FINAL: EXATAMENTE DEPOIS DA 25
    # =====================================================================
    # 🎬 [NARRAÇÃO DO DIRETOR]: O ápice dramático do programa! O jogador tem 500 mil reais na mão.
    # O sistema para a engrenagem automática e faz a pergunta decisiva: Desistir e ficar rico ou arriscar tudo pelo Milhão?
    if jogando:
        print(input(f"\n 🎤 🎉 PARABÉNS {nome_usuario}! Você destruiu a pergunta 25 e conquistou impressionantes 💵 R$ {Valor_Acumulado:,.2f} reais! 🎉 💎 \n\n | 🆙 TECLE ENTER PARA DEFINIR SEU DESTINO NO PORTAL DA FORTUNA | \n"))
        print("=====================================================================")
        print("💀 🔥 👀 ATENÇÃO! ESTAMOS DIANTE DO PORTAL DA PERGUNTA DO MILHÃO 👀 🔥 💀")
        print("• Nível de dificuldade: Pergunta do Milhão - Pergunta de maior raciocínio e interpretação de sociologia contemporânea! 💀")
        print("=====================================================================\n")
        print("🎤 Lembre-se do regulamento de ferro do milhão: Se acertar você vira uma lenda e leva 1 Milhão de Reais.")
        print("💀 Se aceitar o desafio e ERRAR, a armadilha do palco cai, limpa os 500 mil e você sai sem nada!")
        
        print("\n🎤 E agora, jogador de elite? Qual vai ser o seu veredito final?")
        opcao_final = input("🎤 DIGITE [P] PARA PARAR COM MEIO MILHÃO OU [C] PARA ENFRENTAR A SOBERANA PERGUNTA DO MILHÃO \n\n 👤 SUA ESCOLHA CRUCIAL: ").upper()
        
        # 🎬 [NARRAÇÃO DO DIRETOR]: Se o jogador escolher 'P', o programa elogia a prudência dele e encerra
        # o script salvando a grana do prêmio.
        if opcao_final == "P":
            print(f"\n 🏆 💵 UMA JOGADA DE MESTRE HISTÓRICA! {nome_usuario}, você foi prudente e se retira do palco com impressionantes 💵 R$ {Valor_Acumulado:,.2f} reais! Você venceu o Cyber Mind!")
            sys.exit()

        print(input("\n 🎤 🔥 CORAGEM PURA! As cortinas de aço se abrem, os tambores rufam intensamente e a plateia prende a respiração... Vale UM MILHÃO DE REAIS! 🔥 💥 \n\n | 🆙 TECLE ENTER PARA EXIBIR A ARREPIANTE PERGUNTA DO MILHÃO | \n"))

        # Execução da Pergunta Final 26 (A pergunta do Milhão)
        jogando = RESPOSTAS_f(26, "Ao interpretar criticamente o fenômeno moderno e digital da 'Uberização do Trabalho' (aplicativos), qual alternativa traça o melhor paralelo de raciocínio unindo as lentes teóricas de Marx e de Weber? 📱 🚴 🧠",
            {"A": "Durkheim decifrava a uberização contemporânea como o auge harmônico da solidariedade mecânica das tribos rurais tradicionais.",
             "B": "Marx elucida o processo através da alienação severa do condutor e da extração contínua de mais-valia, ao passo que Weber detalha perfeitamente a racionalização técnica e burocrática executada de forma fria pelo algoritmo.",
             "C": "Weber classificava o design tecnológico e a lógica matemática dos aplicativos móveis de entrega rápidos como ação social estritamente afetiva e irracional.",
             "D": "Marx previa teoricamente que o uso de celulares e motocicletas de propriedade própria dos motoqueiros traria a emancipação revolucionária automática da categoria."}, "B", 1000000)
        
        # 🎬 [NARRAÇÃO DO DIRETOR]: Vitória Suprema! O jogador sobreviveu à Pergunta 26.
        # Soltamos os efeitos especiais finais e encerramos a exibição com chave de ouro!
        if jogando:
            print(input(f"\n 👑 🏆 💎 INACREDITÁVEL! SOLTEM OS FOGOS DE ARTIFÍCIO! PARABÉNS {nome_usuario} !!! VOCÊ DETONOU O JOGO E GANHOU O PRÊMIO MÁXIMO DE 1 MILHÃO DE REAIS! 🎉 🎉 🎉 \n\n | 🆙 TECLE ENTER PARA EXPLODIR A CASCATA DE CONFETES E ENCERRAR O SHOW 🎊 | \n"))