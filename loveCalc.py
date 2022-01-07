# A program that tests the compatibility between two people.
# love scores 10-90 or bad
#love score 40-50 are ok
#Takes both people's names and checks for the number of times the letters in the word TRUE occurs. 
# checks for the number of times the letters in the word LOVE occurs. 
#combines these numbers to make a 2 digit number.

print("welcome to the love calculator!")
name1 = input("what is your name?")
name2 = input("what is their name?")

combined_string = name1 + name2
lower_case_string = combined_string.lower()   # lowercases their name and your name

t = lower_case_string.count("t")    #use count plus string character 
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e               #add variable.  will add all character in the count function


l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))  # will give error becuase strings cant go with integers so convert str to int

print(love_score)

if (love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score}, yo go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, You are alright together.")
else:
    print(f"Your score is {love_score}.")

