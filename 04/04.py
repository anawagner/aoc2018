import re
from operator import itemgetter

# returns list of tuples (month,day,hour,minute,message entry)
# sorted by month, day, hour, and minute in that order
def get_data(file):
    infile = open(file,"r")
    data = infile.read()
    infile.close()
    entries = re.findall(r'\[\d+-(\d+)-(\d+)\s(\d+):(\d+)\]\s(.*)\n',data)
    return sorted(entries, key=itemgetter(0,1,2,3))

# print functions for visualizing and checking data
def print_data(data):
    counter = 0
    for entry in data:
        counter += 1
        for item in entry:
            print(item," ", end="")
        print("")
    print("There are", counter, "entries")

# returns dictionary of data for each nap ie:
# {'sleep': 19, 'duration': 4, 'wake': 23, 'id': '1637'}
def get_all_naps(data):
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

# returns a dictionary of key = guard id, value = total sleep time,
# one entry per guard
def guard_totals(naps):
    guard_total = {}
    for nap in naps:
        guard_total[nap['id']] = nap['duration'] + guard_total.get(nap['id'],0)
    return guard_total

#returns id of the guard with the most sleep time
def sleepiest_guard(naps):
    totals = guard_totals(naps)
    return max(totals, key=totals.get)

#returns all the naps for one guard
def get_one_guard_naps(naps, id):
    return list(filter(lambda nap: nap['id'] in id, naps))

# returns the minute most naped from a set of given guard naps
# in a tuple with the count  (minute, count)
def max_nap_minute(naps):
    minute_sleep_counts = {}
    for nap in naps:
        for n in range(nap['sleep'],nap['wake']):
            minute_sleep_counts[n] = minute_sleep_counts.get(n,0) + 1
    minute = max(minute_sleep_counts, key=lambda k: minute_sleep_counts[k])
    return (minute, minute_sleep_counts[minute])

# returns (id, minute, count) of the minute most slept by any one guard
def most_napped_minute_any_guard(naps):
    list_of_max = []
    for id in guard_totals(naps).keys():
        min_count = max_nap_minute(get_one_guard_naps(naps,id))
        list_of_max.append( (id, min_count[0], min_count[1]))
    return max(list_of_max, key=itemgetter(2))

def main():
    filename = "input.txt"
    the_data = get_data(filename)
    naps = get_all_naps(the_data)
    the_sleepy_guard = sleepiest_guard(naps)
    print("Most sleeping guard: ", the_sleepy_guard)
    sleepy_minute = max_nap_minute(get_one_guard_naps(naps,the_sleepy_guard))[0]
    print("Most sleepy minute for sleepiest guard: ", sleepy_minute)
    print("Answer1: ", int(the_sleepy_guard) * sleepy_minute)
    consistent_sleepy = most_napped_minute_any_guard(naps)
    print("consitent sleepy time for one guard", consistent_sleepy)
    print("Answer2: ",int(consistent_sleepy[0]) * consistent_sleepy[1])

main()
