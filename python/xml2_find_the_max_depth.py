import xml.etree.ElementTree as etree

maxdepth = 0


def depth(elem, level):
    global maxdepth
    elements = list(elem.iter())
    if len(elements) == 1:
        maxdepth = max(maxdepth, level + 1)
    else:
        for i in range(1, len(elements)):
            depth(elements[i], level + 1)


if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml = xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
