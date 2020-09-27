import random
min = 1
max = 6

roll = "yes"

while roll == "yes" or roll == "y":
    print ("Rolling the dices...")
    print ("The values are....")
    print (random.randint(min, max))
    print (random.randint(min, max))

    roll_again = input("Do you want to roll the dices again?")
