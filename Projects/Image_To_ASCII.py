from os import _exit
from sys import exit
from PIL import Image

# External package : via
# python3 -m pip install --upgrade pip
# python3 -m pip install --upgrade Pillow
# Source : https://pillow.readthedocs.io/en/stable/installation.html

def main():
    class Thing():
        def __init__(self):
            self.ini()

        def ini(self):
            x = input("Input file location...\n")
            im = Image.open(f"{x}", "r")
            width = im.size[0]

            t = list(im.getdata())
            grayscale = []
            for e in t:
                y = []
                d = 0
                for i, m in enumerate(e):
                    if i != 3:
                        y.append([0.2126, 0.7152, 0.0722][i] * (m/255))

                for e in y:
                    d += int((e * 255) // 1)
                grayscale.append(d // 4)

            sym = """\u25fc$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`' """
            syml = []
            for e in sym:
                syml.append(e)

            final = ""

            for i, e in enumerate(grayscale):
                if i % width == 0:
                    final += "\n"
                final += f"{syml[int(e)]} "

            Target = open(f"{x}_ASCII.txt", "w", encoding="utf-8")
            Target.write(final)

    Thing()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Ended...")
        try:
            exit()
        except SystemExit:
            _exit(0)
