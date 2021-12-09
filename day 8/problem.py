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
print(count)

#dab = 0, 2, 5
#ab = 2, 5
#eafb = 1, 2, 3, 5
#acedgfb = 0, 1, 2, 3, 4, 5, 6, 7
#cdfgeb = 
#cdfbe = 