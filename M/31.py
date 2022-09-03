
def solution(input):
    rows = len(input)
    cols = len(input[0])
    row_grey = [0 for _ in range(rows)]
    col_grey = [0 for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            if input[i][j] == '1':
                row_grey[i] += 1
                col_grey[j] += 1
    print(row_grey)
    print(col_grey)
    max_row = float('-inf')
    max_col = float('-inf')
    for r in row_grey:
        max_row = max(max_row, r)
    for c in col_grey:
        max_col = max(max_col, c)
    return max_row + max_col

def main():
    grid = [['1', '1', '1'],['0', '1', '1'],['0', '1', '0']]
    ans = solution(grid)
    print(ans)

if __name__ == "__main__":
    main()