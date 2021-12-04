#December 4th, 2021

listOfBoards = []
listOfNumbers = []

with open("input.txt") as input_file:
	fullInput = [line.split() for line in input_file.readlines()]
	listOfNumbers = [int(number) for number in fullInput[0][0].split(",")]

	for i in range(2, len(fullInput), 6):
		board = []
		for j in range(0, 5):
			board.append(fullInput[i + j])
		listOfBoards.append(board)

def checkHorizontal(board, row):
	bingo = True
	for column in range(5):
		if int(board[row][column]) > 0: #filled squares are denoted with negative values
			bingo = False
	return bingo

def checkVertical(board, column):
	bingo = True
	for row in range(5):
		if int(board[row][column]) > 0: #filled squares are denoted with negative values
			bingo = False
	return bingo

def checkBingo(board):

	for row in range(5): #check all rows for bingo
		bingo = checkHorizontal(board, row)
		if bingo: 
			return bingo

	for col in range(5): #check all columns for bingo
		bingo = checkVertical(board, col)
		if bingo: 
			return bingo

	return False

def updateBoard(board, value):
	for row in range(5):
		for col in range(5):
			space = int(board[row][col])
			if space != value: continue
			board[row][col] = -1 * space

def resetAllBoards(boardList): #sets all boards back to their default values
	for board in boardList:
		for row in range(5):
			for col in range(5):
				board[row][col] = abs(int(board[row][col]))

def getBoardSum(board):
	sum = 0
	for row in range(5):
		for col in range(5):
			if(int(board[row][col]) > 0): 
				sum += abs(int(board[row][col]))
	return sum

#problem 1
winningBoard = None
currentNumber = None
for number in listOfNumbers:
	bingoFound = False
	for board in listOfBoards:
		updateBoard(board, number)
		bingo = checkBingo(board)
		if bingo: 
			bingoFound = True
			winningBoard = board
			currentNumber = number
			break
	if bingoFound: break

sum = getBoardSum(winningBoard)
answer = sum * currentNumber

print(f"Sum: {sum}\nLast Pulled Number: {currentNumber}\nPart 1 answer: {answer}")

#problem 2
resetAllBoards(listOfBoards)

totalNumberOfBoards = len(listOfBoards)
boardsRemaining = totalNumberOfBoards

currentNumber = None
lastBoard = None
listOfBoardsWithBingos = [False for _ in range(totalNumberOfBoards)]
for number in listOfNumbers:
	for i in range(totalNumberOfBoards):
		board = listOfBoards[i]
		updateBoard(board, number)
		bingo = checkBingo(board)

		if not bingo: continue
		if(not listOfBoardsWithBingos[i]):
			boardsRemaining -= 1
			currentNumber = number
			lastBoard = board
			listOfBoardsWithBingos[i] = True
			
	if boardsRemaining == 0:
		break

sum = getBoardSum(lastBoard)
answer = sum * currentNumber

print(f"Sum: {sum}\nLast Pulled Number: {currentNumber}\nPart 2 answer: {answer}")
