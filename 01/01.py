def main():
    sum = 0
    frequencies = set([0])
    repeats = False

    while not repeats:
        infile = open("input.txt","r")
        for line in infile:
            sum += eval(line)
            if sum in frequencies:
                print("repeats: ", sum)
                repeats = True
                break
            frequencies.add(sum)
        infile.close()

    print("sum is: ", sum)
main()
