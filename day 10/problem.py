#December 10th, 2021
input = []
with open("input.txt") as input_file:
	input = [line.strip() for line in input_file.readlines()]

closers =  {'>':0,']':0,'}':0,')':0} #tracks how many of each closing pair caused a corruption
corruption_points = {'>':25137,']':57,'}':1197,')':3} #the point values for each corrupted closer
completion_points = {'<':4,'[':2,'{':3,'(':1} #the point value for each autocompleted closer
chunkPairs = {'<':'>','[':']','{':'}','(':')',} #the opener/closer pairs
corrutped_score = 0 #total corrupted score
autocomplete_scores = [] #list of all autocompleted scores
corruptedLines = [] #list of all corrupted lines
def scanChunk(string, offset): #recursively find all chunks
	i = offset
	autocomplete_score = 0
	while(i < len(string)): #check each char in string
		char = string[i]
		if char in chunkPairs.keys(): #if the char is an opener
			closer = scanChunk(string, i+1) #recall function on next char, get a closer triplet
			if closer == None or closer[2] != -1: #if closer is none (no end found for chunk) or the chunk was corrupted
				if closer != None: #if it was not none, add and then multiply as per instructions
					autocomplete_score += closer[2]
					autocomplete_score *= 5
				autocomplete_score += completion_points[char] #increase score by point value 
				return (chunkPairs[char], i, autocomplete_score) #return a successful triplet
			elif closer[0] == chunkPairs[char]: #if the closer matches the most recent opening chunk
				i = closer[1] + 1 #increase i to bypass the current chunk
			elif string not in corruptedLines: #if the line was not marked as corrupt
				corruptedLines.append(string) #add it to corrupt lines
				closers[closer[0]] += 1 #increase the closer count for the corrupt closer
				return(chunkPairs[char], i+1, -1) #return a corrupted triplet
			else: #if the value is corrupted and is marked as corrupt just return a failed triplet and do nothing
				return(chunkPairs[char], i+1, -1)
		else:
			return (char, i, -1) #if the current character is a corrupt closer, return a failed triplet
for line in input: #scan all lines for chunks
	value = scanChunk(line, 0) #get a triplet returned
	if value != None and line not in corruptedLines: #if the line was not marked astriplet isn't corrupt
		autocomplete_scores.append(value[2]) #add a new completed line to the autocomplete scores
autocomplete_scores.sort() #sort all scores, the answer is the median score
for closer in closers.keys(): corrutped_score += corruption_points[closer] * closers[closer] #calculate corrupted score
print(f"Part 1 Answer: \n\tScore: {corrutped_score}")
print(f"Part 2 Answer: \n\tScore: {autocomplete_scores[len(autocomplete_scores)//2]}")