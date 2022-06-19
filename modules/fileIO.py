# Python ファイルを読み込み
def read_file(filename: str):
    with open(filename, "r") as f:
        return f.read()


# PyFuck ファイルを書き込み
def write_file(filename: str, fuck: str):
    with open(filename, "w") as f:
        f.write(fuck)