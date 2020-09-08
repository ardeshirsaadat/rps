import random
moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        move_human = input("Rock, paper or scissors?")
        return move_human




def beats(one, two):
    if ((one == 'rock' and two == 'scissors') or
        (one == 'scissors' and two == 'paper') or
        (one == 'paper' and two == 'rock')):
        print("player 1 wins")
        return "p1"
    elif ((one == 'rock' and two == 'paper') or
         (one == 'scissors' and two == 'rock') or
         (one == 'paper' and two == 'scissors')):
         print("player1 loses")
         return "p2"   
    else:
        print("its a tie")


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.point_p1 = 0
        self.point_p2 = 0

        
    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        # beats(move1, move2)
        self.keep_score(move1, move2)
        print(f"player1 score: {self.point_p1} player2 score: {self.point_p2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")
    

    def keep_score(self, one, two):
        person_won = beats(one, two)
        if person_won == "p1":
            self.point_p1 +=1
        elif person_won == "p2":
            self.point_p2 +=1  


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
