import random

'''Request lower and upper values of range from user. 
    Next, ensure first inputted value is lower than second inputted value
    (low_val <= up_val). Note the range is inclusive and values must be integers.
    Then, generate a random number within the range.
    Finally, compare user's guess to the random number generated with visual indicator. 
'''

low_val = input("Enter lower value of range: ")
up_val = input("Enter upper value of range: ")

# Validating numbers inputted by user to make up a range of values
while ((low_val.strip("-")).isnumeric() == False) or \
      ((up_val.strip("-")).isnumeric() == False) or (int(low_val) > int(up_val)):
    print("Try again, first value should be less than or equal to second value \
    and both values should be integers")
    low_val = input("Enter lower value of range: ")
    up_val = input("Enter upper value of range: ")

# Calculating random value
random_num = random.randint(int(low_val),int(up_val))                                                      

status = False

# Checking that user's guess matches random number
while status == False:
    print("Guess the randomized number")
    user_in = input("Enter your guess: ")

    if user_in.lstrip('-').isdigit():
        user_in = int(user_in)

        if  user_in <= int(up_val) and user_in>=int(low_val):
            if user_in == random_num:
                print("Congratulations, you win! Good bye!")
                from tkinter import messagebox
                messagebox.showinfo("Woot woot!", "You guessed correctly!")
                status = True
    
            elif user_in < random_num:
                print("Good try, guess higher!")

            elif user_in > random_num:
                print("Good try, guess lower!")
                
        else:
            print("Please guess in the range!")
    else:
        print("Only integers please!")

