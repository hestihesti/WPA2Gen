import os
import sys
from termcolor import colored
import time
import random

options = '''

1. Adjectives
2. Verbs
3. Gist

'''


def genr():
	print(colored(options, 'cyan'))
	sel = int(input('> '))
	i = 0
	print('\n')
	name = input('What Would You Like To Name The File:\n> ')
	words = int(input('How Many Words Would You Like To Generate:\n> '))
	if sel == 1:
		while i != words:
			i += 1
			with open('adjectives.txt', 'r') as f1:
				words1 = f1.read().splitlines()
			with open('nouns.txt', 'r') as f2:
				words2 = f2.read().splitlines()
			word1 = random.choice(words1)
			word2 = random.choice(words2)

			num = str(random.randint(1, 999)).zfill(3)
			result = word1 + word2 + num + '\n'
			print(colored(result, 'yellow'))
			time.sleep(1)

			with open(name, 'a') as f3:
				f3.write(result)

		print(colored('\n \n[+] COMPLETED [+]\n \n', 'green'))
		cat = 'cat ' + name
		os.system(cat)
		chmod = 'chmod +x ' + name
		os.system(chmod)


	elif sel == 2:
		while i != words:
			i += 1
			with open('verb.txt', 'r') as f1:
				words1 = f1.read().splitlines()
			with open('nouns.txt', 'r') as f2:
				words2 = f2.read().splitlines()
			word1 = random.choice(words1)
			word2 = random.choice(words2)

			num = str(random.randint(1, 999)).zfill(3)
			result = word1 + word2 + num + '\n'
			print(colored(result, 'yellow'))
			time.sleep(1)

			with open(name, 'a') as f3:
				f3.write(result)

		print(colored('\n \n[+] COMPLETED [+]\n \n', 'green'))
		cat = 'cat ' + name
		os.system(cat)
		chmod = 'chmod +x ' + name
		os.system(chmod)


	elif sel == 3:
		while i != words:
			i += 1
			with open('gist.txt', 'r') as f1:
				words1 = f1.read().splitlines()
			with open('nouns.txt', 'r') as f2:
				words2 = f2.read().splitlines()
			word1 = random.choice(words1)
			word2 = random.choice(words2)

			num = str(random.randint(1, 999)).zfill(3)
			result = word1 + word2 + num + '\n'
			print(colored(result, 'yellow'))
			time.sleep(1)

			with open(name, 'a') as f3:
				f3.write(result)

		print(colored('\n \n[+] COMPLETED [+]\n \n', 'green'))
		cat = 'cat ' + name
		os.system(cat)
		chmod = 'chmod +x ' + name
		os.system(chmod)



	else:
		print('Error Occurred')

	mv = 'mv ' + name + ' generated'
	os.system(mv)

genr()
