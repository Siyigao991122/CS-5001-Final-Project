import random

class bet:
    '''The class bet defines objects of player's bet score and computer's bet score that can be used in the continue_game function to record
    each round and the final bet for computer and human.'''
    def __init__(self, comp_score, human_score):
        '''Define computer score object and human score object'''
        self.comp_score = comp_score                
        self.human_score = human_score
        if not type(self.human_score) is int:            # Check the datatype of human_score is correct
            raise TypeError
        if not type(self.comp_score) is int:                # Check the datatype of comp_score is correct
            raise TypeError

    def get_the_bet(self, bet_given):
        '''The function will get the input of the integer bet and subtract from the original bet score, 100, and update it to the two objects: self.comp_score and 
        self.human_score in each round of the game'''
        if not type(bet_given) is int:                  #Raise ValueError if the given bet is not an integer
            raise ValueError('Please enter an positivev integer')
        self.comp_score -= bet_given
        self.human_score -= bet_given
        if self.comp_score <= 0:                        # Check if the bet input has exceeded the current bet
            return 'computer has reached 0'
        elif self.human_score <= 0:
            return 'You have reached 0'
        return self.human_score


def start():
    '''The start() function pairs up suits with each ranks to generate 52 cards in poker game. Then it selects 2 cards for both computer and 
    the player as their starting cards in the game and select another 3 cards for the card pool preparing to be showed to the player one card 
    at a time in later rounds.'''

    # This is the description of the game
    print('HI THERE, WELCOME TO TEXAS POKER GAME!\n'
          'First time player? No worries, this is an easy and funny text based poker game with three rounds in total. '
          'Your bet is 100 in the beginning. An ante will be made if you choose to start the game, which is 2 points.\n'
          'Then you enter the first round of the game. You now have two cards available, so what you need to do is to check the rest three cards in\n'
          'the card pool to see if you can match any of the combination in the hand ranking table. Things can get interesting from here with\n'
          'different strategies, but luck is also important! If your cards seem to have little chance to win, add less bet or just Quit and Run!')
    # This is the Poker hand ranking table
    print('#######Card Ranking Table#########\n'
          '-------------------------------\n|♦10 ♦J ♦Q ♦K ♦A     Royal Flush|\n-------------------------------\n|♣7 ♣8 ♣9 ♣10 ♣J  Straight Flush|\n'
          '-------------------------------\n|♦4 ♥4 ♣4 ♠4 ♥J   Four of a Kind|\n-------------------------------\n|♦3 ♥3 ♣3 ♠2 ♥2       Full house|\n'
          '-------------------------------\n|♠K ♠9 ♠J ♠5 ♠A            Flush|\n-------------------------------\n|♦7 ♥8 ♣9 ♠10 ♥J        Straight|\n'
          '-------------------------------\n|♦2 ♥2 ♣2 ♠3 ♥J  Three of a Kind|\n-------------------------------\n|♦5 ♥5 ♣2 ♠2 ♠Q         Two Pair|\n'
          '-------------------------------\n|♣3 ♥3 ♣6 ♠7 ♥K             Pair|\n-------------------------------\n|♣K ♥3 ♣J ♦1 ♥2        High Card|')

    poker=['♦', '♥', '♣', '♠']
    number = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    pair = []
    for i in poker:                                 # Combines each suit with all ranks to form 52 card deck
        for j in range(len(number)):
            pair.append([f'{i} {number[j]}'])
    computer_card = []
    human_card = []
    i = 0

    # Randomly assign two cards to computer and player and create card pool with three cards
    while i < 2:
        computer_card1 = random.choice(pair)
        pair.remove(computer_card1)
        computer_card.append(computer_card1)
        human_card1 = random.choice(pair)
        pair.remove(human_card1)
        human_card.append(human_card1)
        i += 1
    common = random.sample(pair, 3)
    return [computer_card, human_card, common]


def continue_game(pair):
    '''The continue_game function takes the returned player's, computer's and card pool's cards from the start function and call the bet
    class by setting the starting bet score to be 100 for both computer and player. In the function, the while loop will execute three times 
    as the three rounds in the poker game to show player the cards in the card pool one card per round. During each round, the function
    needs an input of round bet to continue executing in the while loop. After the execution of the while loop, the function returns the 
    remaining bet score and the final 5-card poker hand from both computer and player.'''
    p = bet(100, 100)           # The bet class is called with 100 and 100 arguments for initial computer score and player score.
    decision = str(input("You sure you wanna start the game? (Yes/No): "))
    decision = decision.lower()
    if decision == 'yes':
        common = pair[2]
        human_card = pair[1]
        computer_card = pair[0]
        card_shown = []
        i = 0
        # While loop iterates three times for the three rounds in the game. Each iteration calls the get_the_bet() function in class bet to 
        # update the bet score
        while i < 3:
            print(f'----------------\n|              |\n|    ROUND{i+1}    |\n|              |\n----------------')
            card_shown.append(common[i])           # The list shown to player that's generated by adding cards from card pool one card per round.
            i += 1
            print(f'card pool: {card_shown}\nYour card: {human_card}') 
            # Check if the bet score is entered correctly as an integer in each round
            try:
                command = int(input('Enter your bet to see the next card.\n(Note: if you quit now you lose all bets in the pool): ' ))
            except:
                return
            print(f'Your current bet: {p.get_the_bet(command)}')
        print('--------------------This is your final round--------------------')
        final_list_com = common + computer_card     # Combining two cards from computer and the three cards in pool to generate a 5-card hand
        final_list_human = common + human_card      #Combining two cards from player and the three cards in pool to generate a 5-card hand
        return [final_list_com, final_list_human, p.comp_score, p.human_score]
    else:
        return

def rules(final_pair):
    '''The rules function takes the final 5-card hand for computer and player from the continue_game function and compare these two poker hands
    by separating the suits and ranks into two dictionary and count each element in the dictionary. The dictionary will be searched based on
    the winning combinations in the real Texas Poker game. '''
    hu_dict = dict()
    com_dict = dict()
    com_dict_number = dict()
    hu_dict_number = dict()
    final_com = final_pair[0]               # Computer's final 5-card hand
    final_hu = final_pair[1]                # Player's final 5-card hand
    comp_bet_score = final_pair[2]          # Computer's bet score after three rounds
    human_bet_score = final_pair[3]         # Player's bet score after three rounds

    # Separating the suits and ranks in the two sets of 5-card hands and put into dictionary. And counts the suits and ranks in dictionary.
    for i in final_hu:
        i = str(i)
        if i[2] not in hu_dict:     # Creates the player's 5-card hand suits dictionary and counts the number of each suits
            hu_dict[i[2]] = 1
        else:
            hu_dict[i[2]] += 1
        if i[4] not in hu_dict_number:  # Creates the player's 5-card hand ranks dictionary and counts the number of each ranks
            hu_dict_number[i[4]] = 1
        else:
            hu_dict_number[i[4]] += 1
    for j in final_com:
        j = str(j)
        if j[2] not in com_dict:        # Creates the computer's 5-card hand suits dictionary and counts the number of each suits
            com_dict[j[2]] = 1
        else:
            com_dict[j[2]] += 1
        if j[4] not in com_dict_number: # Creates the computer's 5-card hand ranks dictionary and counts the number of each ranks
            com_dict_number[j[4]] = 1
        else:
            com_dict_number[j[4]] += 1
    # print(hu_dict, hu_dict_number, com_dict, com_dict_number)
    hu_dict_v = hu_dict.values()
    com_dict_v = com_dict.values()
    hu_dict_number_v = hu_dict_number.values()
    com_dict_number_v = com_dict_number.values()

# Compare the suits in the 5-card poker hand
    if 5 in hu_dict_v:             # Check if all 5 cards have the same suit for player
        hu_result = 'Flush'
    if 5 in com_dict_v:
        com_result = 'Flush'        # Check if all 5 cards have the same suit for computer

# Compare the ranks in the 5-card poker hand
    if 4 in hu_dict_number_v:                       # Check if any rank has all four cards present in the poker hand
        hu_result = 'Four of a kind'
    elif 3 in hu_dict_number_v:                     # Check if any rank has three cards present in the poker hand
        if 2 in hu_dict_number_v:
            hu_result = 'Full house'
        else:
            hu_result = 'Three of a kind'
    elif len([k for k,v in hu_dict_number.items() if v == 2]) == 2:    # Check if there's two pairs of cards with same rant in the poker hand
        hu_result = 'Two pairs'
    elif 2 in hu_dict_number_v:                     ## Check if there's a pair of cards with same rank in the poker hand.
        hu_result = 'One pair'
    else:
        hu_result = 'High card'
    
    if 4 in com_dict_number_v:
        com_result = 'Four of a kind'
    elif 3 in com_dict_number_v:
        if 2 in com_dict_number_v:
            com_result = 'Full house'
        else:
            com_result = 'Three of a kind'
    elif len([k for k,v in com_dict_number.items() if v == 2]) == 2:
        com_result = 'Two pairs'
    elif 2 in com_dict_number_v:
        com_result = 'One pair'
    else:
        com_result = 'High card'
    # This list is ordered based on the poker hand rankings
    ranking = ['High card', 'One pair', 'Two pairs', 'Three of a kind', 'Full house', 'Four of a kind', 'Flush']
    ranking_hu = ranking.index(hu_result)       # Compare the poker hand by the index of each rankings in the ranking list
    ranking_com = ranking.index(com_result)
    print(f'The computer\'s cards: {final_com}\nYour cards: {final_hu}')
    if ranking_hu > ranking_com:
        human_bet_score = human_bet_score + 2*(100 - human_bet_score)
        print(f'The Computer got: {com_result}\nYou got: {hu_result}\n--------------------\n|    You Win!!!!!   |\n|       \N{winking face}          |\n--------------------')
        print(f'Your score: {human_bet_score}\n Computer\'s score: {comp_bet_score}')
    elif ranking_hu < ranking_com:
        comp_bet_score = comp_bet_score + 2*(100 - comp_bet_score)
        print(f'The Computer got: {com_result}\nYou got: {hu_result}\n--------------------\n|    You Lose...   |\n|       \N{melting face}          |\n--------------------')
        print(f'Your score: {human_bet_score}\nComputer\'s score: {comp_bet_score}')
    else:
        print(f'The Computer got: {com_result}\nYou got: {hu_result}\n--------------------\n|       Fold        |\n|        \N{handshake}         |\n--------------------')    
        print(f'Your score: 100\nComputer\'s score: 100')


def menu():
    '''The menu function takes in the user input from keyboard and convert it into lower case. Then it returns the input for the use in run
    function'''
    choice = input('What would you like to do?\nstart\nquit\nIf you are in the final round please enter "Final"\n: ')
    choice = choice.lower()
    return choice


def run():
    '''The run funtion takes the returned command from menu function and put it into if statement to start any associated function that 
    matches the command'''
    while True:
        command = menu()
        if command == 'final':
            rules(final_pair)
        elif command == "start":
            pair = start()
            final_pair = continue_game(pair)
        elif command == 'quit':
            return


if __name__ == "__main__":
    run()
