import textwrap

def wrap(string, max_width):
    my_wrap = textwrap.TextWrapper(width=max_width)
    wrap_list = my_wrap.wrap(text=string)
    return '\n'.join(wrap_list)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

