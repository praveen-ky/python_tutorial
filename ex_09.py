# Find all lines starting with from and print out the days and the number of days
fname = input("Enter the file name:")
handle = open(fname)
lst = list()
days = list()
count = dict()
for line in handle:
    line.rstrip()
    if not line.startswith("From "):
        continue
    else:
        lst = line.split()
        days.append(lst[2])

for day in days:
    count[day]=  count.get(day,0) + 1

print(count)

# Read Maillog and build a histogram no. of messages from each email address:

fname = input("Enter the file name:")
handle = open(fname)
lst = list()
emailids = list()
count = dict()

for line in handle:
    if not line.startswith("From "):    continue
    else:
        lst = line.rstrip().split()
        emailids.append(lst[1])

for emailid in emailids:
    count[emailid] = count.get(emailid,0)+1

print(count)

# to find maximum and minimum


fname = input("Enter the file name:")
handle = open(fname)
lst = list()
emailids = list()
count = dict()

for line in handle:
    if not line.startswith("From "):    continue
    else:
        lst = line.rstrip().split()
        emailids.append(lst[1])

for emailid in emailids:
    count[emailid] = count.get(emailid,0)+1

for k,v in sorted(count.items()):
    print(k,v)