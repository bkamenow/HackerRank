def custom_sort(char):
    if char.islower():
        return 0, char
    elif char.isupper():
        return 1, char
    elif char.isdigit() and int(char) % 2 == 1:
        return 2, char
    elif char.isdigit() and int(char) % 2 == 0:
        return 3, char


S = input()

sorted_string = ''.join(sorted(S, key=custom_sort))
print(sorted_string)
