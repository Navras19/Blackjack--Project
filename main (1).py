############### Blackjack Project #####################

import random
# from replit import clear
from art import logo
"""Returns a random cards from a deck."""
def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    
    card = random.choice(cards)
    return card



def calculate_score(cards):
   
 # if 11 in cards and 10 in cards and len(cards)==2:
    
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards) > 21 :
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

    
def compare(user_score,computer_score):
    if user_score > 21 :
        return " ~You went over.You lose:("
    if  computer_score > 21:
        return "Computer lose.You win:) "
        
    if user_score == computer_score:
        return "It's a draw."
    elif user_score == 0:
        return "You have got a blackjack. You win :)"
    elif computer_score == 0:
        return "Computer has got a blackjack. Computer wins :)"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose. Computer wins"
        


def play_game():
    print(logo)

    
    user_cards = []
    computer_cards = []
    is_game_over = False
    for card in range (2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())
    
    while not is_game_over:    
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your card : {user_cards} and your currunt score: {user_score}")
        print(f"Computer's first card : {computer_cards[0]} ")
        if user_score == 0 or computer_cards == 0 or user_score > 21:
            is_game_over = True
        else:
            ask_user = input("Type 'y' to get  another card , type 'n' to pass: ")
            if ask_user == 'y':
                user_cards.append(deal_cards())
                print(user_cards)
            else:
                is_game_over = True
    
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's  final hand : {computer_cards} and computer's final score: {computer_score}")
    print(compare(user_score,computer_score))


while input("Do you want to play a game of Blackjack ? Type 'y' or 'n': ") == 'y':
    # clear()
    play_game()
        
















# def compare(user_score,computer_score):
#     if user_score > 21 and computer_score > 21:
#         return " ~You went over .You lose:("
        
#     if user_score == computer_score:
#         return "It's a draw."
#     elif user_score == 0:
#         return "You have got a blackjack. You win :)"
#     elif computer_score == 0:
#         return "Computer has got a blackjack. Computer wins :)"
#     elif user_score > computer_score:
#         return "You win"
#     else:
#         return "You lose. Computer wins"
        
# compare(user_score,computer_score)




# def calculate_score():
#     user_score = 0
#     for score in user_cards:
#         user_score+=score
#     print(f"Your total score is {user_score}")

#     computer_score = 0
#     for score in computer_cards:
#         computer_score+=score
       
#     print(f"The computer's score is {computer_score}")
#     if 11 in user_cards and user_score > 21 :
#          user_cards.remove(11)
#          user_cards.append(1)
#     if 11 in computer_cards and computer_score > 21 :
#          computer_cards.remove(11)
#          computer_cards.append(1)

#     if 11 in user_cards and 10 in user_cards:
#         print("You have a blackjack. You win")
#     if 11  in computer_cards and 10 in computer_cards:
#         print("Computer has a blackjack.Computer wins")
        
# calculate_score()