from os import _exit, system, name
from random import randint


def main():
    class Game():
        def __init__(self) -> None:
            self.iters = 0
            self.ini()

        def ini(self):
            if self.iters == 0:
                print("Number guessing Game")

            num = randint(0, 100)
            tries = 0

            while 1:
                if tries == 0:
                    print("The number is between 1 and 100")

                x = input("\nEnter your guess...\n")

                if not x.replace(" ", ""):
                    print("Not a valid input")
                    continue
                try:
                    y = int(x)
                except ValueError:
                    continue
                if y == num:
                    z = "no (how)" if tries == 0 else tries
                    t = "tries" if tries != 1 else "try"
                    print(
                        f"You guessed the number {num} right, after {z} {t} !")
                    break

                print("Number is too great" if y > num else "Number is too small")
                tries += 1
            self.ini()
            self.iters += 1

        def clear(self):
            system("cls" if name == "nt" else "clear")

    Game()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("[Game closed...]")
        try:
            exit(0)
        except SystemExit:
            _exit()
