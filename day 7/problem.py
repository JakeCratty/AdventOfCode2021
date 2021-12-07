#December 7th, 2021

crabPositions = []
with open("input.txt") as input_file:
	crabPositions = [int(x) for x in [line.split(",") for line in input_file.readlines()][0]]

#part 1 solution
def getFuelCostToPosition(currentPos, destination):
	fuelCost = abs(currentPos - destination)
	return fuelCost

#part 2 solution
def getFuelCostToPosition_2(currentPos, destination):
	distance = abs(currentPos - destination)
	fuelCost = 0
	for i in range(distance+1): #1 2 3 4 5 6 7
		fuelCost += i
	return fuelCost

bestResults = (-1, -1)
smallestX = min(crabPositions)
largestX = max(crabPositions)
for pos in range(smallestX, largestX):
	#print(f"Percentage done: {(pos / largestX) * 100} %")
	totalFuel = 0
	for crab in crabPositions: totalFuel += getFuelCostToPosition_2(crab, pos)
	if(totalFuel < bestResults[0] or bestResults[0] < 0): bestResults = (totalFuel, pos)

print(f"Least Fuel: {bestResults[0]} for position {bestResults[1]}")