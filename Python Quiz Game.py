print("Welcome to python quiz game")
score=0
print("Who is the prime minister of India'?")
print("1. Narendra modi\n2. Gandhi Ki \n3. Sonia Gandhi \n4. Ambedkar")
ans=int(input("Your choice-enter option number : "))
if(ans==1):
    print("Correct")
    score+=1
else:
    print("Wrong")
print("Sun rises in ")
print("1. East \n2. West \n3. North \n4. South")
ans=int(input("Your choice-enter option number : "))
if(ans==1):
    print("Correct")
    score+=1
else:
    print("Wrong")
print("Bulb was invented by")
print("1. Thomas Alfa edison\n2. Rudolf\n3. Karl Benz\n4. Daltona")
ans=int(input("Your choice-enter option number : "))
if(ans==1):
    print("Correct")
    score+=1
else:
    print("Wrong")
print("Your score is : ",score," out of 3")