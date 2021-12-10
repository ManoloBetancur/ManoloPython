import math
import random


def main():
	print("The dict of random_numbers are: ")
	#Generate a seed to always get the same example of 100 random numbers
	random.seed(980220)
	random_numbers={}
	for i in range(1,101):
		random_numbers[i]=random.randint(1,101)

	print(random_numbers)
	print()
	print("The dictionary with each value squared ")

	#Print all the numbers that are divisible of 3 of the list
	square={k:random_numbers[k]**2 for k in random_numbers}
	print(square)
	#Print all the even numbers of the list
	even_numbers={k:random_numbers[k] for k in random_numbers if random_numbers[k]%2==0}
	#Print all the odd numbers of the list
	odd_numbers={k:random_numbers[k] for k in random_numbers if random_numbers[k]%2==1}

	print("The even numbers are:")
	print(even_numbers)
	print("The odd numbers are:")
	print(odd_numbers)


if __name__ == '__main__':
	main()