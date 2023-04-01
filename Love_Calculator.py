name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

full_name = name1 + name2
lower_name = full_name.lower()      #lower case combined names

t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")


l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")

true = t + r + u + e
love = l + o + v + e
true = str(true)
love = str(love)
true_love = true + love     #2 digit number necessary
true_love = int(true_love)

if true_love < 10 or true_love > 90:
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif true_love > 40 and true_love < 50:
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}.")

    

