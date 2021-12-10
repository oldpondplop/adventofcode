from dataclasses import dataclass

@dataclass
class Num:
    v: int
    m: bool

def check(b,r,c):
    if sum(x.m for x in r) == 5:
        return True
    elif sum(y[c].m for y in b) == 5:
        return True

def play(b,n):
    for row in b:
        for c,col in enumerate(row):
            if col.v == n: 
                col.m = True
                return check(b,row,c)
def score(b,n):
    return sum(col.v for row in b for col in row if not col.m) * n

with open('inp_d4.txt','r') as file:
    numbers, *raw_boards = file.read().strip().split('\n\n')
    numbers = [int(i) for i in numbers.split(',')]

boards = [[[Num(int(e),False) for e in line.split()] for line in board.split('\n')] for board in raw_boards]

last_board = len(boards)
win_cnt = 0

for number in numbers:
    for i,board in enumerate(boards):
        if board is None:
            continue
        if play(board, number):
            win_cnt+=1
            if win_cnt == 1 or win_cnt == last_board:
                print(score(board,number))
            boards[i] = None