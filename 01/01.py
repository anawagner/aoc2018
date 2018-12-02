infile = open("input.txt","r")

sum = 0

for line in infile:
    sum += eval(line)
infile.close()

print(sum)
