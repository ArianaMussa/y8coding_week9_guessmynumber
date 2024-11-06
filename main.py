from random import randint 

correct = randint(16, 64)
number = None
while number != correct:

    print("Guess my number")
    number = int(input())

    if number > correct:
        print("LOWER!")
    
    if number < correct:
        print("HIGHER!")

    if number == correct:
        print("YOU WON!!!!!") 

five_less = correct - 5
five_more = correct + 5

if number in range(five_less, five_more+1):
     print("ALMOST! YOU ARE 5 AWAYYYYY!")
