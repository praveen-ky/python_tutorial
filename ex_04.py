# Grade program using functions:

Score = input("Enter the Score: ")
Score = float(Score)

# Defining Functions: 

def computgrade( score ):
    score = float()
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

# Calling functions:
computgrade(Score)
