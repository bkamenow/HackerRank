def climbingLeaderboard(ranked, player):
    ranked = sorted(set(ranked), reverse=True)
    player_leaderboard = []

    for player_score in player:
        while ranked and player_score >= ranked[-1]:
            ranked.pop()

        position = len(ranked) + 1
        player_leaderboard.append(position)
    return player_leaderboard


if __name__ == '__main__':
    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    print(result)
