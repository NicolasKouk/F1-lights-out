import time
import random
from termcolor import colored

names = []; leaderboard = []

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
			leaderboard.append(x);
		f.close()
	except:
		f = open("leaderboard.txt", "w")
		f.close()


def update_leaderboard():
	f = open("leaderboard.txt", "w")
	for x in leaderboard:
		f.write(x[0] + x[1] + '\n')
	f.close()


def add_time(player, time):
	for i in range(len(leaderboard)):
		if leaderboard[i][1] > time:
			leaderboard.insert(i, [player, time])
			return

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
	
	print(colored(" ___     ___     ___     ___     ___ ", "white"))
	print(colored("|", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|", "white"))
	print(colored("|", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|", "white"))
	print(colored("|", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|", "white"))
	print(colored("|   |   |   |   |   |   |   |   |   |", "white"))
	print(colored("|   |   |   |   |   |   |   |   |   |", "white"))
	
	if n > 0:
		print(colored("|", "white") + colored(r1, "red") + colored("|   |", "white") + colored(r2, "red") + colored("|   |", "white")+ colored(r3, "red") + colored("|   |", "white")+ colored(r4, "red") + colored("|   |", "white")+ colored(r5, "red") + colored("|", "white"))
		print(colored("|", "white") + colored(r1, "red") + colored("|   |", "white") + colored(r2, "red") + colored("|   |", "white")+ colored(r3, "red") + colored("|   |", "white")+ colored(r4, "red") + colored("|   |", "white")+ colored(r5, "red") + colored("|", "white"))
		print(colored("|", "white") + colored(r1, "red") + colored("|   |", "white") + colored(r2, "red") + colored("|   |", "white")+ colored(r3, "red") + colored("|   |", "white")+ colored(r4, "red") + colored("|   |", "white")+ colored(r5, "red") + colored("|", "white"))
	else:
		print(colored("|", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|", "white"))
		print(colored("|", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|", "white"))
		print(colored("|", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|   |", "white")+ colored(g, "green") + colored("|", "white"))
		
	print(colored("|___|   |___|   |___|   |___|   |___|", "white"))
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
		print(colored("Hi! \n", "white"))
	else:
		print(colored("Hi, " + active_player +"! \n", "white"))
	print(colored("Press Enter when all lights turn green.\n", "white"))
	print(colored("Press 0 if it's not you", "white"))
	print(colored("Press 1 to start playing", "white"))
	print(colored("Press 3 to see the highscores", "white"))
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
		print(colored('GO!!!', "white"))
		
		start = time.time()
		a = input()
		end = time.time()
		
		reactime = end - start
		if reactime > 0.05:
			print(reactime)
			add_time(active_player, reactime)
			update_leaderboard()
		else:
			print(colored("FALSE START", "red"))
		print(colored("\nPress Enter to play again", "white"))
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
		
		
