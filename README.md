Roulette Simulator
==================

Simulates the Martingale betting strategy on the french roulette.\n
Allows you to define the following variables:

	fund = 315
	depth = 3
	minBet = 5
	maxBet = 900

| Variable        | Description         |
| ------------- |-------------|
| *fund*   | The starting capital |
| *depth*  | The typical Martingale strategy uses a depth of 1. E.g. after the appearance of a red number once, you bet on a black number. A depth of 3 for example means that a red number has to appear three times in a row before betting on black.    |
| *minBet* | Minimum betting capital |
| *maxBet* | Maximum betting capital (limited by the casino) |

### Requirements

- matplotlib

### Example

<img src="https://raw.github.com/seblau/roulette-simulator/master/example.png" alt="Image" />