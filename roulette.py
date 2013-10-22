import random
import matplotlib.pyplot as plt

redNumbers = (1,3,5,7,9,12,14,16,18,19,21,23,25,27,30,32,34,36)
modes = ('red', 'black', 'even', 'odd', 'low', 'high')
bets = {'red': 'black', 'black': 'red', 'even': 'odd', 'odd': 'even', 'low': 'high', 'high': 'low'}
debug = False


def findSequence():
	broke = False

	if len(history) >= depth:
		for mode in modes:
			broke = False
			for j in range(depth):
				element = history[-1*(j+1)]
	
				if mode == 'red':
					if element not in redNumbers:
						broke = True
						break
				if mode == 'black':
					if element in redNumbers:
						broke = True
						break
				if mode == 'even':
					if element % 2 != 0:
						broke = True
						break
				if mode == 'odd':
					if element % 2 == 0:
						broke = True
						break
				if mode == 'low':
					if element > 18:
						broke = True
						break
				if mode == 'high':
					if element < 19:
						broke = True
						break
			if not broke:
				return mode
		return None
	else:
		return None


def placeBet():
	return bets[sequence]


def win():
	if number in redNumbers and bet == 'red':
		return True
	if number not in redNumbers and bet == 'black':
		return True
	if number % 2 == 0 and bet == 'even':
		return True
	if number % 2 != 0 and bet == 'odd':
		return True
	if number < 19 and bet == 'low':
		return True
	if number > 18 and bet == 'high':
		return True


if __name__ == "__main__":

	startingCapital = 315
	depth = 3
	minBet = 10
	maxBet = 900

	numberOfPlays = 100
	playingDuration = 50

	mean_development = [0] * playingDuration

	for j in range(numberOfPlays):
		if debug: print '###### Game number %d started ######' % (j)

		fund = startingCapital
		fund_development = []
		history = []
		status = 'WAIT'
		sequence = None
		bet = None
		amount = minBet

		for i in range(playingDuration):
			number = random.randint(0, 36)
			history.append(number)
	
			if bet is not None:
				if win():
					fund = fund + amount * 2
					if debug: print 'WON %d, %d in pot' % (amount, fund)
					status = 'WAIT'
					sequence = None
					bet = None
					amount = minBet
				else:
					if fund == 0:
						if debug: print 'No money left'
						break
					else:
						amount = amount * 2

			fund_development.append(fund)
	
			if status == 'WAIT':
				sequence = findSequence()
				if sequence is not None:
					if debug: print sequence
					status = 'PLAY'
				else:
					status = 'WAIT'
	
			if status == 'PLAY':
				bet = placeBet()
				if fund < amount: amount = fund
				if amount > maxBet: amount = minBet
				if debug: print 'Bet %d on %s' % (amount, bet)
				fund = fund - amount
			else:
				bet = None

		for f in range(playingDuration):
			if f >= len(fund_development):
				h = 0
			else:
				h = fund_development[f]

			mean_development[f] = (mean_development[f] * j + h) * 1.0 / (j + 1)

	plt.xlabel('number of games')
	plt.ylabel('money')
	plt.plot(mean_development, label='mean fund development')
	plt.legend()
	plt.show()
