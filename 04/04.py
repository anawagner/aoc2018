import re
from operator import itemgetter

def get_data(file):
    infile = open(file,"r")
    data = infile.read()
    infile.close()
    entries = re.findall(r'\[\d+-(\d+)-(\d+)\s(\d+):(\d+)\]\s(.*)\n',data)
    return sorted(entries, key=itemgetter(0,1,2,3))

def print_data(data):
    counter = 0
    for entry in data:
        counter += 1
        for item in entry:
            print(item," ", end="")
        print("")
    print("There are", counter, "entries")

def print_naps(naps):
    counter = 0
    for nap in naps:
        print(nap)
        print("")
        counter += 1
    print("there are:",counter,"naps")

def get_all_guard_naps(data):
    guard_naps = []
    for entry in data:
        if re.search(r'Guard',entry[4]):
            id = re.search(r'#(\d+)',entry[4]).group(1)
        elif re.search(r'asleep',entry[4]):
            sleep = int(entry[3])
        elif re.search(r'wake',entry[4]):
            wake = int(entry[3])
            nap = {'id':id,'sleep':sleep,'wake':wake,'duration': wake - sleep }
            guard_naps.append(nap)
    return guard_naps

def guard_totals(naps):
    guard_total = {}
    for nap in naps:
        guard_total[nap['id']] = nap['duration'] + guard_total.get(nap['id'],0)
    return guard_total

def sleepiest_guard(naps):
    totals = guard_totals(naps)
    return max(totals, key=totals.get)

def get_one_guard_naps(naps, id):
    sleepy_guard_naps = []
    for nap in naps:
        if nap['id'] == id:
            sleepy_guard_naps.append(nap)
    return sleepy_guard_naps

def minute_counts(naps):
    sleep_min = {}
    for nap in naps:
        for n in range(nap['sleep'],nap['wake']):
            sleep_min[n] = sleep_min.get(n,0) + 1
    return sleep_min

def sleepiest_time(naps):
    min_counts = minute_counts(naps)
    minute = max(min_counts, key=lambda k: min_counts[k])
    count = min_counts[minute]
    return (minute,count)

def consistent_sleep_minute(naps):
    list_of_max = []
    for id in guard_totals(naps).keys():
        min_count = sleepiest_time(get_one_guard_naps(naps,id))
        list_of_max.append( (id, min_count[0], min_count[1]))
    return max(list_of_max, key=itemgetter(2))

def main():
    filename = "input.txt"
    the_data = get_data(filename)
    #print_data(the_data)
    naps = get_all_guard_naps(the_data)
    #print_naps(naps)
    the_sleepy_guard = sleepiest_guard(naps)
    print("Most sleeping guard: ", the_sleepy_guard)
    sleepy_minute = sleepiest_time(get_one_guard_naps(naps, the_sleepy_guard))
    print("Most sleepy minute for sleepiest guard: ", sleepy_minute)
    answer = int(the_sleepy_guard) * int(sleepy_minute[0])
    print("answer 1: ", answer)
    consistent_sleepy = consistent_sleep_minute(naps)
    print("consitent sleepy time for one guard", consistent_sleepy)
    answer2 = int(consistent_sleepy[0]) * int(consistent_sleepy[1])
    print("answer 2: ", answer2)

main()
