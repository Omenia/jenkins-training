# coding: utf-8

class Calculate(object):

    def calculate(self, a,b,c):
        a = float(a)
        b = float(b)
        if c == '+':
            ret_val = str(a + b)
        elif c == '-':
            ret_val = str(a - b)
        elif c == '*':
            ret_val = str(a * b)
        elif c == '/':
            ret_val = str(a / b)
        else:
            ret_val = "Unknown operator"
        return ret_val


