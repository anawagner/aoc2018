def checksum(filename):
    twos = 0
    threes = 0
    infile = open(filename,"r")
    for line in infile:
        for char in line:
            if line.count(char) == 2:
                twos += 1
                break
        for char in line:
            if line.count(char) == 3:
                threes += 1
                break
    infile.close()
    print("checksum: ", twos*threes)

def differ_by_one(filename):
    infile = open(filename, "r")
    ids_list = infile.readlines()
    infile.close()

    for id in ids_list:
        id_len = len(id) - 1
        infile = open(filename, "r")
        for line in infile:
            count = 0
            result = []
            for i in range(id_len):
                if id[i] == line[i]:
                    count += 1
                    result.append(id[i])
            if count == id_len - 1:
                print(id, line, ''.join(result))
        infile.close()

def main():
    filename = "input.txt"
    checksum(filename)
    differ_by_one(filename)

main()
