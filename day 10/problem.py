input = []
with open("input.txt") as input_file:
	input = [line.strip() for line in input_file.readlines()]

closers =  {'>':0,']':0,'}':0,')':0}
openers = {'<':0,'[':0,'{':0,'(':0}
def scanChunk(string, offset):
	chunkPairs = {'<':'>','[':']','{':'}','(':')',}
	completion_points = {'<':4,'[':2,'{':3,'(':1}
	i = offset
	autocomplete_score = 0
	while(i < len(string)):
		char = string[i]
		if char in chunkPairs.keys():
			closer = scanChunk(string, i+1)
			if closer == None:
				autocomplete_score += completion_points[char]
				print(f"no match found for {char}. Adding {completion_points[char]} to score.")
				break
			if closer[0] == chunkPairs[char]: #they match
				i = closer[1] + 1
			else:
				corruptedLines.append(string)
				closers[closer[0]] += 1
				break
		else:
			return (char, i)

corruptedLines = []
for line in input: scanChunk(line, 0)
for corruptedLine in corruptedLines: input.remove(corruptedLine)
corruption_points = {'>':25137,']':57,'}':1197,')':3}
score = 0
for closer in closers.keys(): score += corruption_points[closer] * closers[closer]
print(f"Part 1 Answer: \n\tScore: {score}")

#problem 2
print(f"Part 2 Answer: \n\tScore: {score}") #{{