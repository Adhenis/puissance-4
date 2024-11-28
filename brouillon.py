import random as rd

COLONNES = 7
#nbr de COLONNES du plateau
LIGNES = 6
#nbr de LIGNES du plateau


def afficher_plateau(plateau) :
    for ligne in plateau :
        print("".join(ligne))


def placer_jeton(plateau, colonne, char) :
    global LIGNES, COLONNES
    i = LIGNES - 1
    if plateau[i][colonne] != '" "' :
        while plateau[i][colonne] != '" "' :
            i -= 1
            #on change la colonne de placement tant qu'elle n'est pas valide
            if i < 0 :
                return True , -1
                #on check si la colonne qu'a choisie le joueur est pleine ou pas et on lui redemande de choisir
    plateau[i][colonne] = f'"{char}"'
    return False , i 


def demander_jeton(nom):
    try :
        guess = int(input(f'{nom} : wich column ? : ')) - 1
        if guess < 0 or guess > COLONNES :
            print("Not in range")
            return
    except ValueError :
        print("Not available")
        return       
    return guess


plateau =[]
#agencement du plateau


for i in range(LIGNES):
    plateau.append(['" "' for i in range(COLONNES)])
#finalisa° du plateau


def is_draw(plateau):
    for i in range(COLONNES):
        if plateau[0][i] == '" "' :
            return False
    return True


def check_victoire_horizontale(char,i,alignement):
    points = 0
    for j in range(COLONNES):
        if plateau[i][j] == char :
            points += 1
            if points >= alignement :
                return True
        else :
            points = 0 
    return False


def check_victoire_verticale(char,j,alignement):
    points = 0
    for i in range(LIGNES):
        if plateau[i][j] == char :
            points += 1
            if points >= alignement :
                return True
        else :
            points = 0       
    return False


def check_victoire_diagonale(char,l,c,alignement):
    points = 0
    patate = l
    tomate = c
    while l < LIGNES and c >= 0 :
        if plateau[l][c] == char :
            points += 1
        else :
            break
        l += 1
        c -= 1
    l = patate
    c = tomate
    while l >= 0 and c < COLONNES  :
        if plateau[l][c] == char :
            points += 1
        else :
            break
        l -= 1
        c += 1
    if points -1 >= alignement :
        return True
    points = 0
    l = patate
    c = tomate
    while l >= 0 and c >= 0 :
        if plateau[l][c] == char :
            points += 1
        else :
            break
        l -= 1
        c -= 1
    l = patate
    c = tomate
    while l < LIGNES and c < COLONNES  :
        if plateau[l][c] == char :
            points += 1
        else :
            break
        l += 1
        c += 1
    if points -1 >= alignement :
        return True
#FIN FONCTION


def check_victoire(char,player,jeton,ligne,alignement):
    if is_draw(plateau) :
        print("Draw !")
        return True
    if check_victoire_horizontale(char,ligne,alignement) :
        print(f"{player} : Wins !(hor)")
        return True
    if check_victoire_verticale(char,jeton,alignement) :
        print(f"{player} : Wins !(ver)")
        return True
    if check_victoire_diagonale(char,ligne,jeton,alignement) :
        print(f"{player} : Wins !(diag)")
        return True
    #on regarde toutes les conditions de victoire en meme temps


def demander_jeton_ia_random(plateau):
    col = []
    for i in range(COLONNES):
        if plateau[0][i] == '" "':
            col.append(i)
    position = rd.choice(col)
    for j in range(0,LIGNES):
        if plateau[j][position] == '" "' :
            ligne = j
    return position , ligne


def demander_jeton_ia(plateau):
    for i in range(COLONNES):
        if check_victoire_verticale('"O"',i,3) and plateau[0][i] == '" "': 
            for j in range(0,LIGNES):
                if plateau[j][i] != '" "' :
                    ligne_jeton = j - 1
            return i , ligne_jeton
    for i in range(COLONNES):
        if check_victoire_verticale('"X"',i,3) and plateau[0][i] == '" "': 
            for j in range(0,LIGNES):
                if plateau[j][i] != '" "' :
                    ligne_jeton = j - 1
            return i , ligne_jeton
    else :
        return demander_jeton_ia_random(plateau)


def check_victoire_ia(plateau,colonne):
    if check_victoire_horizontale('"O"',ligne_jeton2,3) :
        
        return colonne - 1



                    #FONCTION JEU :


while True :
    jeton1 = demander_jeton("Player 1")
    while jeton1 == None :
        jeton1 = demander_jeton("Player 1")
    colonne_pleine, ligne_jeton = placer_jeton(plateau, jeton1, 'X')
    while colonne_pleine == True :
        print("Colonne pleine.")
        jeton1 = demander_jeton("Player 1")
        colonne_pleine, ligne_jeton = placer_jeton(plateau, jeton1, 'X')
    jeton2, ligne_jeton2 = demander_jeton_ia(plateau)
    placer_jeton(plateau, jeton2, 'O')
    afficher_plateau(plateau)
    if check_victoire('"X"',"Player 1",jeton1,ligne_jeton,4):
        break
    if check_victoire('"O"',"AI",jeton2,ligne_jeton2,4):
        break
    #on affiche le plateau de jeu