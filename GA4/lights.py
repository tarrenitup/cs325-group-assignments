from cnf2sat import satisfiable

#opens input File to get n and the input Array/Board
inputFile = open('input.txt','r')
infoLine = inputFile.readline().rstrip().split(",")
n = int(infoLine[0])
m = int(infoLine[1])

lightsInfo = inputFile.readline().split(",")
lightState = []
lightState.append('None')
for i in range (0,m):
    lightState.append(int(lightsInfo[i]))

lightConnections = []
lightConnections.append('None')
for i in range (0,m):
    lightConnections.append([])

for i in range (1,n+1):
    switchConnections = inputFile.readline().split(",")
    j = 0
    while (True):
        lightConnections[int(switchConnections[j])].append(i)
        if (switchConnections[j] == switchConnections[-1]):
            break
        j = j + 1

satInput = []
for i in range (1,m+1):
    if(lightState[i] == 0):
        satInput.append((lightConnections[i][0]*-1, lightConnections[i][1]))
        satInput.append((lightConnections[i][0], lightConnections[i][1]*-1))
    elif(lightState[i] == 1):
        satInput.append((lightConnections[i][0], lightConnections[i][1]))
        satInput.append((lightConnections[i][0]*-1, lightConnections[i][1]*-1))

outputFile = open('output.txt','w')
if (satisfiable(satInput)):
    outputFile.write('yes')
else:
    outputFile.write('no')

outputFile.close()
inputFile.close()
