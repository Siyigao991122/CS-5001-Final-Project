# CS-5001-Final-Project Readme

* Semester: 2023 Spring
* Student: Siyi Gao

The project is named "Texas Poker", so it can be read from the name that this project is a text based poker game in python. 

Description:
From the beginning, there'll be a brief description about the rules and a ranking table printed out on the screen. Then player can choose if they want to start the game with an ante of 2. If they choose to start the game, player's bet will automatically be deducted from 100 to 98 with the first ante applied. During the first round, the first card in card pool will be shown to the player along with the 2 cards that's assigned to the player, so there are three cards in total that's been shown on the screen. From here, player can compare the available cards with hand ranking table to measure their possibility to win the game, if the chance is pretty low (the cards are extremely random), they can quit the game by losing the bets in the pool. If they decide to continue the game, they'll be asked to enter the amount of bet based on their confidence of their cards in order to enter the next round. Thus, the second and third round are basically copies of the first round, only with bets contnually being updated. When players reaching the final round, there'll be a notification saying "This is the final round", so currently all five cards are printed to the screen and player need to enter "final" command to see the final result. By entering the command, both 5-card hands from player and computer will be printed out and the compare results will also be printed out, indicating what kind of poker hand does both side got. Finally, based on if the player win or lose the game, there'll be a slogan board with emoji printed to the screen and this the end of the whole game. After that, player can enter "start" to startover and the process is exactly the same as described above.

Key aspects:
The first key aspect is that there're three rounds in total for the game and in each round, one of the cards from the card pool will be shown to the player, so they can match the cards shown in card pool with their own cards to see if it's possible to match any of the hand rankings. The second key aspect is that the player will be provided with two cards from the beginning as their base cards so they can make decision if or not to continue the game just by viewing their own cards when game started. The third key aspect is that the bet score will be 100 for both computer and player and it will be updated during each round depending on what number does the player enter as the bet for each round. In the final round, the bet score will be calculated based on if the player win, lose or fold the game. The fourth key aspect is that the project contains the poker hand measuring and comparing process following the ranking rules of real Texas Poker game, so the information about player's poker hand will be made available in the project. The final key aspect is that since this is an text based game, the hand rankings table, round number, cards display, bets, warning sign and the final winning sign are all printed on the screen as text. 
