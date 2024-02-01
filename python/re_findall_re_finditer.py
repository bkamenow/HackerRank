import re


def find_vowels_between_consonants(s):
    pattern = r'(?<=[^aeiouAEIOU])[aeiouAEIOU]{2,}(?=[^aeiouAEIOU])'
    return re.findall(pattern, s)


if __name__ == "__main__":
    S = input()
    result = find_vowels_between_consonants(S)

    if result:
        for match in result:
            print(match)
    else:
        print(-1)
