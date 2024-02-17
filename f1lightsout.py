import time
import random
from termcolor import colored

names = []; leaderboard = []

colormode = True

def read_players_file():
	try:
		f = open("players.txt", "r")
		for x in f:
			x = x.strip()
			names.append(x)
		f.close()
	except:
		f = open("players.txt", "w")
		f.close()

def update_players_file():
	f = open("players.txt", "w")
	for p in names:
		f.write(p + '\n')
	f.close()

def read_leaderboard():
	try:
		f = open("leaderboard.txt", "r")
		for x in f:
			x = x.split()
			leaderboard.append( [x[0], float(x[1])] );
		f.close()
	except:
		f = open("leaderboard.txt", "w")
		f.close()


def update_leaderboard():
	f = open("leaderboard.txt", "w")
	for x in leaderboard:
		f.write(str(x[0]) + ' ' + str(x[1]) + '\n')
	f.close()


def add_time(player, time):
	for i in range(len(leaderboard)):
#		print("leaderboard[",i,"][1] = ", leaderboard[i][1])
#		print("time = ", time)
		if leaderboard[i][1] > time:
			leaderboard.insert(i, [player, time])
			return

	# if we reached this point, leaderboard must be empty or this was the worst time
	# so we add the element at the end of the leaderboard
	leaderboard.append([player, time]) 


def print_leaderboard():
	print(10*'\n')
	print("Leaderboard: ")
	counter = 1
	for x in leaderboard:
		if counter == 11:
			return
		print( (counter < 10)*' ' + str(counter) + '. ' + x[0] + (15-len(x[0]))*' ' + str(x[1]))
		counter += 1
	print((10-counter)*'\n')

# prints lights n seconds to go
def print_lights(n):
	print(25*'\n')
	
	g = r5 = r4 = r3= r2= r1= 3*' '
	if n == 0:
		g = 3*'#'
	if n <= 5 and n > 0:
		r5 = 3*'#'
		if n <= 4:
			r4 = 3*'#'
			if n <= 3:
				r3 = 3*'#'
				if n <= 2:
					r2 = 3*'#'
					if n <= 1:
						r1 = 3*'#'
	
	if colormode:
		print(colored(" ___     ___     ___     ___     ___ ", "white"))
		print(colored("|", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|", "white"))
		print(colored("|", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|", "white"))
		print(colored("|", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|", "white"))
		print(colored("|   |   |   |   |   |   |   |   |   |", "white"))
		print(colored("|   |   |   |   |   |   |   |   |   |", "white"))
	else:
		print(" ___     ___     ___     ___     ___ ")
		print("|"+ g + "|   |"+ g + "|   |"+ g + "|   |"+ g + "|   |"+ g + "|")
		print("|"+ g + "|   |"+ g + "|   |"+ g + "|   |"+ g + "|   |"+ g + "|")
		print("|"+ g + "|   |"+ g + "|   |"+ g + "|   |"+ g + "|   |"+ g + "|")
		print("|   |   |   |   |   |   |   |   |   |")
		print("|   |   |   |   |   |   |   |   |   |")
	
	if n > 0:
		if colormode:
			print(colored("|", "white") + colored(r1, "red") + colored("|   |", "white") + colored(r2, "red") + colored("|   |", "white")+ colored(r3, "red") + colored("|   |", "white")+ colored(r4, "red") + colored("|   |", "white")+ colored(r5, "red") + colored("|", "white"))
			print(colored("|", "white") + colored(r1, "red") + colored("|   |", "white") + colored(r2, "red") + colored("|   |", "white")+ colored(r3, "red") + colored("|   |", "white")+ colored(r4, "red") + colored("|   |", "white")+ colored(r5, "red") + colored("|", "white"))
			print(colored("|", "white") + colored(r1, "red") + colored("|   |", "white") + colored(r2, "red") + colored("|   |", "white")+ colored(r3, "red") + colored("|   |", "white")+ colored(r4, "red") + colored("|   |", "white")+ colored(r5, "red") + colored("|", "white"))
		else:
			print("|" + r1 + "|   |" + r2 + "|   |"+ r3 + "|   |"+ r4 + "|   |"+ r5 + "|")
			print("|" + r1 + "|   |" + r2 + "|   |"+ r3 + "|   |"+ r4 + "|   |"+ r5 + "|")
			print("|" + r1 + "|   |" + r2 + "|   |"+ r3 + "|   |"+ r4 + "|   |"+ r5 + "|")
	else:
		if colormode:
			print(colored("|", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|", "white"))
			print(colored("|", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|", "white"))
			print(colored("|", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|", "white"))
		else:
			print("|"+ g + "|   |"+ g + "|   |"+ g + "|   |"+ g + "|   |"+ g + "|")
			print("|"+ g + "|   |"+ g + "|   |"+ g + "|   |"+ g + "|   |"+ g + "|")
			print("|"+ g + "|   |"+ g + "|   |"+ g + "|   |"+ g + "|   |"+ g + "|")

	if colormode: print(colored("|___|   |___|   |___|   |___|   |___|", "white"))
	else: print("|___|   |___|   |___|   |___|   |___|")
	print(2*'\n')
	if n > 0:
		print()


read_players_file()
try:
	active_player = names[0]
except IndexError:
	active_player = ''

read_leaderboard()

running = True
while (running):
	print(25*'\n')
	if names == []:
		if colormode: print(colored("Hi! \n", "white"))
		else: print("Hi! \n")
	else:
		if colormode: print(colored("Hi, " + active_player +"! \n", "white"))
		else: print("Hi, " + active_player +"! \n")
	if colormode: print(colored("Press Enter when all lights turn green.\n", "white"))
	else: print("Press Enter when all lights turn green.\n")
	if names == []:
		if colormode: print(colored("Press 0 to set up a profile", "white"))
		else: print("Press 0 to set up a profile")
	else:
		if colormode: print(colored("Press 0 if it's not you", "white"))
		else: print("Press 0 if it's not you")
	if colormode: print(colored("Press 1 to start playing", "white"))
	else: print("Press 1 to start playing")
	if colormode: print(colored("Press 2 to see the story behind the game", "white"))
	else: print("Press 2 to see the story behind the game")
	if colormode: print(colored("Press 3 to see the highscores", "white"))
	else: print("Press 3 to see the highscores")
	if colormode: print(colored("Press 4 to go to settings", "white"))
	else: print("Press 4 to go to settings")
	a = input()
	print('\n')
	
	if a == '1':
		print_lights(5)
		time.sleep(1)
		print_lights(4)
		time.sleep(1)
		print_lights(3)
		time.sleep(1)
		print_lights(2)
		time.sleep(1)
		print_lights(1)
		time.sleep(2.8*random.random() + 0.2)
		print_lights(0)
		if colormode: print(colored('GO!!!', "white"))
		else: print('GO!!!')
		
		start = time.time()
		a = input()
		end = time.time()
		
		reactime = end - start
		if reactime > 0.05:
			reactime = round(reactime,3)
			print(reactime)
			add_time(active_player, reactime)
			update_leaderboard()
		else:
			if colormode: print(colored("FALSE START", "red"))
			else: print("FALSE START")
		if colormode: print(colored("\nPress Enter to play again", "white"))
		else: print("\nPress Enter to play again")
		a = input()
		
	elif a == '0':
		if not names == []:
			for i in range(len(names)):
				print(str(i) + '. ' + names[i])
			print("\nChoose your name")
		else:
			print("Type your name")
		a = input()
		if len(a) == 0:
			continue
		if a[0] == '-':
				if not a[1:].isnumeric():
					continue
				a = int(a[1:])
				if a >= len(names):
					continue
				names.pop(a)
				if len(names) > 0:
					active_player = names[0]
				else:
					active_player = ''
				update_players_file()
		elif a.isnumeric():
			a = int(a)
			if a < len(names):
				active_player = names[a]
		else:
			if a not in names:
				names.append(a)
				update_players_file()
			active_player = a
	
	
	elif a == '3':		
		print_leaderboard()
		if colormode: print(colored("\n\nPress Enter to go back in the main menu. ", "white"))
		else: print("\n\nPress Enter to go back in the main menu. ")
		a = input()
		if a == "clear":
			leaderboard = []
			update_leaderboard()

	elif a == '2':
		print(20*'\n')
		if colormode:
			print(colored("F1 Lights Out\n", "white"))
			print(colored("Top F1 drivers need to have top reflexes to beat their opponents at the start of the race.", "white"))
			print(colored("Do you have what it takes to take the advantage?", "white"))
			print(colored("\nPress Enter when all lights turn green to accelerate!", "white"))
			print(colored("\n\nMade by CaptainKouk", "white"))
			print(colored("\nPress Enter to go back in the main menu.", "white"))
		else:
			print("F1 Lights Out\n")
			print("Top F1 drivers need to have top reflexes to beat their opponents at the start of the race.")
			print("Do you have what it takes to take the advantage?")
			print("\nPress Enter when all lights turn green to accelerate!")
			print("\n\nMade by CaptainKouk")
			print("\nPress Enter to go back in the main menu.")
		a = input()
	
	elif a == '4':
		print(20*'\n')
		if colormode: print(colored("Settings\n\n\n", "white"))
		else: print("Settings\n\n\n")
		if colormode: print(colored("1. Color mode        Y/N\n", "white"))
		else: print("1. Color mode        Y/N\n")

		print(3*'\n')
		if colormode: print(colored("Type the number of the setting and then the letter (Y for yes or N for no)", "white"))
		else: print("Type the number of the setting and then the letter (Y for yes or N for no)")
		a = input('\n').upper()

		if a == '1Y':
			colormode = True
		elif a == '1N':
			colormode = False



