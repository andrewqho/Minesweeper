from tkinter import *
import random
import time

###############################################
#                   Game                      #
###############################################

def generateBoard(x_size, y_size, mine_count):
    board = [['E' for i in range(y_size)] for i in range(x_size)]
    
    while(mine_count > 0):
        rand_x = random.randint(0, x_size-1)
        rand_y = random.randint(0, y_size-1)
        
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

            if((adj_x) < x_size and (adj_x) > -1 and adj_y < y_size and adj_y > -1):

                if board[adj_x][adj_y] == 'M':
                
                    adj_mine_count = adj_mine_count + 1

    if adj_mine_count == 0:
        board[x_coord][y_coord] = 'B'
        
        for i in range (-1, 2):
        
            for j in range(-1, 2):
                
                adj_x = x_coord + i
                adj_y = y_coord + j

                if((adj_x) < x_size and (adj_x) > -1 and adj_y < y_size and adj_y > -1):
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
    for i in range(0, x_size):
        for j in range(0, y_size):
            if(board[i][j] == 'M'):
                if(flag[i][j] == False):
                    return False
            else:
                if(flag[i][j] == True):
                    return False
    return True

def check_Lose():
    for i in range(0, x_size):
        for j in range(0, y_size):
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

    adj_xcen = xcen + (300/x_size)
    adj_ycen = ycen + (300/y_size)

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

    if(raw_x_coord > 150 and raw_y_coord > 150 and raw_x_coord < 750 and raw_y_coord < 750):

        x_coord = int((raw_x_coord - 150)/(600/x_size))
        y_coord = int((raw_y_coord - 150)/(600/y_size))
    
        if(not check_gameOver() and not flag[x_coord][y_coord]):
            if(x_coord < x_size and x_coord > -1 and y_coord < y_size and y_coord > -1):
        
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

    if(raw_x_coord > 150 and raw_y_coord > 150 and raw_x_coord < 750 and raw_y_coord < 750):

        x_coord = int((raw_x_coord - 150)/(600/x_size))
        y_coord = int((raw_y_coord - 150)/(600/y_size))

    if(not check_gameOver()):
        if(x_coord < x_size and x_coord > -1 and y_coord < y_size and y_coord > -1):
            
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
        draw_text(c, 20, 230, 80, "You win! Click the restart button to play again!")
    else:
        draw_text(c, 20, 230, 80, "You lose! Click the restart button to play again!")

def restart_on_click(event):                  
    gameOver = False
    new_board = generateBoard(x_size, y_size, mine_count)

    for i in range(0, x_size):
    	for j in range(0, y_size):
    		board[i][j] = new_board[i][j]


    for i in range(0, x_size):
    	for j in range(0, y_size):
    		flag[i][j] = False
    		visited[i][j] = False

    redraw()

def redraw():
    if(not gameOver):
        c.delete("all")

        for i in range (0, x_size):
            for j in range(0, y_size):
                
                square_id = board[i][j]
                if(square_id != 'E' and square_id != 'M'):
                    draw_square(c, "#A9A9A9", 600/x_size, 600/y_size, 150 + (600/x_size)*j, 150 + (600/y_size)*i)
                else:
                    draw_square(c, "#D3D3D3", 600/x_size, 600/y_size, 150 + (600/x_size)*j, 150 + (600/y_size)*i)   
                if square_id != 'M':
                    if square_id != 'B':
                        if square_id != 'E':
                            draw_text(c, 12, 150 + (600/y_size)*j, 150 + (600/y_size)*i, square_id)
    
        for i in range (0, x_size):
            for j in range(0, y_size):
                    if(flag[i][j] and (board[i][j] == 'E' or board[i][j] == 'M')):
                        draw_text(c, int(190/x_size), 150 + (600/x_size)*j, 150 + (600/y_size)*i, "FLAG")

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

    x_size = 27
    y_size = x_size
    mine_count = 200


    board = generateBoard(x_size, y_size, mine_count)

    visited = [[False for i in range(y_size)] for i in range(x_size)]

    flag =  [[False for i in range(y_size)] for i in range(x_size)]

    for i in range (0, x_size):
        for j in range(0, y_size):
            draw_square(c, "#D3D3D3", (600/x_size), (600/y_size), 150 + (600/x_size)*i, 150 + (600/y_size)*j)  

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