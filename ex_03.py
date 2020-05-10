#Pay computation to give the employee 1.5 times the hourly rate for hours worked above 40

hrs = input("Enter Hours: ")
hrs = int(hrs)
rate = input("Enter Rate: ")
rate = float(rate)

if(hrs>40):
    pay = ((hrs-40)*1.5*rate) + (40*rate)
else:
    pay = hrs * rate

#Pay program using 'try' and 'except' to handle non numeric input gracefully with error message to user:

hrs = input("Enter Hours: ")

try:
    hrs = int(hrs)
except:
    print("Please enter numeric input")
    
rt = input("Enter Rate: ")

try:
    rt = float(rt)
except:
    print("Please enter numeric report")
    

if(hrs>40):
    pay = ((hrs-40)*1.5*rt) + (40*rt)
else:
    pay = hrs * rt

#Program to prompt score between 0.0 to 1.0. with error handling if out of range. And if  in range then tell the grade:

score = input("Enter Score: ")
score = float(score)
try:
    if score in range(0,1):
        if score >= 0.9:
            print(" Your grade is 'A', Good job :), Really proud of you! keep up the good work")
        elif score >= 0.8:
            print(" Your grade is 'B', Good job, Stay persistent and u can get even better grades")
        elif score >=0.7:
            print(" Your grade is 'C', Decent job, though better results are expected")
        elif score >= 0.6:
            print(" Your grade is 'D', Hey there is a loot of room for improvement")
        else:
            print(" Your grade is 'F', Hang on there ik u can do better")
    else:
        print("Please enter a no. between 0 and 1")
except:
    print(' Please enter a valid INPUT!!!')