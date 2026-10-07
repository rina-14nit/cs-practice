def winner(names: list[str], scores: list[float]):
    if not names:
        return ""
    max_score = max(scores)
    name_winner = scores.index(max_score)
    return names[name_winner]
def average(scores: list[float]):
    if not scores:
        return 0.0
    return round(sum(scores) / len(scores), 2)