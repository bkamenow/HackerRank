import re


def extract_text_between_braces(text):
    pattern = re.compile(r'{(.*?)}', re.DOTALL)
    matches = pattern.findall(text)
    return matches


def hex_color_code(text):
    pattern = r'#([0-9A-Fa-f]{3,6})'
    result = re.findall(pattern, text)
    return ['#' + color for color in result]


if __name__ == '__main__':
    n = int(input())

    css = '\n'.join(input() for _ in range(n))

    clear_code = extract_text_between_braces(css)

    clear_code_string = '\n'.join(clear_code)

    res = hex_color_code(clear_code_string)

    print('\n'.join(res))
