#December 6th, 2021

initalState = []

with open("input.txt") as input_file:
	initalState = [[int(x) for x in line.split(",")] for line in input_file.readlines()][0]

fishAges = initalState.copy()
def simulateOneDay(allFish):
	for fishIndex in range(len(fishAges)-1, -1, -1): #iterate backwards
		fishAges[fishIndex]-=1
		fishAge = fishAges[fishIndex]
		if(fishAge == -1):
			fishAges.append(8)
			fishAges[fishIndex] = 6

for day in range(0, 80):
	#print(f"Day {day}: count: {len(fishAges)}")
	simulateOneDay(fishAges)

print(f"Pat 1 Answer: {len(fishAges)}")

#problem 1 Recursive - doesn't work, takes too long to run recursively too

with open("input.txt") as input_file:
	fishAges = [[int(x) for x in line.split(",")] for line in input_file.readlines()][0]

numberOfNewFishperFish = []

def findNewFish(age, daysLeft, x):
	#print(f"Starting new fish: {age}, {daysLeft}")
	if(daysLeft <= 0): 
		return 1
	totalFish = 1
	while(daysLeft >= 0):
		#print(f"\t\t{age}, {daysLeft}")
		if(age < 0):
			age = 6
			#if(x <= 5): print("Creating new fish at level " + str(x) + ". Days left: " + str(daysLeft))
			totalFish += findNewFish(8, daysLeft, x + 1)
		age -= 1
		daysLeft -= 1
	#print("Fish ended " + str(totalFish))
	return totalFish

daysToSimulate = 80
for fish in fishAges:
	numberOfNewFishperFish.append(findNewFish(fish, daysToSimulate, 0))
sum = 0
for fishes in numberOfNewFishperFish:
	sum += fishes
print(f"Total fishes after {daysToSimulate} days: {sum}")

#problem 2 - using dual dictionaries as buffers
def clearBuffer(buffer):
	for day, _ in buffer.items(): buffer[day] = 0

def advanceDay(getBuffer, storeBuffer):
	clearBuffer(storeBuffer)
	for key in getBuffer.keys():
		numberOfFish = getBuffer[key]
		daysLeft = key - 1
		#print(f"Curreny Day: {key} : Fish: {numberOfFish} : days left: {daysLeft}")
		if(daysLeft < 0):
			storeBuffer[8] += numberOfFish
			daysLeft = 6
		#print(f"Storing {numberOfFish} in store buffer at day {daysLeft}")
		storeBuffer[daysLeft] += numberOfFish
		#print(storeBuffer)

buffer1 = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
buffer2 = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
#add starting fish to dictionary
for fish in fishAges:
	buffer1[fish] += 1

for i in range(256):
	if(i%2==0):
		advanceDay(buffer1, buffer2)
	else:
		advanceDay(buffer2, buffer1)
	#print(buffer1)
	#print(buffer2)
	#print("----")

sum = 0
for key in buffer1:
	sum += buffer1[key]
print(f"Fish after {daysToSimulate} days: {sum}")