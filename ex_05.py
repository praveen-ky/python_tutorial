# Repeatedly reads no. until the users enter "done". Once "done" is entered Print out the total, count and average of the no.s and use error handling.

count = 0
add = 0
while True :
    num = input("Enter the no.: ")
    if num == "done": 
        break
    else:  
        try:
            num  = int(num)
        except: 
            print("Please enter a valid no.")
            continue
        count += 1
        add = add + num
avg = add / count
print("Your Total, Count and average are as follows respectively: ",add,"\t",count,"\t",avg)