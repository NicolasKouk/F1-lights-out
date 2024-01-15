import time
import random
from termcolor import colored

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
else:
	print(colored("FALSE START", "white"))
