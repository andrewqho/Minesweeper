def minesweeper(x_coord, y_coord):

	if(board[x_coord][y_coord] == 'M'):
		board[x_coord][y_coord] = 'X'

	elif(board[x_coord][y_coord] == 'E'):
		minesweeper_helper(visited, x_coord, y_coord) 

def minesweeper_helper(visited, x_coord, y_coord):
	
	adj_mine_count = 0
	visited[x_coord][y_coord] = True

	for i in range (-1, 2):
		
		for j in range(-1, 2):
		
			adj_x = x_coord + i
			adj_y = y_coord + j

			if((adj_x) < 4 and (adj_x) > -1 and adj_y < 5 and adj_y > -1):

				if board[adj_x][adj_y] == 'M':
				
					adj_mine_count = adj_mine_count + 1

	if adj_mine_count == 0:
		board[x_coord][y_coord] = 'B'
		
		for i in range (-1, 2):
		
			for j in range(-1, 2):
				
				adj_x = x_coord + i
				adj_y = y_coord + j

				if((adj_x) < 4 and (adj_x) > -1 and adj_y < 5 and adj_y > -1):
					if(visited[adj_x][adj_y] == False):
						minesweeper_helper(visited, adj_x, adj_y)
	else:
		board[x_coord][y_coord] = str(adj_mine_count)

def print_board():
	print(" ")
	for i in range(0, 4):
		for j in range(0, 5):
			if(board[i][j] == 'M'):
				print('E', end = " ")
			else:
				print(board[i][j], end = " ")
		print(" ")
	print(" ")

def check_game_over():
	gameOver = True
	for i in range(0, 4):
		for j in range(0, 5):
			if(board[i][j] == 'E'):
				gameOver = False
			elif(board[i][j] == 'X'):
				return True
	return gameOver

def check_WL():
	for i in range(0, 4):
		for j in range(0, 5):
			if(board[i][j] == 'X'):
				return False
	return True

###############################################
#                   Game                      #
###############################################

gameOver = False

win = False

visited = [[False, False, False, False, False], 
		   [False, False, False, False, False], 
		   [False, False, False, False, False], 
		   [False, False, False, False, False]]

board = [['E', 'E', 'M', 'E', 'E'],
 		 ['M', 'E', 'M', 'E', 'E'],
 		 ['E', 'E', 'E', 'E', 'E'],
 		 ['E', 'E', 'E', 'E', 'E']]

print_board()

while(True):
	x_coord = int(input("Input X: "))
	y_coord = int(input("Input y: "))
	minesweeper(x_coord, y_coord)
	print_board()
	if(check_game_over()):
		break

print("Game over!")

if(check_WL()):
	print("You win!")
else:
	print("You lose!")

