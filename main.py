import random
print("Infinity Dice")

numberofSides = int(input("How many sides?: "))
playGame = "yes"

def infinityDiceRoll(numberofSides):
  print("You rolled", random.randint(1, numberofSides))
while playGame == "yes":
  infinityDiceRoll(numberofSides)
  playGame = input("Roll again? ")