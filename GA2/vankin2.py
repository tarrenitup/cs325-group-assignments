#opens input File to get n and the input Array/Board
inputFile = open('input.txt','r')
info = inputFile.readline()
n = int(info)

#declare variables
x = 0
y = 0
scoreGrid = []
inputGrid = []

#make scoreGrid size n x n, and fill it with "flag" to decrease runtime (for recursive version only) later
for i in range (0,n):
	scoreGrid.append([])
	for j in range (0,n):
		scoreGrid[i].append("flag")						#a node with "flag" is a node that hasn't calculated its max score yet

#read input.txt's array info into inputGrid
for i in range (0,n):
	inputGrid.append([])
	line = inputFile.readline().split(",")
	for j in range(0,n):
		inputGrid[i].append(int(line[j]))

#NOTE: Apparently in 2D arrays, the first index is determines the row you're on (up down), and the second index
#	   determines the column(left right). Hence, I called arrays with [y][x] to make sure y corresponds with
#	   the vertical axis, and x corresponds to the horizontal axis

#recursive function to fill scoreGrid with max score for each node
#def findMax(y,x):
#	if(scoreGrid[y][x] == "flag"):						#only calculate the score for this node if it hasn't already been calculated
#		if (x == (n-1) and y == (n-1)):							#If on Bottom right corner node,
#			scoreGrid[y][x] = inputGrid[y][x]					#max score is just whatever it is in the inputGrid
#			return inputGrid[y][x]
#		elif (x == n-1):																		#If on Right edge,
#			scoreGrid[y][x] = max(findMax(y+1,x) + inputGrid[y][x], inputGrid[y][x])			#take larger value between: node below's max Score + current node (moving down) and current node (moving right, off board)
#			return scoreGrid[y][x]
#		elif (y == n-1):																		#If on Bottom edge,
#			scoreGrid[y][x] = max(findMax(y,x+1) + inputGrid[y][x], inputGrid[y][x])			#take larger value between: right node's max Score + current node (moving right) and current node (moving down, off board)
#			return scoreGrid[y][x]
#		else:																									#Nodes with a node both below and to right i.e. not on bottom or right edge. Take larger value between:
#			scoreGrid[y][x] = max(findMax(y,x+1) + inputGrid[y][x], findMax(y+1,x) + inputGrid[y][x])			#right node's max Score + current node (moving right) and node below's max Score + current node (moving down)
#			return scoreGrid[y][x]
#	else:
#		return scoreGrid[y][x]							#max Score for this node already calculated. Just return it (other nodes need this to calculate their max score)

#iterative function to fill scoreGrid with max score for each node
def findMax(y,x):
	for x in range (n-1,-1,-1):
		for y in range (n-1,-1,-1):
			if (x == (n-1) and y == (n-1)):							#If on Bottom right corner node,
				scoreGrid[y][x] = inputGrid[y][x]					#max score is just whatever it is in the inputGrid
			elif (x == n-1):																		#If on Right edge,
				scoreGrid[y][x] = max(scoreGrid[y+1][x] + inputGrid[y][x], inputGrid[y][x])			#take larger value between: node below's max Score + current node (moving down) and current node (moving right, off board)
			elif (y == n-1):																		#If on Bottom edge,
				scoreGrid[y][x] = max(scoreGrid[y][x+1] + inputGrid[y][x], inputGrid[y][x])			#take larger value between: right node's max Score + current node (moving right) and current node (moving down, off board)
			else:																									#Nodes with a node both below and to right i.e. not on bottom or right edge. Take larger value between:
				scoreGrid[y][x] = max(scoreGrid[y][x+1] + inputGrid[y][x], scoreGrid[y+1][x] + inputGrid[y][x])			#right node's max Score + current node (moving right) and node below's max Score + current node (moving down)

findMax(0,0)

inputFile.close()

#find max score from scoreGrid
maxValue = 0
for i in range (0, n):
	for j in range (0, n):
		if scoreGrid[i][j] > maxValue:
			maxValue = scoreGrid[i][j]

#write to output.txt
outputFile = open('output.txt','w')
outputFile.write(str(maxValue))
outputFile.close()
