# You can play flougame https://gameforge.com/en-US/littlegames/flou/

from tkinter import *
from itertools import permutations


def play_flou(game_map):
    map = game_map.split("\n")
    all_moves = set()
    x_limit = len(map)
    y_limit = len(map[0])
    all_elements = set()
    direction = {1: "Right", 2:"Down", 3: "Left", 4: "Up"}
    initial_moves = set()
    class Flou:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.answer = ""
            self.moves = set()
            self.save_x = x
            self.save_y = y

        def _down(self):
            x = self.x
            check = len(self.moves)
            while True:
                x += 1
                if 0 <= x < x_limit and map[x][self.y] == "." and not (x, self.y) in all_moves:
                    self.moves.add((x, self.y))
                    all_moves.add((x, self.y))
                else:break
            self.x = x - 1
            if check == len(self.moves): return False
            else:
                return True

        def _right(self):
            check = len(self.moves)
            y = self.y
            while True:
                y += 1
                if 0 <= y < y_limit and map[self.x][y] == "." and not (self.x, y) in all_moves:
                    self.moves.add((self.x, y))
                    all_moves.add((self.x, y))
                else:
                    break
            self.y = y - 1
            if check == len(self.moves):
                return False
            else:
                return True

        def _up(self):
            check = len(self.moves)
            x = self.x
            while True:
                x = x - 1
                if 0 <= x < x_limit and map[x][self.y] == "." and not (x, self.y) in all_moves:
                    self.moves.add((x, self.y))
                    all_moves.add((x, self.y))
                else:
                    break
            self.x = x + 1
            if check == len(self.moves):
                return False
            else:
                return True

        def _left(self):
            y = self.y
            check = len(self.moves)

            while True:
                y += -1
                if 0 <= y < y_limit and map[self.x][y] == "." and (self.x,y) not in all_moves:
                    self.moves.add((self.x, y))
                    all_moves.add((self.x, y))
                else:
                    break
            self.y = y + 1
            if check == len(self.moves):
                return False
            else:
                return True

        def _do(self, current):
            if current == 1:
                return self._right()
            if current == 2:
                return self._down()
            if current ==3:
                return self._left()
            if current == 4:
                return self._up()

        def make_move(self, current):
            total = 0
            checker = current
            while True:
                result = self._do(current)
                total += 1
                current += 1
                if current == 5:current = 1
                if not result:break
            dir = direction[checker]
            self.answer = [dir, self.save_x, self.save_y]
            if total == 0:return False
            else:return True

    for row,part in enumerate(map):
        for column, i in enumerate(part):
            if i == "B":
                all_elements.add(Flou(row,column))
                all_moves.add((row, column))

    def back_before(element):
        nonlocal all_moves
        element.answer = ""
        all_moves = all_moves - element.moves
        element.x = element.save_x
        element.y = element.save_y
        element.moves = set()




    def do(current):
        if current == limit_of_elements:
            if len(all_moves) == x_limit * y_limit:
                for x in data:
                    if x.moves:continue
                    else:return False
                return True
            else:return False
        element = data[current]
        for x,dir in enumerate(["Right", "Down", "Left", "Up"], start=1):
            element.make_move(x)
            result = do(current + 1)
            if result:return True
            back_before(element)



    limit_of_elements = len(all_elements)
    for perm in permutations(all_elements):
        data = list(perm)
        result = do(0)
        if result:
            return [(element.answer[1], element.answer[2], element.answer[0]) for element in data]


data = []
root = Tk()
root.geometry("900x900+500+200")

row_num = int(input("Row number: "))
column_num = int(input("Column number: "))
ust_frame = Frame()
ust_frame.pack(pady=10)
alt_frae = Frame()
alt_frae.pack()

def do():
    pass


class MyButtons:
    data = []
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.button = Button(ust_frame, height=2, width=2, command=self.change)
        self.button.grid(row=row, column=column)
        self.click = False
        MyButtons.data.append(self)

    def change(self):
        self.button.config(highlightbackground="black")
        self.click = True


for row in range(row_num):
    for column in range(column_num):
        MyButtons(row, column)

def fnish():
    data = [["." for k in range(column_num)] for y in range(row_num)]
    for x in MyButtons.data:
        row = x.row
        column = x.column
        if x.click:
            data[row][column] = "B"
    move = []
    for x in data:
        y = ""
        for a in x:
            y += a
        move.append(y)
    res = "\n".join(move)
    print(res)
    print(play_flou(res))

start_button = Button(alt_frae,text="Start", font=("Helvetica", 30, "bold"), bg="red", command=fnish)
start_button.grid(row=0, column=0, pady=10)

root.mainloop()