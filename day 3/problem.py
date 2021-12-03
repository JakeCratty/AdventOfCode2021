#December 3rd, 2021

#get input from input.txt
diagnosticReport = []
with open("input.txt") as input_file:
	diagnosticReport = [str(line).split() for line in input_file.readlines()]


#functions used in both problems 1 and 2
def getCommonBitPerColumn(bitStringList, index):
	#iterate over each bitstring in bitStringList, get most common bit in each column
	bitFrequency = [0, 0]
	for bitString in bitStringList:
		bit = int(bitString[0][index])
		bitFrequency[bit] += 1

	mostCommonBit = 0
	if bitFrequency[1] >= bitFrequency[0]:
		mostCommonBit = 1
	return mostCommonBit

#problem 1
def getGammaAndEpsilon(commonBitList): #build gamma and epsilon rates based on the common bit list
	gamma_rate = ""
	epsilon_rate = ""
	for bit in commonBitList:
		gamma_rate += str(bit)
		epsilon_rate += str((bit + 1) % 2) #flip bits for epsilon
	return gamma_rate, epsilon_rate

rateLength = len(diagnosticReport[0][0]) #length of each bit string

bitCountPerColumn = [[0] for _ in range(rateLength)] #a list of the most common bits per column
for columnIndex in range(len(bitCountPerColumn)):
	bitCountPerColumn[columnIndex] = getCommonBitPerColumn(diagnosticReport, columnIndex) #calculate most common bit per column
gamma_rate, epsilon_rate = getGammaAndEpsilon(bitCountPerColumn)

 #convert bitstring to base 10
gamma_int = int(gamma_rate, 2)
epsilon_int = int(epsilon_rate, 2)

print(f"Gamma: {gamma_int}\nEpsilon: {epsilon_int}\nPart 1 Answer: {gamma_int * epsilon_int}\n")


#----------------------------------------------------------------------------------------------------------------
#problem 2
def refineList(bitStringList, criteria):
	for i in range(len(bitStringList)-1, -1, -1):
		bitString = bitStringList[i]
		if(int(bitString[0][index]) != criteria):
			bitStringList.remove(bitString)
	return bitStringList

oxygen_rate = 0
scrub_rate = 0

oxyCopy = diagnosticReport.copy()
scrubCopy = diagnosticReport.copy()


for index in range(rateLength):
	oxyCriteria = getCommonBitPerColumn(oxyCopy, index)
	scrubCriteria = (getCommonBitPerColumn(scrubCopy, index) + 1) % 2
	if(len(oxyCopy) > 1): oxyCopy = refineList(oxyCopy, oxyCriteria)
	if(len(scrubCopy) > 1): scrubCopy = refineList(scrubCopy, scrubCriteria)

oxy_int = int(oxyCopy[0][0], 2)
scrub_int = int(scrubCopy[0][0], 2)

print(f"Oxygen Generator Rating: {oxy_int}\nC02 Scrubber Rating: {scrub_int}\nPart 2 Answer: {oxy_int * scrub_int}")