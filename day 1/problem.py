# Advent of Code 2021 - December 1st


#Problem 1
with open("input.txt") as inputfile:
	depthList = [int(line) for line in inputfile.readlines()]

depthIncreaseCount = 0
for i in range(1, len(depthList)):
	if(depthList[i] > depthList[i-1]):
		depthIncreaseCount += 1

print(f"Depth increases: {depthIncreaseCount}")


#Problem 2
windowCountIncreases = 0
for i in range(1, len(depthList) - 2):
	currentSum = 0
	previousSum = 0
	for j in range(i, i+3): currentSum += int(depthList[j])
	for j in range(i-1, i+2): previousSum += int(depthList[j])
	if(currentSum > previousSum): windowCountIncreases += 1

print(f"Window increases: {windowCountIncreases}")
