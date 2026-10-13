import random
words=list(map(str,input().split()))
word=random.choice(words)
guess_letters=[]
wrong_guess=0
max_guess=6
while wrong_guess<max_guess:
    dis=""
    for e in word:
        if e in guess_letters:
            dis+=e
        else:
            dis+="_"
    print("Word: ",dis)
    print("Wrong Guesses: ",wrong_guess,"/",max_guess)
    if "_" not in dis:
        print("You Won")
        print("The Word is : ",word)
        break
    guess=input("Guess a letter: ").lower()
    if guess in guess_letters:
        print("You Already Guesses This Letter")
        continue
    guess_letters.append(guess)
    if guess in word:
        print("Correct Guess")
    else:
        print("Wrong Guess")
        wrong_guess+=1
else:
    print("Oops You Lost")
    print("The Word is: ",word)