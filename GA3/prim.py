#A = adjacency matrix, u = vertex u, v = vertex v
def weight(A, u, v):
    return A[u][v]

#A = adjacency matrix, u = vertex u
def adjacent(A, u):
    L = []
    for x in range(len(A)):
        if A[u][x] > 0 and x <> u:
            L.insert(0,x)
    return L

#Q = min queue
def extractMin(Q):
    q = Q[0]
    Q.remove(Q[0])
    return q

#Q = min queue, V = vertex list
def decreaseKey(Q, K):
    for i in range(len(Q)):
        for j in range(len(Q)):
            if K[Q[i]] < K[Q[j]]:
                s = Q[i]
                Q[i] = Q[j]
                Q[j] = s

#V = vertex list, A = adjacency list, r = root
def prim(V, A, r):
    u = 0
    v = 0

    # initialize and set each value of the array P (pi) to none
    # pi holds the parent of u, so P(v)=u means u is the parent of v
    P=[None]*len(V)

    # initialize and set each value of the array K (key) to some large number (simulate infinity)
    K = [999999]*len(V)

    # initialize the min queue and fill it with all vertices in V
    Q=[0]*len(V)
    for u in range(len(Q)):
        Q[u] = V[u]

    # set the key of the root to 0
    K[r] = 0
    decreaseKey(Q, K)    # maintain the min queue

    # loop while the min queue is not empty
    while len(Q) > 0:
        u = extractMin(Q)    # pop the first vertex off the min queue

        # loop through the vertices adjacent to u
        Adj = adjacent(A, u)
        for v in Adj:
            w = weight(A, u, v)    # get the weight of the edge uv

            # proceed if v is in Q and the weight of uv is less than v's key
            if Q.count(v)>0 and w < K[v]:
                # set v's parent to u
                P[v] = u
                # v's key to the weight of uv
                K[v] = w
                decreaseKey(Q, K)    # maintain the min queue
    return P

inputFile = open('input.txt','r')
info = inputFile.readline()
n = int(info)

A = []
V1 = []
V2 = []
V3 = []

#read input.txt's array info into A
for i in range (0,n):
	A.append([])
	line = inputFile.readline().split(",")
	for j in range(0,n):
		A[i].append(int(line[j]))

for i in range(0, n):
    V1.append([])
    V1[i] = i
    V2.append([])
    V2[i] = i
    V3.append([])
    V3[i] = i

#first tree
P1 = prim(V1, A, 0)
PFull = []
for i in range (1,n):
    PFull.append([i, P1[i]])
print P1
print PFull

sum = 0

for i in range (1, len(P1)):
    sum += A[i][P1[i]]

print sum

mindif = 9999999999
tempdif = 0
lFlag = 0

for i in range (1, n):
    temp = A[i][P1[i]]
    for j in range(0, n):
        lFlag = 0
        if j != P1[i] and i != j:
            tempdif = abs(temp - A[i][j])
            if tempdif < mindif:
                print("i j", i, j)
                for k in range (0, n-1):
                    if (PFull[k][0] == j and PFull[k][1] == i):
                        lFlag = 1
                if lFlag == 0:
                    mindif = tempdif
                    print("setting", mindif)
                    x = i
                    y = j

print(sum + mindif)

mindif2 = 9999999999

for i in range (1, n):
    temp = A[i][P1[i]]
    for j in range(0, n):
        if j != P1[i]:
            tempdif = abs(temp - A[i][j])
        if tempdif < mindif2 and tempdif != mindif:
            mindif2 = tempdif

print(sum + mindif2)
