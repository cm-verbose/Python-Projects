from sys import exit
from os import _exit, system, name


def main():
    class Calculator():
        def __init__(self):
            self.ini()

        def clear(self):
            system("cls" if name == "nt" else "clear")

        def ini(self):
            print("\nCalculator terminal app")
            while 1:
                exp = input("\nEnter an expression...\n")
                if not exp:
                    print("[No expression found]\n")
                    continue
                if self.calc(exp) != None:
                    print(self.calc(exp))
                else:
                    continue

        def calc(self, exp):
            try:
                exp = exp.replace("^", "**")
                f = ""
                for k, v in enumerate(str(eval(exp))[::-1]):
                    if k % 3 == 0:
                        f += " "
                    f += v
                return f[::-1]
            except Exception:
                print("Hmm... something went wrong\n")
                return
    Calculator()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("[Calculator closed...]")
        try:
            exit(0)
        except SystemExit:
            _exit(0)
