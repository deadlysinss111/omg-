#exercice 1

#la grille du jeu doit être une liste de liste contenant des chaines de caractère, soit vide (" "), soit plein (* ou o)


#exercice 2

#voici un exemple de fonction qui permettrait de vider une grille
def empty(grid):
    for i in grid:
        for j in grid:
            j=" "

#on va ici plutot recréer une grille vide à chaque fois grace à la fonction suivante
def setup():
    grid=[]
    for i in range(8):
        row=[]
        for j in range(9):
            row.append(" ")
        grid.append(row)
    return(grid)


#exercice 3

def see(grid):
    for i in range(len(grid)):
        row=""
        if i==0 or i==len(grid)-1:
            row="  1 2 3 4 5 6 7 "
        else:
            for j in range(len(grid[i])):
                if j==0 or j==len(grid[i])-1:
                    row+=f"{7-i} "
                else:
                    row+=f"{grid[i][j]} "  #on part du principe que les emplacements rouges et jaunes de grid sont déja respectivement * et o
        print(row)


#exercice 4

def checkPlayable(grid, x):
        if grid[1][x]==" ":#il suffit de check la case la plus haute d'une colonne : si elle est vide, c'est bon, si elle est remplie, c'et que toutes la colonne est remplie
            return True
        return False


#exercice 5

def play(grid, x, player):
    playerStone=["*","o"]
    if checkPlayable(grid, x)==False:
        print("impossible de jouer ici")
        return [grid, 0]
    else:
        for y in range(6, 0, -1):
            if grid[y][x]==" ":
                grid[y][x]=playerStone[player]
                return [grid, y]


#exercice 6

def checkVertical(grid, y, x):
    serie=1
    player=grid[y][x]
    streak=0
    i=grid[y-streak][x]
    while i==player :
        streak+=1
        i=grid[y-streak][x]
    serie+=streak-1
    streak=0
    i=grid[y+streak][x]
    while i==player :
        streak+=1
        i=grid[y+streak][x]
    serie+=streak-1
    return[serie, player]

def checkHorizontal(grid, y, x):
    serie=1
    player=grid[y][x]
    streak=0
    i=grid[y][x-streak]
    while i==player :
        streak+=1
        i=grid[y][x-streak]
    serie+=streak-1
    streak=0
    i=grid[y][x+streak]
    while i==player :
        streak+=1
        i=grid[y][x+streak]
    serie+=streak-1
    return[serie, player]

def checkDiagonaleDecroissante(grid, y, x):
    serie=1
    player=grid[y][x]
    #diagonale haute gauche
    streak=0
    i=grid[y+streak][x-streak]
    while i==player :
        streak+=1
        i=grid[y+streak][x-streak]
    serie+=streak-1
    #diagonale bas droite
    streak=0
    i=grid[y-streak][x+streak]
    while i==player :
        streak+=1
        i=grid[y-streak][x+streak]
    serie+=streak-1
    return[serie, player]
    

def checkDiagonaleCroissante(grid, y, x):
    serie=1
    player=grid[y][x]
    #diagonale bas gauche
    streak=0
    i=grid[y-streak][x-streak]
    while i==player :
        streak+=1
        i=grid[y-streak][x-streak]
    serie+=streak-1
    #diagonale haute droite
    streak=0
    i=grid[y+streak][x+streak]
    while i==player :
        streak+=1
        i=grid[y+streak][x+streak]
    serie+=streak-1
    return[serie, player]

def state(grid, y, x):
    maxAndDirections=[]
    v=["vertical", checkVertical(grid, y, x)]
    h=["horizontal", checkHorizontal(grid, y, x)]
    dc=["verticale croissante", checkDiagonaleCroissante(grid, y, x)]
    dd=["verticale decroissante", checkDiagonaleDecroissante(grid, y, x)]
    maxLenght=max(v[1][0], h[1][0], dc[1][0], dd[1][0])
    maxAndDirections.append(maxLenght)
    maxAndDirections.append(grid[7-y][x])
    for i in [v,h,dc,dd]:
        if i[1][0]==maxLenght:
            maxAndDirections.append(i[0])
    return maxAndDirections

def checkWin(grid, y, x):
    if (state(grid, y, x))[0]>3:
        return True
    return False

def checkFull(grid):
    count=2 #on start le compteur à 2 car il y a 2 colonnes qui sont des bordures, on aurait aussi pu soustraire à la largeur de la grille lors de la vérification
    for i in range(len(grid[0])):
        if i!=0 and i!=len(grid[0])-1:
            if not checkPlayable(grid, i):
                count+=1
    if count==len(grid[0]):
        return True
    return False

def game():
    grid=setup()
    currentTurn=0
    isPlaying=True
    see(grid)
    while isPlaying:
        print(f"au tour du joueur {currentTurn+1}")
        print(f"coup conseillé : {trueConseil(grid, currentTurn)}")
        x=int(input("quelle colonne ?"))
        tempon=play(grid, x, currentTurn)
        grid=tempon[0]
        see(grid)
        if checkWin(grid, tempon[1], x):
            print(f"le joueur {currentTurn+1} a gagné, ggwp")
            isPlaying=False
            print(isPlaying)
        elif checkFull(grid):
            print("draw, ggwp")
            isPlaying=False
            print(isPlaying, "zzz")
        elif currentTurn==0 and tempon[1]!=0: #on vérifie que le joueur du tour a bien joué avant de changer de tour, sinon on ne change pas de tour
            currentTurn=1
        elif tempon[1]!=0:
            currentTurn=0
        

#exercice 7

from random import randint
def conseil(grid):
    rdm=0
    while rdm==0 or not checkPlayable(grid, rdm):
        rdm=randint(1,7)
    return rdm


#exercice 8
def trueConseil(grid, player):
    playerStone=["*","o"]
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x]==playerStone[player]:
                tempon=state(grid, y, x)
                if tempon[0]==3: #si on a un alignement de 3 de nos pions
                    if "vertical" in tempon:
                        i=grid[y][x]
                        streak=0
                        while i==playerStone[player]:
                            if y+streak<8:
                                if checkPlayable(grid, x):
                                    streak+=1
                                    i=grid[y+streak][x]
                                else:
                                    i="break"
                            else:
                                i="break" #on cherche a sortir de la boucle sans trigger le if suivant
                        if i==" " and  y+streak<8: #on regarde si on peut jouer le coup
                            return x
                    if "horizontal" in tempon:
                        #on regarde si le coup à jouer et à gauche
                        i=grid[y][x]
                        streak=0
                        while i==playerStone[player]:
                            if x-streak>0:
                                if checkPlayable(grid, x-streak):
                                    streak+=1
                                    i=grid[y][x-streak]
                                else:
                                    i="break"
                            else:
                                i="break"
                        if i==" " and grid[y-1][x-streak] and x-streak>0: #on regarde si on peut jouer le coup
                            print("eeeeeh")
                            return x-streak
                        #puis on regarde à droite
                        i=grid[y][x]
                        streak=0
                        while i==playerStone[player]:
                            if x+streak<8:
                                if checkPlayable(grid, x+streak):
                                    streak+=1
                                    i=grid[y][x+streak]
                                else:
                                    i="break"
                            else:
                                i="break"
                        if i==" " and grid[y-1][x+streak] and x+streak<8: #on regarde si on peut jouer le coup
                            return x+streak
                    if "verticale croissante" in tempon:
                        #on regarde si le coup à jouer et à gauche
                        i=grid[y][x]
                        streak=0
                        while i==playerStone[player]:
                            if x-streak>0 and y-streak>0:
                                if checkPlayable(grid, x-streak):
                                    streak+=1
                                    i=grid[y-streak][x-streak]
                                else:
                                    i="break"
                            else:
                                i="break"
                        if i==" " and grid[y-(streak+1)][x-streak]!=" " and x-streak>0 and y-streak>0: #on regarde si on peut jouer le coup
                            return x-streak
                        #puis on regarde à droite
                        i=grid[y][x]
                        streak=0
                        while i==playerStone[player]:
                            if x+streak<8 and y-streak>0:
                                if checkPlayable(grid, x+streak):
                                    streak+=1
                                    i=grid[y+streak][x+streak]
                                else:
                                    i="break"
                            else:
                                i="break"
                        if i==" " and grid[y+streak-1][x+streak]!=" " and x+streak<8 and y-streak>0: #on regarde si on peut jouer le coup
                            return x+streak
                    if "verticale decroissante" in tempon:
                        #on regarde si le coup à jouer et à gauche
                        i=grid[y][x]
                        streak=0
                        while i==playerStone[player]:
                            if x-streak>0 and y+streak<7:
                                if checkPlayable(grid, x-streak):
                                    streak+=1
                                    i=grid[y+streak][x-streak]
                                else:
                                    i="break"
                            else:
                                i="break"
                        if i==" " and grid[y+streak-1][x-streak]!=" " and x-streak>0 and y+streak<7: #on regarde si on peut jouer le coup
                            return x-streak
                        #puis on regarde à droite
                        i=grid[y][x]
                        streak=0
                        while i==playerStone[player]:
                            if y-streak>0 and x+streak <8:
                                if checkPlayable(grid, x+streak):
                                    streak+=1
                                    i=grid[y-streak][x+streak]
                                else:
                                    i="break"
                            else:
                                i="break"
                        if i==" " and grid[y-(streak+1)][x+streak]!=" " and y-streak>0 and x+streak <8: #on regarde si on peut jouer le coup
                            return x+streak
            
            if grid[y][x]!=playerStone[player] and grid[y][x]!=" ": #si on a un alignement de 3 pions adverse
                tempon=state(grid, y, x)
                if tempon[0]==3: #si on a un alignement de 3 de nos pions
                    if "vertical" in tempon:
                        i=grid[y][x]
                        streak=0
                        while i==playerStone[player]:
                            if y+streak<8:
                                if checkPlayable(grid, x):
                                    streak+=1
                                    i=grid[y+streak][x]
                                else:
                                    i="break"
                            else:
                                i="break" #on cherche a sortir de la boucle sans trigger le if suivant
                        if i==" " and  y+streak<8: #on regarde si on peut jouer le coup
                            return x
                    if "horizontal" in tempon:
                        #on regarde si le coup à jouer et à gauche
                        i=grid[y][x]
                        streak=0
                        while i==playerStone[player]:
                            if x-streak>0:
                                if checkPlayable(grid, x-streak):
                                    streak+=1
                                    i=grid[y][x-streak]
                                else:
                                    i="break"
                            else:
                                i="break"
                        if i==" " and grid[y-1][x-streak] and x-streak>0: #on regarde si on peut jouer le coup
                            print("eeeeeh")
                            return x-streak
                        #puis on regarde à droite
                        i=grid[y][x]
                        streak=0
                        while i==playerStone[player]:
                            if x+streak<8:
                                if checkPlayable(grid, x+streak):
                                    streak+=1
                                    i=grid[y][x+streak]
                                else:
                                    i="break"
                            else:
                                i="break"
                        if i==" " and grid[y-1][x+streak] and x+streak<8: #on regarde si on peut jouer le coup
                            return x+streak
                    if "verticale croissante" in tempon:
                        #on regarde si le coup à jouer et à gauche
                        i=grid[y][x]
                        streak=0
                        while i==playerStone[player]:
                            if x-streak>0 and y-streak>0:
                                if checkPlayable(grid, x-streak):
                                    streak+=1
                                    i=grid[y-streak][x-streak]
                                else:
                                    i="break"
                            else:
                                i="break"
                        if i==" " and grid[y-(streak+1)][x-streak]!=" " and x-streak>0 and y-streak>0: #on regarde si on peut jouer le coup
                            return x-streak
                        #puis on regarde à droite
                        i=grid[y][x]
                        streak=0
                        while i==playerStone[player]:
                            if x+streak<8 and y-streak>0:
                                if checkPlayable(grid, x+streak):
                                    streak+=1
                                    i=grid[y+streak][x+streak]
                                else:
                                    i="break"
                            else:
                                i="break"
                        if i==" " and grid[y+streak-1][x+streak]!=" " and x+streak<8 and y-streak>0: #on regarde si on peut jouer le coup
                            return x+streak
                    if "verticale decroissante" in tempon:
                        #on regarde si le coup à jouer et à gauche
                        i=grid[y][x]
                        streak=0
                        while i==playerStone[player]:
                            if x-streak>0 and y+streak<7:
                                if checkPlayable(grid, x-streak):
                                    streak+=1
                                    i=grid[y+streak][x-streak]
                                else:
                                    i="break"
                            else:
                                i="break"
                        if i==" " and grid[y+streak-1][x-streak]!=" " and x-streak>0 and y+streak<7: #on regarde si on peut jouer le coup
                            return x-streak
                        #puis on regarde à droite
                        i=grid[y][x]
                        streak=0
                        while i==playerStone[player]:
                            if y-streak>0 and x+streak <8:
                                if checkPlayable(grid, x+streak):
                                    streak+=1
                                    i=grid[y-streak][x+streak]
                                else:
                                    i="break"
                            else:
                                i="break"
                        if i==" " and grid[y-(streak+1)][x+streak]!=" " and y-streak>0 and x+streak <8: #on regarde si on peut jouer le coup
                            return x+streak

            if grid[y][x]==playerStone[player]:
                tempon=state(grid, y, x)
                if tempon[0]==2: #si on a un alignement de 2 de nos pions
                    if "vertical" in tempon:
                        i=grid[y][x]
                        streak=0
                        while i==playerStone[player]:
                            if y+streak<8:
                                if checkPlayable(grid, x):
                                    streak+=1
                                    i=grid[y+streak][x]
                                else:
                                    i="break"
                            else:
                                i="break" #on cherche a sortir de la boucle sans trigger le if suivant
                        if i==" " and  y+streak<8: #on regarde si on peut jouer le coup
                            return x
                    if "horizontal" in tempon:
                        #on regarde si le coup à jouer et à gauche
                        i=grid[y][x]
                        streak=0
                        while i==playerStone[player]:
                            if x-streak>0:
                                if checkPlayable(grid, x-streak):
                                    streak+=1
                                    i=grid[y][x-streak]
                                else:
                                    i="break"
                            else:
                                i="break"
                        if i==" " and grid[y-1][x-streak] and x-streak>0: #on regarde si on peut jouer le coup
                            print("eeeeeh")
                            return x-streak
                        #puis on regarde à droite
                        i=grid[y][x]
                        streak=0
                        while i==playerStone[player]:
                            if x+streak<8:
                                if checkPlayable(grid, x+streak):
                                    streak+=1
                                    i=grid[y][x+streak]
                                else:
                                    i="break"
                            else:
                                i="break"
                        if i==" " and grid[y-1][x+streak] and x+streak<8: #on regarde si on peut jouer le coup
                            return x+streak
                    if "verticale croissante" in tempon:
                        #on regarde si le coup à jouer et à gauche
                        i=grid[y][x]
                        streak=0
                        while i==playerStone[player]:
                            if x-streak>0 and y-streak>0:
                                if checkPlayable(grid, x-streak):
                                    streak+=1
                                    i=grid[y-streak][x-streak]
                                else:
                                    i="break"
                            else:
                                i="break"
                        if i==" " and grid[y-(streak+1)][x-streak]!=" " and x-streak>0 and y-streak>0: #on regarde si on peut jouer le coup
                            return x-streak
                        #puis on regarde à droite
                        i=grid[y][x]
                        streak=0
                        while i==playerStone[player]:
                            if x+streak<8 and y-streak>0:
                                if checkPlayable(grid, x+streak):
                                    streak+=1
                                    i=grid[y+streak][x+streak]
                                else:
                                    i="break"
                            else:
                                i="break"
                        if i==" " and grid[y+streak-1][x+streak]!=" " and x+streak<8 and y-streak>0: #on regarde si on peut jouer le coup
                            return x+streak
                    if "verticale decroissante" in tempon:
                        #on regarde si le coup à jouer et à gauche
                        i=grid[y][x]
                        streak=0
                        while i==playerStone[player]:
                            if x-streak>0 and y+streak<7:
                                if checkPlayable(grid, x-streak):
                                    streak+=1
                                    i=grid[y+streak][x-streak]
                                else:
                                    i="break"
                            else:
                                i="break"
                        if i==" " and grid[y+streak-1][x-streak]!=" " and x-streak>0 and y+streak<7: #on regarde si on peut jouer le coup
                            return x-streak
                        #puis on regarde à droite
                        i=grid[y][x]
                        streak=0
                        while i==playerStone[player]:
                            if y-streak>0 and x+streak <8:
                                if checkPlayable(grid, x+streak):
                                    streak+=1
                                    i=grid[y-streak][x+streak]
                                else:
                                    i="break"
                            else:
                                i="break"
                        if i==" " and grid[y-(streak+1)][x+streak]!=" " and y-streak>0 and x+streak <8: #on regarde si on peut jouer le coup
                            return x+streak

#j'ai conscience que ce n'est pas le code optimal mais j'ai cherché à faire un puissance 4 sans m'occuper du bot, puis a rajouter un bot qui s'accorde au code déja existant et non a accorder le code déja existant pour faciliter celui du bot.

game()