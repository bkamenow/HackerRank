def sherlockAndAnagrams(s):
    n = len(s)
    anagram_count = 0

    substr_count = {}

    for i in range(n):
        for j in range(i + 1, n + 1):
            sorted_substring = ''.join(sorted(s[i:j]))

            substr_count[sorted_substring] = substr_count.get(sorted_substring, 0) + 1

    for count in substr_count.values():
        anagram_count += (count * (count - 1)) // 2

    return anagram_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        print(result)
