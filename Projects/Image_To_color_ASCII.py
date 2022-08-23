from os import _exit
from sys import exit
from PIL import Image


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

            syml = ['◼', '$', '@', 'B', '%', '8', '&', 'W', 'M', '#', '*', 'o', 'a', 'h', 'k', 'b', 'd', 'p', 'q', 'w', 'm', 'Z', 'O', '0',
                    'Q', 'L', 'C', 'J', 'U', 'Y', 'X', 'z', 'c', 'v', 'u', 'n', 'x', 'r', 'j', 'f', 't', '/', '\\', '|', '(', ')', '1', '{', '}',
                    '[', ']', '?', '-', '_', '+', '~', '&#60;', '	&#62;', 'i', '!', 'l', 'I', ';', ':', ',', '"', '^', '`', "'", ' ']

            final = ""

            colors = []
            for e in t:
                d = []
                for g in e:
                    d.append(hex(g).split("x")[-1])
                colors.append("".join(d))

            for i, e in enumerate(grayscale):
                if i % width == 0:
                    final += "<br>\n"
                final += f'<b style="color:#{colors[i]}">{syml[int(e)]}</b> '

            Target = open("example.html", "w", encoding="utf-8")
            Target.write(
                f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Document</title><style>*{{font-family:consolas}}</style>
                </head><body>{final}</body></html>"""
            )

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
