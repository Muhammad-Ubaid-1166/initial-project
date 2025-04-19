
import random  

def all_inputs(): # r
    strings = ["r", "p", "s"]
    random_choice = random.choice(strings)
    computer_input = random_choice
    if computer_input == "r":
        computer_input = "rock"
    elif computer_input == "p":
        computer_input = "paper"
    elif computer_input == "s":
        computer_input = "scissor"

    user_input = input("enter r , p , s: ").strip().lower()
    try:
        if user_input == "r":
            user_input = "rock"
        elif user_input == "p":
            user_input = "paper"
        elif user_input == "s":
            user_input = "scissor"
        else:
            print("invalid word!")
            return all_inputs()
    except ValueError:
        print("invalid word!")
    print(f"you choose ->{user_input}")
    print(f"computer choose ->{computer_input}")
    return user_input, computer_input
def winning_conditions(user_inputs,computer_inputs):
    if user_inputs == computer_inputs:
        print("its a draw!")
    elif (user_inputs == "rock" and computer_inputs == "gun") or \
         (user_inputs == "paper" and computer_inputs == "rock") or \
         (user_inputs == "rock" and computer_inputs == "scissor") or \
         (user_inputs == "scissor" and computer_inputs == "paper") or \
         (user_inputs == "gun" and computer_inputs == "paper"):  
        print("You win!")  
    else:
        print("computer win!")
while True:
    if __name__ == "__main__":
        user_inputs, computer_inputs = all_inputs()        
        if user_inputs and computer_inputs:  # Ensure valid inputs
                winning_conditions(user_inputs, computer_inputs)