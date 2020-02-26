#Black Magic the game written by Travis Pressler and Alexander Pressler
print("Paul Benois")
import random

undefined = 0
heads = 1
tails = 2
money = 100
num = random.randint(1, 10)

#User input below
bet = 20
choice = heads

#Below is non-user inputs
choice_heads = (choice == heads)
choice_tails = (choice == tails)

def coin_flip():
  if (num > 5) and (choice_heads):
    return "You won! Heads has gained $" + str(bet) + "!"
  elif (num > 5) and (choice_tails):
    return "You have lo st! You lose -$" + str(bet) + "!"
  elif (num <= 5) and (choice_tails):
    return "You won! Tails has gained $" + str(bet) + "!"
  elif (num <= 5) and (choice_heads):
    return "You have lost! You lose -$" + str(bet) + "!"
  elif (choice == undefined):
    return "You have not chosen a side yet!"
  else:
    return "Something went wrong please try again."

def money_stuff():
  if (num > 5) and (choice_heads):
    return money + bet
  elif (num > 5) and (choice_tails):
    return money - bet
  elif (num <= 5) and (choice_tails):
    return money + bet
  elif (num <= 5) and (choice_heads):
    return money - bet

#Call your game of chance functions here
print("Coin Flip")

print(coin_flip())

print("You now have a total of $" + str(money_stuff()))
