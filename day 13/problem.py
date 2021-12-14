#December 13th, 2021
input = []
dotLocations = []
foldInstructions = []
with open("input.txt") as input_file:
	for line in input_file.readlines():
		line = line.strip()
		if "," in line: dotLocations.append(line.split(","))
		elif "x" in line or "y" in line: foldInstructions.append(line)

originalMap = {}
def addToColumn(map, x, y):
	if x not in map.keys(): map[x] = []
	if y not in map[x]: map[x].append(y)

def foldX(foldLine):
	newMap = {}
	for x in originalMap.keys():
		for i in range(len(originalMap[x])-1, -1, -1):
			y = originalMap[x][i]
			if(x < foldLine): 
				addToColumn(newMap, x, y)
			elif(x != foldLine):
				addToColumn(newMap, foldLine - (x - foldLine), y)

	return newMap

def foldY(foldLine):
	newMap = {}
	for x in originalMap.keys():
		for i in range(len(originalMap[x])-1, -1, -1):
			y = originalMap[x][i]
			if(y < foldLine):
				addToColumn(newMap, x, y)
			elif(y != foldLine): 
				addToColumn(newMap, x, foldLine - (y - foldLine))
	return newMap

def getHighest(col):
	highest = 0
	for row in col:
		if row > highest:
			highest = row
	return highest
for location in dotLocations:
	x = int(location[0])
	y = int(location[1])
	addToColumn(originalMap, x, y)

for fold in foldInstructions:
	axis = fold.split("=")[0][-1]
	foldLine = int(fold.split("=")[1])
	if(axis == "x"): 
		originalMap = foldX(foldLine)
	else: 
		originalMap = foldY(foldLine)

with open("output.txt", 'w+') as output_file:
	highestCol = 0
	for x in originalMap.keys():
		highestInColumn = getHighest(originalMap[x])
		if highestInColumn > highestCol: highestCol = highestInColumn
	for x in originalMap.keys():
		for y in range(0, highestCol):
			if y in originalMap[x]:
				output_file.write("#")
			else:
				output_file.write(".")
		output_file.write("\n")
