import re

html = ''
for _ in range(int(input())):
    html += input()

html = re.sub(r'<!--.*?-->', '', html)
tags = re.findall('<([^/].*?)>', html)
for tag in tags:
    print(re.match('[^ ]+', tag).group())
    attrs = re.findall('([^ ]+)="(.+?)"', tag)
    for attr in attrs:
        print(f'-> {attr[0]} > {attr[1]}')