# 4 задание
class Cell:
    def __init__(self, number):
        self.number = number
        self.status = ''

    def cell_status(self, status):
        if self.status == '':
            self.status = status
            return True
        else:
            return False


class Board:
    def __init__(self):
        self.cells = [Cell(i) for i in range(9)]

    def grid(self):
        print('1|2|3')
        print('4|5|6')
        print('7|8|9')

    def new_board(self):
        print(f'{self.cells[0].status}|{self.cells[1].status}|{self.cells[2].status}')
        print(f'{self.cells[3].status}|{self.cells[4].status}|{self.cells[5].status}')
        print(f'{self.cells[6].status}|{self.cells[7].status}|{self.cells[8].status}')


class Player:
    def __init__(self, char, name):
        self.char = char
        self.name = name

    def moving(self, board):
        while True:
            move = input(f'Ход - {self.name}: ')
            if (move in ['1', '2', '3', '4', '5', '6', '7', '8', '9']
                    and board.cells[int(move) - 1].cell_status(self.char)):
                break
            else:
                print('Ошибка знака')


board = Board()
board.grid()
player1 = Player('x', 'первый игрок')
player2 = Player('o', 'второй игрок')
player_s_move = player1
while True:
    player_s_move.moving(board)
    board.new_board()
    if ((board.cells[0].status in ['x'] and board.cells[1].status in ['x'] and board.cells[2].status in ['x']) or
        (board.cells[3].status in ['x'] and board.cells[4].status in ['x'] and board.cells[5].status in ['x']) or
        (board.cells[6].status in ['x'] and board.cells[7].status in ['x'] and board.cells[8].status in ['x']) or
        (board.cells[0].status in ['x'] and board.cells[3].status in ['x'] and board.cells[6].status in ['x']) or
        (board.cells[1].status in ['x'] and board.cells[4].status in ['x'] and board.cells[7].status in ['x']) or
        (board.cells[2].status in ['x'] and board.cells[5].status in ['x'] and board.cells[8].status in ['x']) or
        (board.cells[0].status in ['x'] and board.cells[4].status in ['x'] and board.cells[8].status in ['x']) or
        (board.cells[2].status in ['x'] and board.cells[4].status in ['x'] and board.cells[6].status in ['x']) or
        (board.cells[0].status in ['o'] and board.cells[1].status in ['o'] and board.cells[2].status in ['o']) or
        (board.cells[3].status in ['o'] and board.cells[4].status in ['o'] and board.cells[5].status in ['o']) or
        (board.cells[6].status in ['o'] and board.cells[7].status in ['o'] and board.cells[8].status in ['o']) or
        (board.cells[0].status in ['o'] and board.cells[3].status in ['o'] and board.cells[6].status in ['o']) or
        (board.cells[1].status in ['o'] and board.cells[4].status in ['o'] and board.cells[7].status in ['o']) or
        (board.cells[2].status in ['o'] and board.cells[5].status in ['o'] and board.cells[8].status in ['o']) or
        (board.cells[0].status in ['o'] and board.cells[4].status in ['o'] and board.cells[8].status in ['o']) or
        (board.cells[2].status in ['o'] and board.cells[4].status in ['o'] and board.cells[6].status in ['o'])):
        print(f'Победа - {player_s_move.name}')
        break
    elif all(i.status != '' for i in board.cells):
        print('Ничья')
        break
    if player_s_move == player2:
        player_s_move = player1
    else:
        player_s_move = player2
