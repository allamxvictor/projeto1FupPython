# -*- coding: utf-8 -*-

# NOME: ALLAN VICTOR GONÇALVES EVANGELISTA  MAT: 476334 Turma: 03


print('*****************\nArena HearthStone\n*****************\n')

while True:  # Verifica se o nome do hero/lacaio é válido.
    meu_hero = input("Nome do seu herói:")

    if (meu_hero.isnumeric()):  # Se o nome tiver apenas números ou negativos o laço volta a se repetir, informando erro.
        print('Nome do herói não pode conter apenas números')

    else:  # Se não for apenas números, então é um valor válido e quebramos laço.
        break

while True:  # Verifica se os pontos de vida são valores válidos.
    vida_hero = input(f"Pontos de vida de {meu_hero.capitalize()}:")

    if(vida_hero.isnumeric() == False):  # Caso o valor entrado não seja numérico, mostra msg de erro e reinicia o laço.
        print('Erro! Digite apenas valores numéricos entre 1 e 30.')

    elif(int(vida_hero) <= 0 or int(vida_hero) > 30):# Caso não esteja no intervalo 1 a 30 mostra erro e reinicia o laço.
        print("Erro! Digíte apenas valores numéricos entre 1 e 30")

    else:  # Caso não seja os casos acima, então é um valor valido e o laço é quebrado.
        break

while True:  # Verifica se o nome do hero/lacaio contém apenas números e informa erro.
    meu_lacaio1 = input("Nome do seu primeiro lacaio:")

    if(meu_lacaio1.isnumeric()):  # Se o nome tiver apenas números ou negativos o laço volta a se repetir pedindo para digitar dnv.
        print('Nome do lacaio não pode conter apenas números')

    else:  # Se não for apenas números e nao for valor negativo então é um valor válido e quebramos laço.
        break

while True:  # Verifica se os pontos de vida e atk são valores válidos.
    vida_lacaio1 = input(f"Pontos de vida de {meu_lacaio1.capitalize()}:")
    atk_lacaio1 = input(f"Pontos de ataque de {meu_lacaio1.capitalize()}:")

    if(vida_lacaio1.isnumeric() == False or atk_lacaio1.isnumeric() == False):
        # Caso o valor entrado não seja numérico, mostra msg de erro e reinicia o laço.
        print('Erro! Digíte apenas valores numéricos entre 1 e 10 para vida, e 0 e 10 para ataque.')
        print('Tente novamente.\n')
    elif(int(vida_lacaio1) <= 0 or int(vida_lacaio1) > 10 or int(atk_lacaio1) < 0 or int(atk_lacaio1) > 10):
    # Caso vida não esteja no intervalo 1 a 10 ou atk no intervalo 0 a 10, mostra erro e reinicia o laço.
        print("Erro! Digíte apenas valores numéricos entre 1 e 10 para vida, e 0 e 10 para ataque.")
        print('Tente novamente.\n')
    else:# Caso não seja os casos acima, então é um valor valido e o laço é quebrado.
        break

while True:# Verifica se o nome do hero/lacaio contém apenas números e informa erro.
    meu_lacaio2 = input("Nome do seu segundo lacaio:")

    if(meu_lacaio2.isnumeric()):# Se o nome tiver apenas números ou negativos o laço volta a se repetir pedindo para digitar dnv.
        print('Nome do lacaio não pode conter apenas números')

    else:# Se não for apenas números então é um valor válido e quebramos laço.
        break

while True:# Verifica se os pontos de vida e atk são valores válidos.
    vida_lacaio2 = input(f"Pontos de vida de {meu_lacaio2.capitalize()}:")
    atk_lacaio2 = input(f"Pontos de ataque de {meu_lacaio2.capitalize()}:")

    if(vida_lacaio2.isnumeric() == False or atk_lacaio2.isnumeric() == False):
    # Caso o valor entrado não seja numérico, mostra msg de erro e reinicia o laço.
        print('Erro! Digíte apenas valores numéricos entre 1 e 10 para vida, e 0 e 10 para ataque.')
        print('Tente novamente.\n')

    elif(int(vida_lacaio2) <= 0 or int(vida_lacaio2) > 10 or int(atk_lacaio2) < 0 or int(atk_lacaio2) > 10):
    # Caso vida não esteja no intervalo 1 a 10 ou atk no intervalo 0 a 10, mostra erro e reinicia o laço.
        print("Erro! Digíte apenas valores numéricos entre 1 e 10 para vida, e 0 e 10 para ataque.")
        print('Tente novamente.\n')

    else:# Caso não seja os casos acima, então é um valor valido e o laço é quebrado.
        break

while True:# Verifica se o nome do hero/lacaio contém apenas números e informa erro.
    hero_inimigo = input("Nome do herói inimigo:")

    if(hero_inimigo.isnumeric()):#  Se o nome tiver apenas números ou negativos o laço volta a se repetir pedindo para digitar dnv.
        print('Nome do herói não pode conter apenas números\n')

    else:# Se não for apenas números então é um valor válido e quebramos laço.
        break

while True:# Verifica se os pontos de vida são valores válidos.
    vida_hero_inimigo = input(f"Pontos de vida de {hero_inimigo.capitalize()}:")

    if(vida_hero_inimigo.isnumeric() == False):# Caso o valor entrado não seja numérico, mostra msg de erro e reinicia o laço.
        print('Erro! Digite apenas valores numéricos entre 1 e 30.')

    elif(int(vida_hero_inimigo) <= 0 or int(vida_hero_inimigo) > 30):# Caso não esteja no intervalo 1 a 30 mostra erro e reinicia o laço.
        print("Erro! Digíte apenas valores numéricos entre 1 e 30")

    else:# Caso não seja os casos acima, então é um valor valido e o laço é quebrado.
        break

while True:# Verifica se o nome do hero/lacaio contém apenas números e informa erro.
    lacaio_inimigo1 = input("Nome do lacaio inimigo:")

    if(lacaio_inimigo1.isnumeric()):
    # Se o nome tiver apenas números o laço volta a se repetir pedindo para digitar dnv.
        print('Nome do lacaio não pode conter apenas números')

    else:# Se não for apenas números ou num negativos então é um valor válido e quebramos laço.
        break

while True:# Verifica se os pontos de vida e atk são valores válidos.
    vida_lacaio_inimigo1 = input(f"Pontos de vida de {lacaio_inimigo1.capitalize()}:")
    atk_lacaio_inimigo1 = input(f"Pontos de ataque de {lacaio_inimigo1.capitalize()}:")

    if(vida_lacaio_inimigo1.isnumeric() == False or atk_lacaio_inimigo1.isnumeric() == False):
    # Caso o valor entrado não seja numérico, mostra msg de erro e reinicia o laço.
        print('Erro! Digíte apenas valores numéricos entre 1 e 10 para vida, e 0 e 10 para ataque.')
        print('Tente novamente.\n')

    elif(int(vida_lacaio_inimigo1) <= 0 or int(vida_lacaio_inimigo1) > 10 or int(atk_lacaio_inimigo1) < 0 or int(atk_lacaio_inimigo1) > 10):
    # Caso vida não esteja no intervalo 1 a 10 ou atk no intervalo 0 a 10, mostra erro e reinicia o laço.
        print("Erro! Digíte apenas valores numéricos entre 1 e 10 para vida, e 0 e 10 para ataque.")
        print('Tente novamente.\n')

    else:# Caso não seja os casos acima, então é um valor valido e o laço é quebrado.
        break


while True:  # Verifica se o nome do hero/lacaio contém apenas números e informa erro.
    lacaio_inimigo2 = input("Nome do segundo lacaio inimigo:")

    if(lacaio_inimigo2.isnumeric()):  # Se o nome tiver apenas números o laço volta a se repetir pedindo para digitar dnv.
        print('Nome do lacaio não pode conter apenas números')

    else:  # Se não for apenas números ou num negativos então é um valor válido e quebramos laço.
        break

while True:  # Verifica se os pontos de vida e atk são valores válidos.
    vida_lacaio_inimigo2 = input(f"Pontos de vida de {lacaio_inimigo2.capitalize()}:")
    atk_lacaio_inimigo2 = input(f"Pontos de ataque de {lacaio_inimigo2.capitalize()}:")

    if(vida_lacaio_inimigo2.isnumeric() == False or atk_lacaio_inimigo2.isnumeric() == False):
        # Caso o valor entrado não seja numérico, mostra msg de erro e reinicia o laço.
        print('Erro! Digíte apenas valores numéricos entre 1 e 10 para vida, e 0 e 10 para ataque.')
        print('Tente novamente.\n')

    elif(int(vida_lacaio_inimigo2) <= 0 or int(vida_lacaio_inimigo2) > 10 or int(atk_lacaio_inimigo2) < 0 or int(atk_lacaio_inimigo2) > 10):
        # Caso vida não esteja no intervalo 1 a 10 ou atk no intervalo 0 a 10, mostra erro e reinicia o laço.
        print("Erro! Digíte apenas valores numéricos entre 1 e 10 para vida, e 0 e 10 para ataque.")
        print('Tente novamente.\n')

    else:  # Caso não seja os casos acima, então é um valor valido e o laço é quebrado.
        break

print('\n*******************\nComeçando a batalha\n*******************\n')

print(f'Ataque de {meu_hero.capitalize()}')

while True:
    lacaio_escolhido = str(input('Escolha um de seus lacaios:'))
    x = False  # Verifica se o lacaio esco

    if(lacaio_escolhido == meu_lacaio1 or lacaio_escolhido == meu_lacaio2):
        x = True
    elif(x != True):
            print(f'Erro: {lacaio_escolhido.capitalize()} não é um de seus lacaios')
    if not (x != True):
        break

while True:  #  Verifica se o alvo é válido
    alvo = str(input('Escolha seu alvo:'))
    x = False

    if(alvo == lacaio_inimigo1 or alvo == lacaio_inimigo2 or alvo == hero_inimigo):
    #  Caso o alvo seja um dos inimigos então é alvo valido e x = true
        x = True

    elif(x != True):#  Caso x ainda seja falso então o alvo escolhido é um aliado então o programa mostra erro e repete o laço.
        print(f'Erro: {alvo.capitalize()} é um lacaio/hero aliado. Escolha um alvo inimigo')

    if not (x != True):#  Caso x não seja diferente de true então o alvo escolhido era valido então quebramos o laço.
        break

print('****Ataque feito!****')

if(lacaio_escolhido == meu_lacaio1 and alvo == lacaio_inimigo1 or lacaio_escolhido == meu_lacaio1 and alvo == lacaio_inimigo2 or
lacaio_escolhido == meu_lacaio1 and alvo == hero_inimigo):  # Verifica qual o alvo do lacaio 1.

    if(alvo == lacaio_inimigo1):  # Caso o alvo seja o lacaio inimigo 1, calcula o dano causado e sofrido após o ataque.
        vida_lacaio_inimigo1 = int(vida_lacaio_inimigo1) - int(atk_lacaio1)  # Dano infligido ao inimigo após o ataque.
        vida_lacaio1 = int(vida_lacaio1) - int(atk_lacaio_inimigo1)  # Dano sofrido após o ataque.

        if(vida_lacaio_inimigo1 <= 0 and vida_lacaio1 <= 0):  # Verifica se os dois lacaios morreram e mostra na tela.
            print(f'Lacaio inimigo, {lacaio_inimigo1.capitalize()} e, lacaio aliádo {meu_lacaio1.capitalize()} morreram!')

            print('\n****Status do tabuleiro****')  # Status do tabuleiro sem o/os lacaio/hero que morreu
            print(f'Herói, {meu_hero.capitalize()} (vida: {vida_hero})')
            print(f'Lacaio, {meu_lacaio2.capitalize()} (ataque: {atk_lacaio2} / vida: {vida_lacaio2})')
            print(f'\nHerói inimigo, {hero_inimigo.capitalize()} (vida:{vida_hero_inimigo})')
            print(f'Lacaio inimigo, {lacaio_inimigo2.capitalize()} (ataque: {atk_lacaio_inimigo2} / vida: {vida_lacaio_inimigo2})')

        elif(vida_lacaio_inimigo1 <= 0):  # Verifica se somente o alvo do ataque morreu e mostra na tela.
            print(f'Lacaio inimigo, {lacaio_inimigo1.capitalize()} morreu!')

            print('\n****Status do tabuleiro****')# Status do tabuleiro sem o/os lacaio/hero que morreu
            print(f'Herói, {meu_hero.capitalize()} (vida: {vida_hero})')
            print(f'Lacaio, {meu_lacaio1.capitalize()} (ataque: {atk_lacaio1} / vida: {vida_lacaio1})')
            print(f'Lacaio, {meu_lacaio2.capitalize()} (ataque: {atk_lacaio2} / vida: {vida_lacaio2})')
            print(f'\nHerói inimigo, {hero_inimigo.capitalize()} (vida:{vida_hero_inimigo})')
            print(f'Lacaio inimigo, {lacaio_inimigo2.capitalize()} (ataque: {atk_lacaio_inimigo2} / vida: {vida_lacaio_inimigo2})')

        elif (vida_lacaio1 <= 0):  # Verifica se o lacaio que atacou morreu e mostra.
            print(f'Lacaio aliado, {meu_lacaio1.capitalize()} morreu!')

            print('\n****Status do tabuleiro****')  # Status do tabuleiro sem o/os lacaio/hero que morreu
            print(f'Herói, {meu_hero.capitalize()} (vida: {vida_hero})')
            print(f'Lacaio, {meu_lacaio2.capitalize()} (ataque: {atk_lacaio2} / vida: {vida_lacaio2})')
            print(f'\nHerói inimigo, {hero_inimigo.capitalize()} (vida:{vida_hero_inimigo})')
            print(f'Lacaio inimigo, {lacaio_inimigo1.capitalize()} (ataque: {atk_lacaio_inimigo1} / vida: {vida_lacaio_inimigo1})')
            print(f'Lacaio inimigo, {lacaio_inimigo2.capitalize()} (ataque: {atk_lacaio_inimigo2} / vida: {vida_lacaio_inimigo2})')

    elif(alvo == lacaio_inimigo2):  # Caso o alvo seja o lacaio inimigo 2, calcula o dano causado e sofrido após o ataque.
        vida_lacaio_inimigo2 = int(vida_lacaio_inimigo2) - int(atk_lacaio1)  # Dano infligido ao inimigo após o ataque.
        vida_lacaio1 = int(vida_lacaio1) - int(atk_lacaio_inimigo2)  #Dano sofrido após o ataque.

        if (vida_lacaio_inimigo2 <= 0 and vida_lacaio1 <= 0):  #Verifica se os dois lacaios morreram e mostra na tela.
            print(f'Lacaio inimigo, {lacaio_inimigo2.capitalize()} e lacaio aliado, {meu_lacaio1.capitalize()} morreram!')

            print('\n****Status do tabuleiro****')
            print(f'Herói, {meu_hero.capitalize()} (vida: {vida_hero})')
            print(f'Lacaio, {meu_lacaio2.capitalize()} (ataque: {atk_lacaio2} / vida: {vida_lacaio2})')
            print(f'\nHerói inimigo, {hero_inimigo.capitalize()} (vida:{vida_hero_inimigo})')
            print(f'Lacaio inimigo, {lacaio_inimigo1.capitalize()} (ataque: {atk_lacaio_inimigo1} / vida: {vida_lacaio_inimigo1})')

        elif (vida_lacaio_inimigo2 <= 0):#  Verifica se somente o alvo do ataque morreu e mostra na tela.
            print(f'Lacaio inimigo, {lacaio_inimigo2.capitalize()} morreu!')

            print('\n****Status do tabuleiro****')
            print(f'Herói, {meu_hero.capitalize()} (vida: {vida_hero})')
            print(f'Lacaio, {meu_lacaio1.capitalize()} (ataque: {atk_lacaio1} / vida: {vida_lacaio1})')
            print(f'Lacaio, {meu_lacaio2.capitalize()} (ataque: {atk_lacaio2} / vida: {vida_lacaio2})')
            print(f'\nHerói inimigo, {hero_inimigo.capitalize()} (vida:{vida_hero_inimigo})')
            print(f'Lacaio inimigo, {lacaio_inimigo1.capitalize()} (ataque: {atk_lacaio_inimigo1} / vida: {vida_lacaio_inimigo1})')

        elif (vida_lacaio1 <= 0):#  Verifica se o lacaio que atacou morreu e mostra.
            print(f'Lacaio aliado, {meu_lacaio1.capitalize()} morreu! ')

            print('\n****Status do tabuleiro****')
            print(f'Herói, {meu_hero.capitalize()} (vida: {vida_hero})')
            print(f'Lacaio, {meu_lacaio2.capitalize()} (ataque: {atk_lacaio2} / vida: {vida_lacaio2})')
            print(f'\nHerói, {hero_inimigo.capitalize()} (vida:{vida_hero_inimigo})')
            print(f'Lacaio inimigo, {lacaio_inimigo1.capitalize()} (ataque: {atk_lacaio_inimigo1} / vida: {vida_lacaio_inimigo1})')
            print(f'Lacaio inimigo,{lacaio_inimigo2.capitalize()} (ataque: {atk_lacaio_inimigo2} / vida: {vida_lacaio_inimigo2})')

    else:#  Caso o alvo do lacaio 1 não seja o inimigo 1 nem o 2 então será o hero inimigo.
        vida_hero_inimigo = int(vida_hero_inimigo) - int(atk_lacaio1)# Calcula o dano sofrido pelo hero inimigo.

        if(vida_hero_inimigo <= 0):#  Verifica se o hero inimigo morreu e mostra na tela.
            print(f'Herói inimigo, {hero_inimigo.capitalize()} morreu!')

            print('\n****Status do tabuleiro****')#  Status do tabuleiro sem o/os lacaio/hero que morreu.
            print(f'Herói, {meu_hero.capitalize()} (vida: {vida_hero})')
            print(f'Lacaio, {meu_lacaio1.capitalize()} (ataque: {atk_lacaio1} / vida: {vida_lacaio1})')
            print(f'Lacaio, {meu_lacaio2.capitalize()} (ataque: {atk_lacaio2} / vida: {vida_lacaio2})\n')
            print(f'Lacaio inimigo, {lacaio_inimigo1.capitalize()} (ataque: {atk_lacaio_inimigo1} / vida: {vida_lacaio_inimigo1})')
            print(f'Lacaio inimigo, {lacaio_inimigo2.capitalize()} (ataque: {atk_lacaio_inimigo2} / vida: {vida_lacaio_inimigo2})')

        else:
            print('\n****Status do tabuleiro****')#  Status do tabuleiro quando ngm morreu.
            print(f'Herói, {meu_hero.capitalize()} (vida: {vida_hero})')
            print(f'Lacaio, {meu_lacaio1.capitalize()} (ataque: {atk_lacaio1} / vida: {vida_lacaio1})')
            print(f'Lacaio, {meu_lacaio2.capitalize()} (ataque: {atk_lacaio2} / vida: {vida_lacaio2})')
            print(f'\nHerói inimigo, {hero_inimigo.capitalize()} (vida:{vida_hero_inimigo})')
            print(f'Lacaio inimigo, {lacaio_inimigo1.capitalize()} (ataque: {atk_lacaio_inimigo1} / vida: {vida_lacaio_inimigo1})')
            print(f'Lacaio inimigo, {lacaio_inimigo2.capitalize()} (ataque: {atk_lacaio_inimigo2} / vida: {vida_lacaio_inimigo2})')

elif(lacaio_escolhido == meu_lacaio2 and alvo == lacaio_inimigo1 or lacaio_escolhido == meu_lacaio2 and alvo == lacaio_inimigo2 or
lacaio_escolhido == meu_lacaio2 and alvo == hero_inimigo):#  Verifica qual o alvo do lacaio 2.

    if (alvo == lacaio_inimigo1):#  Caso o alvo seja o lacaio inimigo 1, calcula o dano causado e sofrido após o ataque.
        vida_lacaio_inimigo1 = int(vida_lacaio_inimigo1) - int(atk_lacaio2)#  Dano infligido ao inimigo após o ataque.
        vida_lacaio2 = int(vida_lacaio2) - int(atk_lacaio_inimigo1)#  Dano sofrido após o ataque.

        if (vida_lacaio_inimigo1 <= 0 and vida_lacaio2 <= 0):#  Verifica se os dois lacaios morreram e mostra na tela.
            print(f'Lacaio inimigo, {lacaio_inimigo2.capitalize()} e, lacaio aliádo {meu_lacaio2.capitalize()} morreram!')

            print('\n****Status do tabuleiro****')#  Status do tabuleiro sem o/os lacaio/hero que morreu.
            print(f'Herói, {meu_hero.capitalize()} (vida: {vida_hero})')
            print(f'Lacaio, {meu_lacaio1.capitalize()} (ataque: {atk_lacaio1} / vida: {vida_lacaio1})')
            print(f'\nHerói inimigo, {hero_inimigo.capitalize()} (vida:{vida_hero_inimigo})')
            print(f'Lacaio inimigo, {lacaio_inimigo2.capitalize()} (ataque: {atk_lacaio_inimigo2} / vida: {vida_lacaio_inimigo2})')

        elif (vida_lacaio_inimigo1 <= 0):#  Verifica se somente o alvo do ataque morreu e mostra na tela.
            print(f'Lacaio inimigo, {lacaio_inimigo1.capitalize()} morreu!')

            print('\n****Status do tabuleiro****')#  Status do tabuleiro sem o lacaio/hero que morreu
            print(f'Herói, {meu_hero.capitalize()} (vida: {vida_hero})')
            print(f'Lacaio, {meu_lacaio1.capitalize()} (ataque: {atk_lacaio1} / vida: {vida_lacaio1})')
            print(f'Lacaio, {meu_lacaio2.capitalize()} (ataque: {atk_lacaio2} / vida: {vida_lacaio2})')
            print(f'\nHerói inimigo, {hero_inimigo.capitalize()} (vida:{vida_hero_inimigo})')
            print(f'Lacaio inimigo, {lacaio_inimigo1.capitalize()} (ataque: {atk_lacaio_inimigo1} / vida: {vida_lacaio_inimigo1})')

        elif (vida_lacaio2 <= 0):#  Verifica se o lacaio que atacou morreu e mostra.
            print(f'Lacaio aliado, {meu_lacaio2.capitalize()} morreu! ')

            print('\n****Status do tabuleiro****')#  Status do tabuleiro sem o lacaio/hero que morreu.
            print(f'Herói, {meu_hero.capitalize()} (vida: {vida_hero})')
            print(f'Lacaio, {meu_lacaio1.capitalize()} (ataque: {atk_lacaio1} / vida: {vida_lacaio1})')
            print(f'\nHerói inimigo, {hero_inimigo.capitalize()} (vida:{vida_hero_inimigo})')
            print(f'Lacaio inimigo, {lacaio_inimigo1.capitalize()} (ataque: {atk_lacaio_inimigo1} / vida: {vida_lacaio_inimigo1})')
            print(f'Lacaio inimigo, {lacaio_inimigo2.capitalize()} (ataque: {atk_lacaio_inimigo2} / vida: {vida_lacaio_inimigo2})')

    elif (alvo == lacaio_inimigo2):#  Caso o alvo seja o lacaio inimigo 2, calcula o dano causado e sofrido após o ataque.
        vida_lacaio_inimigo2 = int(vida_lacaio_inimigo2) - int(atk_lacaio2)# Dano infligido após o ataque.
        vida_lacaio2 = int(vida_lacaio2) - int(atk_lacaio_inimigo2)#  Dano sofrido após o ataque.

        if (vida_lacaio_inimigo2 <= 0 and vida_lacaio2 <= 0):#  Verifica se os dois lacaios morreram e mostra na tela.
            print(f'Lacaio inimigo, {lacaio_inimigo2.capitalize()} e lacaio aliado, {meu_lacaio2.capitalize()} morreram!')

            print('\n****Status do tabuleiro****')#  Status do tabuleiro sem o lacaio/hero que morreu.
            print(f'Herói, {meu_hero.capitalize()} (vida: {vida_hero})')
            print(f'Lacaio, {meu_lacaio1.capitalize()} (ataque: {atk_lacaio1} / vida: {vida_lacaio1})')
            print(f'\nHerói inimigo, {hero_inimigo.capitalize()} (vida:{vida_hero_inimigo})')
            print(f'Lacaio inimigo, {lacaio_inimigo1.capitalize()} (ataque: {atk_lacaio_inimigo1} / vida: {vida_lacaio_inimigo1})')

        elif (vida_lacaio_inimigo2 <= 0):#  Verifica se somente o alvo do ataque morreu e mostra na tela.
            print(f'Lacaio inimigo, {lacaio_inimigo2.capitalize()} morreu!')

            print('\n****Status do tabuleiro****')#  Status do tabuleiro sem o lacaio/hero que morreu.
            print(f'Herói, {meu_hero.capitalize()} (vida: {vida_hero})')
            print(f'Lacaio, {meu_lacaio1.capitalize()} (ataque: {atk_lacaio1} / vida: {vida_lacaio1})')
            print(f'Lacaio, {meu_lacaio2.capitalize()} (ataque: {atk_lacaio2} / vida: {vida_lacaio2})')
            print(f'\nHerói inimigo, {hero_inimigo.capitalize()} (vida:{vida_hero_inimigo})')
            print(f'Lacaio inimigo, {lacaio_inimigo1.capitalize()} (ataque: {atk_lacaio_inimigo1} / vida: {vida_lacaio_inimigo1})')

        elif (vida_lacaio2 <= 0):#  Verifica se o lacaio que atacou morreu e mostra.
            print(f'Lacaio aliado, {meu_lacaio1.capitalize()} morreu! ')

            print('\n****Status do tabuleiro****')#  Status do tabuleiro sem o lacaio/hero que morreu.
            print(f'Herói, {meu_hero.capitalize()} (vida: {vida_hero})')
            print(f'Lacaio, {meu_lacaio1.capitalize()} (ataque: {atk_lacaio1} / vida: {vida_lacaio1})')
            print(f'\nHerói inimigo, {hero_inimigo.capitalize()} (vida:{vida_hero_inimigo})')
            print(f'Lacaio inimigo, {lacaio_inimigo1.capitalize()} (ataque: {atk_lacaio_inimigo1} / vida: {vida_lacaio_inimigo1})')
            print(f'Lacaio inimigo, {lacaio_inimigo2.capitalize()} (ataque: {atk_lacaio_inimigo2} / vida: {vida_lacaio_inimigo2})')

    else:#  Caso o alvo do lacaio 2 não seja o inimigo 1 nem o 2 então será o hero inimigo.
        vida_hero_inimigo = int(vida_hero_inimigo) - int(atk_lacaio2)# Calcula o dano sofrido pelo hero inimigo.

        if (vida_hero_inimigo <= 0): #  Verifica se o hero inimigo morreu e mostra na tela.
            print(f'Herói inimigo, {hero_inimigo.capitalize()} morreu!')

            print('\n****Status do tabuleiro****')#  Status do tabuleiro sem o lacaio/hero que morreu.
            print(f'Herói, {meu_hero.capitalize()} (vida: {vida_hero})')
            print(f'Lacaio, {meu_lacaio1.capitalize()} (ataque: {atk_lacaio1} / vida: {vida_lacaio1})')
            print(f'Lacaio, {meu_lacaio2.capitalize()} (ataque: {atk_lacaio2} / vida: {vida_lacaio2})')
            print(f'\nLacaio inimigo, {lacaio_inimigo1.capitalize()} (ataque: {atk_lacaio_inimigo1} / vida: {vida_lacaio_inimigo1})')
            print(f'Lacaio inimigo, {lacaio_inimigo2.capitalize()} (ataque: {atk_lacaio_inimigo2} / vida: {vida_lacaio_inimigo2})')
        else:
            print('\n****Status do tabuleiro****')#  Status do tabuleiro quando ngm morreu.
            print(f'Herói, {meu_hero.capitalize()} (vida: {vida_hero})')
            print(f'Lacaio, {meu_lacaio1.capitalize()} (ataque: {atk_lacaio1} / vida: {vida_lacaio1})')
            print(f'Lacaio, {meu_lacaio2.capitalize()} (ataque: {atk_lacaio2} / vida: {vida_lacaio2})')
            print(f'\nHerói inimigo, {hero_inimigo.capitalize()} (vida:{vida_hero_inimigo})')
            print(f'Lacaio inimigo, {lacaio_inimigo1.capitalize()} (ataque: {atk_lacaio_inimigo1} / vida: {vida_lacaio_inimigo1})')
            print(f'Lacaio inimigo, {lacaio_inimigo2.capitalize()} (ataque: {atk_lacaio_inimigo2} / vida: {vida_lacaio_inimigo2})')
