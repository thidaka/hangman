from random import shuffle

class Card:
	suits = ("spades", "hearts", "diamonds", "clubs")
	values = (None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")

	def __init__(self, v, s):
		"""スーツ（マーク）も値も整数値です"""
		self.value = v
		self.suit = s

	def __lt__(self, c2):
		return self.value < c2.value or self.value == c2.value and self.suit < c2.suit
	def __gt__(self, c2):
		return self.value > c2.value or self.value == c2.value and self.suit > c2.suit

	def __repr__(self):
		return self.values[self.value] + " of " + self.suits[self.suit]

class Deck:
	def __init__(self):
		self.cards = []
		for i in range (2, 15):
			for j in range (0, 4):
				self.cards.append(Card(i,j))
				shuffle(self.cards)

	def remove_card(self):
		if len(self.cards) == 0:
			return
		return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.card = None
        self.wins = 0


class Game:

    def __init__(self, name1="", name2=""):
        self.deck = Deck()
        self.player1 = Player(name1) if name1 != "" else Player(input("Player1の名前: "))
        self.player2 = Player(name2) if name2 != "" else Player(input("Player2の名前: "))

    def wins(self, winner):
        print("このラウンドの勝者は {} です".format(winner))

    def draw(self, p1, p1c, p2, p2c):
        print("{} は {} を，{} は {} を引きました".format(p1, p1c, p2, p2c))

    def winner(self, player1, player2):
        print("{} は {} 勝、 {} は {} 勝でした".format(player1.name, player1.wins, player2.name, player2.wins))
        if player1.wins > player2.wins:
            return (player1.name)
        elif player1.wins == player2.wins:
            return("引き分けです")
        else:
            return (player2.name)

    def play_game(self):
        p1 = self.player1.name
        p2 = self.player2.name
        cards = self.deck.cards
        print("Game を開始します")
        while len(cards) > 1:
            response = input("q で終了します。それ以外のキーで play: ")
            if response == "q" or response == "Q":
                break
            p1c = self.deck.remove_card()
            p2c = self.deck.remove_card()
            self.draw(p1, p1c, p2, p2c)
            if p1c > p2c:
                self.player1.wins += 1
                self.wins(p1)
            else:
                self.player2.wins += 1
                self.wins(p2)

        win = self.winner(self.player1, self.player2)
        print("ゲーム終了； 勝者は {} です".format(win))

#deck = Deck()
#for card in deck.cards:
#	print(card)

game = Game()
game.play_game()
