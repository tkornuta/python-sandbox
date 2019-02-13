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

class TicTacToe(object):

    def __init__(self):
        self.board_state = []
        # Initialize the board.
        for _ in range(3):
            self.board_state.append(["-"] * 3)
        #print(self.board_state)

    def print(self):
        for y in range(3):
            row = ""
            for x in range(3):
                row +=  self.board_state[y][x] + "|"   
            row = row[:-1]
            print(row)

    def add_token(self, y, x, token):
        self.board_state[y][x] = token

    def check_if_board_full(self):
        for y in range(3):
            for x in range(3):
                if (self.board_state[y][x] == "-"):
                    return False
        return True

    def add_next_token(self):
        token = "O"
        if self.check_if_board_full():
            raise Exception("Board is full")

        for y in range(3):
            for x in range(3):
                if (self.board_state[y][x] == "-"):
                    self.add_token(y, x, token)
                    return

    def add_user_token(self):
        x = -1
        y = -1
        while x > 2 or x < 0 or y > 2 or y < 0 :
            try:
                y = int(input("Row?"))
                x = int(input("Column?"))
                if self.board_state[y][x] != "-":
                    print("Move not legal")
                    x = -1
                    y = -1
            except:
                print("Both coordinates must be integers between 0 and 2")
                x = -1
                y = -1
        # Coordinates are ok.
        self.add_token(y, x, "X")

if __name__ == "__main__":
    b = TicTacToe()
    b.print()
    # Add x to top row middle column.
    # b.add_token(0,1,"X")
    b.print()
    while True:
        b.add_user_token()
        b.add_next_token()
        b.print()

    #while True:
    #    b.add_next_token()
    #    b.print()

    #while not b.check_if_board_full():
