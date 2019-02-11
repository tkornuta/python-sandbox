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

class Board(object):
    def __init__(self, height, width, num_mines):
        # Copy variables.
        self.height = height
        self.width = width
        self.num_mines = num_mines
        # Current position.
        self.cur_x = 0
        self.cur_y = 0
        # Check settings.
        assert (num_mines < width*height), "Number of mines must be smaller than the board size!"
        # Generate board.
        self.generate_board()


    def generate_board(self):
        # Board with mines.
        self.board_mines = []
        for _ in range(self.height):
            self.board_mines.append( [False] * self.width)
        curr_mines = 0
        while curr_mines < self.num_mines:
            # Random x and y position.
            x = random.randint(0,self.width-1)
            y = random.randint(0,self.height-1)
            if (not self.board_mines[y][x]):
                self.board_mines[y][x] = True
                curr_mines += 1

        # Board with "user" mines.
        self.board_user_mines = []
        for _ in range(self.height):
            self.board_user_mines.append( [False] * self.width)

        # Board with numbers.
        self.board_numbers = []
        # Empty board (with zeros).
        for _ in range(self.height):
            self.board_numbers.append( [0] * self.width)
        # Increment numbers around bombs.
        for y in range(self.height):
            for x in range(self.width):
                if self.board_mines[y][x]:
                    # Place bombs around.
                    for y_p in range(y-1,y+2):
                        for x_p in range(x-1,x+2):
                            # "Truncate"
                            if (x_p) not in range(self.width):
                                continue
                            if (y_p) not in range(self.height):
                                continue
                            self.board_numbers[y_p][x_p] += 1 

        # "Discovered" board.
        self.board_discovered = []
        for _ in range(self.height):
            self.board_discovered.append( [False] * self.width)


    def print_board_mines(self):
        for y in range(self.height):
            line = ""
            for x in range(self.width):
                val = "*" if self.board_mines[y][x] else " "
                line += val
            print (line)

    def print_board_numbers(self):
        for y in range(self.height):
            line = ""
            for x in range(self.width):
                val = str(self.board_numbers[y][x]) if self.board_numbers[y][x]>0 else " "
                val = "*" if self.board_mines[y][x] else val
                line += val
            print (line)

    def print_board_discovered(self):
        print("+" + " - "*self.width + "+")
        for y in range(self.height):
            line = "|"
            for x in range(self.width):
                # Get "discovered value".
                if self.board_discovered[y][x]:
                    val = str(self.board_numbers[y][x]) if self.board_numbers[y][x]>0 else " "
                    val = "*" if self.board_mines[y][x] else val
                else:
                    val = "x"
                # Eventually overwrite it with user bomb.
                if self.board_user_mines[y][x]:
                    val = "f"
                # Add "user position".  
                if (x == self.cur_x and y == self.cur_y):
                    val = "<" + val + ">"
                else:
                    val = " " + val + " "

                line += val
            print (line + "|")
        print("+" + " - "*self.width + "+")


    def print_board_final(self):
        # Counters:
        good_flags = 0
        bad_flags = 0
        print("+" + " - "*self.width + "+")
        for y in range(self.height):
            line = "|"
            for x in range(self.width):
                # Get "discovered value".
                val = str(self.board_numbers[y][x]) if self.board_numbers[y][x]>0 else " "

                if self.board_mines[y][x] and self.board_user_mines[y][x]:
                    val = "F" # Good hypothesis (bomb)
                    good_flags += 1
                elif not self.board_mines[y][x] and self.board_user_mines[y][x]:
                    val = "X" # Bad hypothesis (no bomb)
                    bad_flags +=1
                elif self.board_mines[y][x] and not self.board_user_mines[y][x]:
                    val = "*" # Undiscovered bomb.
                val = " " + val + " "
                # Add to line.
                line += val
            print (line + "|")
        print("+" + " - "*self.width + "+")
        # Print statistics.
        print("Good mine flags (F): {}/{}".format(good_flags, self.num_mines))
        print("Bad mine flags (X): {}".format(bad_flags))

    def user_action(self):
        allowed_keys = ['UP, DOWN, LEFT, RIGH, SPACE, f(add/remove mine flag), q(quit), ESC']
        print("Press a key ({}): ".format(allowed_keys))
        # Read key.
        key = getkey()
        # Move keys.
        if key == keys.UP:
            self.cur_y = self.cur_y-1 if self.cur_y > 0 else self.cur_y
        elif key == keys.DOWN:
            self.cur_y = self.cur_y+1 if self.cur_y < self.height-1 else self.cur_y
        elif key == keys.LEFT:
            self.cur_x = self.cur_x-1 if self.cur_x > 0 else self.cur_x
        elif key == keys.RIGHT:
            self.cur_x = self.cur_x+1 if self.cur_x < self.width-1 else self.cur_x
        # Bomb keys.
        elif key in ['f', 'F']:
            self.board_user_mines[self.cur_y][self.cur_x] = (not self.board_user_mines[self.cur_y][self.cur_x])
        # Exit keys
        elif key in ['q','Q', keys.ESCAPE]:
            return False
        elif key == " ":
            return self.action_unreveil()
        else:
            # Handle other text characters
            print("<bad key pressed>")

        return True

    def discovered_all(self):
        num_flags = 0
        for y in range(self.height):
            for x in range(self.width):
                if not self.board_user_mines[y][x] and not self.board_discovered[y][x]:
                    return False
                if self.board_user_mines[y][x]:
                    num_flags +=1
        if num_flags > self.num_mines:
            # User marked to many mines. Still not good.
            return False
        # Seems that user marked all of them.
        return True

    def unreveil_recursive(self, y, x):
            # Check boarders.
            if (x <0) or (x > self.width-1) or (y <0) or (y > self.height-1):
                return
            # If already discovered.
            if self.board_discovered[y][x]:
                return
            # Otherwise.
            self.board_discovered[y][x] = True
            # If it is zero - unreveil neigbours.
            if self.board_numbers[y][x] == 0:
                self.unreveil_recursive(y-1, x)
                self.unreveil_recursive(y+1, x)
                self.unreveil_recursive(y, x-1)
                self.unreveil_recursive(y, x+1)

    def action_unreveil(self):
        """ Function unreveils given element of board.
        If it was 0, it unreveils the whole piece of board containing zero up to borders"


        :return: True if it was not a bomb, False if it was a bomb.
        """
        # If hit a bomb - finish!
        if self.board_mines[self.cur_y][self.cur_x]:
            # Unreveil all.
            self.print_board_final()
            print("KABOOM! (you loose)")
            return False
        # Unreveil all possible positions staring from current.
        self.unreveil_recursive(self.cur_y, self.cur_x)
        # Check terminal condition.
        if self.discovered_all():
            # Unreveil all.
            self.print_board_final()
            print("CONGRATULATIONS! (you win)")
            return False
        # Continue.
        return True

if __name__ == "__main__":
    difficulty = ""
    while difficulty not in ["e","h","m"]:
        print("Set difficulty (e[asy], m[edium], h[ard]): ")
        # Read key.
        difficulty = getkey()

    if difficulty == 'e':
        height = 5
        width = 5
        mines = 5   
    elif difficulty == 'm':
        height = 8
        width = 8
        mines = 8    
    else:
        height = 10
        width = 10
        mines = 15   

    # Generate board.
    board = Board(height, width, mines)
    while True:
        board.print_board_discovered()
        if not board.user_action():
            break
