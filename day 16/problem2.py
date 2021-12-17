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

def parsePacket(binary, pt, packet_level):
	print(f"--New Packet Detected on layer {Fore.RED}{packet_level}{Style.RESET_ALL}.")
	packetLength = 6 #tracks this packets total length to be returned at the end
	versionNumber = int(binary[pt:pt+3], 2)
	versionTotal = versionNumber
	packetID = int(binary[pt+3:pt+6], 2)
	pt += 6
	print(f"\tVersion Number: {Fore.GREEN}{versionNumber}{Style.RESET_ALL}, Packet ID: {Fore.YELLOW}{packetID}{Style.RESET_ALL}")
	
	if(packetID == 4): #literal value
		literal = binary[pt:]
		literal, length = extractLiteral(literal)
		pt += length
		print(f"\tPacket value: {literal}")
	else: #operator
		lengthTypeID = int(binary[pt:pt+1], 2)
		pt += 1
		print(f"\tLength Type ID: {lengthTypeID}")
		if(lengthTypeID == 0):
			lengthOfSubPackets = int(binary[pt:pt+15], 2)
			print(f"\tLength of subpackets: {lengthOfSubPackets}")
			pt += 15
			index = pt
			while(index < pt + lengthOfSubPackets):
				versionNumber, index = parsePacket(binary, index, packet_level + 1)
				versionTotal += versionNumber
			pt = index
		else:
			numberOfSubPackets = int(binary[pt:pt+11], 2)
			print(f"\tNumber of sub packets: {numberOfSubPackets}")
			pt += 11
			index = pt
			packets = 0
			while(packets < numberOfSubPackets):
				versionNumber, index = parsePacket(binary, index, packet_level + 1)
				versionTotal += versionNumber
				packets += 1
			pt = index

	if(packet_level == 0):
		return versionTotal
	else:
		return versionTotal, pt

if __name__ == "__main__":
	init()
	with open("input.txt") as input_file:
		hexString = input_file.readline()
	binaryString = hexToBinary(hexString)
	totalVersionNumber = parsePacket(binaryString, 0, 0)
	print(f"Part 1 Answer: {totalVersionNumber}")
