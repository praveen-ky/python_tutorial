#Open file read it line by line and create a list of unique words

fname = input("Enter the name of the file:")
handle = open(fname)
words = list()
unique = list()
for line in handle:
    
    words = line.rstrip().split()
    
    for word in words:
        if word in unique  :
            continue
        else:
            unique.append(word)

unique.sort()
print(unique)

#open file find line that starts with from and using split get the email ids and count it.

fname = input("Enter the name of the file:")
handle = open(fname)

for line in handle:
    if not line.startswith("From"):
        continue
    else:
        sentence = line.split()
        emailids = sentence[1]
        count+=1
    print(emailids)
print("there were "+count+" lines in the file with From as the first word")

#take a list of num from user and give max and min

lst = list()
while True:
    num = input("Enter the number: ")
    if num == "done":    break
    else:
        try:
            num = int(num)
        except:
            print("Invalid Input. Please enter a valid int")
            continue
        lst.append(num)

lst.sort()
print("Maximum:",max(lst))
print("Minimum:",min(lst))