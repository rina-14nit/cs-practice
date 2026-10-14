def read_rows(lines):
    rows = []
    header = ""
    for line in lines:
        line = line.strip()
        values = line.split(",")
        clean_values = []
        [clean_values.append(v.strip()) for v in values]
        if header == "":
            header = clean_values
            continue
        if len(clean_values) != len(headers):
            continue
        rows.append(dict(zip(header, clean_values)))
    return rows
