import re

def get_rectangle(claim):
    rect_tuple = re.findall(r'#(\d+)\s@\s(\d+),(\d+):\s(\d+)x(\d+)',claim)
    return tuple(eval(str) for str in rect_tuple[0])

def get_claims(filename):
    claims = []
    infile = open(filename,"r")
    for line in infile:
        claims.append(get_rectangle(line.rstrip()))
    infile.close()
    return claims

def count_overlaps(grid):
    count = 0
    for row in grid:
        for sq in row:
            if len(sq) > 1:
                count += 1
    return count

def grid(claims, grid_w, grid_h):
    grid = [ [[] for x in range(grid_w)] for y in range(grid_h)]
    for claim in claims:
        (claim_id, x, y, w, h) = claim
        for i in range(w):
            for j in range(h):
                row = y + j
                col = x + i
                grid[row][col].append(claim_id)
    return grid

def print_grid(grid):
    for row in grid:
        for col in row:
            print(col, end="")
        print('\n', end="")

def good_claim(grid, claims):
    good_id = []
    for claim in claims:
        (claim_id, x, y, w, h) = claim
        claim_grid = []
        for j in range(h):
            row = y + j
            claim_grid.append(grid[row][x:x+w])
        if count_overlaps(claim_grid) == 0:
            good_id.append(claim_id)
    return good_id

def main():
    filename = "subinput.txt"
    grid_width = 51
    grid_height = 51
    the_claims = get_claims(filename)
    the_grid = grid(the_claims, grid_width, grid_height)
    print("overlaps:", count_overlaps(the_grid))
    #print_grid(the_grid)
    print("Good Claim", good_claim(the_grid,the_claims))
main()
