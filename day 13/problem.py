#December 13th, 2021
import os

input = []
dotLocations = []
foldInstructions = []
originalMap = {}

with open("input.txt") as input_file:
	for line in input_file.readlines():
		line = line.strip()
		if "," in line: dotLocations.append(line.split(","))
		elif "x" in line or "y" in line: foldInstructions.append(line)

def addToRow(map, x, y):
	if y not in map.keys(): map[y] = []
	if x not in map[y]: map[y].append(x)

def foldX(foldLine):
	newMap = {}
	for y in originalMap.keys():
		for i in range(len(originalMap[y])-1, -1, -1):
			x = originalMap[y][i]
			if(x < foldLine): 
				addToRow(newMap, x, y)
			elif(x != foldLine):
				addToRow(newMap, foldLine - (x - foldLine), y)

	return newMap

def foldY(foldLine):
	newMap = {}
	for y in originalMap.keys():
		for i in range(len(originalMap[y])-1, -1, -1):
			x = originalMap[y][i]
			if(y < foldLine):
				addToRow(newMap, x, y)
			elif(y != foldLine): 
				addToRow(newMap, x, foldLine - (y - foldLine))
	return newMap

def getWidest(row):
	widest = 0
	for col in row:
		if col > widest:
			widest = col
	return widest

#problem 2 (no problem 1 - too easy / got overwritten)
for location in dotLocations:
	x = int(location[0])
	y = int(location[1])
	addToRow(originalMap, x, y)

for fold in foldInstructions:
	axis = fold.split("=")[0][-1]
	foldLine = int(fold.split("=")[1])
	if(axis == "x"): 
		originalMap = foldX(foldLine)
	else: 
		originalMap = foldY(foldLine)

block = u'█'.encode("utf8")
space = u' '.encode("utf8")
newline = u'\n'.encode("utf8")

with open('outputfile.txt', mode='wb') as output_file:
	widestRow = 0
	highestCol = 0
	for y in originalMap.keys():
		widestInRow = getWidest(originalMap[y])
		if widestInRow > widestRow: widestRow = widestInRow
		if y > highestCol: highestCol = y
	for y in range(0, (highestCol+1)*2):
		yVal = y//2
		print(yVal)
		for x in range(0, (widestRow+1)):
			if yVal in originalMap.keys() and x in originalMap[yVal]:
				output_file.write(block + block)
			else:
				output_file.write(space + space)
		output_file.write(newline)
