from enum import Enum
import copy

class Color(Enum):
	WHITE = 0
	BLUE = 1
	ORANGE = 2
	GREEN = 3
	RED = 4
	YELLOW = 5


class Cube:

	#Basic cube setup
	whiteArray = [[Color.WHITE,Color.WHITE,Color.WHITE],[Color.WHITE,Color.WHITE,Color.WHITE],[Color.WHITE,Color.WHITE,Color.WHITE]]
	blueArray = [[Color.BLUE,Color.BLUE,Color.BLUE],[Color.BLUE,Color.BLUE,Color.BLUE],[Color.BLUE,Color.BLUE,Color.BLUE]]
	yellowArray = [[Color.YELLOW,Color.YELLOW,Color.YELLOW],[Color.YELLOW,Color.YELLOW,Color.YELLOW],[Color.YELLOW,Color.YELLOW,Color.YELLOW]]
	greenArray = [[Color.GREEN,Color.GREEN,Color.GREEN],[Color.GREEN,Color.GREEN,Color.GREEN],[Color.GREEN,Color.GREEN,Color.GREEN]]
	redArray = [[Color.RED,Color.RED,Color.RED],[Color.RED,Color.RED,Color.RED],[Color.RED,Color.RED,Color.RED]]
	orangeArray = [[Color.ORANGE,Color.ORANGE,Color.ORANGE],[Color.ORANGE,Color.ORANGE,Color.ORANGE],[Color.ORANGE,Color.ORANGE,Color.ORANGE]]
	#Assembling the cube as arrays
	rubik = [whiteArray, blueArray, orangeArray, greenArray, redArray, yellowArray]	
	#Define an isSolved method - Pending	
	solvedRubik = [copy.deepcopy(whiteArray), copy.deepcopy(blueArray), copy.deepcopy(orangeArray), copy.deepcopy(greenArray), copy.deepcopy(redArray), copy.deepcopy(yellowArray)]	

	#Helper methods

	def isAxialColor(self, axialColor):
		return (axialColor != Color.WHITE and axialColor != Color.YELLOW)

	def equatorialClockwise(self, faceColor):
		faceColor = faceColor.value
		whiteRow = self.rubik[Color.WHITE.value][2]
		yellowRow = self.rubik[Color.YELLOW.value][2]
		previousIndex = 0
		nextIndex = 0
		previousRow = []
		nextRow = []

		#Conditionals in order to skip the white and yellow layers
		if ((faceColor - 1) == 0):
			previousIndex = faceColor - 3
		else:
			previousIndex = faceColor - 1
		if((faceColor + 1) == 5):
			nextIndex = faceColor + 3
		else:
			nextIndex = faceColor + 1
		#Actual swapping process

		nextRow = copy.deepcopy(self.rubik[nextIndex][2])
		previousRow = copy.deepcopy(self.rubik[previousIndex][2])

		self.rubik[Color.WHITE.value][2] = previousRow
		self.rubik[Color.YELLOW.value][0] = nextRow

		self.verticallyModify(2, previousIndex, Color.YELLOW)
		self.verticallyModify(0, nextIndex, Color.WHITE)

	def verticallyModify(self, column, index, color):
		for i in range (3):
			self.rubik[index][i][column] = color

	def axialClockwise(self, faceColor):
		if faceColor == Color.WHITE:
			self.shiftRow(0, True)
		elif faceColor == Color.YELLOW:
			self.shiftRow(2, False)

	def shiftRow(self, rowIndex, isForward):
		if(isForward):
			self.performRowShift(rowIndex)
		else:
			for i in range(0,2):
				self.performRowShift(rowIndex)

	def performRowShift(self, rowIndex):
		#Shift the rows of each side forward
		blueRow = copy.deepcopy(self.rubik[Color.BLUE.value])[rowIndex]
		orangeRow = copy.deepcopy(self.rubik[Color.ORANGE.value])[rowIndex]
		greenRow = copy.deepcopy(self.rubik[Color.GREEN.value])[rowIndex]
		redRow = copy.deepcopy(self.rubik[Color.RED.value])[rowIndex]

		tempBlue = copy.deepcopy(blueRow)
		blueRow = copy.deepcopy(orangeRow)
		orangeRow = copy.deepcopy(greenRow)
		greenRow = copy.deepcopy(redRow)
		redRow = tempBlue

		self.rubik[Color.BLUE.value][rowIndex] = blueRow
		self.rubik[Color.ORANGE.value][rowIndex] = orangeRow
		self.rubik[Color.GREEN.value][rowIndex] = greenRow
		self.rubik[Color.RED.value][rowIndex] = redRow

	#Public Methods
	def outputCube(self):
		for side in self.rubik:
			for row in side:
				for element in row:
					print(element, end = " ")
				print()
			print()

	def getCube(self):
		return self.rubik

	def setCube(self, customRubik):
		self.rubik = customRubik

	#Rotate clockwise is always invoked with the white center of the cube facing upwards. Only the four equitorial sides' faces may be rotated 
	def rotateEquatorial(self, faceColor):
		if self.isAxialColor(faceColor):
			self.equatorialClockwise(faceColor)

	#The face color for axial is either Yellow or White
	def rotateAxial(self, faceColor):
		if not(self.isAxialColor(faceColor)):
			self.axialClockwise(faceColor)

	def isSolved(self):
		flag = True
		for sideIndex in range(0,5):
			for rowIndex in range(0,2):
				for columnIndex in range(0,2):
					if self.rubik[sideIndex][rowIndex][columnIndex] != self.solvedRubik[sideIndex][rowIndex][columnIndex]:
						flag = False
		return flag

