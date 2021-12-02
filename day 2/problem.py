#December 2nd, 2021

instructions = []
with open("input.txt") as input_file:
	instructions = [line.split() for line in input_file.readlines()]

#problem 1
depth = 0
horizontalPosition = 0

for instruction in instructions:
	direction = instruction[0]
	distance = int(instruction[1])

	if(direction == "forward"): horizontalPosition += distance
	elif(direction == "down"): depth += distance
	elif(direction == "up"): depth -= distance

print(f"Depth: {depth} | Horizontal Position: {horizontalPosition} | Answer: {(depth * horizontalPosition)}")

#problem 2
depth = 0
horizontalPosition = 0
aim = 0
for instruction in instructions:
	direction = instruction[0]
	delta = int(instruction[1])

	if(direction == "forward"): 
		horizontalPosition += delta
		depth += aim * delta
	elif(direction == "down"): aim += delta
	elif(direction == "up"): aim -= delta


print(f"Depth: {depth} | Horizontal Position: {horizontalPosition} | Answer: {(depth * horizontalPosition)}")


