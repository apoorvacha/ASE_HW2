def transpose(t, u):
    u = []
    for i in range(len(t[0])):
        row = []
        for j in range(len(t)):
            row.append(t[j][i])
        u.append(row)

def repCols(cols):
    cols = cols.copy()
    for col in cols:
        col[-1] = str(col[0]) + ":" + str(col[-1])
        for j in range(1, len(col)):
            col[j-1] = col[j]
        col.pop()
        cols.insert(0, ["Num" + str(i) for i in range(1, len(cols[0]) + 1)])
        cols[0][-1] = "thingX"
        return cols

def repRows(t, rows, u):
    rows = rows.copy()
    for j, s in enumerate(rows[-1]):
        rows[0][j] = str(rows[0][j]) + ":" + str(s)
    rows.pop()
    for n, row in enumerate(rows):
        if n == 0:
            row.append("thingX")
        else:
            u = t[-(n+1) + 1]
            row.append(u[-1])
    return rows