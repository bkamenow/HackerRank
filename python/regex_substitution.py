import re


def modify_text(lines):
    for line in lines:
        modified_line = re.sub(r'(?<=\s)&&(?=\s)', 'and', line)
        modified_line = re.sub(r'(?<=\s)\|\|(?=\s)', 'or', modified_line)
        print(modified_line)


if __name__ == "__main__":
    n = int(input())
    lines = [input() for _ in range(n)]
    modify_text(lines)
