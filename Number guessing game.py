import random
x = random.randint(1,100)
ch=10
while ch>0:
    z=int(input("Guess The Number Between 1 to 100:"))
    if x == z:  
       print("Congratulations you guessed it right","Your score is", ch*10)
       break
    elif x > z:
       print("You guessed too small!", ch-1, "tries left")
    elif x < z:
       print("You Guessed too high!", ch-1, "tries left")
    ch= ch-1
else:
    print("The number is",x)
    print("Better Luck Next time!")
