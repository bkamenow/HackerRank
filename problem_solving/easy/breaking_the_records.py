def breakingRecords(scores):
    best = scores[0]
    worst = scores[0]
    worst_record_count = 0
    best_record_count = 0
    for score in scores:
        if worst > score:
            worst = score
            worst_record_count += 1
        if best < score:
            best = score
            best_record_count += 1

    return best_record_count, worst_record_count


if __name__ == '__main__':
    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(result)