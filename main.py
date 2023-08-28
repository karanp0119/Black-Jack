import random

def house_hit(hand):
    hand.append(random.choice(card))

def new_hit(hand):
    hand.append(random.choice(card))
    print("Here is your new hand:", hand)

def check_house(user_hand, computer_hand):
    while sum(computer_hand) < 17:
        house_hit(computer_hand)
    if sum(computer_hand) > 21:
        print("You win, the dealer has gone over 21. Here is their hand:", computer_hand)
    elif 17 <= sum(computer_hand) <= 21:
        if sum(computer_hand) > sum(user_hand):
            print("You've lost, here is the dealer's hand:", computer_hand)

        elif sum(computer_hand) == sum(user_hand):
            print("No one wins, its a tie. Here is the dealers hand: ", computer_hand)
        else:
            print("You've won! Here is the dealer's hand:", computer_hand)

def check_twentyone(user_hand, computer_hand):
    if sum(user_hand) == 21:
        check_house(user_hand, computer_hand)
    elif sum(user_hand) > 21:
        print("You've lost, here's the dealer's hand:", computer_hand)

print("Hi, welcome to Blackjack!")

card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer_hand = [random.choice(card)]
user_hand = [random.choice(card), random.choice(card)]
print("The dealer's hand is:", computer_hand)
print("Your hand is:", user_hand)

check_twentyone(user_hand, computer_hand)

while sum(user_hand) < 21:
    hit = input("Do you wish to hit? Y or N\n")
    if hit.lower() == 'y':
        new_hit(user_hand)
        check_twentyone(user_hand, computer_hand)
    else:
        check_house(user_hand, computer_hand)
        break
