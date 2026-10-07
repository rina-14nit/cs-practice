def winner(names: list[str], scores: list[float]):
    max_score = max(scores)
    name_winner = scores.index(max_score)
    return names[name_winner]
print(winner(names, scores))