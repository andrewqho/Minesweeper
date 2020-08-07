from tkinter import *
import random
import time

###############################################
#                   Game                      #
###############################################

def generateBoard():
    board = [['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
             ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E']]

    mine_count = 15
    
    while(mine_count > 0):
        rand_x = random.randint(0, 7)
        rand_y = random.randint(0, 7)
        
        if(board[rand_x][rand_y] != 'M'):
            board[rand_x][rand_y] = 'M'
            mine_count = mine_count - 1

    return board


def minesweeper(x_coord, y_coord):

    if(board[x_coord][y_coord] == 'M'):
        board[x_coord][y_coord] = 'X'
        visited[x_coord][y_coord] = True

    elif(board[x_coord][y_coord] == 'E'):
        minesweeper_helper(x_coord, y_coord) 

def minesweeper_helper(x_coord, y_coord):
    
    adj_mine_count = 0
    visited[x_coord][y_coord] = True

    for i in range (-1, 2):
        
        for j in range(-1, 2):
        
            adj_x = x_coord + i
            adj_y = y_coord + j

            if((adj_x) < 8 and (adj_x) > -1 and adj_y < 8 and adj_y > -1):

                if board[adj_x][adj_y] == 'M':
                
                    adj_mine_count = adj_mine_count + 1

    if adj_mine_count == 0:
        board[x_coord][y_coord] = 'B'
        
        for i in range (-1, 2):
        
            for j in range(-1, 2):
                
                adj_x = x_coord + i
                adj_y = y_coord + j

                if((adj_x) < 8 and (adj_x) > -1 and adj_y < 8 and adj_y > -1):
                    if(visited[adj_x][adj_y] == False):
                        minesweeper_helper(adj_x, adj_y)
    else:
        board[x_coord][y_coord] = str(adj_mine_count)

def check_gameOver():
    if(check_Win() or check_Lose()):
        return True
    return False

def check_Win():
    gameOver = True
    for i in range(0, 8):
        for j in range(0, 8):
            if(board[i][j] == 'M'):
                if(flag[i][j] == False):
                    return False
            else:
                if(flag[i][j] == True):
                    return False
    return True

def check_Lose():
    for i in range(0, 8):
        for j in range(0, 8):
            if(board[i][j] == 'X'):
                return True
    return False

###############################################
#                  Graphics                   #
###############################################

def draw_square(canvas, color, width, height, xcen, ycen):
    """ Draws a square on the given canvas with a given color, width, height, and center
    """
    x1 = xcen
    x2 = xcen + width
    y1 = ycen
    y2 = ycen + height

    rect = canvas.create_rectangle(x1, y1, x2, y2, fill = color, outline = "BLACK")

    return rect

def draw_text(canvas, size, xcen, ycen, text):

    adj_xcen = xcen + 30
    adj_ycen = ycen + 30

    color = "BLACK"

    if text == '1':
        color = "BLUE"
    elif text == '2':
         color = "RED"
    elif text == '3':
         color = "GREEN"
    elif text == "FLAG":
         color = "RED"
    text = canvas.create_text(adj_xcen, adj_ycen, font=("Cambria", size), fill = color, text = text)

def minesweeper_on_button_press(event):
    raw_x_coord = event.y
    raw_y_coord = event.x

    if(raw_x_coord > 150 and raw_y_coord > 150):

        x_coord = int((raw_x_coord - 150)/60)
        y_coord = int((raw_y_coord - 150)/60)
    
        print(str(x_coord) + ", " + str(y_coord))
    
        if(not check_gameOver()):
            if(x_coord < 8 and x_coord > -1 and y_coord < 8 and y_coord > -1):
        
                minesweeper(x_coord, y_coord)
                redraw()
    
            if(check_Win() == True):
                if(check_Lose() == False):
                    gameOver = True
                    display_endscreen(True)
            elif(check_Win() == False):
                if(check_Lose() == True):
                    gameOver = True
                    display_endscreen(False)

def flag_on_button_press(event):

    raw_x_coord = event.y
    raw_y_coord = event.x

    x_coord = int((raw_x_coord - 150)/60)
    y_coord = int((raw_y_coord - 150)/60)

    if(not check_gameOver()):
        if(x_coord < 8 and x_coord > -1 and y_coord < 8 and y_coord > -1):
            
            flag[x_coord][y_coord] = (not flag[x_coord][y_coord])
            redraw()

        if(check_Win() == True):
            if(check_Lose() == False):
                gameOver = True
                display_endscreen(True)
        elif(check_Win() == False):
            if(check_Lose() == True):
                gameOver = True
                display_endscreen(False)

def display_endscreen(win):

    if(win):
        draw_text(c, 20, 200, 80, "You win! Click the restart button to play again!")
    else:
        draw_text(c, 20, 200, 80, "You lose! Click the restart button to play again!")

def restart_on_click(event):                  
    gameOver = False
    new_board = generateBoard()

    for i in range(0, 8):
    	for j in range(0, 8):
    		board[i][j] = new_board[i][j]


    for i in range(0, 8):
    	for j in range(0, 8):
    		flag[i][j] = False
    		visited[i][j] = False

    redraw()

def redraw():
    if(not gameOver):
        c.delete("all")

        for i in range (0, 8):
            for j in range(0, 8):
                
                square_id = board[i][j]
                if(square_id != 'E' and square_id != 'M'):
                    draw_square(c, "#A9A9A9", 60, 60, 150 + 60*j, 150 + 60*i)
                else:
                    draw_square(c, "#D3D3D3", 60, 60, 150 + 60*j, 150 + 60*i)   
                if square_id != 'M':
                    if square_id != 'B':
                        if square_id != 'E':
                            draw_text(c, 12, 150 + 60*j, 150 + 60*i, square_id)
    
        for i in range (0, 8):
            for j in range(0, 8):
                    if(flag[i][j]):
                        draw_text(c, 12, 150 + 60*j, 150 + 60*i, "FLAG")

    restart_box = c.create_rectangle(645, 90, 725, 40, fill="BLUE", tags='restart_box')    
    c.tag_bind('restart_box', '<ButtonPress-1>', restart_on_click)

    restart_text = c.create_text(687, 65, text='Restart', tags='restart_button')
    c.tag_bind('restart_button', '<ButtonPress-1>', restart_on_click) 

    minesweeper_text = draw_text(c, 40, 200, 30, "M I N E S W E E P E R")

    c.pack()

###############################################
#                Running Game                 #
###############################################

if __name__ == '__main__':

    root = Tk()

    root.geometry('900x900')

    c = Canvas(root, width=900, height=900)

    c.pack()

    gameOver = False

    board = generateBoard()

    visited = [[False, False, False, False, False, False, False, False], 
              [False, False, False, False, False, False, False, False], 
              [False, False, False, False, False, False, False, False], 
              [False, False, False, False, False, False, False, False], 
              [False, False, False, False, False, False, False, False], 
              [False, False, False, False, False, False, False, False], 
              [False, False, False, False, False, False, False, False], 
              [False, False, False, False, False, False, False, False]]

    flag =  [[False, False, False, False, False, False, False, False], 
            [False, False, False, False, False, False, False, False], 
            [False, False, False, False, False, False, False, False], 
            [False, False, False, False, False, False, False, False], 
            [False, False, False, False, False, False, False, False], 
            [False, False, False, False, False, False, False, False], 
            [False, False, False, False, False, False, False, False], 
            [False, False, False, False, False, False, False, False]]

    for i in range (0, 8):
        for j in range(0, 8):
            draw_square(c, "#D3D3D3", 60, 60, 150 + 60*i, 150 + 60*j)  

    # Quit command
    root.bind('<q>', quit)   


    #minesweeper button press
    c.bind('<Button-1>', minesweeper_on_button_press)
    

    #flag button press
    c.bind('<Control-Button-1>', flag_on_button_press)
    

    #restart button
    restart_box = c.create_rectangle(645, 90, 725, 40, fill="BLUE", tags='restart_box')    
    c.tag_bind('restart_box', '<ButtonPress-1>', restart_on_click)

    restart_text = c.create_text(687, 65, text='Restart', tags='restart_button')
    c.tag_bind('restart_button', '<ButtonPress-1>', restart_on_click)   

    # M I N E S W E E P E R
    minesweeper_text = draw_text(c, 40, 200, 30, "M I N E S W E E P E R")

    c.pack()

    root.mainloop()