def main():
    sum = 0
    frequencies = [0]
    repeats = False

    while not repeats:
        infile = open("input.txt","r")
        for line in infile:
            sum += eval(line)
            frequencies.append(sum)
            if frequencies.count(sum) > 1:
                print("repeats: ", sum)
                repeats = True
                break
        infile.close()

    print("sum is: ", sum)
main()
