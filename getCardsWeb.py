import math
import sys

# change to take sequence as argument
def doAll(userSeq):
	# get
	# assumed sequence of length 5, 1s and 0s only
	sequence = userSeq
	numCards = 5

	# works for numCards = 5
	sequence = generate(sequence, numCards)
	return outputCards(sequence, numCards)

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
	suits = {"00": "of Clubs", "01": "of Spades", "10": "of Diamonds", "11": "of Hearts"}
	values = {"000":"8", "001":"Ace", "010":"2", "011":"3", "100":"4", "101":"5", "110":"6", "111":"7"}

	results = []

	for card in range(numCards):
		info = colors[sequence[card]]
		info += " " + values[sequence[card + 2 : card + 5]]
		info += " " + suits[sequence[card : card + 2]]

		results += info,

	return "<br>".join(results)

def main():
	doAll()

if __name__ == "__main__":
	main()