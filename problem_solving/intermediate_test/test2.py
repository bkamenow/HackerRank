def split(node, x):
    assert node['l'] <= x <= node['r']
    if x == node['l'] or x == node['r']:
        return
    if 'lc' in node:
        if x == node['lc']['r']:
            return
        if x < node['lc']['r']:
            split(node['lc'], x)
        else:
            split(node['rc'], x)
        node['val'] = max(node['lc']['val'], node['rc']['val'])
    else:
        node['lc'] = {'l': node['l'], 'r': x, 'val': x - node['l']}
        node['rc'] = {'l': x, 'r': node['r'], 'val': node['r'] - x}
        node['val'] = max(x - node['l'], node['r'] - x)


def getMaxArea(w, h, isVertical, distance):
    w_root = {'l': 0, 'r': w, 'val': w}
    h_root = {'l': 0, 'r': h, 'val': h}
    ans = []

    for iv, d in zip(isVertical, distance):
        if iv:
            split(w_root, d)
        else:
            split(h_root, d)
        ans.append(w_root['val'] * h_root['val'])

    return ans


if __name__ == '__main__':

    w = int(input().strip())

    h = int(input().strip())

    isVertical_count = int(input().strip())

    isVertical = []

    for _ in range(isVertical_count):
        isVertical_item = int(input().strip()) != 0
        isVertical.append(isVertical_item)

    distance_count = int(input().strip())

    distance = []

    for _ in range(distance_count):
        distance_item = int(input().strip())
        distance.append(distance_item)

    result = getMaxArea(w, h, isVertical, distance)

    print(result)
