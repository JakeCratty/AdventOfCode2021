#December 16th, 2021
from colorama import init, Fore, Style
hexToBinaryMap = {	"0":"0000",
					"1":"0001",
					"2":"0010",
					"3":"0011",
					"4":"0100",
					"5":"0101",
					"6":"0110",
					"7":"0111",
					"8":"1000",
					"9":"1001",
					"A":"1010",
					"B":"1011",
					"C":"1100",
					"D":"1101",
					"E":"1110",
					"F":"1111"}

def hexToBinary(hexString):
	binaryString = ""
	for char in hexString:
		binaryString += hexToBinaryMap[char]
	return binaryString

def extractLiteral(literal):
	# print("stripping zeros")
	# indexOfFirst = literal.index("1")
	# literal = literal[indexOfFirst:]
	binaryLiteralValue = ""
	length = 0
	while(literal[0] ==  "1"):
		length += 5
		value = literal[1:5]
		binaryLiteralValue += value
		literal = literal[5:]

	length += 5
	value = literal[1:5]
	literal = literal[5:]
	binaryLiteralValue += value
	literalValue = int(binaryLiteralValue, 2)
	return literalValue, length

	pass

def applyOperator(id, valueList):
	if(id == 0):
		result = 0
		for value in valueList:
			result += value
	elif(id == 1):
		result = 1
		for value in valueList:
			result *= value
	elif(id == 2):
		result = -1
		for value in valueList:
			if value < result or result == -1:
				result = value
	elif(id == 3):
		result = -1
		for value in valueList:
			if value > result: result = value
	elif(id == 5):
		result = (0, 1)[valueList[0] > valueList[1]]
	elif(id == 6):
		result = (0, 1)[valueList[0] < valueList[1]]
	elif(id == 7):
		result = (0, 1)[valueList[0] == valueList[1]]
	return result

def parsePacket(binary, pt, packet_level):
	packetLength = 6 #tracks this packets total length to be returned at the end
	versionNumber = int(binary[pt:pt+3], 2)
	packetID = int(binary[pt+3:pt+6], 2)
	pt += 6
	
	if(packetID == 4): #literal value
		literal = binary[pt:]
		result, length = extractLiteral(literal)
		pt += length
	else: #operator
		lengthTypeID = int(binary[pt:pt+1], 2)
		pt += 1
		subpacket_values = []
		if(lengthTypeID == 0):
			lengthOfSubPackets = int(binary[pt:pt+15], 2)
			pt += 15
			index = pt
			while(index < pt + lengthOfSubPackets):
				result, index = parsePacket(binary, index, packet_level + 1)
				subpacket_values.append(result)
			pt = index
		else:
			numberOfSubPackets = int(binary[pt:pt+11], 2)
			pt += 11
			index = pt
			packets = 0
			while(packets < numberOfSubPackets):
				result, index = parsePacket(binary, index, packet_level + 1)
				subpacket_values.append(result)
				packets += 1
			pt = index
		result = applyOperator(packetID, subpacket_values)

	if(packet_level == 0):
		return result
	else:
		return result, pt

if __name__ == "__main__":
	init()
	with open("input.txt") as input_file:
		hexString = input_file.readline()
	binaryString = hexToBinary(hexString)
	total = parsePacket(binaryString, 0, 0)
	print(f"Part 2 Answer: {total}")
