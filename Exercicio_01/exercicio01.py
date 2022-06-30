#Exercício 01

from random import randrange, sample 
random_list = []

for x in range(5): 
	random_list.append(randrange(0,100)) 	# atribuindo valroes aleatórios

if sorted(random_list, reverse=True) == random_list: 
	print("Lista está ordenada!")

else:
	while(sorted(random_list, reverse=True) != random_list): 
		random_list = sample(random_list, len(random_list)) 
		print(random_list)

	print("Lista ordenada com sucesso! ->", random_list)