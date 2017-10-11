#Program: select.py - CS325 Assignment 1
#Authors: James Barry, Tarren Engberg, James Luo

import binascii

#read input.txt for m, n, k
inputFile = open('input.txt','r')
info = inputFile.readline()
m, n, k = info.split(",")
m = int(m)
n = int(n)
k = int(k)
inputFile.close()

#place .dat files into 'Arrays'
Arrays = []
for x in range (1,m+1):
    fileName = str(x) +'.dat'
    Arrays.append(open(fileName,'rb'))

def close_files(filearray, inputfile, outputfile):
    for x in range (0,m):
        filearray[x].close()
    inputfile.close()
    outputfile.close()

def read_chunk(fileobject, chunk_index):

    f = fileobject
    f.seek((chunk_index)*4)
    byte = f.read(4)
    return(int((binascii.hexlify(byte)), 16))

#f.write('Answer: '+str(output))
#print(output)

def binary_search(fileobject, v, n):

    min = 0
    max = n-1


    while True:
        midpoint = (min+max)//2
        if max <= min:
            return midpoint
        if read_chunk(fileobject, midpoint) < v:
            if min == midpoint:
                return min
            min = midpoint
        elif read_chunk(fileobject, midpoint > v):
            if max == midpoint:
                return min
            max = midpoint
        else:
            return midpoint

min = 0
max = n-1
result = 0

outputFile = open('output.txt','w')

def print_lists(fileobjects, numobjects, listsize):
    for i in range(0, numobjects):
        for j in range(0, listsize):
            print("chunks", read_chunk(fileobjects[i], j))


if m == 1:
    outputFile.write(str(read_chunk(Arrays[m-1], k-1)))
    close_files(Arrays, inputFile, outputFile)
    exit()

elif n == 1:
    for i in range (0, m):
        count = 1
        v = read_chunk(Arrays[i], 0)
        for j  in range (0, m):
            if v > read_chunk(Arrays[j], 0):
                count += 1
        if count == k:
            outputFile.write(str(v))
            close_files(Arrays, inputFile, outputFile)
            exit()


for i in range (0, m):

    min = 0
    max = n-1
    flag = -1
    while flag == -1:

        midpoint = (min+max)//2
        kindex = 0

        for j in range (0, m):

            if i != j:

                kindex += binary_search(Arrays[j], read_chunk(Arrays[i], midpoint), n)

        print(k, kindex)
        kindex += midpoint
        kindex += m
        print(k, kindex)
        if kindex == k:

            outputFile.write(str(read_chunk(Arrays[i], midpoint)))
            flag = 1

        elif kindex < k:

            min = midpoint

        elif kindex > k:

            max = midpoint

        if j == m-1:
            break

    if flag == 1:
        break

close_files(Arrays, inputFile, outputFile)
