# BlackJack Game

## Overview
An interactive blackjack game written in python. This game allows you to play with a dealer until there is a winner.

## Requirements
This game requires `python3.x`.

## Rules of the game
* You can choose to Hit/Twist or Stand/Stick depending on your hand total.
* Dealer must hit on 16 or lower cards.
* If you are dealt a  total of 21 cards at the inital round, you have a Blackjack.

## How to play game
Enter `python3 game_script.py` in your terminal.

* You can choose to Hit by pressing 'h' on your keyboard, if you are not
satisfied with the two initial card dealt for you or Stand by pressing 's' and
see if the dealer goes bust (total hand score greater than 21) or Quit the game by pressing 'q'.

## Testing
There are unit tests for this game.

To run the tests, enter `python3 test_game_script.py` in your terminal.

## Improvements
* Make a Blackjack base class with common methods and inherit from this base class to create variations of the game with different rules.
* Add ability to place a stake or bet on a hand.
* Implement doubling, splitting and insurance.
* Add code coverage using `coverage` python library.