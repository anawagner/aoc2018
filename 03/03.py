def get_rectangle(claim):
    parts = claim.split()
    claim_id = eval(parts[0][1:])
    position = parts[2].split(',')
    x = eval(position[0])
    y = eval(position[1][:-1])
    size = parts[3].split('x')
    width = eval(size[0])
    height = eval(size[1])
    return [claim_id, x, y, width, height]

def get_claims(filename):
    claims = []
    infile = open(filename,"r")
    for line in infile:
        claims.append(get_rectangle(line.rstrip()))
    infile.close()
    return claims

def count_xs(grid):
    count = 0
    for row in grid:
        row_count = row.count('X')
        count += row_count
    return count

def grid(claims):
    grid_w = 1001
    grid_h = 1001
    grid = [ [0 for x in range(grid_w)] for y in range(grid_h)]
    for claim in claims:
        claim_id = claim[0]
        x = claim[1]
        y = claim[2]
        w = claim[3]
        h = claim[4]
        for i in range(w):
            for j in range(h):
                row = y + j
                col = x + i
                if str(grid[row][col]).isalpha() or (str(grid[row][col]).isdigit() and grid[row][col] > 0):
                    grid[row][col] = "X"
                else:
                    grid[row][col] = claim_id
    return grid

def print_grid(grid):
    for row in grid:
        for col in row:
            print(col, end="")
        print('\n', end="")

def good_claim(grid, claims):
    good_id = 0
    for claim in claims:
        claim_id = claim[0]
        x = claim[1]
        y = claim[2]
        w = claim[3]
        h = claim[4]
        claim_grid = []
        for j in range(h):
            row = y + j
            claim_grid.append(grid[row][x:x+w])
        if count_xs(claim_grid) == 0:
            good_id = claim_id
    return good_id

def main():
    filename = "input.txt"
    the_claims = get_claims(filename)
    the_grid = grid(the_claims)
    print("Good Claim", good_claim(the_grid,the_claims))
    print("count", count_xs(the_grid))
main()
