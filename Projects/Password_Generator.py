from os import _exit, system, name
from sys import exit
from random import randint


def main():
    class Generator():
        def __init__(self):
            self.ini()

        def ini(self):
            self.clear()
            print("Password generator")

            while 1:
                x = input("Enter the length of the password\n")
                try:
                    x = int(x)
                    if x > 2 ** 8:
                        print("Length of the password too great")
                except ValueError:
                    continue

                f = ""
                for _ in range(x):
                    f += chr(randint(32, 100))
                print(f)

        def clear(self):
            system("cls" if name == "nt" else "clear")

    Generator()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("[App closed...]")
        try:
            exit(0)
        except SystemExit:
            _exit()
