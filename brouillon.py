import random as rd

COLONNES = 7
#nbr de COLONNES du plateau
LIGNES = 6
#nbr de LIGNES du plateau
ALIGNEMENT = 4


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


def check_victoire_horizontale(char,i):
    points = 0
    for j in range(COLONNES):
        if plateau[i][j] == char :
            points += 1
            if points == ALIGNEMENT :
                return True
        else :
            points = 0
    return False


def check_victoire_verticale(char,j):
    points = 0
    for i in range(LIGNES):
        if plateau[i][j] == char :
            points += 1
            if points == ALIGNEMENT :
                return True
        else :
            points = 0
    return False


def check_victoire_diagonale(char,l,c):
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
    if points - 1 >= ALIGNEMENT :
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
    if points - 1 >= ALIGNEMENT :
        return True

#FIN FONCTION

def check_victoire(jeton,char,player,ligne):
    if is_draw(plateau) :
        print("Draw !")
        return True
    if check_victoire_horizontale(char,ligne) :
        print(f"{player} : Wins !(hor)")
        return True
    if check_victoire_verticale(char,jeton) :
        print(f"{player} : Wins !(VER")
        return True
    if check_victoire_diagonale(char,ligne,jeton) :
        print(f"{player} : Wins !(diag)")
        return True
    #on regarde toutes les conditions de victoire en meme temps


def demander_jeton_ia_random(plateau):
    j = 0
    col = []
    for i in range(COLONNES):
        if plateau[0][i] == '" "':
            col.append(i)
    position = rd.choice(col)
    while plateau[j][position] == '" "':
        j += 1
        ligne = j + 1
    return position , ligne

def demander_jeton_ia(plateau):
    return demander_jeton_ia_random(plateau)


#def _check_victoire_ia(plateau,colonne)



                    #FONCTION JEU :


while True :
    jeton1 = demander_jeton("Player 1")
    while jeton1 == None :
        jeton1 = demander_jeton("Player 1")
    colonne_pleine, ligne = placer_jeton(plateau, jeton1, 'X')
    while colonne_pleine == True :
        print("Clonne pleine.")
        jeton1 = demander_jeton("Player 1")
        colonne_pleine, ligne = placer_jeton(plateau, jeton1, 'X')
    afficher_plateau(plateau)
    if check_victoire(jeton1,'X',"Player 1",ligne):
        break
    jeton2 , ligne2 = demander_jeton_ia(plateau)
    placer_jeton(plateau, jeton2, 'O')
    afficher_plateau(plateau)
    if check_victoire(jeton2,'O',"AI",ligne2):
        break
    #on affiche le plateau de jeu