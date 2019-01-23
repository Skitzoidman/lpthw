from sys import exit

def gold_room():
	print("This room is full of gold. How much do you take?")

	choice = input("> ")
#	how_much = int(choice)
	if "0" or "1" in choice:
		how_much =  int(choice)
		if how_much < 50:
			print("Nice, you are not greedy. You win!")
			exit(0)
		else:
			dead("You greedy bastard!")

	else:
		dead("Man, learn to type a number")



def dead(why):
	print(why, "Good job")
	exit(0)

gold_room()
