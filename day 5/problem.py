#December 5th, 2021

ventMap = []
with open("input.txt") as input_file:
	ventMap = [line.strip() for line in input_file.readlines()]

def getCoords(vent): #convert coordinate strings into integer coordinates
	coords = vent.split(" -> ")

	startingCoords = coords[0].split(",")
	endingCoords = coords[1].split(",")

	x1 = int(startingCoords[0])
	y1 = int(startingCoords[1])
	x2 = int(endingCoords[0])
	y2 = int(endingCoords[1])

	return x1, y1, x2, y2

def addVentCoordsToMap(ventCoords, map): #adds the x,y location of each vent to the map dictionary
	x1 = ventCoords[0]
	y1 = ventCoords[1]
	x2 = ventCoords[2]
	y2 = ventCoords[3]
	deltaX = x1 - x2
	deltaY = y1 - y2

	#problem 1 conditions
	if(deltaX == 0): #slope is horizontal
		dir = (1, -1)[y1 > y2]
		y2 += dir #add padding for range function
		for i in range(y1, y2, dir): #dir is either +1 or -1
			if(x1 not in map): map[x1] = {} #create new x coordinate dictionary
			if (i in map[x1]):
				currentValue = map[x1][i]
				map[x1][i] = currentValue + 1
			else:
				map[x1][i] = 1 #create new y coordinate dictionary within x dictionary

	if(deltaY == 0): #slope is vertical
		dir = (1, -1)[x1 > x2]
		x2 += dir #add padding for range function
		for i in range(x1, x2, dir): #dir is either +1 or -1
			if(i not in map): map[i] = {}
			if (y1 in map[i]):
				currentValue = map[i][y1]
				map[i][y1] = currentValue + 1
			else:
				map[i][y1] = 1

	#adding problem 2 conditions
	if(abs(deltaX) != abs(deltaY)): return

	xDir = (1, -1)[x1 > x2]
	yDir = (1, -1)[y1 > y2]
	x2 += xDir #add padding for range function
	y2 += yDir #add padding for range function
	xIndex = x1 #these are the starting indices which get increased by _dir each loop
	yIndex = y1
	for i in range(0, abs(deltaX)+1, 1):#loop N times where n is the pipe length
		if(xIndex not in map): 
			map[xIndex] = {}
		if(yIndex not in map[xIndex]):
			map[xIndex][yIndex] = 1
		else:
			currentValue = map[xIndex][yIndex]
			map[xIndex][yIndex] = currentValue + 1
		xIndex += xDir
		yIndex += yDir

allVentCoords = []
for vent in ventMap:
	x1, y1, x2, y2 = getCoords(vent)
	allVentCoords.append((x1, y1, x2, y2))

map = {} #a 2d dictionary of all visited coordinates
for ventCoords in allVentCoords:
	addVentCoordsToMap(ventCoords, map)

#solve by counting all coordinates visited more than 1 time
count = 0
for x in map.keys():
	for y in map[x].keys():
		if map[x][y] > 1: 
			count += 1

print(f"Total Spaces with more than 1 overlap: {count}")
