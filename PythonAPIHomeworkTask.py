#import requests
import requests
#save url as a variable and save the data as a variable
url = "https://opentdb.com/api.php?amount=25&category=20"
response = requests.get(url)
questions = response.json()
name = input("What is your name?")

#create username and password
username = input("What username would you like to use?")


# import more modules
import string
import random

#password generator

# store all characters in lists 
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)


# Ask user about the number of characters
user_input = input("How many characters do you want in your password? ")


# check this input is it number? is it more than 8?
while True:

	try:

		characters_number = int(user_input)

		if characters_number < 8:

			print("Your number should be at least 8.")

			user_input = input("Please, Enter your number again: ")

		else:

			break

	except:

		print("Please, Enter numbers only.")

		user_input = input("How many characters do you want in your password? ")


# shuffle all lists
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)


# calculate 30% & 20% of number of characters
part1 = round(characters_number * (30/100))
part2 = round(characters_number * (20/100))


# generation of the password (60% letters and 40% digits & punctuations)
result = []

for x in range(part1):

	result.append(s1[x])
	result.append(s2[x])

for x in range(part2):

	result.append(s3[x])
	result.append(s4[x])


# shuffle result
random.shuffle(result)

# join result
password = "".join(result)
print("Strong Password: ", password, "is your password. ")

#login 
username_check = input("What is your USERNAME ? ")
password_check = input("What is your PASSWORD ? ")

if username_check == username and password_check == password:
    print ("Hi ," + name + " Welcome to my quiz game!")
    print ("Note: if your spelling is incorrect it is considered a wrong answer. Punctuation is also important. Please use capital letters.")
else:
      print ("Username and Password do not correspond. Please re-enter")
score = 0

# function to calculate score percentage
def score_percentage(score):
    (score/25)*100
#check if player is playing
playing = input('Do you want to play?')
if playing == 'Yes':
    # the trivia game
    for item in questions["results"]: 
        print(item["question"])
         given_answer = input('Answer:')
        if item["correct_answer"] ==  given_answer:
            score+=1
            print (score) 
            print ("Yaay! Correct!")
    else: 
        print ("Wrong answer")
        print (f"The correct answer is: {item['correct_answer']}")
        print (score)
else:
    print ("You are NOT playing. What a shame!")
while score > 0:
    print (score_percentage(score))