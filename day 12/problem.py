#December 12th, 2021

input = []
with open("input.txt") as input_file:
	input = [line.strip().split('-') for line in input_file.readlines()]

nodeMap = {}
for connection in input:
	a = connection[0]
	b = connection[1]

	if a not in nodeMap.keys(): nodeMap[a] = [b]
	else: nodeMap[a].append(b)

	if b not in nodeMap.keys(): nodeMap[b] = [a]
	else: nodeMap[b].append(a)

def traverseAll(currentNode, smallCavesVisited, beenToSmallCaveTwice):
	connections = nodeMap[currentNode]
	pathsFound = 0
	if currentNode.islower(): smallCavesVisited.append(currentNode)
	for connection in connections:
		if connection == "start": continue
		elif connection == "end": 
			pathsFound += 1
			continue
		elif connection not in smallCavesVisited:
			pathsFound += traverseAll(connection, smallCavesVisited.copy(), beenToSmallCaveTwice)
		elif connection in smallCavesVisited and not beenToSmallCaveTwice:
			pathsFound += traverseAll(connection, smallCavesVisited.copy(), True)

	return pathsFound

totalPaths = traverseAll("start", [], False)
print(f"Part 2 Answer:\n\tTotal Paths Found: {totalPaths}")
