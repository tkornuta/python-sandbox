# Copyright (C) tkornuta, 2019
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import random
from getkey import getkey, keys

class TicTacToe(object):

    def __init__(self, size=3, line=3):
        self.board_state = []
        self.size = size
        self.line = line
        assert self.size > 1, "Board size must be greater than 1"
        # Initialize the board.
        for _ in range(self.size):
            self.board_state.append(["-"] * self.size)
        #print(self.board_state)
        self.ux = 0
        self.uy = 0

    def print(self):
        for y in range(self.size):
            row = ""
            for x in range(self.size):
                if self.ux == x and self.uy == y:
                    row += "<" + self.board_state[y][x] + ">|"   
                else:
                    row +=  " " + self.board_state[y][x] + " |"   
            row = row[:-1]
            print(row)

    def add_token(self, y, x, token):
        self.board_state[y][x] = token

    def check_if_board_full(self):
        for y in range(self.size):
            for x in range(self.size):
                if (self.board_state[y][x] == "-"):
                    return False
        return True
    
    def check_if_line(self):
        for y in range(self.size):
            for x in range(self.size):
                token = self.board_state[y][x]
                # Skip
                if token == "-":
                    continue
                # Check to left.
                line = True
                for l in range(1,self.line):
                    if x+l >= self.size:
                        line = False
                        break
                    if self.board_state[y][x+l] != token:
                        line = False
                        break
                if line:
                    print("{} won!".format(token))
                    return True
                # Check to down-left.
                line = True
                for dl in range(1,self.line):
                    if x+dl >= self.size or y+dl >= self.size:
                        line = False
                        break
                    if self.board_state[y+dl][x+dl] != token:
                        line = False
                        break
                if line:
                    print("{} won!".format(token))
                    return True
                # Check to down.
                line = True
                for d in range(1,self.line):
                    if y+d >= self.size:
                        line = False
                        break
                    if self.board_state[y+d][x] != token:
                        line = False
                        break
                if line:
                    print("{} won!".format(token))
                    return True
                # Check to down-right.
                line = True
                for dr in range(1,self.line):
                    if x-dr < 0 or y+dr >= self.size:
                        line = False
                        break
                    if self.board_state[y+dr][x-dr] != token:
                        line = False
                        break
                if line:
                    print("{} won!".format(token))
                    return True

    def add_next_token(self):
        token = "O"
        if self.check_if_board_full():
            raise IndexError("Board is full")

        for y in range(self.size):
            for x in range(self.size):
                if (self.board_state[y][x] == "-"):
                    self.add_token(y, x, token)
                    return

    def add_user_token(self):
        x = -1
        y = -1
        while x >= self.size or x < 0 or y >= self.size or y < 0 :
            try:
                y = int(input("Row?"))
                x = int(input("Column?"))
                if self.board_state[y][x] != "-":
                    print("Move not legal")
                    x = -1
                    y = -1
            except ValueError:
                print("Both coordinates must be integers between 0 and 2")
                x = -1
                y = -1
            except KeyboardInterrupt:
                print("Bye!")
                exit()
        # Coordinates are ok.
        self.add_token(y, x, "X")

    def user_action(self):
        while True:
            allowed_keys = ['UP, DOWN, LEFT, RIGH, SPACE, q(quit), ESC']
            print("Press a key ({}): ".format(allowed_keys))
            # Read key.
            key = getkey()
            # Move keys.
            if key == keys.UP:
                self.uy = self.uy-1 if self.uy > 0 else self.uy
            elif key == keys.DOWN:
                self.uy = self.uy+1 if self.uy < self.size-1 else self.uy
            elif key == keys.LEFT:
                self.ux = self.ux-1 if self.ux > 0 else self.ux
            elif key == keys.RIGHT:
                self.ux = self.ux+1 if self.ux < self.size-1 else self.ux
            # Exit keys
            elif key in ['q','Q', keys.ESCAPE]:
                return False
            elif key == " ":
                # Check if the move is legal.
                if self.board_state[self.uy][self.ux] != "-":
                    print("Move not legal")
                else:
                    self.add_token(self.uy, self.ux, "X")
                    return True
            else:
                # Handle other text characters
                print("<bad key pressed>")
            self.print()
        return True


if __name__ == "__main__":
    while True:
        difficulty = ""
        while difficulty not in ["e","m","h", "q","Q", keys.ESCAPE]:
            print("Set difficulty (e[asy], m[edium], h[ard]) (ESC or q to quit): ")
            # Read key.
            difficulty = getkey()

        # Exit keys
        if difficulty in ['q','Q', keys.ESCAPE]:
            print("Bye!")
            exit()
        elif difficulty == 'e':
            size = 3
            line = 3
        elif difficulty == 'm':
            size = 5
            line = 3
        else:
            size = 7
            line = 4
        
        # Generate board.
        print("Generating board {}x{}, line length {}...".format(size, size, line))
        b = TicTacToe(size, line)
        b.print()
        while True:
            # User move.
            if not b.user_action():
                break
            b.print()
            # Check conditions.
            if b.check_if_line():
                break               
            if b.check_if_board_full():
                print("Board full: tie!")
                break
            # "AI" move.
            b.add_next_token()
            b.print()
            # Check conditions.
            if b.check_if_line():
                break               
            if b.check_if_board_full():
                print("Board full: tie!")
                break

