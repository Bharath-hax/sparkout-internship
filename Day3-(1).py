import random  

def guess_num():
    n = random.randint(1, 100)  
    attempt = 0                 
    
    print("I'm thinking of a number between 1 and 100.")
    
    while True:  
        
        try:
            target = int(input("Enter the guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
            
        attempt += 1  
        print(f"Attempt number: {attempt}")  
        
        if target == n:  # Compare with 'n', not the module 'random'
            print(f"{target} is the correct number! You won!")
            break  # Exit the loop when the user wins
        else:
            print(f"{target} is not correct.")
            if n > target:  # Compare 'n' with 'target' to give hints
                print(f"Hint: The secret number is larger than {target}.")
            else:
                print(f"Hint: The secret number is lower than {target}.")

# Run the game
guess_num()
