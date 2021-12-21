#December 14th, 2021
def updatePairCount(pair, change, pairDict):
	if pair in pairDict.keys():
		pairDict[pair] += change
	else:
		pairDict[pair] = change

def combine(pair, count, reactionDict, pairCountDict, charCountDict):
	if(pair in reactionDict.keys()):
		resultChar = reactionDict[pair]
		newPair1 = pair[0] + resultChar
		newPair2 = resultChar + pair[1]
		updatePairCount(newPair1, count, pairCountDict)
		updatePairCount(newPair2, count, pairCountDict)
		if resultChar in charCountDict.keys():
			charCountDict[resultChar] += count
		else: charCountDict[resultChar] = 1

def getMostAndLeastCommon(charDict):
	mostCommon = ('', -1)
	leastCommon = ('', -1)
	for char in charDict.keys():
		count = charDict[char]
		if count > mostCommon[1]: mostCommon = (char, count)
		elif count < leastCommon[1] or leastCommon[1] == -1:
			leastCommon = (char, count)
	return mostCommon, leastCommon

if __name__ == '__main__':
	reactionDict = {}
	pairCountDictA = {}
	pairCountDictB = {}
	charCountDict = {}
	with open("input.txt") as input_file:
		input = [line.strip() for line in input_file.readlines()]
		polymerString = input[0]
		for i in range(2, len(input)):
			reaction = input[i].split(" -> ")
			reactionDict[reaction[0]] = reaction[1]

	#problem 2
	for i in range(1, len(polymerString)):
		startingPair = polymerString[i-1:i+1]
		updatePairCount(startingPair, 1, pairCountDictA)
	for char in polymerString:
		if char in charCountDict.keys(): charCountDict[char] += 1
		else: charCountDict[char] = 1
	for generation in range(20):
		print(f"Generation: {generation}")
		pairCountDictB = {}
		for pair in pairCountDictA.keys():
			count = pairCountDictA[pair]
			combine(pair, count, reactionDict, pairCountDictB, charCountDict)
		pairCountDictA = {}
		for pair in pairCountDictB.keys():
			count = pairCountDictB[pair]
			combine(pair, count, reactionDict, pairCountDictA, charCountDict)

	mostCommon, leastCommon = getMostAndLeastCommon(charCountDict)

	print(mostCommon, leastCommon)
	print(f"Part 2 Answer: {mostCommon[1] - leastCommon[1]}")