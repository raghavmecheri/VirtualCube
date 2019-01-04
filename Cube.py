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

	#Basic cube setupx
	whiteArray = [[Color.WHITE,Color.WHITE,Color.WHITE],[Color.WHITE,Color.WHITE,Color.WHITE],[Color.WHITE,Color.WHITE,Color.WHITE]]
	blueArray = [[Color.BLUE,Color.BLUE,Color.BLUE],[Color.BLUE,Color.BLUE,Color.BLUE],[Color.BLUE,Color.BLUE,Color.BLUE]]
	yellowArray = [[Color.YELLOW,Color.YELLOW,Color.YELLOW],[Color.YELLOW,Color.YELLOW,Color.YELLOW],[Color.YELLOW,Color.YELLOW,Color.YELLOW]]
	greenArray = [[Color.GREEN,Color.GREEN,Color.GREEN],[Color.GREEN,Color.GREEN,Color.GREEN],[Color.GREEN,Color.GREEN,Color.GREEN]]
	redArray = [[Color.RED,Color.RED,Color.RED],[Color.RED,Color.RED,Color.RED],[Color.RED,Color.RED,Color.RED]]
	orangeArray = [[Color.ORANGE,Color.ORANGE,Color.ORANGE],[Color.ORANGE,Color.ORANGE,Color.ORANGE],[Color.ORANGE,Color.ORANGE,Color.ORANGE]]
	#Assembling the cube as arrays
	rubik = [whiteArray, blueArray, orangeArray, greenArray, redArray, yellowArray]	
	#Define an isSolved method - Pending	
	solvedRubik = [whiteArray, blueArray, orangeArray, greenArray, redArray, yellowArray]	

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

	#Note that rotate clockwise is always invoked with the white center of the cube facing upwards. Only the four equitorial sides' faces may be rotated 
	def rotateEquatorial(self, faceColor):
		if validAxialColor(faceColor):
			self.equatorialClockwise(faceColor)

	def rotateAxial(self, faceColor, axialColor):
		if !(validAxialColor(faceColor)) and validAxialColor(axialColor):
			self.axialClockwise(faceColor, axialColor)

	#Helper methods
	def __validAxialColor__(axialColor):
		return (axialColor != Color.WHITE and axialColor != Color.YELLOW)

	def __equatorialClockwise__(self, faceColor):
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

	def __verticallyModify__(self, column, index, color):
		for i in range (3):
			self.rubik[index][i][column] = color

	def __axialClockwise__(self, faceColor, axialColor):
		if faceColor == Color.WHITE:
			self.shiftFirstRowForward()
		elif faceColor == Color.YELLOW:
			self.shiftFirstRowBackward()

	def __shiftFirstRowForward__(self):

	def __shiftFirstRowBackward__(self):


myCube = Cube()
myCube.outputCube()
myCube.rotateClockwise(Color.BLUE)
myCube.outputCube()

