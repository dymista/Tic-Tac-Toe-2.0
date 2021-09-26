import random
import tiktak_helpers as H

 
def update_result():
    '''update result'''
    from gui_tiktak import colors

    global result, red, blue

    # Um die globale Variable "colors" zu aktualisieren in Abhängigkeit von der Auswahl der Farbe des Spielers.
    # Die Punkte der Spieler werden hier auch aktualisiert.
    if colors[True] == "red":
        if H.is_tiktak(get_pts([True])): 
            result = True
            blue += 1
        elif H.is_tiktak(get_pts([False])): 
            result = False
            red += 1
        elif get_pts([None]) == []: result = 'draw'   

    elif colors[True] == "blue":
        if H.is_tiktak(get_pts([True])):
            result = False
            red += 1
        elif H.is_tiktak(get_pts([False])):
            result = True
            blue +=1
        elif get_pts([None]) == []: result = 'draw'   

def get_pts(players):
    '''return list of positions where player in the list players have played'''
    return [pt for (pt,p) in pts_player.items() if p in players]

def is_legal(pt):
    '''check if move is illegal'''
    return  pt not in get_pts([True,False])
       
def play(pt):
    '''player plays point pt'''
    global ptm
    if result is None and is_legal(pt): 
        pts_player[pt] = ptm 
        update_result()
        ptm = not ptm
        return True 

def new_game():
    '''start new game'''
    global ptm, result
    result = None
    ptm = True
    for pt in pts_player: 
        pts_player[pt] = None

def select_move():
    free = get_pts([None])
    winners = H.get_threats(get_pts([ptm]), free)
    threats = H.get_threats(get_pts([not ptm]), free)
    
    if winners: return winners[0]
    elif threats: return random.choice(threats)
    elif free: return  random.choice(free)   

# game variables
X = [-100,0, 100] 
H.X = X
pts_player = {(x,y): None for x in X for y in X}
ptm = True # player to move
result = None

red = 0  # Globale Variable. Die punkte vom roten Spieler 
blue = 0 # Globale Variable. Die punkte vom blauen Spieler 