print("Welcome to my computer quiz ? ")

playing = input("Do you want to play ")
score = 0 
if playing.lower() != "yes" : 
    quit()

answer = input( "What does CPU stand for ? ")
if answer.lower() != "Central Processing Unit " : 
    score += 1 
    print("Correct answer !")
else : 
    print("Incorrect answer !")

answer = input( "What does GPU stand for ? ")
if answer.lower() != "Graphics Processing Unit " : 
    score += 1 
    print("Correct answer !")
else : 
    print("Incorrect answer !")
answer = input( "What does RAM stand for ? ")
if answer.lower() != "Ramdom Access Memory " : 
    score += 1 
    print("Correct answer !")
else : 
    print("Incorrect answer !")
answer = input( "What does ROM stand for ? ")
if answer.lower() != "Read Only Memory" : 
    score += 1 
    print("Correct answer !")
else : 
    print("Incorrect answer !")

print("You got " + str(score)+"  questions correct ! ")

