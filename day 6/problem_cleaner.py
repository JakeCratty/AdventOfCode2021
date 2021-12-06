#problem 1 and 2 - using dual dictionaries as buffers:

def clearBuffer(buffer):
	for day, _ in buffer.items(): buffer[day] = 0

def advanceDay(getBuffer, storeBuffer):
	clearBuffer(storeBuffer)
	for key in getBuffer.keys():
		numberOfFish = getBuffer[key]
		daysLeft = key - 1
		if(daysLeft < 0):
			storeBuffer[8] += numberOfFish
			daysLeft = 6
		storeBuffer[daysLeft] += numberOfFish

def simulateXDays(days):
	buffer1 = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
	buffer2 = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}
	for fish in initialState[:]: buffer1[fish] += 1
	for i in range(days):
		if(i%2==0):	advanceDay(buffer1, buffer2)
		else: advanceDay(buffer2, buffer1)
	sum = 0
	for key in buffer1:
		sum += buffer1[key]
	print(f"Fish after {days} days: {sum}")

if __name__ == "__main__":
	initialState = []
	with open("input.txt") as input_file:
		initialState = [[int(x) for x in line.split(",")] for line in input_file.readlines()][0]
	simulateXDays(80)
	simulateXDays(256)
	simulateXDays(512)
	simulateXDays(1024)