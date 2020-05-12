# Program to read through a file and print the contents of the file line by line in upper case:

fname = input("Enter the file name: ")
handle = open(fname)

for line in handle:
    print(line.upper())

#look through file to find average X-DSPAM-Confidence

fname = input("Enter the file name: ")
handle = open(fname)
sum = 0
count = 0
for line in handle:
    if not line.startswith('X-DSPAM Confidence:'):
        continue
    else:
        count+=1
        pos = line.find(':')
        num = float(line[pos+1:])
        sum = sum + num
average = sum/count
print("Average spam confidence:",average)

# Easter Eggs:

fname = input("Enter the file name: ")
if fname == "na na boo boo":    print("NA NA BOO BOO TO YOU - You have been punk'd!")
handle = open(fname)
sum = 0
count = 0
for line in handle:
    if not line.startswith('X-DSPAM Confidence:'):
        continue
    else:
        count+=1
        pos = line.find(':')
        num = float(line[pos+1:])
        sum = sum + num
average = sum/count
print("Average spam confidence:",average)
