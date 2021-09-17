import re


def find_max_ap(students_line):
    pattern = r'AP{1,}'
    return re.findall(pattern, students_line)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        students_line = input()
        res = find_max_ap(students_line)
        if len(res) != 0:
            print(len(max(res, key=len)) - 1)
        else:
            print(0)
