Roulette Simulator
==================

Simulates the Martingale betting strategy on the french roulette.\n
Allows you to define the following variables:

	debug = True
	
	startingCapital = 315
	depth = 3
	minBet = 10
	maxBet = 900

	numberOfPlays = 100
	playingDuration = 50

| Variable        | Description         |
| ------------- |-------------|
| *debug*  | If set to True print debugging information to console |
| *startingCapital*   | The starting capital |
| *depth*  | The typical Martingale strategy uses a depth of 1. E.g. after the appearance of a red number once, you bet on a black number. A depth of 3 for example means that a red number has to appear three times in a row before betting on black.    |
| *minBet* | Minimum betting capital |
| *maxBet* | Maximum betting capital (limited by the casino) |
| *numberOfPlays* | Number of casino games you would like to simulate. The average fund development gets plotted. |
| *playingDuration* | Duration of one casino game counted how often the ball rolls |

### Requirements

- matplotlib

### Example

Plots the average fund development of 100 casino games with a playing duration of 50, starting capital 315, depth = 3, minBet = 10 and maxBet = 900. 

<img src="https://raw.github.com/seblau/roulette-simulator/master/example.png" alt="Image" />
