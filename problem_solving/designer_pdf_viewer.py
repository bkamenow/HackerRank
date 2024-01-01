def designerPdfViewer(h, word):
    letter_to_index = {chr(i + 97): i for i in range(26)}

    numbers_for_letters = []

    for letter in word:
        index = letter_to_index.get(letter)
        if index is not None:
            numbers_for_letters.append(h[index])

    largest_num = max(numbers_for_letters)

    return largest_num * len(word)


if __name__ == '__main__':
    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)
    print(result)
