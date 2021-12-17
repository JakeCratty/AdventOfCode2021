#December 14th, 2021 Part 2

reactionDict = {}
totalCountDictionary = {}

def addToDictionary(d1, char):
	if char in d1.keys():
		d1[char] += 1
	else:
		d1[char] = 1

def mergeDictionaries(d1, d2):
	newDict = {}
	#print("merging")
	for key in d1.keys():
		newDict[key] = d1[key]
	for key in d2.keys():
		if key in newDict.keys():
			newDict[key] += d2[key]
		else:
			newDict[key] = d2[key]

	#print(f"result: {newDict}")
	return newDict

def mergeCountDictionaries(d1, d2, pairKey):
	newDict = {}
	for key in d1.keys():
		newDict[key] = d1[key]
	for key in d2.keys():
		newDict[pairKey] = d2[key]
	return newDict

def getTotalCharCountPerPair(pair, generations):
	global totalCountDictionary

	#print(f"{(totalCountDictionary)}")
	charCountDict = {}
	if generations == 0:
		charCountDict = {pair[0]:0, pair[1]:0}
		pass
	elif pair in totalCountDictionary.keys() and generations in totalCountDictionary[pair].keys():
		print("Using total count dictionary")
		return totalCountDictionary[pair][generations]
	elif pair in reactionDict.keys():
		result = reactionDict[pair]
		addToDictionary(charCountDict, result)
		pair1 = pair[0] + reactionDict[pair]
		pair1CharCountDict = getTotalCharCountPerPair(pair1, generations-1)
		mergeDictionaries(charCountDict, pair1CharCountDict)
		pair2 = reactionDict[pair] + pair[1]
		pair2CharCountDict = getTotalCharCountPerPair(pair2, generations-1)
		mergeDictionaries(charCountDict, pair2CharCountDict)
	else:
		print(f"{pair} not in reaction list")
		addToDictionary(charCountDict, pair[0])
		addToDictionary(charCountDict, pair[1])

	generationCount = {generations:charCountDict}
	if pair in totalCountDictionary.keys():
		print(f"Using total count dict for generation:  {generations}")
		print(f"totcd: {totalCountDictionary} thiscd: {generationCount}")
		mergeCountDictionaries(totalCountDictionary[pair], generationCount, pairKey)
		print(f"result: {totalCountDictionary}")
	else:
		print(f"Total CD: {totalCountDictionary}")
		print(f"Adding new pair to total dictionary: {len(totalCountDictionary.keys())}")
		totalCountDictionary[pair] = generationCount
	return charCountDict

if __name__ == '__main__':
	polymerString = "" #NNCB -> NCNBCHB

	with open("input.txt") as input_file:
		input = [line.strip() for line in input_file.readlines()]
		polymerString = input[0]
		for i in range(2, len(input)):
			reaction = input[i].split(" -> ")
			reactionDict[reaction[0]] = reaction[1]

	charCountDict = {}
	addToDictionary(charCountDict, polymerString[0])
	for i in range(1, len(polymerString)):
		print(f"{i} out of {len(polymerString)-1}")
		pair = polymerString[i-1:i+1]
		addToDictionary(charCountDict, polymerString[i])
		newCharDict = getTotalCharCountPerPair(pair, 40)
		charCountDict = mergeDictionaries(newCharDict, charCountDict)
	print(f"{charCountDict}")