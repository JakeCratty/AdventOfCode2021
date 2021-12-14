#December 11, 2021

octopusMapInput = []
octopusMap = []
with open("input.txt") as input_file:
	octopusMapInput = [line.strip() for line in input_file.readlines()]
for line in octopusMapInput:
	for ch in line:
		octopusMap.append(int(ch))
mapwidth = len(octopusMapInput[0])
mapheight = len(octopusMapInput)
mapsize = mapwidth * mapheight
totalFlashes = 0

def step(map):
	for i in range(len(octopusMap)):
		octopusMap[i] += 1

def printMap(map):
	for y in range(mapheight):
		for x in range(mapwidth):
			print(map[y * mapwidth + x], end='')
		print()

def flash(index):
	global totalFlashes
	global octopusMap
	neighbors = []
	octopusMap[index] = -1
	if(index < mapwidth or index >= mapsize - mapwidth): #top or bottom rows
		if(index%mapwidth==0): #left column
			neighbors.append(index+1)
			if(index == 0): neighbors.append(index+mapwidth+1) #top left corner gets bottom right neighbor
			else: neighbors.append(index-mapwidth+1) #bottom left corner gets top right neighbor
		elif((index+1)%mapwidth == 0): #right column
			neighbors.append(index-1)
			if(index==mapwidth-1): neighbors.append(index + mapwidth - 1) #top right corner
			elif(index == mapsize-1): neighbors.append(index - mapwidth - 1) #bottom right corner
		else: #all non corners in top and bottom rows
			if(index < mapwidth):
				neighbors.append(index+mapwidth+1)
				neighbors.append(index+mapwidth-1)
			else:
				neighbors.append(index-mapwidth+1)
				neighbors.append(index-mapwidth-1)
			neighbors.append(index+1)
			neighbors.append(index-1)
		if(index < mapwidth): neighbors.append(index + mapwidth) #top row gets bottom neighbor
		else: neighbors.append(index - mapwidth) #bottom row gets top neighbor
	elif(index % mapwidth == 0 or (index+1)%mapwidth == 0): #left and right columns but not corners
		neighbors.append(index-mapwidth) #get above
		neighbors.append(index+mapwidth) #get below
		if(index % mapwidth == 0): #left row
			neighbors.append(index+1)
			neighbors.append(index-mapwidth+1)
			neighbors.append(index+mapwidth+1)
		else: 
			neighbors.append(index-1)
			neighbors.append(index-mapwidth-1)
			neighbors.append(index+mapwidth-1)
	else:
		neighbors.append(index+1)
		neighbors.append(index-1)
		neighbors.append(index+mapwidth)
		neighbors.append(index-mapwidth)
		neighbors.append(index-mapwidth+1)
		neighbors.append(index-mapwidth-1)
		neighbors.append(index+mapwidth+1)
		neighbors.append(index+mapwidth-1)

	for neighbor in neighbors:
		if octopusMap[neighbor] >= 0:
			octopusMap[neighbor] += 1
			if octopusMap[neighbor] > 9:
				flash(neighbor)
				if(day < 100): totalFlashes += 1
day = 0
done = False
while not done:
	step(octopusMap)
	for i in range(len(octopusMap)):
		if octopusMap[i] > 9:
			flash(i)
			if(day < 100): totalFlashes += 1
	for i in range(len(octopusMap)):
		if octopusMap[i] == -1:
			octopusMap[i] = 0
	day += 1
	done = True
	for i in range(1, 10):
		if i in octopusMap: done = False
print(f"Part 1 Answer:\n\tTotal Flashes After 100 Days: {totalFlashes}")
print(f"Part 2 Answer:\n\tNumber of Days until All Flash: {day}")