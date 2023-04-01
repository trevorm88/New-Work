import random
print("Welcome to rock paper scissors!!!")
rps = input("Type rock, paper or scissors")
rps = rps.lower()
print(rps)

if rps == "rock":
    rps = 0
elif rps == "paper":
    rps = 1
else:
    rps = 2

bot = random.randint(0,2)
# 0 = rock
# 1 = paper
# 2 = scissors

if rps == 0 and bot ==0:
    print("Play Again")
elif rps == 0 and bot ==1:
    print("You rock, lose to paper")
elif rps == 0 and bot == 2:
    print("You rock win to paper!")
elif rps == 1 and bot == 0:
    print("You paper win to rock")
elif rps ==1 and bot ==1:
    print("Play Again")
elif rps == 1 and bot == 2:
    print("You paper lose to scissors")
elif rps == 2 and bot == 0:
    print("You scissors lose to rock")
elif rps == 2 and bot == 1:
    print("You scissors win to paper")
elif rps == 2 and bot == 2:
    print("Play again!")







