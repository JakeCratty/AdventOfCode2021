#December 15th, 2021

input = []
with open("input.txt") as input_file:
	input = [line.strip() for line in input_file]

for line in input:
	print(line)

