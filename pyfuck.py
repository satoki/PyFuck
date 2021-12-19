print(
    """ ____        _____           _
|  _ \ _   _|  ___|   _  ___| | __
| |_) | | | | |_ | | | |/ __| |/ /
|  __/| |_| |  _|| |_| | (__|   <
|_|    \__, |_|   \__,_|\___|_|\_\\
       |___/
                                    by Satoki
"""
)

# Pythonファイルを読み込み
def read_file(filename: str):
    with open(filename, "r") as f:
        return f.read()


# PyFuckファイルを書き込み
def write_file(filename: str, fuck: str):
    with open(filename, "w") as f:
        return f.write(fuck)


if __name__ == "__main__":
    python_code = read_file(input("FileName: "))

    pyfuck = ""
    for c in python_code:
        pyfuck += "chr("
        ord_c = ord(c)
        fuck = int("1" * len(str(ord_c)))
        while ord_c != 0:
            for i in range(int(ord_c / fuck)):
                if pyfuck[-1] != "(":
                    pyfuck += "+"
                pyfuck += f"{str(fuck)}"
            ord_c = int(ord_c % fuck)
            fuck = int(fuck / 10)
        pyfuck += ")+"

    write_file("output.py", f"exec({pyfuck[:-1]})")
    print("-> output.py")
