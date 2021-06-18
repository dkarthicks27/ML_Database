class Pointer:
    def __init__(self, pointed):
        self.pointed = pointed
        self.count = 1

    def compare(self, np):
        pass

    def change(self, new_point):
        if self.pointed == new_point:
            self.count += 1
            return True
        else:
            return False




def balanced_string(s):
    pass

import re

if __name__ == '__main__':
    # inp = input()
    inp = "RLLLLRRRLR"
    balanced_string(inp)
    # x = balanced_string(inp)

