import random

rndmNum = random.randint(1, 10)

guess = int(input("Enter an integer from 1 to 10: "))

while True:
	if guess < rndmNum:
		print ("too low")
		guess = int(input("Enter an integer from 1 to 10: "))

	elif guess > rndmNum:
		print ("too high")
		guess = int(input("Enter an integer from 1 to 10: "))

	else:
		print ("Congrats you guessed correctly!")
		break
	