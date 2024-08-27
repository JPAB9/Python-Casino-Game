import random
import time

# Text ANSIS
blue_text = "\033[34m"
orange_text = "\033[38;5;214m"
green_text = "\033[32m"
red_text = "\033[31m"
yellow_text = "\033[33m"
magenta_text = '\033[35m'
reset_text = "\033[0m"
black_text = "\033[30m"
green_text = "\033[32m"


# Background ANSIS
bg_black = '\033[40m'
bg_red = '\033[41m'
bg_green = '\033[42m'
bg_yellow = '\033[43m'
bg_blue = '\033[44m'
bg_magenta = '\033[45m'
bg_cyan = '\033[46m'
bg_white = '\033[47m'
bg_reset = '\033[49m'


# Casino game

# Saving stuff (learned from GPT)

def save_progress(balance):
    with open("casino_save.txt", "w") as file:
        file.write(str(balance))
    print("Progress saved!")

def load_progress():
    try:
        with open("casino_save.txt", "r") as file:
            balance = float(file.read())
            print(f"Progress loaded! Your balance is ${balance}")
            return balance
    except FileNotFoundError:
        print("No save file found. Starting a new game.")
        return 0.0  

balance = load_progress()

# Normal regular variables

amount = 15000 


print(f'''
                                    {red_text}===WARNING==={reset_text}
                        This overall game does not support nor promote any activities related
                        to gambling games/activities, this game is made purely for fun
                        and is inspired by a recent meme related to gambling.
        {red_text}===IF YOU THINK THIS GAME COULD ENCOURAGE YOU OR OTHERS TO GAMBLE, IT IS ADVISED TO QUIT.==={reset_text}
''')

print(f'''{orange_text}
                              ####     ##      #####    ####    ##   ##   #####                             
                             ##  ##   ####    ##   ##    ##     ###  ##  ##   ##                            
 ######   ######            ##       ##  ##   #          ##     #### ##  ##   ##           ######   ######  
                            ##       ##  ##    #####     ##     ## ####  ##   ##                            
 ######   ######            ##       ######        ##    ##     ##  ###  ##   ##           ######   ######  
                             ##  ##  ##  ##   ##   ##    ##     ##   ##  ##   ##                            
                              ####   ##  ##    #####    ####    ##   ##   #####                        
{reset_text}''')

time.sleep(1)

print("Welcome to the casino, here's everything youll need to know.")

time.sleep(1)

print('''
    Available games/game changes:
          Betting: This game consists of betting a certain amount of
          money from your balance on either the color red or black,
          if the color you betted for matches, your money is doubled, otherwise, you loose
          it all
      
          Roulette: This game consists of a roulette with 3 collumns and 3 different
          figures, if all 3 figures on the roulette match, your money is doubled, otherwise,
          you loose.
      
          Withdraw: Withdraw money from your bank account to your current balance
      
          Balance: Shows your current balance
      
    Available system commands/settings:
          Exit: exits the program
      
          Help: Shows this page
      
          Save: Saves current progress into a file to be able to continue later.   
            |save.clear: clears all progress
      
        --- Your default balance is $1000 --- 
            ''')
time.sleep(1)

#betting template
#try:
# bet = float(input("Enter the amount of money you bet: $"))
# 
# if bet <= 0:
#     raise ValueError("Invalid betting input, please enter a number larger than 0$.")
# 
# elif bet > balance:
#     raise ValueError(f"You cannot bet more money than your current balance. ({bet} > {balance}).")
#
#    except ValueError as e:
#       print(f"Error: {e}")
#       return balance

def betting(balance):
    try:
        bet = float(input("Enter the amount of money you bet: $"))
        
        if bet <= 0:
            raise ValueError("Invalid betting input, please enter a number larger than 0$.")
        
        elif bet > balance:
            raise ValueError(f"You cannot bet more money than your current balance. ({bet} > {balance}).")
        
        color_bet = input(f"{bet} on red or black? [r/b]: ").strip().lower()
        
        if color_bet not in ["r", "b"]:
            raise ValueError("Invalid color choice. Please enter 'r' for red or 'b' for black.")
        
    except ValueError as e:
        print(f"Error: {e}")
        return balance
    
    colors = [
        "r","b"
    ]
    
    r_b = random.choice(colors)
    print(f"The wheel landed on: {r_b}")
    time.sleep(1)
    
    if color_bet == r_b:
        print(f"{blue_text}You won! Congrats!{reset_text}")
        balance += bet * 2
        print(f"Your balance is now ${balance}")


    
    else: 
        balance -= bet
        print(f"Sadly you lost ${bet}. Your new balance is ${balance}.")
    
    return balance

def roulette(balance):
    try:
        bet = float(input("Enter the amount of money you bet: $"))
        if bet <= 0:
            raise ValueError("Invalid betting input, please enter a number larger than 0$.")
        elif bet > balance:
            raise ValueError(f"You cannot bet more money than your current balance. ({bet} > {balance}).")

    except ValueError as e:
        print(f"Error: {e}")

    choices1 = ["$", "#", "@"]
    choices2 = ["$", "#", "@"]
    choices3 = ["$", "#", "@"]

    pick1 = random.choice(choices1)
    pick2 = random.choice(choices2)
    pick3 = random.choice(choices3)

    print(f'''
            |        |       |
      {pick1}     |    {pick2}   |   {pick3}   |
            |        |       |
    ''')

    if pick1 == "$" and pick2 == "$" and pick3 == "$":
        print(f"{blue_text}Congrats! you won!{reset_text}")
        balance += bet * 2
        print(f"Your balance is now {balance}")

    elif pick1 == "#" and pick2 == "#" and pick3 == "#":
        print(f"{blue_text}Congrats! you won!{reset_text}")
        balance += bet * 2
        print(f"Your balance is now {balance}")
    
    elif pick1 == "@" and pick2 == "@" and pick3 == "@":
        print(f"{blue_text}Congrats! you won!{reset_text}")
        balance += bet * 2
        print(f"Your balance is now {balance}")

    else:
        balance -= bet
        print(f"{red_text}Sadly you lost ${bet}, your balance is now ${balance}{reset_text}")

    return balance

def high(balance):
    try:
    
        bet = float(input("Enter the amount of money you bet: $"))
        
        if bet <= 0:
            raise ValueError("Invalid betting input, please enter a number larger than 0$.")
        
        elif bet > balance:
            raise ValueError(f"You cannot bet more money than your current balance. ({bet} > {balance}).")
        
    except ValueError as e:
        print(f"Error: {e}")
        return balance
    
    player = random.randint(1, 100)
    
    bet_bot1 = random.randint(1, balance)
    bet_bot2 = random.randint(1, balance)
    bet_bot3 = random.randint(1, balance)

    
    bot1 = random.randint(1, 100)
    bot2 = random.randint(1, 100)
    bot3 = random.randint(1, 100)

    if player > bot1 and player > bot2 and player > bot3:
        balance += (bet_bot1 + bet_bot2 + bet_bot3)
        print(f"{blue_text}Your number is the largest! You win! Numbers: bot1: {bot1} bot2: {bot2} bot3: {bot3} < You: {player}{reset_text}")
        print(f"Your balance is now {balance}")

        print(f"bot bets: bot1: {bet_bot1} bot2: {bet_bot2} bot3: {bet_bot3}")

    #If there's a rare tie, nobody wins.

    elif player == bot1 or player == bot2 or player == bot3:
        print(f"{green_text}There seems to be a tie, nobody wins. Numbers: bot1: {bot1} bot2: {bot2} bot3: {bot3} < You: {player}{reset_text}")
        print(f"Your balance is now {balance}")
        
        print(f"bot bets: bot1: {bet_bot1} bot2: {bet_bot2} bot3: {bet_bot3}")

    #If player_number !> bots

    else: 
        balance -= bet
        print(f"{red_text}Sadly, your number was not the largest. Numbers: bot1: {bot1} bot2: {bot2} bot3: {bot3} You: {player}{reset_text}")
        print(f"Your balance is now {balance}")
        
        print(f"bot bets: bot1: {bet_bot1} bot2: {bet_bot2} bot3: {bet_bot3}")
    return balance

#saving and usage functions

def clear_progress():
    while True:
        confirm = input("Are you sure you want to clear progress?[y/n]: ").lower()
        if confirm == "y":
            with open("casino_save.txt", "w") as file:
                file.write("0.0")
            print("Progress cleared!")
            balance = 1000
            amount = 15000
            break

        elif confirm == "n":
            print("clearing cancelled!")
            break

        else:
            print(f"{red_text}Error: Invalid input, please input y for 'yes' and n for 'no'.{reset_text}")

def withdraw(balance, amount):
    print(f"You have {balance}$ in your balance")
    print(f"You have {amount}$ in your bank account")
    
    while True:
        withdraw = input("Would you like to withdraw money from your account to your casino balance? [y/n]: ")
        if withdraw.lower() == "y":
            amount_withdraw = int(input("How much money would you like to withdraw?: "))
            if amount_withdraw <= amount:
                amount -= amount_withdraw
                balance += amount_withdraw
                print(f"Successfully withdrew {amount_withdraw}$ from your bank account. New bank balance: {amount}$ Casino balance: {balance}$.")
                break
            else:
                print(f"Insufficient funds! You have {amount}$ in your bank account.")
        elif withdraw.lower() == "n":
            print("Withdrawal cancelled!")
            break
        else:
            print("Error: Incorrect input, please input either 'y' or 'n'.")
    
    return balance, amount

    
def deposit(balance, amount):

    while True:

        deposit = input("Would you like to deposit money from you balance to your bank account? [y/n]: ")
        if deposit.lower() == "y":
            amount_deposit = int(input("How much money would you like to deposit?: " + "$"))

            if amount_deposit < balance:
                amount = balance - amount_deposit
                print(f"Succesfully deposited {amount_deposit}$ to your bank account!")
                break
        
            else:
                print(f"Insuficient funds! You have {balance}$ in your balance.")
        
        elif deposit.lower() == "n":
            print(f"{red_text}deposit cancelled!{reset_text}")
            break
                
    return balance, amount
            



while True: #main while loop
    user_input = input("What would you like to do?: ").lower()

    if user_input == "help":
        print('''
            Available games/game changes:
                  Betting: This game consists of betting a certain amount of
                  money from your balance on either the color red or black,
                  if the color you betted for matches, your money is doubled, otherwise, you loose
                  it all.

                  Roulette: This game consists of a roulette with 3 collumns and 3 different
                  figures, if all 3 figures on the roulette match, your money is doubled, otherwise,
                  you loose.
              
                  Withdraw: Withdraw money from your bank account to your current balance.

                  Balance: Shows your current balance.

            Available system commands/settings:
                  Exit: exits the program

                  Help: Shows this page.

                  Save: Saves current progress into a file to be able to continue later.   
                  |save.clear: clears all progres
              
                --- Your default balance is $1000 --- 
            ''')

    elif user_input == "save" :
       print("Saving progress...")
       time.sleep(1)
       save_progress(balance)     

    elif user_input == "save.clear":
        print("Clearing progress...")
        time.sleep(1)
        clear_progress()
        balance = 1000.0  # Reset balance to $1000
        amount = 15000.0  # Reset amount to $15,000
        print(f"Progress cleared. Your balance is now ${balance}, and your bank account has ${amount}.")


    elif user_input == "balance":
        print(f"Your current balance is {balance}$")

    elif user_input == "exit":
        print("Saving progress...")
        time.sleep(1)
        save_progress(balance)
        print(f"Exiting casino.py...")
        time.sleep(1)
        break

    elif user_input == "withdraw":
        balance, amount = withdraw(balance, amount)

    elif user_input == "deposit":
        balance, amount = deposit(balance, amount) # so basically balance, amount is used to call the same function cuz if i do balance= {} and amount= {} it calls def twice
        
    #if balance is 0    

    elif balance <= 0 and amount <= 0:
        print(f"{red_text}You lost all your money in gambling, please exit the casino as you do not have anymore money to bet{reset_text}")
        time.sleep(2)
        print("deleting progress...")
        time.sleep(1)
        clear_progress()        
        break
        

    #games and activities are here now

    elif user_input == "betting":
        balance = betting(balance)

    elif user_input == "roulette":
        balance = roulette(balance)

    elif user_input == "high":
        balance = high(balance)
    
    else:
        print(f"{red_text}Command unavailable or mistyped, please try again{reset_text}")

