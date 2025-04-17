import random
# Card class to define a card with value and suit
class Card:
    def __init__(self, value, suit):#Card class ka constructor
        self.value = value  # Number of the card (1-13) e.g  "10 of Spades"
        self.suit = suit    # Suit: Spades, Hearts, Diamonds, Clubs
    def __str__(self):#Yeh ek special Python function hai jo object ko string mein convert karta hai.
        return f"{self.value} of {self.suit}"#Jab print(card) likhte ho, toh yahi function call hota hai. or 7 of hearts print kryga
# Player class to store player information and their assigned card
class Player:
    def __init__(self, player_id):#(jaise Player 1, Player 2)
        self.id = player_id  # Player's ID (1, 2, 3,...)
        self.card = None     # Initially no card assigned
# Reflex Agent class to perform all tasks
class CasinoAgent:
    def __init__(self):
        self.players = []  # List to hold player objects
        self.cards = []    # List to hold card objects
        self.suits_order = {"Spades": 4, "Hearts": 3, "Diamonds": 2, "Clubs": 1} #Yeh dictionary hai jo suits ki priority batata hai.
    # Step 1: Identify number of players
    def get_players(self):
        n = int(input("Enter number of players: "))
        #i har player ka ID
        for i in range(1, n + 1):#Yeh loop 1 se n tak chalega.second argument exclusive hota hai,
            self.players.append(Player(i))#har iteration mai aik new player add hota ha player class k object m
        print(f"{n} players added.\n")#Finally, kitne players add hue yeh print hota hai.
    # Step 2: Add same number of unique cards
    def generate_cards(self):#Yeh function cards generate karta hai:
        possible_suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        possible_values = list(range(1, 14))  # Values 1 to 13
        # Create a full deck first.yeh nested loops ki tarah kaam karte hain.Pehle suit ko iterate karta hai (Spades, Hearts, Diamonds, Clubs).
        # Har suit ke liye, value (1 se 13 tak) ko iterate karta hai.Har combination ke liye ek Card(value, suit) object create hoga.
        full_deck = [Card(value, suit) for suit in possible_suits for value in possible_values]#Yeh ek full deck banata hai, jisme har suit ke har value ka card hota hai.
        # Randomly pick cards equal to number of players.Yeh function full_deck se randomly jitni players hain, utne cards pick karta hai.
        self.cards = random.sample(full_deck, len(self.players))#Yeh function list se duplicate-free random selections karta hai.
        print(f"{len(self.cards)} cards generated.\n")
    # Step 3-5: Roll dice, assign cards, and avoid duplicates
    def assign_cards(self):
        assigned_players = set()#yeh set un players ko store karega jinhon ne card receive kiya hai.
        assigned_cards = set()
        while len(assigned_players) < len(self.players):#Jab assigned_players ka size, total players ke barabar ho jayega, tab loop ruk jayega.
            # Roll dice to pick random player and card index
            player_index = random.randint(0, len(self.players) - 1)#Yeh randomly ek player ka index select karta hai (0 se le kar len(self.players) - 1 tak).
            card_index = random.randint(0, len(self.cards) - 1)#........Isse randomly player aur card select hote hain har iteration mein.
            # Check if player or card is already assigned
            if player_index in assigned_players or card_index in assigned_cards:
                continue  # Skip and roll again
            # Assign the card to the player.randomly selected player ko card assign karne ka kaam karti hain:
            #Yeh player ka card hai, jo initially None tha (jab player object banaya gaya tha), lekin ab yeh card assign ho raha hai.
            #Yeh players list mein se specific player ko access karta hai (using player_index).
            self.players[player_index].card = self.cards[card_index]
            #Yeh line player_index ko assigned_players set mein add kar deti hai, jisse yeh track hota hai ke yeh player already card receive kar chuka hai.
            assigned_players.add(player_index)
            assigned_cards.add(card_index)
            print(f"Player {self.players[player_index].id} gets card: {self.cards[card_index]}")#Yeh line assigned card  jis player ko mila ha vo donu ko print kar deti hai,

    # Step 6: Announce winner based on highest card
    def announce_winner(self):
        def card_priority(card):
            # Higher value is better, suit priority used as tiebreaker
            #ek tuple return kar rahi hai, jismein do values hain:
            return (card.value, self.suits_order[card.suit])#Yeh nested function hai jo card ki value aur suit ki priority return karta hai as a tuple.
        # Use max() to get player with highest priority card
        #Yeh list hai sab players ki, max() function ko yeh batata hai ke kis basis par max dhoondhna hai. Hum card ki strength ke basis par winner dhoondhna chahte hain.
        #Yeh short anonymous function hai jo har player p ke liye kaam karega.#p.card → current player ka card
        #card_priority() → us card ka (value, suit) tuple banata hai
        winner = max(self.players, key=lambda p: card_priority(p.card))
        print(f"\n Winner is Player {winner.id} with card: {winner.card}")#Winner player ka ID aur card print karega.
    # Function to run the full game
    def play_game(self):
        self.get_players()
        self.generate_cards()
        self.assign_cards()
        self.announce_winner()
# Run the game
agent = CasinoAgent()
agent.play_game()
