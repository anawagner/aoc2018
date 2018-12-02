infile = open("input.txt","r")

twos = 0
threes = 0
for line in infile:
    for char in line:
        if line.count(char) == 2:
            twos += 1
            break
    for char in line:
        if line.count(char) == 3:
            threes += 1
            break

print(twos*threes)

infile.close()
