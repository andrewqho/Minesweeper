from tkinter import *

###############################################
#                   Game                      #
###############################################

def minesweeper(x_coord, y_coord):

    if(board[x_coord][y_coord] == 'M'):
        board[x_coord][y_coord] = 'X'

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

def print_visited():
    print(" ")
    for i in range(0, 8):
        for j in range(0, 8):
        	print(visited[i][j], end=" ")
        print(" ")
    print(" ")

def print_flag():
    print(" ")
    for i in range(0, 8):
        for j in range(0, 8):
            print(flag[i][j], end=" ")
        print(" ")
    print(" ")

def print_board():
    print(" ")
    for i in range(0, 8):
        for j in range(0, 8):
            print(board[j][i], end = " ")
        print(" ")
    print(" ")

###############################################
#                  Graphics                   #
###############################################

def draw_square(canvas, width, height, xcen, ycen):
    """ Draws a square on the given canvas with a given color, width, height, and center
    """
    x1 = xcen
    x2 = xcen + width
    y1 = ycen
    y2 = ycen + height

    rect = canvas.create_rectangle(x1, y1, x2, y2, fill = "#D3D3D3", outline = "BLACK")

    return rect

def draw_text(canvas, xcen, ycen, text):

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
    text = canvas.create_text(adj_xcen, adj_ycen, fill = color, text = text)

def minesweeper_on_button_press(event):
    raw_x_coord = event.x
    raw_y_coord = event.y

    x_coord = int((raw_x_coord - 150)/60)
    y_coord = int((raw_y_coord - 150)/60)

    print(str(x_coord) + ", " + str(y_coord))

    minesweeper(x_coord, y_coord)

    c.delete("all")

    print_board()
    print_visited()
    print_flag()

    for i in range (0, 8):
        for j in range(0, 8):
            
            draw_square(c, 60, 60, 150 + 60*i, 150 + 60*j)
            
            square_id = board[i][j]
    
            if square_id != 'M' and square_id != 'B' and square_id != 'E':
                draw_text(c, 150 + 60*i, 150 + 60*j, square_id)

    for i in range (0, 8):
        for j in range(0, 8):
               if(flag[i][j]):
                draw_text(c, 150 + 60*i, 150 + 60*j, "FLAG")

def flag_on_button_press(event):
    print("Here")
    raw_x_coord = event.x
    raw_y_coord = event.y

    x_coord = int((raw_x_coord - 150)/60)
    y_coord = int((raw_y_coord - 150)/60)

    print(str(x_coord) + ", " + str(y_coord))

    flag[y_coord][x_coord] = True

    c.delete("all")

    for i in range (0, 8):
        for j in range(0, 8):
            
            draw_square(c, 60, 60, 150 + 60*i, 150 + 60*j)
            
            square_id = board[i][j]
    
            if square_id != 'M' and square_id != 'B' and square_id != 'E':
                draw_text(c, 150 + 60*i, 150 + 60*j, square_id)

    for i in range (0, 8):
        for j in range(0, 8):
               if(flag[i][j]):
                draw_text(c, 150 + 60*i, 150 + 60*j, "FLAG")


###############################################
#                Running Game                 #
###############################################

board = [['E', 'M', 'M', 'M', 'M', 'E', 'E', 'E'],
         ['E', 'E', 'E', 'E', 'E', 'M', 'E', 'E'],
         ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
         ['E', 'M', 'E', 'M', 'M', 'E', 'E', 'M'],
         ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'],
         ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'M'],
         ['E', 'E', 'E', 'E', 'E', 'E', 'E', 'M'],
         ['E', 'E', 'M', 'E', 'E', 'E', 'E', 'E']]

visited = [[False, False, False, False, False, False, False, False], 
           [False, False, False, False, False, False, False, False], 
           [False, False, False, False, False, False, False, False], 
           [False, False, False, False, False, False, False, False], 
           [False, False, False, False, False, False, False, False], 
           [False, False, False, False, False, False, False, False], 
           [False, False, False, False, False, False, False, False], 
           [False, False, False, False, False, False, False, False]]

flag =     [[False, False, False, False, False, False, False, False], 
           [False, False, False, False, False, False, False, False], 
           [False, False, False, False, False, False, False, False], 
           [False, False, False, False, False, False, False, False], 
           [False, False, False, False, False, False, False, False], 
           [False, False, False, False, False, False, False, False], 
           [False, False, False, False, False, False, False, False], 
           [False, False, False, False, False, False, False, False]]

if __name__ == '__main__':

    root = Tk()

    root.geometry('900x900')

    c = Canvas(root, width=900, height=900)

    c.pack()

    for i in range (0, 8):
        for j in range(0, 8):
            
            draw_square(c, 60, 60, 150 + 60*i, 150 + 60*j)
            
            # square_id = board[i][j]
    
            # if square_id != 'M' and square_id != 'B' and square_id != 'E':
            #     draw_text(c, 150 + 60*i, 150 + 60*j, square_id)

    
    root.bind('<q>', quit)
    
    c.bind('<Button-1>', minesweeper_on_button_press)
    
    c.bind('<Control-Button-1>', flag_on_button_press)

    root.mainloop()

# gameOver = False

# win = False

# print_board()

# while(True):
#     x_coord = int(input("Input X: "))
#     y_coord = int(input("Input y: "))
#     minesweeper(x_coord, y_coord)
#     print_board()
#     if(check_game_over()):
#         break

# print("Game over!")

# if(check_WL()):
#     print("You win!")
# else:
#     print("You lose!")

# if __name__ == '__main__':
#     root = Tk()
#     root.geometry('800x800')
#     c = Canvas(root, width=800, height=800)
#     c.pack()
    
#     for i in range

#     # Event Callbacks
#     root.bind('<Key>', key_handler)
#     c.bind('<Button-1>', drawStar_on_button_press)

#     root.mainloop()
