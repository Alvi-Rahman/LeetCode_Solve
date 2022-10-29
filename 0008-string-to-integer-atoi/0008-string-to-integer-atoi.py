class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.strip()

        if not(s and (s[0].isdigit() or s[0] == "-" or s[0] == "+")):
            return 0
        int_obj = ""
        sign = None
        if s[0] == "-" or s[0] == "+":
            sign = s[0]
            s = s[1:]
        for i in s:
            if not i.isdigit():
                break
            int_obj += i
        if not int_obj or not int_obj.isnumeric():
            return 0
        if sign:
            int_obj = sign + int_obj

        int_obj = int(int_obj)

        if int_obj > 0 and (int_obj + 1) / 2**31 > 1:
            return 2 ** 31 - 1
        elif int_obj < 0 and -int_obj / 2**31 > 1:
            return -2**31
        return int_obj