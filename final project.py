import random

# features:
# - random
# - if
# - variables
# - input
# - eval
# - list
# - print
# - math
# - comments
# - loops
# - while
# - compare

# asking the "customer" what "pizza" they want
numpizzas = eval(input("How many pizzas do you want?"))

toppings = ["olives", "mushrooms", "pineapple", "chicken", "bacon"]

pizza_toppings = []

while True:
    topping = input("What topping(s) do you want? We have: " + ", " .join(toppings) + "\nPress enter DONE when your selection is complete.")

    if topping == "DONE":
        break
    if topping not in toppings:
        print ("We don't offer ", topping)
    elif topping in pizza_toppings:
        print("\nYou already have selected ", topping)
    else:
        pizza_toppings.append(topping)

numtopping = len(pizza_toppings)

print("You have ordered ", numtopping , "toppings")
crust = input("What crust do you want on your pizza? We have thin or pan")

# calculating the price
if crust == "thin":
    cost_per_pizza = numpizzas * (numtopping + 0.25)

elif crust == "pan":
    cost_per_pizza = numpizzas * (numtopping + 1.25)
# printing the price of the pizza
print("The cost of your pizza is $", cost_per_pizza)
# random disount
luck = random.randint(1, 2)
if luck == 2:
    print("You are a lucky winner, you receive a 40% discount!")

    apply = input("Do you want to apply the discount?(y/n) ")
    if apply == "y":
        print("The cost of your pizza is now $", cost_per_pizza)
        cost_per_pizza = (cost_per_pizza / 5) * 3

# arcade
player = input("While waiting for your pizza, do you want to join arcade (or leave):")
scorep = 0
scorec = 0
while player != "leave":
    choices = ["rock", "paper", "scissors"]
    player = input("Do you want to be rock, paper, or scissors")
    player = player.lower()
    computer = random.choice(choices)
    print("You chose " + player + ", and the computer chose " + computer + ".")
    if player == computer:
        print("It's a tie!")
        print("Score is", scorep, "(you), and", scorec, "(computer)!")

    elif player == "rock":
        if computer == "scissors":
            print("You win!")
            scorep += 1
            print("Score is", scorep, "(you), and", scorec, "(computer)!")
        else:
            print("Computer wins!")
            scorec += 1
            print("Score is", scorep, "(you), and", scorec, "(computer)!")
    elif player == "paper":
        if computer == "rock":
            print("You win!")
            scorep += 1
            print("Score is", scorep, "(you), and", scorec, "(computer)!")
        else:
            print("Computer wins!")
            scorec += 1
            print("Score is", scorep, "(you), and", scorec, "(computer)!")
    elif player == "scissors":
        if computer == "paper":
            print("You win!")
            scorep += 1
            print("Score is", scorep, "(you), and", scorec, "(computer)!")
        else:
            print("Computer wins!")
            scorec += 1
            print("Score is", scorep, "(you), and", scorec, "(computer)!")
    elif player == "leave":
        print("Thanks for playing")
    else:
        print("I think there was some sort of error...")
print("Thank you, your pizza is ready")

# animation
# TO DO: draw a circle for the pizza