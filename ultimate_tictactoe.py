import os

class Game:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        self.board = [['-', '-', '-'],
                      ['-', '-', '-'],
                      ['-', '-', '-']]
        self.gameOver = False
        self.count = 0

    def emptyCheck(self, x, y):
        if self.board[x][y] == '-':
            return True
        else:
            return False
            
    def boardWrite(self, x, y, OTurn):
        if OTurn == True and self.emptyCheck(x, y):
            self.board[x][y] = 'O'
        elif OTurn == False and self.emptyCheck(x, y):
            self.board[x][y] = 'X'
        self.count += 1
        return 0

    def winCheck(self):
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '-':
            return self.board[0][0]
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] != '-':
            return self.board[0][2]
        elif self.board[0][0] == self.board[0][1] == self.board[0][2] != '-':
            return self.board[0][0]
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] != '-':
            return self.board[1][0]
        elif self.board[2][0] == self.board[2][1] == self.board[2][2] != '-':
            return self.board[2][0]
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] != '-':
            return self.board[0][0]
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] != '-':
            return self.board[0][1]
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] != '-':
            return self.board[0][2]
        else:
            return False

class UltimateGame:
    def __init__(self):
        self.games = [[Game(0,0), Game(0,1),Game(0,2)],
                      [Game(1,0), Game(1,1), Game(1,2)],
                      [Game(2,0), Game(2,2), Game(2,3)]]
        self.lastAnswer
        self.Answer
        self.gameOver = False

    def test(self):
        self.games[0][0].board[1][1] = '1'
        self.games[0][1].board[1][1] = '2'
        self.games[0][2].board[1][1] = '3'
        self.games[1][0].board[1][1] = '4'
        self.games[1][1].board[1][1] = '5'
        self.games[1][2].board[1][1] = '6'
        self.games[2][0].board[1][1] = '7'
        self.games[2][1].board[1][1] = '8'
        self.games[2][2].board[1][1] = '9'

    def update(self, X, Y, x, y, OTurn):
        self.games[X][Y].boardWrite(x, y, OTurn)

    def render(self):
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        print(self.games[i][k].board[j][l], end=' ')
                    print(' ', end='')
                print()
            print()

    def GameLoop(self):
        while self.gameOver == False:
            
    
game = UltimateGame()
game.test()
game.render()