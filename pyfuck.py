print(""" ____        _____           _
|  _ \ _   _|  ___|   _  ___| | __
| |_) | | | | |_ | | | |/ __| |/ /
|  __/| |_| |  _|| |_| | (__|   <
|_|    \__, |_|   \__,_|\___|_|\_\\
       |___/
                                    by Satoki
""")

with open(input("FileName: "), "r") as input_file, \
                    open("output.py", "w") as output_file:
    python_code = input_file.read()
    
    pyfuck = ""
    for c in python_code:
        pyfuck += "chr("
        ord_c = ord(c)
        fuck = int('1' * len(str(ord_c)))
        while ord_c != 0:
            for i in range(int(ord_c / fuck)):
                if pyfuck[-1] != "(":
                    pyfuck += "+"
                pyfuck += f"{str(fuck)}"
            ord_c = int(ord_c % fuck)
            fuck = int(fuck / 10)
        pyfuck += ")+"

    output_file.write(f"exec({pyfuck[:-1]})")
    print("-> output.py")