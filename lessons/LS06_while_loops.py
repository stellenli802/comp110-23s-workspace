"""While-loop example in a string"""

cards: str = "5235"

card_index: int = 0
low_card: int = int(cards[0])
#Look at each number in the string
while card_index < 4: 
    #check if current card is less than low card
    current_card: int = int(cards[card_index])
    if(current_card < low_card):
        #update low card with current card
        low_card = current_card
    card_index = card_index + 1
print(low_card)