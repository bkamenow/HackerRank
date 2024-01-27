def checkMagazine(magazine, note):
    word_count = {}

    for word in magazine:
        word_count[word] = word_count.get(word, 0) + 1

    for word in note:
        if word_count.get(word, 0) == 0:
            return 'No'
        else:
            word_count[word] -= 1

    return 'Yes'

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    res = checkMagazine(magazine, note)

    print(res)
