import random
moves = ['rock', 'paper', 'scissors']


class Player:
    def __init__(self):
        self.my_move = 0
        self.their_move = 0

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            move_human = input("Choose rock, paper or scissors.").lower()
            if move_human in moves:
                return move_human


class ReflectPlayer(Player):
    def __init__(self, opponent):
        super().__init__()
        self.opponent = opponent

    def move(self):
        if self.opponent.my_move == 0:
            return random.choice(moves)
        else:
            return self.opponent.my_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move == 0:
            return random.choice(moves)
        elif self.my_move == "rock":
            return "paper"
        elif self.my_move == "paper":
            return "scissors"
        elif self.my_move == "scissors":
            return "rock"


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
        self.keep_score(move1, move2)
        print(f"player1 score: {self.point_p1} player2 score: {self.point_p2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        number_rounds = int(input("How many rounds would you like to play?"))
        print("Game start!")
        for round in range(number_rounds):
            print(f"Round {round + 1}:")
            self.play_round()
        self.who_won()

    def play_single_game(self):
        print("Game start")
        self.play_round()
        self.who_won()

    def keep_score(self, one, two):
        person_won = beats(one, two)
        if person_won == "p1":
            self.point_p1 += 1
        elif person_won == "p2":
            self.point_p2 += 1

    def who_won(self):
        if self.point_p1 > self.point_p2:
            print("player 1 wins the match")
        elif self.point_p2 > self.point_p1:
            print("player 2 wins the match")
        else:
            print("the match is a tie!! good job both of you!")
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
