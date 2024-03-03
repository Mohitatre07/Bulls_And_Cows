import random

def getDigits(num): 
    return [int(i) for i in str(num)]

def noDuplicates(num): 
    num_li = getDigits(num) 
    if len(num_li) == len(set(num_li)): 
        return True
    else: 
        return False

def generateNum(): 
    while True: 
        num = random.randint(1000, 9999) 
        if noDuplicates(num): 
            return num

def numOfBullsCows(num, guess): 
    bull_cow = [0, 0] 
    num_li = getDigits(num) 
    guess_li = getDigits(guess) 
      
    for i, j in zip(num_li, guess_li): 
        if j in num_li: 
            if j == i: 
                bull_cow[0] += 1
            else: 
                bull_cow[1] += 1
                  
    return bull_cow 

def getHint(num, guess):
    num_li = getDigits(num)
    guess_li = getDigits(guess)
    hint = []
    
    for i, digit in enumerate(guess_li):
        if digit == num_li[i]:
            hint.append(str(digit))
        else:
            hint.append('*')
    
    return ' '.join(hint)

def playGame():
    num = generateNum() 
    max_tries = int(input("How many tries do you want? (Maximum 9): "))
    tries = min(max_tries, 9)  # Ensure maximum 9 tries

    while tries > 0: 
        guess = int(input("Enter your guess: ")) 
          
        if not noDuplicates(guess): 
            print("Number should not have repeated digits. Try again.") 
            continue
        if guess < 1000 or guess > 9999: 
            print("Enter 4 digit number only. Try again.") 
            continue
          
        bull_cow = numOfBullsCows(num, guess) 
        print(f"{bull_cow[0]} bulls, {bull_cow[1]} cows")
        print("Hint:", getHint(num, guess))
        tries -= 1
          
        if bull_cow[0] == 4: 
            print("You guessed right!") 
            break
    
    if bull_cow[0] != 4:
        print(f"You ran out of tries. Number was {num}")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        playGame()
    else:
        print("Thanks for playing!")

# Start the game
playGame()
