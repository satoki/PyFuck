from modules.fileIO import read_file, write_file
from modules.pyfuck import PyFuck

if __name__ == "__main__":
    print(read_file("modules/logo.txt"))
    python_code = read_file(input("FileName: "))
    pyfuck = PyFuck.make_pyfuck(python_code)
    write_file("output.py", f"exec({pyfuck})")
    print("-> output.py")
