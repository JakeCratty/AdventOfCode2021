segmentsPerNumber = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6] #0 1 2 3 4 5 6 7 8 9

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

#dab = 0, 2, 5
#ab = 2, 5
#eafb = 1, 2, 3, 5
#acedgfb = 0, 1, 2, 3, 4, 5, 6, 7
#cdfgeb = 
#cdfbe = 

#problem 2
print("\nProblem 2")
print("---------")
def removeFromPossibleSegments(ch):
	print(f"Removing {ch}")
	for key in possibleSegments.keys():
		if ch in possibleSegments[key]:
			possibleSegments[key].remove(ch)
def unscrambleSegments(): 
	pass
digitOne = ""
digitTwo = ""
digitThree = ""
digitFour = ""
digitFive = ""
digitSix = ""
digitSeven = ""
digitEight = ""
digitNine = ""
possibleSegments = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[]}
testInput = [[line[0].split() for line in input]][0]
print(testInput)
print([line[0].split() for line in input][0])
for digitList in [[line[0].split() for line in input]][0]: #determine for sure digits 1, 4, 7, and 8
	print(f"digit list: {digitList}")
	for segments in digitList:
		if(len(segments) == 2):
			digitOne = segments
		elif(len(segments) == 3):
			digitSeven = segments
		elif(len(segments) == 4):
			digitFour = segments
		elif(len(segments) == 7):
			digitEight = segments
print(f"1: {digitOne}| 4: {digitFour}| 7: {digitSeven}| 8: {digitEight}")

for segment in digitSeven: #use digits 1 and 7 to figure out segment 0
	if segment not in digitOne: 
		possibleSegments[0] = segment
	else: 
		possibleSegments[2] += segment #add the other segments to possibly segments 2 and 5
		possibleSegments[5] += segment

for segment in digitFour: #using digit four, add the possible segments to 1 and 3 (not the ones found in digit 1)
	if segment not in digitOne:
		possibleSegments[1] += segment
		possibleSegments[3] += segment

for segment in digitEight: #using digit 8, add the possible segments to 4 and 6, but not the one that's definitely segment 0
	if segment not in digitFour and segment != possibleSegments[0]:
		possibleSegments[4] += segment
		possibleSegments[6] += segment

for digitList in [[line[0].split() for line in input]][0]:
	for segments in digitList:
		if(len(segments) == 6): #if the digit has 6 segments
			for ch in possibleSegments[2]: #if the segments don't have one of the ones from digit 1
				if ch not in segments:  
					digitSix = segments #this is definitely digit 6
					removeFromPossibleSegments(ch) #we found segment 2 so remove it from all possible and add it to segment 2
					possibleSegments[2] = ch

for digitList in [[line[0].split() for line in input]][0]:
	for segments in digitList:
		if(len(segments) == 5 and possibleSegments[2] not in segments): #if the digit has 5 segments
			digitFive = segments

for segment in possibleSegments[6]: #determine segment 4 and 6 using digit five
	if(segment not in digitFive):
		removeFromPossibleSegments(segment)
		possibleSegments[4] = segment
	else:
		removeFromPossibleSegments(segment)
		possibleSegments[6] = segment

for digitList in [[line[0].split() for line in input]][0]:
	for segments in digitList:
		if(len(segments) == 5 and segments != digitFive): #if the digit has 5 segments and is digit two or three
			if(possibleSegments[5][0] not in segments):
				digitTwo = segments
			else:
				digitThree = segments

for segment in digitTwo: #find segment 3, which also finds segment 1
	if segment in possibleSegments[3]:
		removeFromPossibleSegments(segment)
		possibleSegments[3] = segment

possibleSegments[1] = possibleSegments[1][0] #clean up the lists
possibleSegments[4] = possibleSegments[4][0]
possibleSegments[5] = possibleSegments[5][0]

print(f"Digit Two: {digitTwo}")
print(f"Digit Three: {digitThree}")
print(possibleSegments)