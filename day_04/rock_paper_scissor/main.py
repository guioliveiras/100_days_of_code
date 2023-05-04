import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

sicssor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

computer_choice = random.randint(0, 2)
user_choice = int(
    input("What do you choose:\n 0 - Rock\n 1 - Paper\n 2 - Scissor\n\n"))

if user_choice not in (0, 1, 2):
    print("Are you STUPID?")

option = [rock, paper, sicssor]
result = ['Drawn', "You Won", "You Lose"]

x = user_choice - computer_choice

print(
    f"\nYou choose {option[user_choice]}\n\n Computer Choose {option[computer_choice]}\n\n {result[x]}")
