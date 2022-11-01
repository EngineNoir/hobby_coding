import random
import pyperclip as pc


class Deck:
    def __init__(self):
        self.library = None
        self.hand = []
        self.battlefield = []
        self.exile = []
        self.manabase = []
        self.graveyard = []


    def populate_deck(self):
        # ask for deck name
        deck_name = str(input("What is the name of the " + 
                        "file for your decklist?: ") + '.txt')

        deck_list = open(deck_name, 'r')
        self.library = deck_list.read().splitlines()
        
    def shuffle_deck(self):
        random.shuffle(self.library)

    def view_cards(self):
        how_many = int(input("How many cards do you wish to view?: "))
        i = 0
        while i < how_many:
            print(str(i+1) + ": " + str(self.library[i]))
            i += 1
    
    def put_top_to_bottom(self):
        how_many = int(input("How many cards do you wish to put on the bottom?: "))
        i = 0
        while i < how_many:
            self.library.append(self.library.pop(0))
            i += 1

    def draw_a_card(self):
        self.hand.append(self.library.pop(0))

    def find_card(self):
        i = 1
        for card in self.library:
            print(str(i) + ": " + str(self.library[i-1]))
            i += 1
        which_card = int(input("Which card do you select?: ")) - 1
        self.hand.append(self.library.pop(which_card))
    
    def mill(self):
        how_many = int(input("How many cards would you like to mill? "))
        i = 0
        while i < how_many:
            self.graveyard.append(self.library.pop(0))
            i += 1

    def battlefield_to_graveyard(self, which_card):
        self.graveyard.append(self.battlefield.pop(which_card))

    def battlefield_to_hand(self, which_card):
        self.hand.append(self.battlefield.pop(which_card))

    def battlefield_to_exile(self, which_card):
        self.exile.append(self.battlefield.pop(which_card))

    def graveyard_to_battlefield(self, which_card):
        self.battlefield.append(self.graveyard.pop(which_card))

    def graveyard_to_hand(self, which_card):
        self.hand.append(self.graveyard.pop(which_card))

    def graveyard_to_exile(self, which_card):
        self.exile.append(self.graveyard.pop(which_card))
 
    def exile_to_battlefield(self, which_card):
        self.battlefield.append(self.exile.pop(which_card))

    def exile_to_hand(self, which_card):
        self.hand.append(self.exile.pop(which_card))

    def mana_to_graveyard(self, which_card):
        self.graveyard.append(self.manabase.pop(which_card))
    
    def graveyard_to_manabase(self, which_card):
        self.manabase.append(self.graveyard.pop(which_card))

    def mana_to_hand(self, which_card):
        self.hand.append(self.manabase.pop(which_card))

    def play_card(self, which_card):
        to_field_or_mana = int(input("Play card to battlefield (1) or manabase (2)?"))
        if to_field_or_mana == 1:
            self.battlefield.append(self.hand.pop(which_card))
        elif to_field_or_mana == 2:
            self.manabase.append(self.hand.pop(which_card))
        else: 
            pass
    
    def put_on_library(self, which_card):
        self.library.insert(0, self.hand[which_card])
        self.hand.pop(which_card)

    def discard_card(self, which_card):
        self.graveyard.append(self.hand.pop(which_card))

    def exile_card(self, which_card):
        self.exile.append(self.hand.pop(which_card))

    def add_token(self):
        token_name = str(input("Token name and stats (e.g. scion 1/1): "))
        self.battlefield.append(token_name)

    def add_to_hand(self):
        card_name = str(input("Card name to add to hand (from sideboard/learn): "))
        self.hand.append(card_name)

    def library_functions(self):
        what_do = int(input("What would you like to do?\nDraw (1) : Scry (2) : Put Top card at Bottom (3) : Search (4) : Mill (5): Shuffle (6)\n"))
        if what_do == 1:
            self.draw_a_card()
        elif what_do == 2: 
            self.view_cards()
        elif what_do == 3:
            self.put_top_to_bottom()
        elif what_do == 4:
            self.find_card()
        elif what_do == 5:
            self.mill()
        elif what_do == 6:
            self.shuffle_deck()
        else:
            return

    def hand_functions(self):
        i = 1
        for card in self.hand:
            print(str(i) + ": " + str(self.hand[i-1]))
            i += 1
        which_card = int(input("Which card do you select?: ")) - 1
        what_do = int(input("What would you like to do?\nPlay (1) : Discard (2) : Put on top of Library (3) : Exile (4) : Add Card from Outside (5)\n"))
        if what_do == 1:
            self.play_card(which_card)
        elif what_do == 2: 
            self.discard_card(which_card)
        elif what_do == 3:
            self.put_on_library(which_card)
        elif what_do == 4:
            self.exile_card(which_card)
        elif what_do == 5:
            self.add_to_hand()
        else:
            return

    def battlefield_functions(self):
        i = 1
        for card in self.battlefield:
            print(str(i) + ": " + str(self.battlefield[i-1]))
            i += 1
        which_card = int(input("Which card do you select?: ")) - 1
        what_do = int(input("Where does this card go?\nGraveyard (1) : Hand (2) : Exile (3) : Add Token (4)\n"))
        if what_do == 1:
            self.battlefield_to_graveyard(which_card)
        elif what_do == 2: 
            self.battlefield_to_hand(which_card)
        elif what_do == 3:
            self.battlefield_to_exile(which_card)
        elif what_do == 4:
            self.add_token()
        else:
            return

    def graveyard_functions(self):
        i = 1
        for card in self.graveyard:
            print(str(i) + ": " + str(self.graveyard[i-1]))
        which_card = int(input("Which card do you select?: ")) - 1
        what_do = int(input("Where does this card go?\nBattlefield (1) : Hand (2) : Manabase (3) : Exile (4)\n"))
        if what_do == 1:
            self.graveyard_to_battlefield(which_card)
        elif what_do == 2: 
            self.graveyard_to_hand(which_card)
        elif what_do == 3:
            self.graveyard_to_manabase(which_card)
        elif what_do == 4:
            self.graveyard_to_exile(which_card)
        else:
            return

    def exile_functions(self):
        i = 1
        for card in self.exile:
            print(str(i) + ": " + str(self.exile[i-1]))
        which_card = int(input("Which card do you select?: ")) - 1
        what_do = int(input("Where does this card go?\nBattlefield (1) : Hand (2)\n"))
        if what_do == 1:
            self.exile_to_battlefield(which_card)
        elif what_do == 2: 
            self.exile_to_hand(which_card)
        else:
            return

    def manabase_functions(self): 
        i = 1
        for card in self.manabase:
            print(str(i) + ": " + str(self.manabase[i-1]))
        which_card = int(input("Which card do you select?: ")) - 1
        what_do = int(input("Where does this card go?\nHand (1) : Graveyard (2)\n"))
        if what_do == 1:
            self.mana_to_hand(which_card)
        elif what_do == 2: 
            self.mana_to_graveyard(which_card)
        else:
            return


game_deck = Deck()
game_deck.populate_deck()
game_deck.shuffle_deck()

while True:
    print("\nBattlefield: " + str(game_deck.battlefield))
    print("Manabase: " + str(game_deck.manabase))
    print("Hand: " + str(game_deck.hand))
    print("Library size: " + str(len(game_deck.library)) + "\n")

    pc.copy("\nBattlefield: " + str(game_deck.battlefield) + 
            "\nManabase: " + str(game_deck.manabase) + 
            "\nHand Size: " + str(len(game_deck.hand)) + 
            ", Library Size: " + str(len(game_deck.library)))

    action = int(input("Library (1) : Hand (2) : Battlefield (3) : Graveyard (4) : Exile (5) : Manabase (6) : Quit (7)\n"))
    if action == 1:
        game_deck.library_functions()
    elif action == 2:
        game_deck.hand_functions()
    elif action == 3:
        game_deck.battlefield_functions()
    elif action == 4:
        game_deck.graveyard_functions()
    elif action == 5:
        game_deck.exile_functions()
    elif action == 6:
        game_deck.manabase_functions()
    else:
        exit()
