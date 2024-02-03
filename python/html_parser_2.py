from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' in data:
            print(">>> Multi-line Comment")
            comments = data.split('\n')
            for comment in comments:
                print(comment.strip())
        else:
            print(">>> Single-line Comment")
            print(data)

    def handle_data(self, data):
        if data != '\n':
            print(">>> Data")
            print(data)


num_lines = int(input())

html_code = ""
for _ in range(num_lines):
    html_code += input().rstrip()
    html_code += '\n'

parser = MyHTMLParser()
parser.feed(html_code)
parser.close()
