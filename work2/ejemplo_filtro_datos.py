#This code is meant to work with python 3.9
import csv

def main(Data):
	print("There is a data set of 500 people")
	print("The data has information about name, country, phone number, and their favorite food")
	print('-'*15)
	#Get de food section from de Data
	favorite_food = [k["list"] for k in Data]
	#List of unique food from the data
	unique_food = list(set(favorite_food))
	print("Unique types of food found in Data")
	print(unique_food)
	print('-'*15)
	#Phone numbers of people who like seafood
	phone_seafood = [k['phone'] for k in Data if k['list'] == 'seafood']
	print("Phone numbers of people who like seafood")
	print(phone_seafood)
	print('-'*15)
	print("Number of people who chose seafood as their favorite food")
	print(len(phone_seafood))
	print('-'*15)
	print("Nationalities found in the data")
	unique_nationality = list(set([k["country"] for k in Data]))
	print(unique_nationality)
	print('-'*15)
	print("Number of different nationalities found")
	print(len(unique_nationality))
	print('-'*15)
	americans = [k['name'] for k in Data if k['country']=='United States']
	print("Number of people from United States")
	print(len(americans))
	print('-'*15)
	print('Name of the people from United Sates')
	print(americans)

	
def read_data():
	with open('Data.csv','r') as file:
		Data_object = csv.DictReader(file)
		Data_list = list(Data_object)
	return Data_list


if __name__ == '__main__':
	Data = read_data()
	main(Data)