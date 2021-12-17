#December 14th, 2021

def insertChar(template, index, char):
	newTemplate = template[0:index]
	newTemplate += char
	newTemplate += template[index:]
	return newTemplate

def scanForPairs(template):
	i = 0
	while(i < len(template)):
		pair = template[i-1:i+1]
		if pair in reactionDict.keys():
			char = reactionDict[pair]
			template = insertChar(template, i, char)
			i += 1

		i += 1
	return template

def getMostAndLeastCommon(template):
	charDict = {}
	for char in template:
		if char not in charDict.keys(): charDict[char] = 0
		charDict[char] += 1
	mostCommon = -1
	leastCommon = -1
	for char in charDict.keys():
		quantity = charDict[char]
		if quantity > mostCommon or mostCommon == -1:
			mostCommon = quantity
		elif quantity < leastCommon or leastCommon == -1:
			leastCommon = quantity
	return [mostCommon, leastCommon]

if __name__ == '__main__':

	reactionDict = {}
	polymerString = ""

	with open("input.txt") as input_file:
		input = [line.strip() for line in input_file.readlines()]
		polymerString = input[0]
		for i in range(2, len(input)):
			reaction = input[i].split(" -> ")
			reactionDict[reaction[0]] = reaction[1]

	for step in range(10):
		polymerString = scanForPairs(polymerString)
	
	#problem 1
	quantities = getMostAndLeastCommon(polymerString)
	print(f"Part 1 Answer: {quantities[0]} - {quantities[1]} = {quantities[0] - quantities[1]}")