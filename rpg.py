# História de "Garras e Unhas."

from os import system

# Tela de Boas-Vindas do usuário ----------------------------------------------------------------------------------------------------------------------
system("cls")
print("Olá meu amigo, antes da nossa aventura começar, qual o seu nome? ʕ•́ᴥ•̀ʔっ♡ ")
nome = input()
system("cls")
print(f"{f'Olá {nome}, seja muito bem vindo(a) ao KeYa History!' : ^140}")
print(f"{'Este é um RPG em produção, com primeiramente apenas uma história.' : ^140}")
print(f"{'Futuramente irei adicionando cada vez mais, dependendo da minha força de vontade e determinação XD' : ^140}")
print(f"{'Por mais é isso... Sem mais enrolação, vamos lá!' : ^140}")
print(f"{'-' * 50 : ^140}")
print(f"{'Jogo feito por KeaK, história feita por TLC e KeaK.' : ^140}")
input(f"{'Aperte Enter para continuar.' : ^140}")
system("cls")

# Introdução do personagem principal --------------------------------------------------------------------------------------------------------------
print("Seu nome é Kauan, onde seu pai se chama Wilian, líder de um clã chamado 'Ak', e sua mãe chamada Helena, atual esposa dele.")
print("Sua infância toda foi ser o oposto das ideias de seu pai, você nunca chegou a ter um preconceito contra os ferais, onde, a vida toda você") 
print("foi lecionado a fazer o contrário.")
print("Você teve uma amiga de infância onde você não lembra o rosto nem o nome... Apenas que era chamado carinhosamente de 'Ka'.")
input()
system("cls")

# Introdução (Cutscene) ---------------------------------------------------------------------------------------------------------------------------
print(f"{'Garras e Unhas.' : ^140}")
print(f"{'Brasil, 1990.' : ^140}")
print()
print("     A rivalidade entre humanos e ferais*, sempre foi algo crescente e normalizado entre a sociedade... Mesmo com semelhanças, os humanos só apontavam as diferenças de acordo com suas")
print("crenças, os tão chamados de 'bestas do demônio', 'pulgentos', 'selvagens' e etc...\n")
print("-"*50)
print("Curiosidade: 'Ferais' segue o mesmo raciocínio de Furrys, antropomórficos onde representa características físicas dependendo do animal.")
input()
system("cls")
print("Então, um certo dia, no destemido 'Clã Ak', o dono havia passado a liderança para seu filho, Kauan, onde faz um novo alistamento... Com uma regra nova, permitido ferais.\n")
input()
print("Em toda a sua história, sempre teve um histórico famoso de ser totalmente contra a essas espécies, maltratando, matando-os, etc, gerando o motivo da grande confusão dessa liberação.")
input("Aperte Enter para continuar...")
system("cls")

# Transição de cenário -----------------------------------------------------------------------------------------------------------------------------
print(f"{'NA ÁREA DE ALISTAMENTO.' : ^140}")
input("Aperte Enter para continuar...")
system("cls")

# Começo do desenvolvimento -------------------------------------------------------------------------------------------------------------------------
input("Kauan — Próximo!")
input("[Chega um indivíduo de ali, de no mínimo 1,70 de altura com uma capa preta, que de certa forma era bem intimidador.]\n")
input("Kauan — Documentos e ficha de inscrição por favor.\n")
input("? — [Apenas pega o papel, que estava todo amassado, e entrega diretamente do comandante.]\n")
input("Você olha indignado pela ousadia daquele ser, apenas respira profundamente antes de fazer qualquer ação.]\n")
input("(Olhando ficha)")
system("cls")

print("—————————————————————————————————————————————————")
print("// Nome:                                         \\")
print("| Luca.                                         |")
print("\\-----------------------------------------------//")
print("| Idade:                                        |")
print("// 20 anos.                                      \\")
print("|-----------------------------------------------|")
print("\\ Estado Civil:                                 //")
print("\\ Solteiro.                                     //")
print("|-----------------------------------------------|")
print("\\ Relação com a família:                        //")
print("// Orfão.                                        \\")
print("|-----------------------------------------------|")
print("\\ Já participou de outros clãs?                 //")
print("// Já.                                           \\")
print("|-----------------------------------------------|")
print("| Quais?                                        /")
print("| Prefiro não dizer.                            \\")
print("|-----------------------------------------------|\n")

input("Você analisa aquela ficha bastante incrédulo, pois além estar com a folha toda amassada, ainda ter informações não completas.")
system("cls")

print(f"{'Você chegou em um novo momento, as escolhas!' : ^140}")
print(f"{'Apenas digite o número que deseja fazer a opção.' : ^140}")
print(f"{'Fique ciente que cada escolha que você possa fazer, irá interferir completamente o furuto.' : ^140}")
input()
system("cls")

while True:
    print("[ 1 ] - ...Tá.")
    print("[ 2 ] - ...")
    print("[ 3 ] - Você está de brincadeira com a minha cara né?")
    opcao1 = int(input())
    system("cls")

    if opcao1 == 1:
        input("Nada é feito contra você.\n")
        input("Você apenas pega a ficha e deixa junto com as outras.\n")
        input("Kauan - Fique atento caso seja aprovado, você ficará sabendo do status da aprovação através da mesma forma que ficou sabendo do recrutamento.\n")
        input("Luca apenas concorda, dá meia volta e vai embora.")

    elif opcao1 == 2:
        input("Nada é feito contra você.")
        input("Fica um silêncio completamente pertubador, porém você decide deixar a ficha junto com as outras.\n")
        input("Luca te encara completamente confuso por ter tido o silêncio como reação, porem não te demonstra diretamente.\n")
        input("Kauan - Apenas fique atento caso seja aprovado, você ficará sabendo do status da aprovação através da mesma forma que ficou sabendo do recrutamento.\n")
        input("Luca apenas concorda, dá meia volta e vai embora.\n")

    elif opcao1 == 3:
        input("Nada é feito contra você, porém, a forma como ele te olha muda drasticamente.")
        input("Luca - Como é?")
        input("Kauan - Isso aí mesmo, você está de brincadeira? Está fazendo perder completamente meu tempo!")
        input("Luca fecha suas mãos se tremendo um pouco de raiva, porém respira bem fundo e acaba se acalmando na hora.")

    else:
        print("Opção inválida, tente novamente.")
        input("Aperte Enter para continuar...")
        system("cls")
        