print(
    """ ____        _____           _
|  _ \ _   _|  ___|   _  ___| | __
| |_) | | | | |_ | | | |/ __| |/ /
|  __/| |_| |  _|| |_| | (__|   <
|_|    \__, |_|   \__,_|\___|_|\_\\
       |___/
                                    by satoki, xryuseix
"""
)

# Python ファイルを読み込み
def read_file(filename: str):
    with open(filename, "r") as f:
        return f.read()


# PyFuck ファイルを書き込み
def write_file(filename: str, fuck: str):
    with open(filename, "w") as f:
        f.write(fuck)


# 数値を PyFuck に変換
def num_to_fuck(num: str):
    digit: int = len(num)  # num の文字数
    num = int(num)
    ones: int = int("1" * digit)  # 11111....111 の数値
    fucks = []  # [1111, 111, 11, 1]
    while num > 0 and ones > 0:
        while num > 0 and ones > 0 and num >= ones:
            num -= ones
            fucks.append(ones)
        ones = ones // 10
    return "+".join(map(str, fucks))


# PyFuck コードを生成
def make_pyfuck(python_code: str):
    pyfuck = ""
    for c in python_code:
        pyfuck += "chr("
        pyfuck += num_to_fuck(str(ord(c)))
        pyfuck += ")+"
    return pyfuck[:-1]


if __name__ == "__main__":
    python_code = read_file(input("FileName: "))
    pyfuck = make_pyfuck(python_code)
    write_file("output.py", f"exec({pyfuck})")
    print("-> output.py")
