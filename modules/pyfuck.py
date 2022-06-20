class PyFuck:
    # PyFuck コードを生成
    @classmethod
    def make_pyfuck(self, python_code: str) -> str:
        pyfuck = ""
        for c in python_code:
            pyfuck += f"chr({self.__num_to_fuck(str(ord(c)))})+"
        return pyfuck[:-1]
    
    # 数値を PyFuck に変換
    def __num_to_fuck(num: str) -> str:
        digit: int = len(num)  # num の文字数
        num = int(num)
        ones = int("1" * digit)  # 11111....111 の数値
        fucks = []  # [1111, 111, 11, 1]
        while num > 0 and ones > 0:
            while num > 0 and ones > 0 and num >= ones:
                num -= ones
                fucks.append(ones)
            ones = ones // 10
        return "+".join(map(str, fucks))
