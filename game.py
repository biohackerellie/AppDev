import random

def roll_dice():
	while True:
		roll = input("Roll dice?: Yes. No. ")
		number = random.randint(1, 20)
		if roll in ["Yes"]:
			print("You rolled a", number)
		else:
			break

roll_dice()

