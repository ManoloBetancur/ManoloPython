from functools import reduce
import random
from random import randint
#Understanding of high orden function

def hello1():
	print("Hello, how are you?")

def hello2():
	print("Hey, how's it going?")

def say_hello(fun1):
	fun1()

def main():
	#Simple example of high orden function

	#Do what function is passed as parameter
	say_hello(hello1)
	say_hello(hello2)

	#Generate a seed to always get the same example of 100 random numbers
	random.seed(980220)
	#List of 100 random numbers from 1 to 100
	random_numbers = [randint(1,100) for i in range(1,101)]
	print("100 random numbers list :")
	print(random_numbers)

	#Use of filter function
	odd = list(filter(lambda x: x%2!=0,random_numbers))
	print("Odd numbers got from filter function")
	print(odd)

	#Use of map function
	incremented_by_1=list(map(lambda x:x+1,random_numbers))
	print("List of random numbers incremented by 1 using map function")
	print(incremented_by_1)
	#Convert all elements of the list in string using map
	print("All elements of the list to string using map")
	print(list(map(str,random_numbers)))

	msg = ['H','e','l','l','o',' ',',','W','o','r','l','d','!']
	print("List of separed strings with message")
	print(msg)

	print("Using reduce function to put the letters together")
	stick = reduce(lambda a,b: a+b,msg)
	print(stick)
if __name__ == '__main__':
	main()