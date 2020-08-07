import sys

board = [['E', 'E', 'M', 'E', 'E'],
 		 ['E', 'E', 'M', 'E', 'E'],
 		 ['E', 'E', 'E', 'E', 'E'],
 		 ['E', 'E', 'E', 'E', 'E']]

def minesweeper(x_coord, y_coord):

	visited = [[False, False, False, False, False], 
			   [False, False, False, False, False], 
			   [False, False, False, False, False], 
			   [False, False, False, False, False]]

	if(board[x_coord][y_coord] == 'M'):
		board[x_coord][y_coord] = 'X' 

	else:
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


#####################################
#             Testing               #
#####################################

minesweeper(3, 0)

for i in range(0, 4):
	for j in range(0, 5):
		print(board[i][j], end = " ")
	print(" ")
