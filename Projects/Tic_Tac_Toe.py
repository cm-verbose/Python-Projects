from os import _exit, system, name
from sys import exit
from random import randint
from time import sleep


def main():
    class Game():
        def __init__(self):
            self.grid = []
            self.Pl = ""
            self.Bt = ""
            self.play_count = 0
            self.ini()

        def ini(self):
            self.clear()
            if self.play_count == 0:
                print("Tic Tac Toe")
            while 1:
                # Determine Xs, Os and the starting player
                x = input("Choose your Xs or your Os\n")

                if x.replace(" ", "").lower() != "x" and x.replace(" ", "").lower() != "o":
                    x = ["x", "o"][randint(0, 1)]
                    print(f"Generated random character : {x.upper()}")
                    sleep(1)

                self.Pl, self.Bt = "X" if x.lower() == "x" else "O", "O" if x.lower() == "x" else "X"

                # Starting player
                st = ["pl", "bt"][randint(0, 1)]
                pl = "you" if st == "pl" else "the bot"
                self.generate_grid()
                self.clear()

                print(f"The starting player is {pl}\n\n")
                sleep(1)
                self.draw_grid()
                while 1:
                    if st == "pl":
                        inp = input("\nEnter the position : (x, y)\n")
                        inp = inp.split(",")
                        m = None
                        try:
                            # (inp[0] and inp[0]) <= 2
                            inp[0] = (-(int(inp[0]) + 1))
                            inp[1] = ((int(inp[1])))
                            m = self.grid[int(inp[0])][int(inp[1])]
                        except ValueError:
                            continue

                        if m == 0 or m == 1:
                            continue

                        self.grid[int(inp[0])][int(inp[1])] = 1

                        if self.grid_verify():
                            print("You win")
                            self.draw_grid()
                            break
                        elif self.grid_verify() == "draw":
                            print("draw")
                            self.draw_grid()
                            break

                        self.clear()
                        self.draw_grid()
                        st = "bt"

                    elif st == "bt":
                        x = randint(0, 2)
                        y = randint(0, 2)
                        m = self.grid[x][y]

                        if m == 0 or m == 1:
                            continue

                        self.grid[x][y] = 0

                        if self.grid_verify() == True:
                            print("You lost")
                            self.draw_grid()
                            break
                        elif self.grid_verify() == "draw":
                            print("draw")
                            self.draw_grid()
                            break

                        self.clear()
                        self.draw_grid()
                        st = "pl"
                while 1:
                    replay = input(
                        "Do you want to play again (yes (y) / no (n))\n")
                    if replay == "yes" or replay == "y":
                        self.grid = []
                        self.Pl = ""
                        self.Bt = ""
                        self.play_count = 1
                        self.ini()
                    elif replay == "no" or replay == "n" or not replay:
                        exit()

        # Clear terminal
        def clear(self):
            system("cls" if name == "nt" else "clear")

        # Generate a 3x3 matrix for the game
        def generate_grid(self):
            for _ in range(3):
                self.grid.append([2, 2, 2])
            return self.grid

        # Draws the grid
        def draw_grid(self):
            sg = ""
            for i, e in enumerate(self.grid):
                sg += (f" {e[0]}  | {e[1]}  | {e[2]} \n")
                if i != 2:
                    sg += ("----|----|----\n")
            # Replaces : 2 = empty space ; 1 = player symbol ; 0 = bot symbol
            sg = sg.replace("2", " ").replace(
                "1", self.Pl).replace("0", self.Bt)
            print(sg)
            return sg

        # See if the player or the bot won
        def grid_verify(self):
            g = self.grid
            z, m, j = [], [], []
            for e in g:
                # Horizontal check
                if e == [1, 1, 1] or e == [0, 0, 0]:
                    return True
                for i in range(len(g)):
                    j.append(e[i])

            for y in range(len(g)):
                p = []
                z.append(g[y][y])
                m.append(g[y][-(y + 1)])

                # Diagonal check
                if (z == [1, 1, 1] or z == [0, 0, 0]) or (m == [1, 1, 1] or m == [0, 0, 0]):
                    return True

                # Vertical check
                for i in range(len(g)):
                    p.append(g[i][y])
                    if p == [1, 1, 1] or p == [0, 0, 0]:
                        return True

            # Draw (special case)
            if 2 not in j:
                return "draw"
    Game()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("[Game ended...]")
        try:
            exit()
        except SystemExit:
            _exit()
