def getRandomNums(filename):
    with open(filename) as f:
        first_line = f.readline().strip()
        random_nums = first_line.split(',')
    return random_nums

# get grid board list from input file
def getGridBoards(filename):
    res = []
    grid = []
    count = 0
    with open(filename) as f:
        for line in f:
            line_li = line.strip().split(' ')
            for elem in line_li:
                if elem == '':
                    line_li.remove(elem)
            if len(line_li) == 5:
                grid.append(line_li)
                count += 1
            if count == 5:
                res.append(grid.copy())
                grid = []
                count = 0
    return res

def lastWinner(random_nums, grid_boards):
    winners = []
    grid_row = 5
    grid_clm = 5
    for num in random_nums:
        for grid in grid_boards:
            # mark number
            for i in range(grid_row):
                for j in range(grid_clm):
                    if grid[i][j] == num:
                        grid[i][j] = 'M'
            # check adjacent rows
            if ['M','M','M','M','M'] in grid and grid not in winners:
                winners.append(grid)
                if len(winners) == len(grid_boards):
                    return grid, num
            # check adjacent clms
            for j in range(grid_clm):
                clm = []
                for i in range(grid_row):
                    clm.append(grid[i][j])
                if clm == ['M','M','M','M','M'] and grid not in winners:
                    winners.append(grid)
                    if len(winners) == len(grid_boards):
                        return grid, num

def getScore(winner, fin_num):
    total = 0
    for row in winner:
        for cell in row:
            if cell != 'M':
                total += int(cell)
    return total * int(fin_num)

random_nums = getRandomNums('input1204.txt')
grid_boards = getGridBoards('input1204.txt')
last_winner, fin_num = lastWinner(random_nums, grid_boards)
score = getScore(last_winner, fin_num)
print(last_winner, fin_num)
print(score)