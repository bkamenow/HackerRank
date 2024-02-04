def stack_cubes(num_test_cases, test_cases):
    results = []

    for i in range(num_test_cases):
        n = test_cases[i][0]
        cubes = test_cases[i][1]

        left, right = 0, n - 1
        top = float('inf')

        while left <= right:
            if cubes[left] >= cubes[right]:
                current_cube = cubes[left]
                left += 1
            else:
                current_cube = cubes[right]
                right -= 1

            if current_cube > top:
                results.append("No")
                break
            else:
                top = current_cube
        else:
            results.append("Yes")

    return results


if __name__ == "__main__":
    N = int(input())
    test_cases = []

    for _ in range(N):
        n = int(input())
        cubes = list(map(int, input().split()))
        test_cases.append((n, cubes))

    results = stack_cubes(N, test_cases)

    for result in results:
        print(result)
