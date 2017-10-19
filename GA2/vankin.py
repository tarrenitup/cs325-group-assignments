#an iterative solution to Vankin's Mile with a simple test case included
#it calculates the max score for each starting position and then finds the highest score
#programmed by James Barry for Amir Nayyeri's CS 325 at OSU

n = 2
inputGrid = [[1, 2, 3], [2, -10, -20], [-20, 20, -10]]
scoreGrid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

#1, 2, 3
#2, -10, -20
#-20, 20, -10
	
print(inputGrid)
print(scoreGrid)
	
for j in range (n, -1, -1):
  for i in range (n, -1, -1):
    if j == n and i == n:
      print(i, j, "n, n index")
      scoreGrid[n][n] = inputGrid[n][n]
    elif j == n and i != n:
      print(i, j, "last column")
      scoreGrid[i][j] = inputGrid[i][j] + scoreGrid[i+1][j]
    elif i == n and j != n:
      print(i, j, "last row")
      if scoreGrid[i][j+1] > 0:
        scoreGrid[i][j] = inputGrid[i][j] + scoreGrid[i][j+1]
      else:
	    scoreGrid[i][j] = inputGrid[i][j]
    else:
      print(i, j, "entering else statement")
      if scoreGrid[i][j+1] > scoreGrid[i+1][j]:
        print(i, j, "right greater than down")
        scoreGrid[i][j] = inputGrid[i][j] + scoreGrid[i][j+1]
      else:
        print(i, j, "down greater than right")
        scoreGrid[i][j] = inputGrid[i][j] + scoreGrid[i+1][j]
	  
print(scoreGrid)
maxValue = 0
for i in range (0, n+1):
  for j in range (0, n+1):
    if scoreGrid[i][j] > maxValue:
      maxValue = scoreGrid[i][j]
	  
print(maxValue)