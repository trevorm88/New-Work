import random
print("Welcome to rock paper scissors!!!")
rps = input("Type rock, paper or scissors\n")
rps = rps.lower()


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

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#BOT
bot = random.randint(0,2)
rockb = 0
paperb= 1
scissorsb = 2

#USER
rocku = "rock"
paperu = "paper"
scissorsu = "scissors"


if rps == rocku and bot == 0:
    print("Tied, Play Again")
    print(rock, rock)
elif rps == rocku and bot == scissorsb:
    print("Rock beats scissors, you win!")
    print(rock, scissors)
elif rps == rocku and bot == paperb:
    print("Paper beats scissors, you lose!")
elif rps == paperu and bot == paperb:
    print("Tied play again!")
    print(paper, paper)
elif rps == paperu and bot == rockb:
    print("Paper beats rock, you win!")
    print(paper, rock)
elif rps == paperu and bot == scissorsb:
    print("Scissors beat paper, you lose!")
    print(paper, scissors)
elif rps == scissorsu and bot == scissorsb:
    print("Tied!")
    print(scissors, scissors)
elif rps == scissorsu and bot == rockb:
    print("Rock beats scissors, you lose!")
    print(scissors, rock)
elif rps == scissorsu and bot == paperb:
    print("Scissors beats paper, you win!")
    print(scissors, paper)
    

    

    