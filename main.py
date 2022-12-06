#Run the slot machine
import random  #slot machine value should be a random number 


#ALL Capital letter means it's a constant ,value is not gonna chaange


MAX_LINES = 3 # global constant so that we can use them anywhere in our program
MAX_BET = 200
MIN_BET = 1
ROWS = 3
COLS = 3

symbol_count={
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
    #for every single rows we have 2 A's , 4 B's and so on to choose from
    }


symbol_value={
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
    #for every single rows we have 2 A's , 4 B's and so on to choose from
    }


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines= []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.appned(line+1)
    return winnings, winnings_lines









    #Logic 1:
"""  # we need to generate what symbols are going to be in each colum based on the frequency of symbols that we have here,  So we essentially need to randomly pick the number of rows inside each column, so if we have 3 rows need to pick 3 symbols that go inside of each of the columns that we have, and for each column we're doing kind of random pick or new random generation of symbols"""

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []

    #Logic2-#contains all of the different values we possibly could select from, and then randomly choose three of those values , and when we choose a value, will remove it from the list, and then we'll choose again
    
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol) # however many symbols we have , will be appended in this list
            #all_symbols=["A","A","B","B","B","B"] so as we have 
    # logic 3 : Now we have all symbols list we need to select what values are going to go in every single column
    # so,let's make a for loop that is going to do this for every column
    columns = []

    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value) # find the 1st instance of list and remove that
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
        #printing the columns vertically
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != (len(columns) -1):
                print(column[row], end=" | ")
            else:
                print(columns[row], end="")
        print()





#collecting user i/p --> gets the deposite from user 
def deposite():
    # to continually enter deposite amount until they give me a valid amount
     while True:
         amount = input("How much Taka you would like to deposite ? Tk")
         if amount.isdigit():
            amount = int(amount)

            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
         else:
            print("Please enter a number")
     return  amount
# so that we can call the main function and re run this program agian  
# 
# 
def get_number_of_lines():
     # to continually enter deposite amount until they give me a valid amount
    while True:
        lines = input("Enter the numbers of lines to be bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)

            if 1<= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid numbers of line.")
        else:
            print("Please enter a number.")
    return  lines  



#Now will implement amount I want to bet for each line

def get_bet():
    while True:
        bet_amount= input(" what amount would you like to bet on each line? Tk ")
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)

            if MIN_BET <= bet_amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} - {MAX_BET} ")
        else:
            print("PLEASE enter a  number.")
    return  bet_amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines 
        if total_bet > balance:
            print(f"Your do not have enough money, your current balance is: {balance}TK ")
        else:
            break
    print(f"You are betting {bet}TK on each line, Total bet is {total_bet}TK ")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"Your Won  TK{winnings}")
    print(f"you won on lines: ", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposite()
    while True:
        print(f"Current balance is TK{balance}")
        answer = input("Press Enter to play, (q to quit). ")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left with TK{balance}")


main()






