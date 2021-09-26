import turtle
import turtle_helpers as th
import tiktak as game
import time

def place_stone(x,y, color):
    '''place a stone on screen at (x,y) with given color'''
    stone = turtle.Turtle('turtle')
    th.fly_to(stone, x, y)
    stone.color(color)
    stones.append(stone)
    # nötig, screen ist so konfiguriert
    screen.update() 

def play(x,y):
    '''play stone at (x,y) if this is a legal move'''
    ptm = game.ptm # player to move
    # finde Punkt in coords der am nächsten bei (x,y) liegt
    pos = th.closest_pt((x,y), coords)
    # falls der Zug möglich ist, werden die
    # Variabeln in game entsprechend geändernt
    # und True zurückgegeben.
    was_legal =  game.play(pos)

    if  was_legal:
        # der Zug war legal, wir können ihn darstellen
        place_stone(*pos, colors[ptm])
        # falls Spiel zu Ende, zeige Gewinner
        if game.result is not None: 
            display_result()

    compi_move()  

def display_result():
    '''display the game result'''
    # um besser  zu erkennen, wann das Spiel zu Ende ist
    th.write(alice, (0,170), 'End of the game')
    screen.update()
    time.sleep(2) # 2 Sekunden warten
    screen.clear()
    
    # rote und blaue Schildkröte fürs Schreiben
    red_turtle = turtle.Turtle()
    red_turtle.hideturtle()
    red_turtle.color("red")
    red_turtle.speed(1000)  # Um die Schildkröte schneller zu machen
    blue_turtle = turtle.Turtle()
    blue_turtle.hideturtle()
    blue_turtle.color("blue")
    blue_turtle.speed(1000)  # Um die Schildkröte schneller zu machen

    # Um das Resultat zu verbessern
    # Anzeigen welche Farbe gewonnen hat
    if game.result and str(game.result) != "draw": winner_color = "Red" 
    elif str(game.result) != "draw": winner_color = "Blue"
    else: winner_color = ""
    if winner_color: th.write(alice, (0,190), f"{winner_color} won")
    else: th.write(alice, (0,190), "Draw")
    # Um die Punkte von den beiden Spieler anzuzeigen
    th.write(red_turtle, (-100, 0), "Red:\n" + str(game.blue))
    th.write(blue_turtle, (100, 0), "Blue:\n" + str(game.red))
    
    # Der Spieler kann Spiel neu starten, noch mal spielen oder das Spiel schliessen.
    th.write(alice, (0,100), '\nPress n for new game or q to quit \nor r to reset the game')
    screen.onkeypress(new_game, 'n') # Falls der Spieler die Taste "n" drückt, dann wird noch mal gespielt.
    screen.onkeypress(exit, 'q') # Falls der Spieler die Taste "q" drückt, wird das Spiel geschlossen.
    screen.onkeypress(reset, 'r') # Falls der Spieler die Taste "r" drückt, wird das Spiel neu gestartet.
    screen.update()
    screen.onclick(play)  

def reset():
    """to reset the game and enable the player to choose the color and whether he wants to play alone or not.
    """
    # Punkte zurücksetzen
    game.blue = 0
    game.red = 0
    screen.clear()
    # Um die Farbe auszuwählen
    choose_color()
    # Alleine (lokal) oder gegen Computer spielen
    alone_or_computer()

def new_game():
    """start a new game
    """
    screen.clear()
    screen.onclick(play)  
    game.new_game()
    alice.clear() # delete alice's writings
    bob.speed(1000) # Um die Schildkröte schneller zu machen
    th.draw_points(bob, coords)
    for s in stones:
        s.hideturtle()
    stones.clear()
    screen.update()
    compi_move()

def compi_move():
    if  computer_player is not None and with_computer and game.ptm == computer_player:
        pt = game.select_move()
        play(*pt)

def alone_or_computer():
    """to choose whether the player wants to play alone or with the computer.
    """
    screen.clear()
    th.write(alice, (0,140), 'Play alone or with the computer')

    bob.speed(1000)   # Um die Schildkröte schneller zu machen
    th.fly_to(bob, -100, -10)
    bob.circle(2)   # ein kleiner Kreis für die Auswahl
    th.write(alice, (-100,0), 'Alone')

    th.fly_to(bob, 100, -10)
    bob.circle(2) # ein kleiner Kreis für die Auswahl
    th.write(alice, (100,0), 'Computer')

    temp_turtle = turtle.Turtle()
    temp_turtle.hideturtle()
    temp_turtle.speed(1000)  # Um die Schildkröte schneller zu machen
    th.fly_to(temp_turtle, -100, -10)
    temp_turtle.circle(2)   # ein kleiner Kreis für die Auswahl

    screen.update()
    def get_mouse_click_coor(x, y):
        global with_computer
        choice = th.closest_pt( (x,y), [(-100,0) ,(100,0)])
        if choice == (-100, 0): 
            with_computer = False
        elif choice == (100, 0): 
            with_computer = True
        new_game() # Die Funktion "new_game()" aufrufen, um diese Schleife zu brechen.

    turtle.onscreenclick(get_mouse_click_coor, 1)
    turtle.mainloop() # warten bis der Spieler etwas auswählt

def choose_color():
    """Let the player choose the color he prefers 
    """
    screen.clear() 

    # rote und blaue Schildkröte fürs Schreiben
    red_turtle = turtle.Turtle()
    red_turtle.hideturtle()
    red_turtle.color("red")
    red_turtle.speed(1000)  # Um die Schildkröte schneller zu machen
    blue_turtle = turtle.Turtle()
    blue_turtle.hideturtle()
    blue_turtle.color("blue")
    blue_turtle.speed(1000)  # Um die Schildkröte schneller zu machen

    th.write(alice, (0,140), 'Which color would you like to choose?')

    th.fly_to(red_turtle, -100, -10)
    red_turtle.circle(2) # ein kleiner Kreis für die Auswahl
    th.write(red_turtle, (-100,0), 'Red')

    th.fly_to(blue_turtle, 100, -10)
    blue_turtle.circle(2) # ein kleiner Kreis für die Auswahl
    th.write(blue_turtle, (100,0), 'Blue')

    screen.update()
    def get_mouse_click_coor(x, y):
        global colors
        choice = th.closest_pt( (x,y), [(-100,0) ,(100,0)])
        if choice == (-100, 0): 
            colors = {True: 'red', False: 'blue'}
        elif choice == (100, 0): 
            colors = {True: 'blue', False: 'red'}
        alone_or_computer() # Die Funktion "alone_or_computer" aufrufen, um diese Schleife zu brechen.


    turtle.onscreenclick(get_mouse_click_coor, 1)
    turtle.mainloop() # warten bis der Spieler etwas auswählt


##########################################
computer_player = False


# set up screen
screen = th.screen(title='Play at top right to win')


# bob is our drawing turtle
bob = turtle.Turtle() 
bob.hideturtle()

# alice is our writing turtle
alice = turtle.Turtle()
alice.hideturtle()

coords = game.pts_player.keys() # coords where one can place a stone
colors = {True: 'red', False: 'blue'}
stones = [] # Liste der gesetzten Steine

with_computer = True # global variable to check whether or not the computer should be playing
choose_color()
