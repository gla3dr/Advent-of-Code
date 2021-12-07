from dataclasses import dataclass
import pprint
import sys


@dataclass
class Val:

    value: int
    marked: bool

    def __repr__(self):
        return f'{"(" if self.marked else ""}{self.value}{")" if self.marked else ""}'


class Board:

    def __init__(self, vals):
        self.__board_rows = [[],[],[],[],[]]
        self.__board_cols = [[],[],[],[],[]]
        self.__board_locs = {}
        for y, row in enumerate(vals.split('\n')):
            for x, col in enumerate(row.split()):
                self.__board_rows[y].append(Val(value=col, marked=False))
                self.__board_cols[x].append(Val(value=col, marked=False))
                self.__board_locs[col] = {'col': x, 'row': y}

    
    def __str__(self):
        return pprint.pformat(self.__board_rows) + '\n\n' + pprint.pformat(self.__board_cols)


    def __mark_num(self, num):
        try:
            loc = self.__board_locs[str(num)]
            self.__board_rows[loc['row']][loc['col']].marked = True
            self.__board_cols[loc['col']][loc['row']].marked = True
        except KeyError as e:
            pass


    def __check(self):
        return (any([all([v.marked for v in row]) for row in self.__board_rows]) or
            any([all([v.marked for v in col]) for col in self.__board_cols]))        


    def mark_and_check(self, num):
        self.__mark_num(num)
        return self.__check()

    def score(self, last):
        return sum([int(v) for v, loc in self.__board_locs.items() if not self.__board_rows[loc['row']][loc['col']].marked]) * int(last)
        

numbers = None
boards = None

with open('2021/Day4/input.txt', 'r') as input:
    sections = input.read().split('\n\n')
    numbers = sections[0].split(',')
    boards = [Board(b) for b in sections[1:]]

for n in numbers:
    for board in boards:
        if board.mark_and_check(n):
            print(board.score(n))
            sys.exit()
