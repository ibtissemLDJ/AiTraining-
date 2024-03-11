##Build a number guessing game where there is a target number the user must find it,
## when the user enter a number, you must indicate if the desired one is less or more than the input, 
##the user has 10 attempts, if he did not find the number within those attempts, he loses, 
##if he finds it he wins, you should put that in a function. Note: you can use the library random 
##to generate the target number or you can simply put it manually in your code
import random 
print("Hello, tell us your name!")
playerName = input("Enter your name here : ")
print ("Welcom "+playerName + " let's explain the game!")
print ("So, in our game there is a target number YOU MUST FIND IT ")
print ("But! I won't let you alone XD  i will help you, by telling you if the number you enter is LESS or MORE then the one desired ^^ ")
print ("let's start th Game! ")
desiredNumber = random.randint(0,1000)
number = input("Enter a number :")
while (int(number)!= desiredNumber & i <10):
    if (int(number) > desiredNumber): 
        print(" the number you provide is GREATER then the desired number.")
    elif (int(number)<desiredNumber):
        print("the number you privide is LESS then the desired number.")
    number= input("Enter another number XD!")
if (int (number)== desiredNumber):
    print("You win! the number is :"+ number )
else:
    print ("Oh Noo Try Again :(")    


