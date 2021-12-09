input = []
with open("input.txt") as input_file:
	input = [line.split(" | ") for line in [line.strip() for line in input_file.readlines()]]

#problem 1
count = 0
for digitList in [[line[1].split() for line in input]][0]:
	for segments in digitList:
		if len(segments) in [2, 3, 4, 7]:
			count += 1
print("Problem 1")
print("---------")
print(count)

#problem 2
print("\nProblem 2")
print("---------")
def removeFromPossibleSegments(possibleSegmentList, ch):
	for key in possibleSegmentList.keys():
		if ch in possibleSegmentList[key]:
			possibleSegmentList[key].remove(ch)

def unscrambleSegments(digitList):
	possibleSegments = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}
	digitZero = ""
	digitOne = ""
	digitTwo = ""
	digitThree = ""
	digitFour = ""
	digitFive = ""
	digitSix = ""
	digitSeven = ""
	digitEight = ""
	digitNine = ""
	for segments in digitList: #set the digits we already know based on number of segments used
		if(len(segments) == 2):
			digitOne = segments
		elif(len(segments) == 3):
			digitSeven = segments
		elif(len(segments) == 4):
			digitFour = segments
		elif(len(segments) == 7):
			digitEight = segments

	for segment in digitSeven: #use digits 1 and 7 to figure out segment 0
		if segment not in digitOne: 
			possibleSegments[0] = segment
		else: 
			possibleSegments[2] += segment #add the other segments to be possibly segments 2 and 5
			possibleSegments[5] += segment

	for segment in digitFour: #using digit four, add the possible segments to 1 and 3 (not the ones found in digit 1)
		if segment not in digitOne:
			possibleSegments[1] += segment
			possibleSegments[3] += segment

	for segment in digitEight: #using digit 8, add the possible segments to 4 and 6, but not the one that's definitely segment 0
		if segment not in digitFour and segment != possibleSegments[0]:
			possibleSegments[4] += segment
			possibleSegments[6] += segment


	for segments in digitList:
		if(len(segments) == 6): #if the digit has 6 segments
			for ch in possibleSegments[2]: #if the segments don't have one of the ones from digit 1
				if ch not in segments:  
					digitSix = segments #this is definitely digit 6
					removeFromPossibleSegments(possibleSegments, ch) #we found segment 2 so remove it from all possible and add it to segment 2
					possibleSegments[2] = ch


	for segments in digitList: #find digit 5
		if(len(segments) == 5 and possibleSegments[2] not in segments): #if the digit has 5 segments and doesn't have segment 2
			digitFive = segments

	for segment in possibleSegments[6]: #determine segment 4 and 6 using digit five
		if(segment not in digitFive):
			removeFromPossibleSegments(possibleSegments, segment)
			possibleSegments[4] = segment
		else:
			removeFromPossibleSegments(possibleSegments, segment)
			possibleSegments[6] = segment


	for segments in digitList:
		if(len(segments) == 5 and segments != digitFive): #if the digit has 5 segments and is digit two or three
			if(possibleSegments[5][0] not in segments): #if it doesn't use segment 5, it's digit 2
				digitTwo = segments
			else:
				digitThree = segments #otherwise we know it's digit 3

	for segment in digitTwo: #find segment 3, which also finds segment 1
		if segment in possibleSegments[3]:
			removeFromPossibleSegments(possibleSegments, segment)
			possibleSegments[3] = segment

	for segments in digitList: #find digit 0 and 9
		if(len(segments) == 6 and segments != digitSix):#if it has six segments but isn't digit six
			if(possibleSegments[3] not in segments): #if it doesn't use segment 3 then its digit 0
				digitZero = segments
			else: 
				digitNine = segments #otherwise its definitely digit 9

	#return all digit combinations
	return [digitZero, digitOne, digitTwo, digitThree, digitFour, digitFive, digitSix, digitSeven, digitEight, digitNine]

def getNumberFromSegmentList(digitSegments, digitCombinations):
	if(len(digitSegments)) == 2: return 1
	if(len(digitSegments) == 4): return 4
	if(len(digitSegments) == 3): return 7
	if(len(digitSegments) == 7): return 8

	for i in range(len(digitCombinations)): #return the digit that corresponds to all used segments
		possibleDigit = digitCombinations[i]
		totalMatches = len(digitSegments)
		maxMatches = totalMatches
		for segment in digitSegments:
			if segment in possibleDigit: 
				maxMatches -= 1
		if maxMatches == 0 and totalMatches == len(possibleDigit): return i

	print("There was a calculation error. Digit could not be determined.")
	return -1

for listOfInputs in [[[line[0].split(), line[1].split()] for line in input]]:
	totalSum = 0
	for digitList in listOfInputs:
		digitCombinations = unscrambleSegments(digitList[0])
		fourDigitNumber = ""
		for outputDigit in digitList[1]:
			fourDigitNumber += str(getNumberFromSegmentList(outputDigit, digitCombinations))

		number = int(fourDigitNumber)
		totalSum += number
	print(f"Part Two Sum: {totalSum}")