def read_rows(lines):
    if len(lines) == 0:
        return []
    headers = []
    for header in lines[0].rstrip().split(','):
        if header.strip():
            headers.append(header.strip())
    rows = []
    for line in lines[1:]:
        row = []
        for elem in line.rstrip().split(','):
            if elem.strip():
                row.append(elem.strip())
        if len(row) == len(headers):
        rows.append({headers[i]: row[i] for i in range(len(headers))})
    return rows

def count_types(rows):
    cnt = dict()
    for elem in rows:
        cnt[elem['тип']] = cnt.get(elem['тип'], 0) + 1
    return cnt

def total_minutes(rows, kind):
    minutes = 0.0
    for elem in rows:
        if elem['тип'] == kind:
            try:
                minutes += float(elem['минуты'].replace(',', '.'))
            except ValueError:
                continue
    return round(minutes, 1)
