#December 9th, 2021

mapRows = []
with open("input.txt") as input_file:
	mapRows = [line.strip() for line in input_file.readlines()]
map = []
for row in mapRows:
	for col in row:
		map.append(int(col))

mapwidth = len(mapRows[0])
mapheight = len(mapRows)
mapsize = mapwidth * mapheight

neighborMap = []
def getNeighbors(index):
	neighbors = []
	value = map[i]
	if(i < mapwidth or i >= mapsize - mapwidth):
		if(i == 0 or i == mapsize - mapwidth): neighbors.append(i+1)
		elif((i+1)%mapwidth == 0): neighbors.append(i-1)
		else:
			neighbors.append(i+1)
			neighbors.append(i-1)
		if(i < mapwidth): neighbors.append(i + mapwidth)
		else: neighbors.append(i - mapwidth)
	elif(i % mapwidth == 0 or (i+1)%mapwidth == 0):
		neighbors.append(i-mapwidth)
		neighbors.append(i+mapwidth)
		if(i % mapwidth == 0): neighbors.append(i+1)
		else: neighbors.append(i-1)
	else:
		neighbors.append(i+1)
		neighbors.append(i-1)
		neighbors.append(i+mapwidth)
		neighbors.append(i-mapwidth)

	return neighbors

for i in range(len(map)): #generate a map of all neighbor indices for each coorindate
	neighbors = getNeighbors(i)
	neighborMap.append(neighbors)

#problem 1
basinCount = 0
basinRiskSum = 0
basinIndices = []
for i in range(len(map)):
	value = map[i]
	neighbors = neighborMap[i]
	allGreater = True
	for neighbor in neighbors:
		if map[neighbor] <= value: allGreater = False
	if allGreater:
		basinCount += 1
		basinRiskSum += (value + 1)
		basinIndices.append(i)
print(f"Part 1: \n\tBasin Count: {basinCount}\n\tBasin Risk Sum: {basinRiskSum}")

#problem 2
def getBasinSize(basinIndex): #recursively build all indices that are a part of a basin
	basinList = [basinIndex]
	neighbors = neighborMap[basinIndex]
	for neighbor in neighbors:
		if(map[neighbor] > map[basinIndex] and map[neighbor] != 9):
			basinList.extend(getBasinSize(neighbor))

	return basinList

largestBasinSizes = []
for basinIndex in basinIndices:
	basinIndexList = getBasinSize(basinIndex)
	currentBasinIndices = []
	for index in basinIndexList: #remove duplicate indices to get true size of basin
		if index not in currentBasinIndices: currentBasinIndices.append(index)

	#add size to list of largest basins and then sort it to keep it increasing in order
	if(len(largestBasinSizes) < 3): 
			largestBasinSizes.append(len(currentBasinIndices))
			largestBasinSizes.sort()
	else:
		for i in range(len(largestBasinSizes)):
			if(len(currentBasinIndices) > largestBasinSizes[i]):
				largestBasinSizes[i] = len(currentBasinIndices)
				largestBasinSizes.sort()
				break
print(f"Part 2 Answer: \n\tProduct of Largest Basin Sizes: {largestBasinSizes[0] * largestBasinSizes[1] * largestBasinSizes[2]}")

