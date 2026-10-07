def winner(names, scores):
    if not names:
        return ""
    max_score = max(scores)
    name_winner = scores.index(max_score)
    return names[name_winner]
def average(scores):
    if not scores:
        return 0.0
    return round(sum(scores) / len(scores), 2)
def ranking(names, scores):
    pari = []
    for i in range(len(names)):
        pari.append([scores[i], names[i]])
        pari.sort(reverse = True)
        for i in pari:
            return i[0]

if __name__ == "__main__":
    names = ["Аня", "Боря", "Вика", "Арина"]
    scores = [7.0, 9.0, 9.0, 10.0]
    print(winner(names, scores))
    print(average(scores))
    print(ranking(names, scores))