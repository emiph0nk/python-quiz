print("Hello there!")
answer = input("Would you like to play?")
score = 0
t_q = 3

if answer != "yes":
    exit()

if answer == "yes":
    print("okay let's begin ")
    ans = input("what is the most used language for game developement")
    if ans.lower == "c#" or "c++":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    print("Moving ON!")
    ans1 = input("Who is the creator of python ")
    if ans1 == "guido van rossum":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    print("NEXT QUESTION!")
    ans2 = input("What is HTML used for? ")
    if ans2 == "web developpement":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    print("Congratulations on finishing the quiz!")
    print("you got " + str(score) + " questions correct!")