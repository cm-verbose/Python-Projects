from os import _exit, system, name
from sys import exit
from random import randint
from time import sleep


def main():
    class Game():
        def __init__(self):
            self.ini()

        def ini(self):
            print("Rock paper scissors")
            while 1:
                x = input("Choose your tool (rock, paper, scissors)\n")
                if x.replace(" ", "").lower() not in ["rock", "paper", "scissors"]:
                    continue
                t = ["rock", "paper", "scissors"][randint(0, 2)]

                for i in range(3):
                    print(f"{3 - i}...")
                    sleep(0.25)

                if t == x:
                    print(f"{x} beats {x}")
                    continue

                if x == "rock":
                    if t == "paper":
                        print(f"you lost, {t} covers {x}")
                    elif t == "scissors":
                        print(f"you win, {x} breaks {t}")
                if x == "paper":
                    if t == "rock":
                        print(f"you win, {x} covers {t}")
                    elif t == "scissors":
                        print(f"you lost, {x} gets cut by {t}")
                if x == "scissors":
                    if t == "rock":
                        print(f"you lost, {t} breaks {x}")
                    elif t == "paper":
                        print(f"you win, {x} cuts {t}")

        def clear(self):
            system("cls" if name == "nt" else "clear")

    Game()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("[Game ended...]")
        try:
            exit()
        except SystemExit:
            _exit(0)
