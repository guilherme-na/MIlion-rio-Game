
print("*" *40)
print("bem vindo ao quem quer ser um milionário!")
print("*" *40)

entrada = input("Deseja participar?: ")
one = {"1. Yusuke Murata", "2. One", "3. Makoto Yukimura", "4. Isayama"}
csgo = {"1. LG", "2. Navi","3. Virtus Pro", "4. Astralis"}
rpg = {"1. DDtank", "2. Ragnarok Online", "3. MU Online", "4. Perfect World"}


pontos = 0

if entrada == "sim":
    print("Bem Vindo! Que os jogos começem :)")
    print("Pontos Iniciais: ", pontos)

else:
    print("Volte sempre que puder :)")
if (entrada == "sim"):
    print("Vamos começar!")
    print("1. Quem criou o mangá One Punch Man?")
    for x in one:
        print(x)
    resposta_01 = input("R: ")
   
    if resposta_01 == "One":
        print("Parabéns, Você acertou a primeira questão!")
        print("Você ganhou 3 pontos pela questão acertada. Total de pontos:", pontos+3)
    else:
        print("Você errou a primeira questão.")
        print("Você perdeu 1 ponto pela questão errada. Total de pontos: ", pontos-1)

    print("2. Qual time de CS:GO ganhou o Major Colombus de 2016?")
    for x in csgo:
        print(x)
    resposta_02 = input("R: ")

    if resposta_02 == "LG":
        print("Parabéns! Você acertou a segunda questão!")
        print("Você ganhou 3 pontos pela questão acertada. Total de pontos:", pontos+3)
    else:
        print("Você perdeu 1 ponto pela questão errada. Total de pontos: ", pontos-1)

    print("3. Qual foi o primeiro MMORPG a chegar no brasil, que distribuia o CD do instalador nas escolas?")
    for x in rpg:
        print(x)
    resposta_03 = input("R: ")

    if resposta_03 == "Ragnarok Online":
       print("Você ganhou 13 pontos pela questão acertada. Total de pontos:", pontos+3)
    else:
        print("Infelizmente Você errou a terceira questão.")
        print("Você perdeu 1 ponto pela questão errada. Total de pontos: ", pontos-1)
