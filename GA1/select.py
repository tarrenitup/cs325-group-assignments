#kth value is 5 when k=7

import binascii

#read input.txt for m, n, k
inputFile = open('input.txt','r')
info = inputFile.readline()
m, n, k = info.split(",")
print(m, n, k)
m = int(m)
n = int(n)
k = int(k)
inputFile.close()

#place .dat files into 'Arrays'
Arrays = []
for x in range (1,m+1):
    fileName = str(x) +'.dat'
    Arrays.append(open(fileName,'rb'))

def read_chunk(fileobject, chunk_index):
	
	f = fileobject
	f.seek((chunk_index)*4)
	byte = f.read(4)
	return(int((binascii.hexlify(byte)), 16))
	
#f.write('Answer: '+str(output))
#print(output)

def binary_search(fileobject, v, n):

	print("v at start of search", v)
	min = 0
	max = n-1
	
	
	while True:
		midpoint = (min+max)//2
		if max <= min:
			return midpoint
		if read_chunk(fileobject, midpoint) < v:
			#print("in less than")
			print("chunk", read_chunk(fileobject, midpoint))
			print("midpoint", midpoint)
			print("v", v)
			print("min", min)
			print("max", max)
			min = midpoint
		elif read_chunk(fileobject, midpoint) > v:
			#print("in greater than")
			max = midpoint
		else: 
			return midpoint
		if max-min == 1:
			return min
			
		
min = 0
max = n-1
result = 0

outputFile = open('output.txt','w')
print_lists(Arrays, m, n)
		
for i in range (0, m):

	min = 0
	max = n-1
	
	while min < max:
	
		midpoint = (min+max)//2
		kindex = 0
	
		for j in range (0, m):
		
			if i != j:
			
				kindex += binary_search(Arrays[j], read_chunk(Arrays[i], midpoint), n)
	
		if kindex == k:
			
			outputFile.write(read_chunks(Arrays[i], midpoint))
			
		elif kindex < k:
		
			max = midpoint
			
		elif kindex > k:
		
			min = midpoint
		
inputFile.close()
outputFile.close()












