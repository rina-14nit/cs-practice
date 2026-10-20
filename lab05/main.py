with open(path, encoding="utf-8") as table:
    rows = read_rows(table)
    

with open("summary.csv", "w", encoding="utf-8") as out:
    out.write(to_csv(counts))