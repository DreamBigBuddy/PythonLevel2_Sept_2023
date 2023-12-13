import random

yes_no = str(input("Would you like to roll the dice?: ")).lower()

while yes_no == "yes":
    dice_1 = random.randint(1,6)
    dice_2 = random.randint(1,6)

    print("Your Numbers are", dice_1, dice_2)

    if dice_1 == 3 or dice_2 == 3:
        print("You lost! One of your dice was equal to 3")
        break
    
    elif dice_2 + dice_1 == 7:
        print("you win Your numbers equal seven")
        break

    yes_no = str(input("You didn't win would you like to go again?: ")).lower()

print("Thanks For playing")
