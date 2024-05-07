from classes import *
import time as time

playing_cards = ['A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣',
                 'A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥',
                 'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦',
                 'A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠']


play_on = True

print("Welcome to Blackjack!")
name = input('Please enter your name: ')
money = int(input('Please enter your money total: $'))
player = Player(name, money)
dealer = Dealer()

while play_on:
    bet = int(input(f"How much would you like to bet? $"))

    player.hand = []
    player.total = 0
    dealer.hand = []
    dealer.total = 0

    deck = Deck(playing_cards)
    deck.shuffle()

    if bet == 0:
        play_on = False
    elif bet > player.money:
        print("Insufficient money. Please choose a lower bet.")
        continue
    else:
        player.place_bet(bet)

    print('\nLet the game begin!\n')

    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())

    print(f"Dealer's hand: {dealer.hand}")
    print(f"Your hand: {player.hand}\n")


    lose = False
    while True:
        add_card = input("Hit or Stand? ")
        if add_card.lower() == 'stand':
            break
        elif add_card.lower() == 'hit':
            player.add_card(deck.deal_card())
            print(f"Your hand now: {player.hand}")
        else:
            continue

        if player.total > 21:
            lose = True
            print("Bust! You lose.\n")
            break

    if lose:
        continue

    # Dealer plays
    print("Now the Dealer plays:")
    while True:
        if dealer.total < 17:
            time.sleep(2)
            dealer.add_card(deck.deal_card())
            print("Hit!")
            print(dealer.hand)
        else:
            time.sleep(2)
            print("Stand!")

            if dealer.total > 21:
                time.sleep(2)
                print("Bust!")
                player.add_winnings(2 * bet)
                print(f"You win!\nYou now have ${player.money}\n")
                time.sleep(3)
                break

            elif player.total > dealer.total:
                time.sleep(2)
                player.add_winnings(2 * bet)
                print(f"You win!\nYou now have ${player.money}\n")
                time.sleep(3)
                break

            elif dealer.total > player.total:
                time.sleep(2)
                print(f"You lose!\nYou now have ${player.money}\n")
                time.sleep(3)
                break

            else:
                time.sleep(2)
                player.add_winnings(bet)
                print(f"It is a draw!\nYou now have ${player.money}\n")
                time.sleep(3)
                break


























