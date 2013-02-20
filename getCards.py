import math
import sys

# change to take sequence as argument
def doAll():
	# get
	# assumed sequence of length 5, 1s and 0s only
	sequence = sys.argv[1]
	numCards = 5

	# works for numCards = 5
	sequence = generate(sequence, numCards)
	outputCards(sequence, numCards)

def generate(sequence, numNew):
	for digit in range(numNew - 1):
		num1 = int(sequence[-3 : -2])
		num2 = int(sequence[-5 : -4])
		sequence += str((num1 + num2) % 2)

	return sequence

# print. later put in file
# assumes cards arranged correctly
def outputCards(sequence, numCards):
	colors = {"1": "Red", "0": "Black"}
	suits = {"00": "of clubs", "01": "of spades", "10": "of diamonds", "11": "of hearts"}
	values = {"000":"8", "001":"ace", "010":"2", "011":"3", "100":"4", "101":"5", "110":"6", "111":"7"}

	for card in range(numCards):
		info = colors[sequence[card]]
		info += " " + values[sequence[card + 2 : card + 5]]
		info += " " + suits[sequence[card : card + 2]]

		print info

def main():
	doAll()

if __name__ == "__main__":
	main()