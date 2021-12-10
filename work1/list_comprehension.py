import math
from random import randint
import random
def main():
	#Generate a seed to always get the same example of 100 random numbers
	random.seed(980220)
	#List of 100 numbers
	random_numbers = [randint(1,100) for i in range(1,101)]
	print("The list of random_numbers are: ")
	print(random_numbers)
	print()
	print("Of those numbers the ones who are divisor of 3 are: ")

	#Print all the numbers that are divisible of 3 of the list
	divisor_of_3=[k for k in random_numbers if k%3==0]
	print(divisor_of_3)
	#Print all the even numbers of the list
	even_numbers=[k for k in random_numbers if k%2==0]
	#Print all the odd numbers of the list
	odd_numbers=[k for k in random_numbers if k%2==1]

	print("The even numbers are:")
	print(even_numbers)
	print("The odd numbers are:")
	print(odd_numbers)


if __name__ == '__main__':
	main()