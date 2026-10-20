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

