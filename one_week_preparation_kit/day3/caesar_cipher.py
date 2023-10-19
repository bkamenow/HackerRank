def caesarCipher(s, k):
    encrypted_string = ""

    for char in s:
        if char.isalpha():
            shift = k % 26
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
            shifted_char = chr(base + (ord(char) - base + shift) % 26)
            encrypted_string += shifted_char
        else:
            encrypted_string += char

    return encrypted_string


if __name__ == '__main__':
    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    print(result)