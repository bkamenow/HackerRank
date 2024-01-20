class TextEditor:
    def __init__(self):
        self.s = ''
        self.string_story = []

    def append_text(self, value):
        self.s += value
        self.string_story.append(self.s)

    def delete_text(self, idx):
        self.s = self.s[:-idx]
        self.string_story.append(self.s)

    def print_char(self, idx):
        if idx < len(self.s):
            print(self.s[idx])

    def undo(self):
        if self.string_story:
            self.string_story.pop()
            if self.string_story:
                self.s = self.string_story[-1]
            else:
                self.s = ''


def text_editor(ops):
    editor = TextEditor()

    for op in ops:
        o, *v = op.split()
        v = ''.join(v)

        if o == '1':
            editor.append_text(v)
        elif o == '2':
            editor.delete_text(int(v))
        elif o == '3':
            editor.print_char(int(v) - 1)
        elif o == '4':
            editor.undo()


if __name__ == "__main__":
    n = int(input())
    ops = [input() for _ in range(n)]
    text_editor(ops)
